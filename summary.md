# Optimization Summary

This file will record metrics and results after each optimization iteration.
## 2026-09-01 15:04:17 UTC — Baseline metrics

```{
  "rules": {
    "tp": 2,
    "fp": 1,
    "fn": 0,
    "precision": 0.6666666666666666,
    "recall": 1.0,
    "f1": 0.8,
    "eval_time_s": 12.789890000014566,
    "issues_count": 5
  },
  "semantic": {
    "semantic_batch_time_s": 0.01320700001087971
  },
  "compatibility": {
    "missing_deps": [],
    "scanner_run": {
      "error": "Command '['uv', 'run', 'python', '-m', 'mcp_sentinel.scanner']' timed out after 60 seconds",
      "run_time_s": 257.98118609999074,
      "scan_report_exists": true
    }
  }
}``

## 2026-09-01 15:06:57 UTC — Baseline metrics

```{
  "rules": {
    "tp": 2,
    "fp": 1,
    "fn": 0,
    "precision": 0.6666666666666666,
    "recall": 1.0,
    "f1": 0.8,
    "eval_time_s": 12.579369199986104,
    "issues_count": 5
  },
  "semantic": {
    "semantic_batch_time_s": 15.117814199998975,
    "runner_stdout": "15.117814199998975"
  },
  "compatibility": {
    "missing_deps": [],
    "scanner_run": {
      "returncode": 1,
      "stdout": "",
      "stderr": "C:\\Users\\MACHENIKE\\AppData\\Local\\Programs\\Python\\Python314\\python.exe: Error while finding module specification for 'mcp_sentinel.scanner' (ModuleNotFoundError: No module named 'mcp_sentinel')\n",
      "run_time_s": 0.1561183999874629,
      "scan_report_exists": true
    }
  }
}``

## 2026-09-01 15:16:20 UTC — Baseline metrics

```{
  "rules": {
    "tp": 2,
    "fp": 1,
    "fn": 0,
    "precision": 0.6666666666666666,
    "recall": 1.0,
    "f1": 0.8,
    "eval_time_s": 14.403795699996408,
    "issues_count": 7
  },
  "semantic": {
    "semantic_batch_time_s": 10.33052850002423,
    "runner_stdout": "10.33052850002423"
  },
  "compatibility": {
    "missing_deps": [],
    "scanner_run": {
      "returncode": 1,
      "stdout": "",
      "stderr": "C:\\Users\\MACHENIKE\\AppData\\Local\\Programs\\Python\\Python314\\python.exe: Error while finding module specification for 'mcp_sentinel.scanner' (ModuleNotFoundError: No module named 'mcp_sentinel')\n",
      "run_time_s": 0.06371369998669252,
      "scan_report_exists": true
    }
  }
}``

## 2026-09-01 15:22:13 UTC — Baseline metrics

```{
  "rules": {
    "tp": 2,
    "fp": 1,
    "fn": 0,
    "precision": 0.6666666666666666,
    "recall": 1.0,
    "f1": 0.8,
    "eval_time_s": 12.767688799998723,
    "issues_count": 7
  },
  "semantic": {
    "semantic_batch_time_s": 13.286935099982657,
    "runner_stdout": "13.286935099982657"
  },
  "compatibility": {
    "missing_deps": [],
    "scanner_run": {
      "returncode": 1,
      "stdout": "",
      "stderr": "C:\\Users\\MACHENIKE\\AppData\\Local\\Programs\\Python\\Python314\\python.exe: Error while finding module specification for 'mcp_sentinel.scanner' (ModuleNotFoundError: No module named 'mcp_sentinel')\n",
      "run_time_s": 0.0636538999970071,
      "scan_report_exists": true
    }
  }
}``

## 2026-09-01 15:36:45 UTC — Baseline metrics

```{
  "rules": {
    "tp": 2,
    "fp": 1,
    "fn": 0,
    "precision": 0.6666666666666666,
    "recall": 1.0,
    "f1": 0.8,
    "eval_time_s": 15.942985899979249,
    "issues_count": 7
  },
  "semantic": {
    "error": "semantic runner timed out"
  },
  "compatibility": {
    "missing_deps": [],
    "scanner_run": {
      "returncode": 1,
      "stdout": "",
      "stderr": "C:\\Users\\MACHENIKE\\AppData\\Local\\Programs\\Python\\Python314\\python.exe: Error while finding module specification for 'mcp_sentinel.scanner' (ModuleNotFoundError: No module named 'mcp_sentinel')\n",
      "run_time_s": 0.06304759997874498,
      "scan_report_exists": true
    }
  }
}``

## 2026-09-01 15:43:01 UTC — Compatibility+OAuth+ModelConfig

```{
  "rules": {
    "tp": 2,
    "fp": 1,
    "fn": 0,
    "precision": 0.6666666666666666,
    "recall": 1.0,
    "f1": 0.8,
    "eval_time_s": 12.012688799994066,
    "issues_count": 7
  },
  "semantic": {
    "semantic_batch_time_s": 13.477663800003938,
    "runner_stdout": "13.477663800003938"
  },
  "compatibility": {
    "missing_deps": [],
    "scanner_run": {
      "returncode": 1,
      "stdout": "Scanning DeepWiki MCP...\nScanning GitMCP Docs...\nScanning 402.bot MCP...\nScanning BGPT Science MCP...\nScanning Find-A-Domain MCP...\nScanning Peek.com MCP...\nScanning Context Awesome...\nScanning Cloudflare Authless Remote Demo...\nScanning Cloudflare Docs MCP...\nScanning Resemble AI MCP...\nScanning Remote MCP Directory Server...\nScanning OpenMesh MCP...\nScanning JSON Toolkit MCP...\nScanning Regex Engine MCP...\nScanning Color Palette MCP...\nScanning Timestamp Converter MCP...\nScanning Prompt Enhancer MCP...\nScanning OpenClaw Intel MCP...\nScanning OpenClaw Fortune MCP...\nScanning MoltBook Publisher MCP...\nScanning FlowZap Docs MCP...\nScanning Kiwi.com Flight Search MCP...\nScanning SiteSpeak Chatbot MCP...\nScanning Brimble Platform MCP...\nScanning Cloudflare Weather MCP...\nScanning Data.gouv.fr MCP...\nScanning MCP Time Server...\nScanning BotSpot Trading MCP...\nScanning SpaceMolt MCP...\n",
      "stderr": "Traceback (most recent call last):\n  File \"<frozen runpy>\", line 198, in _run_module_as_main\n  File \"<frozen runpy>\", line 88, in _run_code\n  File \"C:\\Users\\MACHENIKE\\Desktop\\mcp-sentinel\\src\\mcp_sentinel\\scanner.py\", line 262, in <module>\n    all_results = asyncio.run(scan_all(), loop_factory=loop_factory)\n  File \"C:\\Users\\MACHENIKE\\AppData\\Local\\Programs\\Python\\Python314\\Lib\\asyncio\\runners.py\", line 204, in run\n    return runner.run(main)\n           ~~~~~~~~~~^^^^^^\n  File \"C:\\Users\\MACHENIKE\\AppData\\Local\\Programs\\Python\\Python314\\Lib\\asyncio\\runners.py\", line 127, in run\n    return self._loop.run_until_complete(task)\n           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^\n  File \"C:\\Users\\MACHENIKE\\AppData\\Local\\Programs\\Python\\Python314\\Lib\\asyncio\\base_events.py\", line 719, in run_until_complete\n    return future.result()\n           ~~~~~~~~~~~~~^^\n  File \"C:\\Users\\MACHENIKE\\Desktop\\mcp-sentinel\\src\\mcp_sentinel\\scanner.py\", line 251, in scan_all\n    results = await asyncio.gather(*(scan_one(t) for t in targets))\n              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"C:\\Users\\MACHENIKE\\Desktop\\mcp-sentinel\\src\\mcp_sentinel\\scanner.py\", line 232, in scan_one\n    result = await scan_server(target)\n             ^^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"C:\\Users\\MACHENIKE\\Desktop\\mcp-sentinel\\src\\mcp_sentinel\\scanner.py\", line 129, in scan_server\n    if not headers:\n           ^^^^^^^\nUnboundLocalError: cannot access local variable 'headers' where it is not associated with a value\n",
      "run_time_s": 17.572533799975645,
      "scan_report_exists": true
    }
  }
}``

## 2026-09-01 15:45:22 UTC — Compatibility+OAuth+ModelConfig+Fix

```{
  "rules": {
    "tp": 2,
    "fp": 1,
    "fn": 0,
    "precision": 0.6666666666666666,
    "recall": 1.0,
    "f1": 0.8,
    "eval_time_s": 11.966798900044523,
    "issues_count": 7
  },
  "semantic": {
    "semantic_batch_time_s": 10.292835399974138,
    "runner_stdout": "10.292835399974138"
  },
  "compatibility": {
    "missing_deps": [],
    "scanner_run": {
      "returncode": 0,
      "stdout": "Scanning DeepWiki MCP...\nScanning GitMCP Docs...\nScanning 402.bot MCP...\nScanning BGPT Science MCP...\nScanning Find-A-Domain MCP...\nScanning Peek.com MCP...\nScanning Context Awesome...\nScanning Cloudflare Authless Remote Demo...\nScanning Cloudflare Docs MCP...\nScanning Resemble AI MCP...\nScanning Remote MCP Directory Server...\nScanning OpenMesh MCP...\nScanning JSON Toolkit MCP...\nScanning Regex Engine MCP...\nScanning Color Palette MCP...\nScanning Timestamp Converter MCP...\nScanning Prompt Enhancer MCP...\nScanning OpenClaw Intel MCP...\nScanning OpenClaw Fortune MCP...\nScanning MoltBook Publisher MCP...\nScanning FlowZap Docs MCP...\nScanning Kiwi.com Flight Search MCP...\nScanning SiteSpeak Chatbot MCP...\nScanning Brimble Platform MCP...\nScanning Cloudflare Weather MCP...\nScanning Data.gouv.fr MCP...\nScanning MCP Time Server...\nScanning BotSpot Trading MCP...\nScanning SpaceMolt MCP...\n\n--- Scan Summary ---\n                          MCP Sentinel \u2014 Scan Summary                          \n+-----------------------------------------------------------------------------+\n| Server                         | Status | Tools | Issues | Highest Severity |\n|--------------------------------+--------+-------+--------+------------------|\n| DeepWiki MCP                   | FAILED |     0 |      1 | MEDIUM           |\n| GitMCP Docs                    | FAILED |     0 |      1 | MEDIUM           |\n| 402.bot MCP                    | FAILED |     0 |      1 | MEDIUM           |\n| BGPT Science MCP               | FAILED |     0 |      1 | MEDIUM           |\n| Find-A-Domain MCP              | FAILED |     0 |      1 | MEDIUM           |\n| Peek.com MCP                   | FAILED |     0 |      1 | MEDIUM           |\n| Context Awesome                | FAILED |     0 |      1 | MEDIUM           |\n| Cloudflare Authless Remote     | FAILED |     0 |      1 | MEDIUM           |\n| Demo                           |        |       |        |                  |\n| Cloudflare Docs MCP            | FAILED |     0 |      1 | MEDIUM           |\n| Resemble AI MCP                | FAILED |     0 |      1 | MEDIUM           |\n| Remote MCP Directory Server    | FAILED |     0 |      1 | MEDIUM           |\n| OpenMesh MCP                   | FAILED |     0 |      1 | MEDIUM           |\n| JSON Toolkit MCP               | FAILED |     0 |      1 | MEDIUM           |\n| Regex Engine MCP               | FAILED |     0 |      1 | MEDIUM           |\n| Color Palette MCP              | FAILED |     0 |      1 | MEDIUM           |\n| Timestamp Converter MCP        | FAILED |     0 |      1 | MEDIUM           |\n| Prompt Enhancer MCP            | FAILED |     0 |      1 | MEDIUM           |\n| OpenClaw Intel MCP             | FAILED |     0 |      1 | MEDIUM           |\n| OpenClaw Fortune MCP           | FAILED |     0 |      1 | MEDIUM           |\n| MoltBook Publisher MCP         | FAILED |     0 |      1 | MEDIUM           |\n| FlowZap Docs MCP               | FAILED |     0 |      1 | MEDIUM           |\n| Kiwi.com Flight Search MCP     | FAILED |     0 |      1 | MEDIUM           |\n| SiteSpeak Chatbot MCP          | FAILED |     0 |      1 | MEDIUM           |\n| Brimble Platform MCP           | FAILED |     0 |      1 | MEDIUM           |\n| Cloudflare Weather MCP         | FAILED |     0 |      1 | MEDIUM           |\n| Data.gouv.fr MCP               | FAILED |     0 |      1 | MEDIUM           |\n| MCP Time Server                | FAILED |     0 |      1 | MEDIUM           |\n| BotSpot Trading MCP            | FAILED |     0 |      1 | MEDIUM           |\n| SpaceMolt MCP                  | FAILED |     0 |      1 | MEDIUM           |\n+-----------------------------------------------------------------------------+\n\nFull report written to: scan_report.md\n",
      "stderr": "",
      "run_time_s": 47.682494800013956,
      "scan_report_exists": true
    }
  }
}``

## 2026-09-01 15:54:32 UTC — Speed-iteration-1

```{
  "rules": {
    "tp": 2,
    "fp": 1,
    "fn": 0,
    "precision": 0.6666666666666666,
    "recall": 1.0,
    "f1": 0.8,
    "eval_time_s": 15.741001299989875,
    "issues_count": 7
  },
  "semantic": {
    "semantic_batch_time_s": 11.983068599947728,
    "runner_stdout": "11.983068599947728"
  },
  "compatibility": {
    "missing_deps": [],
    "scanner_run": {
      "returncode": 0,
      "stdout": "Scanning DeepWiki MCP...\nScanning GitMCP Docs...\nScanning 402.bot MCP...\nScanning BGPT Science MCP...\nScanning Find-A-Domain MCP...\nScanning Peek.com MCP...\nScanning Context Awesome...\nScanning Cloudflare Authless Remote Demo...\nScanning Cloudflare Docs MCP...\nScanning Resemble AI MCP...\nScanning Remote MCP Directory Server...\nScanning OpenMesh MCP...\nScanning JSON Toolkit MCP...\nScanning Regex Engine MCP...\nScanning Color Palette MCP...\nScanning Timestamp Converter MCP...\nScanning Prompt Enhancer MCP...\nScanning OpenClaw Intel MCP...\nScanning OpenClaw Fortune MCP...\nScanning MoltBook Publisher MCP...\nScanning FlowZap Docs MCP...\nScanning Kiwi.com Flight Search MCP...\nScanning SiteSpeak Chatbot MCP...\nScanning Brimble Platform MCP...\nScanning Cloudflare Weather MCP...\nScanning Data.gouv.fr MCP...\nScanning MCP Time Server...\nScanning BotSpot Trading MCP...\nScanning SpaceMolt MCP...\n\n--- Scan Summary ---\n                          MCP Sentinel \u2014 Scan Summary                          \n+-----------------------------------------------------------------------------+\n| Server                         | Status | Tools | Issues | Highest Severity |\n|--------------------------------+--------+-------+--------+------------------|\n| DeepWiki MCP                   | FAILED |     0 |      1 | MEDIUM           |\n| GitMCP Docs                    | FAILED |     0 |      1 | MEDIUM           |\n| 402.bot MCP                    | FAILED |     0 |      1 | MEDIUM           |\n| BGPT Science MCP               | FAILED |     0 |      1 | MEDIUM           |\n| Find-A-Domain MCP              | FAILED |     0 |      1 | MEDIUM           |\n| Peek.com MCP                   | FAILED |     0 |      1 | MEDIUM           |\n| Context Awesome                | FAILED |     0 |      1 | MEDIUM           |\n| Cloudflare Authless Remote     | FAILED |     0 |      1 | MEDIUM           |\n| Demo                           |        |       |        |                  |\n| Cloudflare Docs MCP            | FAILED |     0 |      1 | MEDIUM           |\n| Resemble AI MCP                | FAILED |     0 |      1 | MEDIUM           |\n| Remote MCP Directory Server    | FAILED |     0 |      1 | MEDIUM           |\n| OpenMesh MCP                   | FAILED |     0 |      1 | MEDIUM           |\n| JSON Toolkit MCP               | FAILED |     0 |      1 | MEDIUM           |\n| Regex Engine MCP               | FAILED |     0 |      1 | MEDIUM           |\n| Color Palette MCP              | FAILED |     0 |      1 | MEDIUM           |\n| Timestamp Converter MCP        | FAILED |     0 |      1 | MEDIUM           |\n| Prompt Enhancer MCP            | FAILED |     0 |      1 | MEDIUM           |\n| OpenClaw Intel MCP             | FAILED |     0 |      1 | MEDIUM           |\n| OpenClaw Fortune MCP           | FAILED |     0 |      1 | MEDIUM           |\n| MoltBook Publisher MCP         | FAILED |     0 |      1 | MEDIUM           |\n| FlowZap Docs MCP               | FAILED |     0 |      1 | MEDIUM           |\n| Kiwi.com Flight Search MCP     | FAILED |     0 |      1 | MEDIUM           |\n| SiteSpeak Chatbot MCP          | FAILED |     0 |      1 | MEDIUM           |\n| Brimble Platform MCP           | FAILED |     0 |      1 | MEDIUM           |\n| Cloudflare Weather MCP         | FAILED |     0 |      1 | MEDIUM           |\n| Data.gouv.fr MCP               | FAILED |     0 |      1 | MEDIUM           |\n| MCP Time Server                | FAILED |     0 |      1 | MEDIUM           |\n| BotSpot Trading MCP            | FAILED |     0 |      1 | MEDIUM           |\n| SpaceMolt MCP                  | FAILED |     0 |      1 | MEDIUM           |\n+-----------------------------------------------------------------------------+\n\nFull report written to: scan_report.md\n",
      "stderr": "",
      "run_time_s": 44.60471929999767,
      "scan_report_exists": true
    }
  }
}``

## 2026-09-01 16:24:52 UTC — Speed-iteration-2

```{
  "rules": {
    "tp": 2,
    "fp": 1,
    "fn": 0,
    "precision": 0.6666666666666666,
    "recall": 1.0,
    "f1": 0.8,
    "eval_time_s": 15.387466999993194,
    "issues_count": 7
  },
  "semantic": {
    "semantic_batch_time_s": 14.461504000006244,
    "runner_stdout": "14.461504000006244"
  },
  "compatibility": {
    "missing_deps": [],
    "scanner_run": {
      "returncode": 0,
      "stdout": "Scanning DeepWiki MCP...\nScanning GitMCP Docs...\nScanning 402.bot MCP...\nScanning BGPT Science MCP...\nScanning Find-A-Domain MCP...\nScanning Peek.com MCP...\nScanning Context Awesome...\nScanning Cloudflare Authless Remote Demo...\nScanning Cloudflare Docs MCP...\nScanning Resemble AI MCP...\nScanning Remote MCP Directory Server...\nScanning OpenMesh MCP...\nScanning JSON Toolkit MCP...\nScanning Regex Engine MCP...\nScanning Color Palette MCP...\nScanning Timestamp Converter MCP...\nScanning Prompt Enhancer MCP...\nScanning OpenClaw Intel MCP...\nScanning OpenClaw Fortune MCP...\nScanning MoltBook Publisher MCP...\nScanning FlowZap Docs MCP...\nScanning Kiwi.com Flight Search MCP...\nScanning SiteSpeak Chatbot MCP...\nScanning Brimble Platform MCP...\nScanning Cloudflare Weather MCP...\nScanning Data.gouv.fr MCP...\nScanning MCP Time Server...\nScanning BotSpot Trading MCP...\nScanning SpaceMolt MCP...\n\n--- Scan Summary ---\n                          MCP Sentinel \u2014 Scan Summary                          \n+-----------------------------------------------------------------------------+\n| Server                         | Status | Tools | Issues | Highest Severity |\n|--------------------------------+--------+-------+--------+------------------|\n| DeepWiki MCP                   | OK     |     3 |      4 | MEDIUM           |\n| GitMCP Docs                    | OK     |     5 |      6 | MEDIUM           |\n| 402.bot MCP                    | FAILED |     0 |      1 | MEDIUM           |\n| BGPT Science MCP               | FAILED |     0 |      1 | MEDIUM           |\n| Find-A-Domain MCP              | OK     |     2 |      3 | MEDIUM           |\n| Peek.com MCP                   | OK     |     6 |      7 | MEDIUM           |\n| Context Awesome                | OK     |     2 |      3 | MEDIUM           |\n| Cloudflare Authless Remote     | FAILED |     0 |      1 | MEDIUM           |\n| Demo                           |        |       |        |                  |\n| Cloudflare Docs MCP            | FAILED |     0 |      1 | MEDIUM           |\n| Resemble AI MCP                | OK     |     6 |      7 | MEDIUM           |\n| Remote MCP Directory Server    | OK     |     1 |      2 | MEDIUM           |\n| OpenMesh MCP                   | FAILED |     0 |      1 | MEDIUM           |\n| JSON Toolkit MCP               | FAILED |     0 |      1 | MEDIUM           |\n| Regex Engine MCP               | FAILED |     0 |      1 | MEDIUM           |\n| Color Palette MCP              | FAILED |     0 |      1 | MEDIUM           |\n| Timestamp Converter MCP        | FAILED |     0 |      1 | MEDIUM           |\n| Prompt Enhancer MCP            | FAILED |     0 |      1 | MEDIUM           |\n| OpenClaw Intel MCP             | FAILED |     0 |      1 | MEDIUM           |\n| OpenClaw Fortune MCP           | FAILED |     0 |      1 | MEDIUM           |\n| MoltBook Publisher MCP         | FAILED |     0 |      1 | MEDIUM           |\n| FlowZap Docs MCP               | FAILED |     0 |      1 | MEDIUM           |\n| Kiwi.com Flight Search MCP     | OK     |     2 |      3 | MEDIUM           |\n| SiteSpeak Chatbot MCP          | FAILED |     0 |      1 | MEDIUM           |\n| Brimble Platform MCP           | FAILED |     0 |      1 | MEDIUM           |\n| Cloudflare Weather MCP         | OK     |     2 |      3 | MEDIUM           |\n| Data.gouv.fr MCP               | OK     |    10 |     11 | MEDIUM           |\n| MCP Time Server                | FAILED |     0 |      1 | MEDIUM           |\n| BotSpot Trading MCP            | FAILED |     0 |      1 | MEDIUM           |\n| SpaceMolt MCP                  | OK     |   219 |    220 | MEDIUM           |\n+-----------------------------------------------------------------------------+\n\nFull report written to: scan_report.md\n",
      "stderr": "",
      "run_time_s": 60.02918830001727,
      "scan_report_exists": true
    }
  }
}``

