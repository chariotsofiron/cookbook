"""Returns the k largest elements in an array."""
import heapq

import pytest


def k_largest_selection(arr: list[int], k: int) -> list[int]:
    """Returns the k largest elements in an array.

    - Mutates the original array
    - Runs k iterations of selection sort

    Time: O(nk)
    """
    if k >= len(arr):
        return sorted(arr, reverse=True)
    for i in range(k):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] > arr[min_idx]:
                min_idx = j
        arr[min_idx], arr[i] = arr[i], arr[min_idx]
    return arr[:k]


def klarge_maxheap(arr: list[int], k: int) -> list[int]:
    """Returns the k largest elements in an array.

    - Solves by building heap and popping k elements off.

    Time: O(n + klogk)
    """
    return heapq.nlargest(k, arr)


@pytest.mark.parametrize(
    ("arr", "k", "expected"),
    [
        ([], 2, []),
        ([1], 2, [1]),
        ([1, 2], 2, [2, 1]),
        ([3, 5, 2, 6, 1, 4], 2, [6, 5]),
    ],
)
def test(arr: list[int], k: int, expected: list[int]) -> None:
    """Runs test cases."""
    assert k_largest_selection(arr, k) == expected
