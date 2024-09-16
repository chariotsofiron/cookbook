"""Stars and bars."""

import itertools
from typing import Iterator


def stars_and_bars(n: int, k: int) -> list[list[int]]:
    """Stars and bars algorithm.

    https://en.wikipedia.org/wiki/Stars_and_bars_(combinatorics)
    https://stackoverflow.com/a/69140296/9518712
    Constraints: k >= 1
    """
    assert k > 0, "k must be greater than 0"
    
    result: list[list[int]] = []
    bins: list[int] = [n] + [0] * (k - 1)
    
    while True:
        result.append(bins.copy())
        if bins[-1] == n:
            return result
        
        if bins[0] > 0:
            bins[0] -= 1
            bins[1] += 1
        else:
            i = 1
            while bins[i] == 0:
                i += 1
            bins[0] = bins[i] - 1
            bins[i + 1] += 1
            bins[i] = 0


def stars_and_bars_itertools(n_items: int, n_bins: int) -> Iterator[list[int]]:
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
            for a, b in zip((-1, *combo), (*combo, n_items + n_bins - 1))
        ]


def test() -> None:
    """Runs test case."""
    assert list(stars_and_bars(2, 3)) == [
        [2, 0, 0],
        [1, 1, 0],
        [0, 2, 0],
        [1, 0, 1],
        [0, 1, 1],
        [0, 0, 2],
    ]
    assert list(stars_and_bars_itertools(2, 3)) == [
        [0, 0, 2],
        [0, 1, 1],
        [0, 2, 0],
        [1, 0, 1],
        [1, 1, 0],
        [2, 0, 0],
    ]
