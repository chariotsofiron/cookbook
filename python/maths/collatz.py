"""Collatz conjecture.

- <https://en.wikipedia.org/wiki/Collatz_conjecture>
"""
from typing import Iterator


def collatz(number: int) -> Iterator[int]:
    """Yields the numbers of the collatz conjecture."""
    while number != 1:
        if number % 2 == 0:
            number //= 2
        else:
            number = 3 * number + 1
        yield number


def test() -> None:
    """Runs test cases."""
    assert list(collatz(12)) == [6, 3, 10, 5, 16, 8, 4, 2, 1]
