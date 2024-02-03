"""Stars and bars."""
import itertools
from typing import Iterator


def stars_and_bars(n_items: int, n_bins: int) -> Iterator[list[int]]:
    """Returns the permations of all possibilities.

    Generate all permutations for putting n indistinguishable items into k
    distinguishable bins.

    There are n+k-1 choose k-1 ways of partitioning n items into k bins.

    # Arguments

    - n_items: The number of indistinguishable items
    - n_bins: The number of distinguishable bins

    # Links

    - <https://stackoverflow.com/a/28969798/9518712>
    """
    for combo in itertools.combinations(
        range(n_items + n_bins - 1), n_bins - 1
    ):
        yield [
            b - a - 1
            for a, b in zip(
                (-1, *combo),
                (
                    *combo,
                    n_items + n_bins - 1,
                ),
            )
        ]


def test() -> None:
    """Runs test case."""
    assert list(stars_and_bars(2, 3)) == [
        [0, 0, 2],
        [0, 1, 1],
        [0, 2, 0],
        [1, 0, 1],
        [1, 1, 0],
        [2, 0, 0],
    ]
