"""Unit tests for the solution."""

import unittest
from main import solve, helper_function


class TestSolution(unittest.TestCase):
    """Test cases for the solution module."""

    def test_solve_returns_string(self):
        """Test that solve() returns a string."""
        result = solve()
        self.assertIsInstance(result, str)

    def test_solve_not_empty(self):
        """Test that solve() returns a non-empty result."""
        result = solve()
        self.assertTrue(len(result) > 0)

    def test_helper_function_exists(self):
        """Test that helper_function is callable."""
        self.assertTrue(callable(helper_function))


if __name__ == "__main__":
    unittest.main()
