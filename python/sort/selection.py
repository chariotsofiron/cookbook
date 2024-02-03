"""Selection sort.

In Selection sort, we divide our input list / array into two parts: the
sublist of items already sorted and the sublist of items remaining to be
sorted that make up the rest of the list. We first find the smallest element
in the unsorted sublist and place it at the end of the sorted sublist. Thus,
we are continuously grabbing the smallest unsorted element and placing it in
sorted order in the sorted sublist. This process continues iteratively until
the list is fully sorted.
"""
import pytest


def selection_sort(arr: list[int]) -> None:
    """Sorts an array in-place using selection sort.

    Time: O(n^2)
    Space: O(1)
    """
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[min_idx], arr[i] = arr[i], arr[min_idx]


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
    selection_sort(arr)
    assert arr == sorted(arr)
