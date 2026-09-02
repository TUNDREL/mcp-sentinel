from .scanner import main as _scanner_main


def main():
    # Expose a module-level main so `python -m mcp_sentinel.scanner` works
    # when the package is run from the repository root.
    _scanner_main()


if __name__ == "__main__":
    main()
