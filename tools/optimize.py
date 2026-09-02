"""Optimization harness: measures accuracy, speed, and compatibility.

Usage: run this script to compute metrics and append results to summary.md.
It will attempt to run the scanner command the user specified and also run
local, deterministic evaluations against `tests/ground_truth.json`.
"""
import json
import os
import sys
import time
import subprocess
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SUMMARY = ROOT / "summary.md"
GROUND = ROOT / "tests" / "ground_truth.json"


def load_ground_truth():
    with open(GROUND, "r", encoding="utf-8") as f:
        return json.load(f)


def evaluate_rules_accuracy():
    """Run the project's `rules.evaluate` on the ground truth fixture.
    Returns detection metrics and timing.
    """
    try:
        sys.path.insert(0, str(ROOT / "src"))
        from mcp_sentinel import rules
    except Exception as e:
        return {"error": f"Could not import rules: {e}"}

    data = load_ground_truth()
    server = data["server"].copy()
    tools = data["tools"]

    findings = {"tools": [], "errors": []}
    for t in tools:
        findings["tools"].append({
            "name": t["name"],
            "description": t["description"],
            "input_schema": t.get("input_schema", {}),
        })

    start = time.perf_counter()
    issues = rules.evaluate(server, findings)
    duration = time.perf_counter() - start

    # Map tool -> flagged
    flagged = {i.get("tool"): i for i in issues if i.get("scope") == "tool"}

    tp = fp = fn = 0
    for t in tools:
        expected = bool(t.get("malicious"))
        predicted = bool(flagged.get(t["name"]))
        if predicted and expected:
            tp += 1
        elif predicted and not expected:
            fp += 1
        elif not predicted and expected:
            fn += 1

    precision = tp / (tp + fp) if tp + fp else 0.0
    recall = tp / (tp + fn) if tp + fn else 0.0
    f1 = (2 * precision * recall) / (precision + recall) if precision + recall else 0.0

    return {
        "tp": tp,
        "fp": fp,
        "fn": fn,
        "precision": precision,
        "recall": recall,
        "f1": f1,
        "eval_time_s": duration,
        "issues_count": len(issues),
    }


def measure_semantic_speed():
    # Run the semantic check in a subprocess to avoid long model downloads
    data = load_ground_truth()
    descriptions = [t["description"] for t in data["tools"] if t["description"].strip()]
    if not descriptions:
        return {"error": "No descriptions to encode in ground truth"}

    runner_code = (
        "import json, time, sys\n"
        "sys.path.insert(0, 'src')\n"
        "from mcp_sentinel import semantic\n"
        "descs = json.loads('" + json.dumps(descriptions).replace("'", "\\'") + "')\n"
        "tools = [{'name': f't{i}', 'description': d} for i,d in enumerate(descs)]\n"
        "start = time.perf_counter()\n"
        "try:\n"
        "    res = semantic.batch_check_semantic_similarity(tools)\n"
        "    dur = time.perf_counter() - start\n"
        "    print(dur)\n"
        "except Exception as e:\n"
        "    print('ERROR:'+str(e))\n"
    )

    try:
        proc = subprocess.run([sys.executable, "-c", runner_code], capture_output=True, text=True, timeout=int(os.getenv("MCP_SENTINEL_SEMANTIC_TIMEOUT", "120")))
        out = proc.stdout.strip()
        if out.startswith("ERROR:"):
            return {"error": out[len("ERROR:"):], "stderr": proc.stderr}
        try:
            duration = float(out.splitlines()[-1])
        except Exception:
            return {"error": "could not parse semantic runner output", "stdout": out, "stderr": proc.stderr}
        return {"semantic_batch_time_s": duration, "runner_stdout": out}
    except subprocess.TimeoutExpired:
        return {"error": "semantic runner timed out"}


def check_compatibility():
    deps = [
        "google.genai",
        "httpx2",
        "mcp",
        "sentence_transformers",
        "rich",
        "dotenv",
    ]
    missing = []
    for d in deps:
        try:
            __import__(d.split(".")[0])
        except Exception:
            missing.append(d)

    # Try running the scanner command the user specified (with a timeout)
    # Prefer a direct python invocation; the user's `uv` wrapper may not be present.
    cmd = [sys.executable, "-m", "mcp_sentinel.scanner"]
    try_cmd = True
    run_result = {}
    if try_cmd:
        start = time.perf_counter()
        try:
            env = os.environ.copy()
            # Ensure the package src is importable when running as a module from repo root
            env["PYTHONPATH"] = str(ROOT / "src")
            proc = subprocess.run(cmd, cwd=str(ROOT), capture_output=True, text=True, timeout=int(os.getenv("MCP_SENTINEL_SCANNER_TIMEOUT", "120")), env=env)
            run_result["returncode"] = proc.returncode
            run_result["stdout"] = proc.stdout[:4000]
            run_result["stderr"] = proc.stderr[:4000]
        except Exception as e:
            run_result["error"] = str(e)
        run_result["run_time_s"] = time.perf_counter() - start

    # Check whether scan_report.md exists
    scan_report = ROOT / "scan_report.md"
    run_result["scan_report_exists"] = scan_report.exists()

    return {"missing_deps": missing, "scanner_run": run_result}


def append_summary(note: str, metrics: dict):
    ts = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    with open(SUMMARY, "a", encoding="utf-8") as f:
        f.write(f"## {ts} — {note}\n\n")
        f.write("```")
        json.dump(metrics, f, indent=2)
        f.write("``""\n\n")


def main():
    summary_header = "# Optimization run summary\n\n"
    if not SUMMARY.exists():
        SUMMARY.write_text(summary_header)

    label = sys.argv[1] if len(sys.argv) > 1 else os.getenv("MCP_SENTINEL_RUN_LABEL", "Run")

    # For speed runs set environment to use a small embedding and enable cache
    os.environ.setdefault("MCP_SENTINEL_EMBED_MODEL", os.getenv("MCP_SENTINEL_EMBED_MODEL", "all-MiniLM-L6-v2"))
    os.environ.setdefault("MCP_SENTINEL_EMBED_CACHE_DIR", os.getenv("MCP_SENTINEL_EMBED_CACHE_DIR", ""))

    res_rules = evaluate_rules_accuracy()
    res_sem = measure_semantic_speed()
    res_comp = check_compatibility()

    metrics = {
        "rules": res_rules,
        "semantic": res_sem,
        "compatibility": res_comp,
    }

    append_summary(label, metrics)
    print(f"{label} metrics written to summary.md")


if __name__ == "__main__":
    main()
