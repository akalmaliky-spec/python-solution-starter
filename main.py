#!/usr/bin/env python3
"""Main solution entrypoint.

- Reads from standard input
- Writes to standard output
- Designed for competitive programming / coding challenges
"""

import sys
from typing import List, Tuple, Optional


def read_input() -> str:
    """
    Read all input from stdin as a single string.
    Adjust this to parse the specific problem format.
    """
    data = sys.stdin.read().strip()
    return data


def solve(raw_input: str) -> str:
    """
    Core solver.

    Replace the body of this function with your problem-specific logic.
    It should be a pure function: input → output (as string).
    """
    # TODO: parse input
    # Example: lines = raw_input.splitlines()

    # TODO: implement logic
    # Example (echo input):
    result = raw_input

    # TODO: format output
    return result


def main() -> None:
    """Entrypoint for CLI execution."""
    raw_input = read_input()
    answer = solve(raw_input)
    # Ensure trailing newline for judges that require it
    sys.stdout.write(str(answer).rstrip() + "\n")


if __name__ == "__main__":
    main()
