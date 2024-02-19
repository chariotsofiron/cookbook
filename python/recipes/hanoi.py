"""The tower of hanoi puzzle.

- <https://en.wikipedia.org/wiki/Tower_of_Hanoi>
"""
from typing import Iterator


def hanoi(n_discs: int) -> Iterator[tuple[int, int]]:
    """Returns the sequence of moves to solve the 3-pillar tower puzzle.

    of hanoi puzzle with n discs starting on pillar 0.

    Solves in 2^n - 1 moves.
    """
    for i in range(1, 2**n_discs):
        yield ((i & i - 1) % 3, ((i | i - 1) + 1) % 3)


def test() -> None:
    """Run tests."""
    assert list(hanoi(3)) == [
        (0, 2),
        (0, 1),
        (2, 1),
        (0, 2),
        (1, 0),
        (1, 2),
        (0, 2),
    ]
