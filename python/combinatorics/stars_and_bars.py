"""Stars and bars."""

import itertools
import math
from typing import Iterator

import pytest


def stars_and_bars(n: int, k: int) -> list[list[int]]:
    """Returns each way of partitioning n items into k bins.

    Generate in lexicographic order.

    n: the target sum
    k: the number of bins

    Same as returning the integer solutions to

    x1 + x2 + x3 + ... + xk = n where xi >= 0

    https://en.wikipedia.org/wiki/Stars_and_bars_(combinatorics)
    https://stackoverflow.com/a/69140296/9518712
    Constraints: k >= 1
    """
    assert k >= 1

    result: list[list[int]] = []
    bins: list[int] = [0] * (k - 1) + [n]

    while True:
        result.append(bins.copy())
        if bins[0] == n:
            return result

        if bins[-1] > 0:
            bins[-1] -= 1
            bins[-2] += 1
        else:
            i = k - 2
            while bins[i] == 0:
                i -= 1
            bins[-1] = bins[i] - 1
            bins[i - 1] += 1
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


def stars_and_bars_count(n: int, k: int) -> int:
    """Returns the number of ways of partitioning n items into k bins."""
    assert k >= 1

    return math.comb(n + k - 1, k - 1)


def snb_min_bound_count(n: int, k: int, bounds: list[int]) -> int:
    """Returns the number of ways of partitioning n items into k bins.

    Each bin must have at least the number of items specified in bounds.

    x_i >= bounds[i] for all i

    # Arguments

    - n: the target sum
    - k: the number of bins
    - bounds: the minimum number of items in each bin
    """
    assert k >= 1
    assert len(bounds) == k

    return math.comb(n - sum(bounds) + k - 1, k - 1)


def snb_upper_bound_count(n: int, k: int, bounds: list[int]) -> int:
    """Returns the number of integer solutions to the equation

    x1 + x2 + x3 + ... + xk = n where xi <= bounds[i-1]
    """
    dp = [[0] * (n + 1) for _ in range(k + 1)]

    dp[0][0] = 1

    for i in range(1, k + 1):
        for j in range(n + 1):
            dp[i][j] = dp[i - 1][j]
            if j > 0:
                # add the number of ways using one more of the ith variable
                dp[i][j] += dp[i][j - 1]
            if j >= bounds[i - 1]:
                # subtract the number of ways that exceed the limit bound[i-1]
                dp[i][j] -= dp[i - 1][j - bounds[i - 1] - 1]

    return dp[k][n]


def snb_both_bounds(n: int, k: int, bounds: list[tuple[int, int]]) -> int:
    adjusted_n = n - sum(l for l, _ in bounds)
    adjusted_bounds: list[int] = [u - l for l, u in bounds]

    if adjusted_n < 0:
        return 0

    return snb_upper_bound_count(adjusted_n, k, adjusted_bounds)


@pytest.mark.parametrize(
    "n, k, expected",
    [
        (
            2,
            3,
            [[0, 0, 2], [0, 1, 1], [0, 2, 0], [1, 0, 1], [1, 1, 0], [2, 0, 0]],
        ),
        (3, 2, [[0, 3], [1, 2], [2, 1], [3, 0]]),
        (1, 4, [[0, 0, 0, 1], [0, 0, 1, 0], [0, 1, 0, 0], [1, 0, 0, 0]]),
        (0, 3, [[0, 0, 0]]),
    ],
)
def test_stars_and_bars(n: int, k: int, expected: list[list[int]]) -> None:
    assert list(stars_and_bars(n, k)) == expected
    assert list(stars_and_bars_itertools(n, k)) == expected


@pytest.mark.parametrize(
    "n, k, upper_bounds, expected",
    [
        (1, 0, [], 0),
        (3, 2, [1, 3], 2),
        (5, 3, [2, 2, 2], 3),
        (4, 4, [1, 1, 1, 1], 1),
        (6, 3, [3, 3, 3], 9),
    ],
)
def test_snb_upper_bound_count(
    n: int, k: int, upper_bounds: list[int], expected: int
) -> None:
    assert snb_upper_bound_count(n, k, upper_bounds) == expected


@pytest.mark.parametrize(
    "n, k, bounds, expected",
    [
        (4, 2, [(1, 3), (2, 4)], 2),
        (5, 3, [(1, 2), (1, 3), (1, 4)], 5),
        (3, 3, [(0, 1), (1, 2), (0, 3)], 4),
        (6, 2, [(2, 4), (2, 4)], 2),
        (7, 4, [(1, 2), (1, 3), (1, 4), (1, 5)], 14),
    ],
)
def test_snb_both_bounds(
    n: int, k: int, bounds: list[tuple[int, int]], expected: int
) -> None:
    assert snb_both_bounds(n, k, bounds) == expected
