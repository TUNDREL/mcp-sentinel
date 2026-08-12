"""Turns raw scan results into a readable terminal summary and a
shareable Markdown report."""

from datetime import datetime, timezone

from rich.console import Console
from rich.table import Table

console = Console()

SEVERITY_ORDER = {"critical": 0, "high": 1, "medium": 2, "low": 3}
SEVERITY_COLOR = {
    "critical": "bold red",
    "high": "red",
    "medium": "yellow",
    "low": "dim",
}


def print_summary_table(results: list[dict]) -> None:
    """Renders a clean, colored overview table straight to the terminal."""
    table = Table(title="MCP Sentinel — Scan Summary")
    table.add_column("Server")
    table.add_column("Status")
    table.add_column("Tools", justify="right")
    table.add_column("Issues", justify="right")
    table.add_column("Highest Severity")

    for r in results:
        status = "OK" if not r["errors"] else "FAILED"
        status_style = "green" if status == "OK" else "red"

        issues = r.get("issues", [])
        highest = min(
            (issues if issues else [{"severity": "none"}]),
            key=lambda i: SEVERITY_ORDER.get(i["severity"], 99),
        )["severity"]
        highest_style = SEVERITY_COLOR.get(highest, "white")

        table.add_row(
            r["name"],
            f"[{status_style}]{status}[/{status_style}]",
            str(len(r["tools"])),
            str(len(issues)),
            f"[{highest_style}]{highest.upper()}[/{highest_style}]",
        )

    console.print(table)


def _severity_counts(results: list[dict]) -> dict[str, int]:
    counts = {"critical": 0, "high": 0, "medium": 0, "low": 0}
    for r in results:
        for issue in r.get("issues", []):
            sev = issue.get("severity", "low")
            counts[sev] = counts.get(sev, 0) + 1
    return counts


def generate_markdown_report(results: list[dict], output_path: str = "scan_report.md") -> str:
    """Writes a full Markdown audit report and returns the file path."""
    scanned = len(results)
    successful = sum(1 for r in results if not r["errors"])
    total_tools = sum(len(r["tools"]) for r in results)
    counts = _severity_counts(results)
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    lines = [
        "# MCP Sentinel — Security Audit Report",
        f"*Generated {timestamp}*",
        "",
        "## Summary",
        f"- **Servers scanned:** {scanned}",
        f"- **Successfully connected:** {successful}",
        f"- **Total tools analyzed:** {total_tools}",
        f"- **Findings:** {counts['critical']} critical, {counts['high']} high, "
        f"{counts['medium']} medium, {counts['low']} low",
        "",
        "## Server Details",
    ]

    for r in results:
        lines.append(f"\n### {r['name']}")
        lines.append(f"URL: `{r['url']}`")

        if r["errors"]:
            lines.append(f"\n**Status: Failed to connect**")
            for err in r["errors"]:
                lines.append(f"- {err}")
            continue

        lines.append(f"\n**Status: OK** — {len(r['tools'])} tools found")

        issues = sorted(
            r.get("issues", []),
            key=lambda i: SEVERITY_ORDER.get(i["severity"], 99),
        )
        if not issues:
            lines.append("\nNo issues flagged.")
        else:
            lines.append("\n**Findings:**")
            for issue in issues:
                tool_ref = f" (`{issue['tool']}`)" if issue.get("tool") else ""
                lines.append(
                    f"- **[{issue['severity'].upper()}]** {issue['rule']}{tool_ref} — {issue['detail']}"
                )

    report_text = "\n".join(lines)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(report_text)

    return output_path