"""Command-line interface for jaclang calculator example."""
from __future__ import annotations

import argparse
import sys
from . import evaluate


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="jaclang-calc")
    parser.add_argument("expression", nargs="?", help="Arithmetic expression to evaluate")
    args = parser.parse_args(argv)

    expr = args.expression
    if not expr:
        # read from stdin
        expr = sys.stdin.read().strip()
    if not expr:
        print("No expression provided", file=sys.stderr)
        return 2

    try:
        result = evaluate(expr)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1

    print(result)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
