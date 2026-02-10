"""Test suite for the solution module."""

import pytest

from main import solve


class TestSolve:
    """Test cases for the solve function."""

    def test_solve_sample_input_1(self):
        """Test solve with sample input: sum of 3 numbers [1, 2, 3]."""
        input_data = "3\n1 2 3"
        result = solve(input_data)
        assert result == "6", f"Expected '6', got '{result}'"

    def test_solve_sample_input_2(self):
        """Test solve with sample input: sum of 4 numbers [10, 20, 30, 40]."""
        input_data = "4\n10 20 30 40"
        result = solve(input_data)
        assert result == "100", f"Expected '100', got '{result}'"

    def test_solve_single_number(self):
        """Test solve with a single number."""
        input_data = "1\n42"
        result = solve(input_data)
        assert result == "42"

    def test_solve_with_zeros(self):
        """Test solve with zeros in input."""
        input_data = "5\n0 1 0 2 0"
        result = solve(input_data)
        assert result == "3"

    def test_solve_with_negative_numbers(self):
        """Test solve with negative numbers."""
        input_data = "3\n-1 2 -3"
        result = solve(input_data)
        assert result == "-2"

    def test_solve_returns_string(self):
        """Test that solve returns a string."""
        input_data = "1\n100"
        result = solve(input_data)
        assert isinstance(result, str)

    def test_solve_with_whitespace(self):
        """Test solve handles extra whitespace in input."""
        input_data = "  3  \n  1   2   3  "
        result = solve(input_data)
        assert result == "6"


@pytest.fixture
def sample_inputs():
    """Fixture providing sample test inputs."""
    return {
        "simple_sum": ("3\n1 2 3", "6"),
        "large_sum": ("4\n10 20 30 40", "100"),
        "single": ("1\n42", "42"),
    }


def test_solve_with_fixture(sample_inputs):
    """Test solve using fixture data."""
    input_data, expected = sample_inputs["simple_sum"]
    result = solve(input_data)
    assert result == expected


# ============ ADD YOUR OWN TESTS BELOW ============
# Add specific tests for your solution logic here
# Use descriptive names and clear assertions
# Examples:
#
# def test_edge_case_empty_input():
#     """Test behavior with empty input."""
#     pass
#
# def test_large_input():
#     """Test with large input datasets."""
#     pass
#
# def test_performance():
#     """Test solution performance."""
#     pass
# ===================================================
