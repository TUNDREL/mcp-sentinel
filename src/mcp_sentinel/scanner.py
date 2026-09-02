import asyncio
import json
import os
import sys
import time

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
PER_TARGET_TIMEOUT = int(os.getenv("MCP_SENTINEL_PER_TARGET_TIMEOUT", "30"))

RETRY_ATTEMPTS = int(os.getenv("MCP_SENTINEL_RETRY_ATTEMPTS", "3"))
RETRY_BACKOFF_SECONDS = int(os.getenv("MCP_SENTINEL_RETRY_BACKOFF_SECONDS", "2"))

# How many servers get scanned at once. Configurable via environment var to
# allow experimentation with concurrency for speed tuning.
MAX_CONCURRENT_SCANS = int(os.getenv("MCP_SENTINEL_MAX_CONCURRENT", "8"))

# Separate, tighter limit specifically for AI review calls. The free-tier
# Gemini quota is far more restrictive than our own scan concurrency, so
# this needs its own smaller cap independent of MAX_CONCURRENT_SCANS above.
MAX_CONCURRENT_AI_REVIEWS = int(os.getenv("MCP_SENTINEL_MAX_AI_REVIEWS", "3"))


# Simple in-memory cache for OAuth tokens: {(token_url, client_id): (token, expiry)}
OAUTH_TOKEN_CACHE: dict = {}


async def _fetch_client_credentials_token(token_url: str, client_id: str, client_secret: str, scope: str | None = None) -> tuple[str, float]:
    async with httpx2.AsyncClient(timeout=10.0) as c:
        data = {"grant_type": "client_credentials"}
        if scope:
            data["scope"] = scope
        resp = await c.post(token_url, data=data, auth=(client_id, client_secret))
        resp.raise_for_status()
        j = resp.json()
        token = j.get("access_token")
        expires = j.get("expires_in", 3600)
        return token, time.time() + int(expires) - 60


async def _get_oauth_headers(target: dict) -> dict | None:
    """Obtain OAuth bearer token for a target.

    Supports pre-provisioned token via `oauth_token_env_var` (or legacy
    `auth_env_var`) or the client_credentials flow using
    `oauth_token_url`, `oauth_client_id_env`, and `oauth_client_secret_env`.
    """
    token_env = target.get("oauth_token_env_var") or target.get("auth_env_var")
    if token_env:
        token = os.getenv(token_env)
        if token:
            return {"Authorization": f"Bearer {token}"}

    token_url = target.get("oauth_token_url")
    client_id_env = target.get("oauth_client_id_env")
    client_secret_env = target.get("oauth_client_secret_env")
    scope = target.get("oauth_scope")

    if token_url and client_id_env and client_secret_env:
        client_id = os.getenv(client_id_env)
        client_secret = os.getenv(client_secret_env)
        if not client_id or not client_secret:
            raise RuntimeError("OAuth client id/secret env vars not set")

        cache_key = (token_url, client_id)
        cached = OAUTH_TOKEN_CACHE.get(cache_key)
        if cached and cached[1] > time.time():
            return {"Authorization": f"Bearer {cached[0]}"}

        token, expiry = await _fetch_client_credentials_token(token_url, client_id, client_secret, scope)
        if not token:
            raise RuntimeError("OAuth token response missing access_token")
        OAUTH_TOKEN_CACHE[cache_key] = (token, expiry)
        return {"Authorization": f"Bearer {token}"}

    raise RuntimeError("OAuth configuration incomplete")


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

    headers = None

    if not url:
        findings["errors"].append("Target is missing a 'url' field — skipping")
        return findings

    # Normalize transport aliases (typos or slightly different names from registries)
    transport_aliases = {
        "steamable-http": "streamable-http",
        "streamable_http": "streamable-http",
        "sse": "sse",
    }

    if target.get("auth_type") == "oauth":
        # Attempt to obtain OAuth headers; errors are recorded but scanning
        # continues where possible so we can still collect metadata.
        try:
            headers = await _get_oauth_headers(target)
        except Exception as e:
            findings["errors"].append(f"OAuth setup failed: {e}")
            # Continue without headers to allow public endpoints to be scanned
            headers = None

    if not headers:
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
    transport_type = transport_aliases.get(transport_type, transport_type)

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
        # Reuse an AsyncClient per call to avoid repeated connection setup
        async with httpx2.AsyncClient(headers=headers, timeout=httpx2.Timeout(30.0, read=300.0), follow_redirects=True) as http_client:
            async with streamable_http_client(url, http_client=http_client) as endpoints:
                # endpoints may be a tuple/list of (read, write, ...) or an object.
                if isinstance(endpoints, (tuple, list)):
                    read, write = endpoints[0], endpoints[1]
                else:
                    read = getattr(endpoints, "read", endpoints)
                    write = getattr(endpoints, "write", None)
                async with ClientSession(read, write) as session:
                    await session.initialize()
                    await _collect_tools(session, findings)

    elif transport_type == "sse":
        async with sse_client(url, headers=headers, timeout=5.0, sse_read_timeout=300.0) as endpoints:
            if isinstance(endpoints, (tuple, list)):
                read, write = endpoints[0], endpoints[1]
            else:
                read = getattr(endpoints, "read", endpoints)
                write = getattr(endpoints, "write", None)
            async with ClientSession(read, write) as session:
                await session.initialize()
                await _collect_tools(session, findings)

    else:
        errors.append(f"Unsupported transport type: {transport_type}")


async def _collect_tools(session: ClientSession, findings: dict) -> None:
    result = await session.list_tools()
    tools_iter = getattr(result, "tools", result)
    for tool in tools_iter:
        # Tool objects from different MCP clients may have different shapes.
        name = getattr(tool, "name", None) or tool.get("name") if isinstance(tool, dict) else None
        description = getattr(tool, "description", None) or tool.get("description") if isinstance(tool, dict) else ""
        input_schema = getattr(tool, "input_schema", None) or tool.get("input_schema") if isinstance(tool, dict) else {}
        findings["tools"].append({
            "name": name,
            "description": description,
            "input_schema": input_schema,
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