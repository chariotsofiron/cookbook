"""Merge sort.

1. Divide the unsorted list into n sublists, each containing one element (a
list of one element is considered sorted).
2. Repeatedly merge sublists to
produce new sorted sublists until there is only one sublist remaining. This
will be the sorted list.
"""

import pytest


def merge_sort(arr: list[int]) -> list[int]:
    """Merge sort.

    Time: O(nlog(n))
    Space: O(n)
    """
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # Merge the sorted lists into a new one
    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    # Checking if any element was left
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1
    return arr


@pytest.mark.parametrize(
    "arr",
    [
        ([]),
        ([1]),
        ([1, 2]),
        ([1, 2, 3]),
        ([1, 2, 3, 4]),
        ([2, 1, 3, 4]),
        ([1, 3, 2, 4]),
        ([1, 2, 4, 3]),
        ([2, 1, 1, 1]),
        ([1, 2, 1, 1]),
        ([1, 1, 2, 1]),
        ([1, 1, 1, 2]),
    ],
)
def test(arr: list[int]) -> None:
    """Run test cases."""
    merge_sort(arr)
    assert arr == sorted(arr)
