"""Bubble sort."""


def bubble_sort(arr: list[int]) -> None:
    """Sorts an array in-place using bubble sort.

    Time: O(n^2)
    Space: O(1)
    """
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def test() -> None:
    """Run test cases."""
    tests = (
        ([1], [1]),
        ([1, 2], [1, 2]),
        ([1, 2, 3], [1, 2, 3]),
        ([1, 2, 3, 4], [1, 2, 3, 4]),
        ([2, 1, 3, 4], [1, 2, 3, 4]),
        ([1, 3, 2, 4], [1, 2, 3, 4]),
        ([1, 2, 4, 3], [1, 2, 3, 4]),
        ([1, 2, 4, 3], [1, 2, 3, 4]),
        ([2, 1, 1, 1], [1, 1, 1, 2]),
        ([1, 2, 1, 1], [1, 1, 1, 2]),
        ([1, 1, 2, 1], [1, 1, 1, 2]),
        ([1, 1, 1, 2], [1, 1, 1, 2]),
    )
    for arg, result in tests:
        bubble_sort(arg)
        assert arg == result


if __name__ == "__main__":
    test()
