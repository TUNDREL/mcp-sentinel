"""Security rules for auditing MCP servers.

Each rule takes either a server-level `findings` dict or an individual
`tool` dict (as produced by scanner.py) and returns an issue dict if it
fires, or None if the check passes clean.
"""
from .semantic import batch_check_semantic_similarity

# Verbs that suggest a tool can take destructive or high-privilege action.
# Presence alone isn't proof of danger — it's a signal worth a human look.
RISKY_VERBS = (
    "delete", "remove", "drop", "destroy", "wipe",
    "write", "create", "update", "modify", "edit",
    "exec", "execute", "run", "eval", "shell",
    "admin", "sudo", "root", "override", "bypass",
)

# Phrases that show up in known prompt-injection / tool-poisoning attempts —
# instructions aimed at the *model*, hidden inside a tool description rather
# than at the human operator.
SUSPICIOUS_PATTERNS = (
    ("ignore previous", None),
    ("ignore all previous", None),
    ("disregard the", None),
    ("do not tell the user", None),
    ("do not inform", None),
    ("without telling", None),
    ("without confirming", None),
    ("without asking", None),
    ("silently", None),
    ("do not mention", None),
    ("hide this from", None),
    ("system prompt", None),
    ("act as", None),
    ("you are now", None),
    # These require nearby context about the USER or CONFIRMATION,
    # not just any use of the word — avoids false positives like game
    # mechanics that legitimately "bypass" a rule or limit.
    ("bypass", ("user", "confirm", "consent", "approval", "tell", "notify", "ask")),
)

RISKY_PARAM_HINTS = (
    "url", "uri", "path", "file", "command", "cmd",
    "query", "sql", "script", "code", "shell", "eval", "exec",
)

# ---------- Server-level rules ----------

def check_missing_auth(target: dict) -> dict | None:
    """Flags servers that accept unauthenticated connections."""
    if not target.get("requires_auth"):
        return {
            "rule": "missing_auth",
            "severity": "medium",
            "scope": "server",
            "detail": "Server accepts unauthenticated connections — anyone with "
                       "the URL can invoke its tools.",
        }
    return None


def check_insecure_transport(target: dict) -> dict | None:
    """Flags servers reachable over plain HTTP instead of HTTPS/WSS."""
    url = target.get("url", "")
    if url.startswith("http://") or url.startswith("ws://"):
        return {
            "rule": "insecure_transport",
            "severity": "high",
            "scope": "server",
            "detail": "Server is reachable over an unencrypted connection — "
                      "credentials and data in transit are exposed.",
        }
    return None


# ---------- Tool-level rules ----------

def check_broad_scope(tool: dict) -> dict | None:
    """Flags tools whose name suggests write/destructive capability."""
    name = (tool.get("name") or "").lower()
    hit = next((v for v in RISKY_VERBS if v in name), None)
    if hit:
        return {
            "rule": "broad_scope",
            "severity": "high",
            "scope": "tool",
            "tool": tool.get("name"),
            "detail": f"Tool name contains '{hit}', suggesting write or "
                      f"destructive capability.",
        }
    return None


def check_suspicious_description(tool: dict) -> dict | None:
    """Flags tool descriptions containing prompt-injection style phrasing —
    instructions aimed at manipulating the calling model, not the user."""
    desc = (tool.get("description") or "").lower()

    for phrase, required_context in SUSPICIOUS_PATTERNS:
        if phrase not in desc:
            continue
        if required_context is None:
            hit = phrase
        else:
            idx = desc.find(phrase)
            window = desc[max(0, idx - 80): idx + 80]
            if not any(ctx in window for ctx in required_context):
                continue
            hit = phrase
        return {
            "rule": "suspicious_description",
            "severity": "critical",
            "scope": "tool",
            "tool": tool.get("name"),
            "detail": f"Description contains manipulative phrasing: '{hit}'. "
                      f"This is a known tool-poisoning pattern.",
        }
    return None


def check_missing_description(tool: dict) -> dict | None:
    """Flags tools with no description at all — the model has to guess what
    they do, and so does a human auditor."""
    desc = tool.get("description")
    if not desc or not desc.strip():
        return {
            "rule": "missing_description",
            "severity": "low",
            "scope": "tool",
            "tool": tool.get("name"),
            "detail": "Tool has no description — behavior is undocumented.",
        }
    return None


def check_unconstrained_schema(tool: dict) -> dict | None:
    """Flags tools whose input schema allows unconstrained strings in
    parameters where that's a genuine injection/traversal risk — not
    every free-text field, since IDs and names are normally unconstrained
    by design."""
    schema = tool.get("input_schema") or {}
    properties = schema.get("properties", {})

    for param_name, param_schema in properties.items():
        if not isinstance(param_schema, dict):
            continue
        if not any(hint in param_name.lower() for hint in RISKY_PARAM_HINTS):
            continue
        if param_schema.get("type") == "string" and not any(
            k in param_schema for k in ("enum", "pattern", "maxLength", "format")
        ):
            return {
                "rule": "unconstrained_schema",
                "severity": "medium",
                "scope": "tool",
                "tool": tool.get("name"),
                "detail": f"Parameter '{param_name}' looks like it could accept "
                          f"paths/commands/queries with no validation.",
            }
    return None


# ---------- Rule runner ----------

# Semantic similarity is intentionally NOT in this tuple — it now runs once
# per server as a single batched call in evaluate() below, not once per
# tool inside the per-tool loop.
SERVER_RULES = (check_missing_auth, check_insecure_transport)
TOOL_RULES = (
    check_broad_scope,
    check_suspicious_description,
    check_missing_description,
    check_unconstrained_schema,
)


def evaluate(target: dict, findings: dict) -> list[dict]:
    """Runs all rules against a scanned server's findings and returns the
    combined list of issues. Called after scan_server() in scanner.py."""
    issues: list[dict] = []

    for rule in SERVER_RULES:
        result = rule(target)
        if result:
            issues.append(result)

    tools = findings.get("tools", [])

    for tool in tools:
        for rule in TOOL_RULES:
            result = rule(tool)
            if result:
                issues.append(result)

    # Batched semantic check — one embedding call for the whole server's
    # tool list, not one call per tool.
    semantic_hits = batch_check_semantic_similarity(tools)
    issues.extend(semantic_hits.values())

    return issues