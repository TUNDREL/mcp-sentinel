def main() -> None:
    # Package entrypoint: delegate to the scanner's main() so the installed
    # `mcp-sentinel` CLI runs the real scanner behavior.
    from . import scanner
    if hasattr(scanner, "main") and callable(getattr(scanner, "main")):
        scanner.main()
    else:
        # Fallback: run scanner module as a script
        import runpy
        runpy.run_module("mcp_sentinel.scanner", run_name="__main__")
