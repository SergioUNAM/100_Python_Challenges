import pytest

def is_even(n):
    return n % 2 == 0


def is_odd(n):
    return n % 2 != 0

@pytest.mark.parametrize("m, n, expected", [(6, 7, 0), (3, 4, 6),(5, 5, 5)])