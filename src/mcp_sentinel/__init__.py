def main() -> None:
    print("Hello from mcp-sentinel!")


def _package_main() -> None:
    # kept minimal; scanner is the normal entrypoint
    from . import scanner
    scanner_main = getattr(scanner, '__main__', None)
    if scanner_main and hasattr(scanner_main, 'main'):
        scanner_main.main()
    else:
        scanner.main()
