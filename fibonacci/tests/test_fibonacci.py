import pytest

from fibonacci.naive import fibonacci_naive


@pytest.mark.parametrize('n, expected', [(0, 0), (1, 1), (2, 1), (3, 2),
                                         (20, 6765)])
def test_naive(n: int, expected: int) -> None:
    assert fibonacci_naive(n) == expected
