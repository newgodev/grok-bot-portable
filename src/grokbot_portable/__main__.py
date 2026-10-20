"""CLI entry: python -m grokbot_portable demo"""

from __future__ import annotations

import sys


def main(argv: list[str] | None = None) -> int:
    args = list(sys.argv[1:] if argv is None else argv)
    if not args or args[0] in ("-h", "--help", "help"):
        print("Usage: python -m grokbot_portable demo")
        print("  demo  — print how files=SSOT / INF works")
        return 0
    cmd = args[0]
    if cmd == "demo":
        from grokbot_portable.demo import run_demo

        return run_demo()
    print(f"Unknown command: {cmd}", file=sys.stderr)
    print("Usage: python -m grokbot_portable demo", file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
