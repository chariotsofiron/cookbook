"""Quick sort.

Links:
    https://en.wikipedia.org/wiki/Quicksort
"""

import pytest


def quicksort_recursive(arr: list[int]) -> list[int]:
    """Quick sort recursive."""
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    below = [i for i in arr[1:] if i < pivot]
    above = [i for i in arr[1:] if i >= pivot]
    return [*quicksort_recursive(below), pivot, *quicksort_recursive(above)]


def partition(array: list[int], begin: int, end: int) -> int:
    """Partitions the array."""
    pivot = array[end]
    wall = begin - 1
    for i in range(begin, end):
        if array[i] <= pivot:
            wall += 1
            array[wall], array[i] = array[i], array[wall]
    array[wall + 1], array[end] = array[end], array[wall + 1]
    return wall + 1


def quicksort(array: list[int], begin: int, end: int) -> None:
    """In-place quick sort."""
    if begin < end:
        i = partition(array, begin, end)
        quicksort(array, begin, (i - 1))
        quicksort(array, (i + 1), end)


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
    quicksort(tmp, 0, len(tmp) - 1)
    assert tmp == sorted(arr)

    tmp = quicksort_recursive(arr.copy())
    assert tmp == sorted(arr)
