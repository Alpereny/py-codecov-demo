import pytest

from src.calculator import add


def test_add():
    value1, value2 = 1, 2
    expected_result = value1 + value2
    result = add(value1, value2)

    assert result == expected_result
