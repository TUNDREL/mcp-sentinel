import asyncio
import json
import os
import sys

from dotenv import load_dotenv
load_dotenv()

import httpx2
from mcp import ClientSession
from mcp.client.streamable_http import streamable_http_client
from mcp.client.sse import sse_client

from . import report
from . import rules
from . import ai_review

# Each individual server scan is capped at this many seconds, so one slow or
# hanging server can't stall the whole batch scan indefinitely.
PER_TARGET_TIMEOUT = 30

RETRY_ATTEMPTS = 3
RETRY_BACKOFF_SECONDS = 2

# How many servers get scanned at once. Capped rather than unbounded — high
# concurrency can worsen DNS flakiness seen on some targets and risks
# tripping rate limits on the servers themselves.
MAX_CONCURRENT_SCANS = 8

# Separate, tighter limit specifically for AI review calls. The free-tier
# Gemini quota (roughly 10-15 requests/minute) is far more restrictive than
# our own scan concurrency, so this needs its own smaller cap independent
# of MAX_CONCURRENT_SCANS above.
MAX_CONCURRENT_AI_REVIEWS = 3


def _flatten_exceptions(exc) -> list[Exception]:
    """Recursively unwrap nested ExceptionGroups down to the real, leaf errors."""
    if isinstance(exc, BaseExceptionGroup):
        flat = []
        for sub in exc.exceptions:
            flat.extend(_flatten_exceptions(sub))
        return flat
    return [exc]


async def scan_server(target: dict) -> dict:
    """Connect to an MCP server over Streamable HTTP or SSE, with optional
    Bearer token auth, and pull its tool definitions for analysis."""
    name = target.get("name", "Unnamed target")
    url = target.get("url")
    findings = {"name": name, "url": url, "tools": [], "errors": []}

    if not url:
        findings["errors"].append("Target is missing a 'url' field — skipping")
        return findings

    if target.get("auth_type") == "oauth":
        findings["errors"].append("OAuth not yet supported — skipping")
        return findings

    headers = None
    if target.get("requires_auth"):
        env_var = target.get("auth_env_var")
        token = os.getenv(env_var) if env_var else None
        if not token:
            findings["errors"].append(
                f"requires_auth is true but no token found in env var '{env_var}'"
            )
            return findings
        headers = {"Authorization": f"Bearer {token}"}

    transport_type = target.get("transport", "streamable-http")

    last_errors: list[str] = []
    for attempt in range(1, RETRY_ATTEMPTS + 1):
        attempt_errors: list[str] = []
        try:
            await asyncio.wait_for(
                _connect_and_collect(url, transport_type, headers, findings, attempt_errors),
                timeout=PER_TARGET_TIMEOUT,
            )
        except* Exception as eg:
            for e in _flatten_exceptions(eg):
                if isinstance(e, asyncio.TimeoutError):
                    attempt_errors.append(f"Timed out after {PER_TARGET_TIMEOUT}s")
                else:
                    attempt_errors.append(f"{type(e).__name__}: {e}")

        if findings["tools"] or not attempt_errors:
            break  # success, or nothing to retry

        last_errors = attempt_errors
        if attempt < RETRY_ATTEMPTS:
            await asyncio.sleep(RETRY_BACKOFF_SECONDS * attempt)

    if not findings["tools"]:
        findings["errors"] = last_errors or ["Unknown failure"]
        if RETRY_ATTEMPTS > 1:
            findings["errors"].append(f"(failed after {RETRY_ATTEMPTS} attempts)")

    return findings


async def _connect_and_collect(
    url: str, transport_type: str, headers: dict | None, findings: dict, errors: list
) -> None:
    """Open the appropriate transport, start a session, and collect tools."""
    if transport_type == "streamable-http":
        http_client = httpx2.AsyncClient(
            headers=headers,
            timeout=httpx2.Timeout(30.0, read=300.0),
        )
        async with streamable_http_client(url, http_client=http_client) as (read, write):
            async with ClientSession(read, write) as session:
                await session.initialize()
                await _collect_tools(session, findings)

    elif transport_type == "sse":
        async with sse_client(
            url,
            headers=headers,
            timeout=5.0,
            sse_read_timeout=300.0,
        ) as (read, write):
            async with ClientSession(read, write) as session:
                await session.initialize()
                await _collect_tools(session, findings)

    else:
        errors.append(f"Unsupported transport type: {transport_type}")


async def _collect_tools(session: ClientSession, findings: dict) -> None:
    result = await session.list_tools()
    for tool in result.tools:
        findings["tools"].append({
            "name": tool.name,
            "description": tool.description,
            "input_schema": tool.input_schema,
        })


async def scan_all(targets_path: str = "targets.json") -> list[dict]:
    try:
        with open(targets_path) as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"Error: '{targets_path}' not found. Check the file exists in your project root.")
        return []
    except json.JSONDecodeError as e:
        print(f"Error: '{targets_path}' contains invalid JSON — {e}")
        return []

    targets = data.get("targets", [])
    scan_semaphore = asyncio.Semaphore(MAX_CONCURRENT_SCANS)
    ai_semaphore = asyncio.Semaphore(MAX_CONCURRENT_AI_REVIEWS)

    async def scan_one(target: dict) -> dict:
        async with scan_semaphore:
            print(f"Scanning {target.get('name', 'Unnamed target')}...")
            result = await scan_server(target)
            result["issues"] = rules.evaluate(target, result)

            # Second-opinion AI review for high-confidence findings only.
            # Runs under its own, smaller semaphore since free-tier LLM
            # rate limits are much tighter than our scan concurrency.
            for issue in result["issues"]:
                if issue["severity"] in ("critical", "high") and issue.get("tool"):
                    matching_tool = next(
                        (t for t in result["tools"] if t["name"] == issue["tool"]), None
                    )
                    if matching_tool:
                        async with ai_semaphore:
                            verdict = await ai_review.review_flag(matching_tool, issue)
                        if verdict:
                            issue["ai_verdict"] = verdict

            return result

    results = await asyncio.gather(*(scan_one(t) for t in targets))
    return list(results)


if __name__ == "__main__":
    # Python 3.14 deprecated the global event-loop-policy system in favor of
    # passing loop_factory directly to asyncio.run(). On Windows, the default
    # Proactor loop has shown DNS-resolution issues with httpx2's async
    # resolver — SelectorEventLoop avoids that. Unix/macOS are unaffected.
    loop_factory = asyncio.SelectorEventLoop if sys.platform == "win32" else None

    all_results = asyncio.run(scan_all(), loop_factory=loop_factory)

    print("\n--- Scan Summary ---")
    report.print_summary_table(all_results)
    path = report.generate_markdown_report(all_results)
    print(f"\nFull report written to: {path}")