"""Bubble sort."""

import pytest


def bubble_sort(arr: list[int]) -> None:
    """Sorts an array in-place using bubble sort.

    Time: O(n^2)
    Space: O(1)
    """
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


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
    bubble_sort(arr)
    assert arr == sorted(arr)
