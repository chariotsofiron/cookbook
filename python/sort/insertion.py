"""Insertion sort.

On each loop iteration, insertion sort removes one element from the array. It
then finds the location where that element belongs within another sorted
array and inserts it there. It repeats this process until no input elements
remain.

- stable
- in-place
- adaptive
- more efficient than bubble and selection sort

"""
import pytest


def insertion_sort(arr: list[int]) -> None:
    """Sorts an array in-place using insertion sort.

    Using swap

    Time: O(n^2)
    Space: O(1)
    """
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j - 1] > arr[j]:
            arr[j - 1], arr[j] = arr[j], arr[j - 1]
            j -= 1


def insertion_sort_optimized(arr: list[int]) -> None:
    """Sorts an array in-place using insertion sort.

    A slightly faster version that moves A[i] to its position in one go and
    only performs one assignment in the inner loop body

    Time: O(n^2)
    Space: O(1)
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i
        while j > 0 and key < arr[j - 1]:
            arr[j] = arr[j - 1]
            j -= 1
        arr[j] = key


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
    tmp = arr.copy()
    insertion_sort(tmp)
    assert tmp == sorted(arr)

    tmp = arr.copy()
    insertion_sort_optimized(tmp)
    assert tmp == sorted(arr)
