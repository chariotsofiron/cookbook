"""Monotonic.

Given an array of integers, using a minimal number of splits, produce a list of
runs. A run is a sequence of numbers that either never decreases or never
increases. Reverse the decreasing runs so they are also increasing.

Examples
--------
- [1, 0] -> [[0, 1]]
- [1, 2, 3, 2, 1] -> [[1, 2, 3], [1, 2]]
- [1, 3, 2] -> [[1, 3], [2]]
- [1, 1, 2, 1] -> [[1, 1, 2], [1]]

Discussed here:
- https://news.ycombinator.com/item?id=28167300

"""

from typing import Iterable

import pytest


def monotonic(nums: Iterable[int]) -> Iterable[list[int]]:
    """Splits a stream of numbers into monotonically increasing runs.

    Supports iterables, no helper functions, runs in O(n) time.
    Sort runs in O(n) time when reversing a list.
    """
    run = []
    for num in nums:
        is_new_run = run and (
            run[0] < run[-1]
            and num < run[-1]
            or run[0] > run[-1]
            and num > run[-1]
        )
        if is_new_run:
            yield sorted(run)
            run.clear()
        run.append(num)
    if run:
        yield sorted(run)


@pytest.mark.parametrize(
    ("test_input", "expected"),
    [
        ([], []),
        ([1], [[1]]),
        ([1, 2], [[1, 2]]),
        ([2, 1], [[1, 2]]),
        ([1, 2, 3], [[1, 2, 3]]),
        ([1, 3, 2], [[1, 3], [2]]),
        ([1, 1, 2], [[1, 1, 2]]),
        ([1, 1, 0], [[0, 1, 1]]),
        ([1, 1, 2, 0], [[1, 1, 2], [0]]),
        ([3, 2, 2, 3], [[2, 2, 3], [3]]),
        ([1, 1, 0, 0], [[0, 0, 1, 1]]),
        ([3, 3, 2, 2, 1, 1], [[1, 1, 2, 2, 3, 3]]),
        ([1, 2, 3, 2, 1, 4, 5, 6, 7], [[1, 2, 3], [1, 2], [4, 5, 6, 7]]),
        ([1, 1, 2, 3, 3, 2, 1, 1], [[1, 1, 2, 3, 3], [1, 1, 2]]),
        ([2, 3, 2, 1], [[2, 3], [1, 2]]),
        ([1, 2, 3, 1, 2, 3, 1, 2, 3], [[1, 2, 3], [1, 2, 3], [1, 2, 3]]),
        ([1, 1, 1, 2, 2, 2, 1, 1, 1], [[1, 1, 1, 2, 2, 2], [1, 1, 1]]),
    ],
)
def test(test_input: list[int], expected: list[list[int]]) -> None:
    """Runs the test cases."""
    assert list(monotonic(test_input)) == expected
