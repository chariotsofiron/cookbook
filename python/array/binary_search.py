"""Binary search.

References
----------
- https://en.wikipedia.org/wiki/Binary_search_algorithm

"""

from typing import Sequence

import pytest


def binary_search(arr: Sequence[int], target: int) -> int| None:
    """Returns the index of the target in the array if it exists.

    arr must be sorted, O(nlogn)

    Best case: O(1)
    Worst case: O(log n)
    """
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        elif arr[mid] > target:
            right = mid - 1
        else:
            return mid
    return None

    # use this line for nearest
    return left if arr[left] - target < target - arr[right] else right


def binary_search_recur(
    arr: Sequence[int], target: int, low: int, high: int
) -> int | None:
    """Recursive variant of binary search."""
    if low > high:  # error case
        return None
    mid = (low + high) // 2
    if target < arr[mid]:
        return binary_search_recur(arr, target, low, mid - 1)
    if target > arr[mid]:
        return binary_search_recur(arr, target, mid + 1, high)
    return mid


@pytest.mark.parametrize(
    ("arr", "target", "expected"),
    [
        ([1, 2, 4, 7, 9, 11], 5, None),
        ([3, 5, 7, 8, 9, 10], 3, 0),
        ([1, 5, 8, 10], 0, None),
        ([1, 5, 8, 10], 5, 1),
        ([1, 5, 8, 10], 10, 3),
    ],
)
def test(arr: list[int], target: int, expected: int) -> None:
    """Runs the test cases."""
    assert binary_search(arr, target) == expected
    assert binary_search_recur(arr, target, 0, len(arr)-1) == expected
