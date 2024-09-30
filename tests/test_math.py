import pytest


def add_two_number(a, b):
    return a + b


@pytest.mark.math
def test_small_number():
    assert add_two_number(1, 2) == 30, "The sum of 1 and 2 should be 3"


@pytest.mark.math
def test_large_number():
    assert add_two_number(100, 300) == 400, "The sum of 100 and 300 should be 400"
