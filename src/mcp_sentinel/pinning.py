"""Tool pinning / rug-pull detection.

Computes a deterministic hash of each tool's identity (name, description,
input schema) and compares it against a locally stored lockfile from a
previous scan of the same server. If a tool's definition has changed since
it was last seen, that's flagged — a server that looked safe when first
approved, then silently altered its tool contract afterward, is a known
real attack pattern ("rug pull"), not just a theoretical concern.

The lockfile (mcp-lock.json) should be committed to git, not gitignored —
like a package-lock.json, it's meant to be a shared "last known good"
baseline across the whole team, not a personal local cache. Whoever runs
the scan next will detect drift regardless of who ran it last.
"""

import hashlib
import json
import os
from pathlib import Path

LOCKFILE_PATH = os.getenv("MCP_SENTINEL_LOCKFILE", "mcp-lock.json")


def _tool_hash(tool: dict) -> str:
    """Deterministic hash of a tool's identity-relevant fields."""
    canonical = json.dumps(
        {
            "name": tool.get("name"),
            "description": tool.get("description"),
            "input_schema": tool.get("input_schema"),
        },
        sort_keys=True,
    )
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()


def _load_lockfile() -> dict:
    path = Path(LOCKFILE_PATH)
    if not path.exists():
        return {}
    try:
        with open(path) as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        return {}


def _save_lockfile(lockfile: dict) -> None:
    with open(LOCKFILE_PATH, "w") as f:
        json.dump(lockfile, f, indent=2, sort_keys=True)


def check_and_update_pins(server_name: str, tools: list[dict]) -> list[dict]:
    """Compares this scan's tools against the stored lockfile entry for
    this server. Returns issue dicts for anything that changed since the
    last recorded scan, then updates the lockfile with current hashes.

    First-ever scan of a server produces no findings (nothing to compare
    against yet) — it just establishes the baseline for next time.
    """
    if not tools:
        return []  # nothing to hash if the server didn't return tools

    lockfile = _load_lockfile()
    previous_hashes = lockfile.get(server_name, {})
    issues = []
    current_hashes = {}

    for tool in tools:
        name = tool.get("name") or "unnamed-tool"
        current_hash = _tool_hash(tool)
        current_hashes[name] = current_hash

        previous_hash = previous_hashes.get(name)
        if previous_hash is not None and previous_hash != current_hash:
            issues.append({
                "rule": "rug_pull_detected",
                "severity": "critical",
                "scope": "tool",
                "tool": name,
                "detail": (
                    f"Tool '{name}' definition changed since the last scan "
                    f"of this server. This could be a legitimate update, "
                    f"or a server that changed behavior after being "
                    f"trusted — a known 'rug pull' attack pattern. Review "
                    f"the change before continuing to trust this tool."
                ),
            })

    # Tools present before but missing now — lower severity, still worth
    # knowing since it's a change in the server's surface area.
    removed = set(previous_hashes.keys()) - set(current_hashes.keys())
    for name in removed:
        issues.append({
            "rule": "tool_removed",
            "severity": "low",
            "scope": "tool",
            "tool": name,
            "detail": f"Tool '{name}' was present in a previous scan but is no longer offered.",
        })

    lockfile[server_name] = current_hashes
    _save_lockfile(lockfile)

    return issues