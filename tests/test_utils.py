"""Tests for utils.py helpers."""

import utils


def test_memoize_caches_results():
    calls = []

    @utils.memoize
    def square(x):
        calls.append(x)
        return x * x

    assert square(4) == 16
    assert square(4) == 16
    assert calls == [4]


def test_timer_returns_wrapped_result():
    @utils.timer
    def add(a, b):
        return a + b

    assert add(2, 3) == 5
    assert add.__name__ == "add"


def test_parse_input_strips_blank_lines():
    assert utils.parse_input(["a\n", "\n", "  b  \n"]) == ["a", "b"]


def test_read_input_missing_file_returns_empty_list():
    assert utils.read_input("does-not-exist.txt") == []


def test_format_output():
    assert utils.format_output(42) == "42"
