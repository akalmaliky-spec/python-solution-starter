"""
Solution starter for coding problems.

This module provides a template for solving coding challenges with:
- Type hints for clarity
- Proper docstrings
- stdin/stdout handling
- Easy testing interface
"""


def solve(input_data: str) -> str:
    """
    Main solution function.

    Args:
        input_data: Raw input as a string (e.g., from stdin)

    Returns:
        The solution result as a string

    Examples:
        >>> solve("3\\n1 2 3")
        '6'
    """
    # ============ PLUG YOUR SOLUTION LOGIC HERE ============
    # Parse input
    lines = input_data.strip().split("\n")
    numbers = list(map(int, lines[1].split()))

    # TODO: Replace this with your actual solution logic
    result = sum(numbers)

    # ========================================================
    return str(result)


def main() -> None:
    """
    Entry point for reading from stdin and printing to stdout.

    Reads all input, passes it to solve(), and prints the result.
    """
    import sys

    input_data = sys.stdin.read()
    output = solve(input_data)
    print(output)


if __name__ == "__main__":
    main()
