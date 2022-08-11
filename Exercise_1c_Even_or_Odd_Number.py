import pytest


def is_even(n):
    return n % 2 == 0


def is_odd(n):
    return n % 2 != 0


# Test for is_even function
@pytest.mark.parametrize("n, expected", [(2, True), (4, True), (288, True)])
def test_is_even(n, expected):
    assert is_even(n) == expected


# Test for is_odd function
@pytest.mark.parametrize("n, expected",[(1, True), (4832, False), (1111111, True)])
def test_is_odd(n, expected):
    assert is_odd(n) == expected


if __name__ == "__main__":
    is_even()
    is_odd()
