"""Tests for main.py solve() function."""

import main


def test_solve_echo():
    """Test that solve returns input as output."""
    input_data = "Hello, World!"
    result = main.solve(input_data)
    assert result == "Hello, World!"


def test_solve_multiline():
    """Test solve with multiline input."""
    input_data = "line1\nline2\nline3"
    result = main.solve(input_data)
    assert "line1" in result
    assert "line2" in result
    assert "line3" in result
