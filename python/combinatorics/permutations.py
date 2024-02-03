"""Generate all permutations of n items."""
import itertools
from typing import Iterator

import pytest


def permute2(arr: list[int], n: int) -> Iterator[tuple[int, ...]]:
    """Generates all permutations of a list.

    - fix element at end
    - permute the rest

    Time: O(n!)
    """
    if n == 1:
        yield tuple(arr)
        return
    for i in range(n):
        arr[i], arr[n - 1] = arr[n - 1], arr[i]
        yield from permute2(arr, n - 1)
        arr[i], arr[n - 1] = arr[n - 1], arr[i]


def permute_heap(arr: list[int], k: int) -> Iterator[tuple[int, ...]]:
    """Generates all permutations of a list.

    Uses heap's algorithm

    Time: O(n!)
    """
    if k == 1:
        yield tuple(arr)
        return
    for i in range(k):
        yield from permute_heap(arr, k - 1)
        if k % 2:
            arr[0], arr[k - 1] = arr[k - 1], arr[0]
        else:
            arr[i], arr[k - 1] = arr[k - 1], arr[i]


@pytest.mark.parametrize(
    ("test_input", "n"),
    [
        ([1, 2, 3], 3),
    ],
)
def test(test_input: list[int], n: int) -> None:
    """Runs test case."""
    expected = list(itertools.permutations(test_input))
    assert sorted(permute_heap(test_input, n)) == expected
    assert sorted(permute2(test_input, n)) == expected
