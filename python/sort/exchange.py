"""Exchange sort.

- <https://arxiv.org/pdf/2110.01111.pdf>
- <https://news.ycombinator.com/item?id=28758106>
"""

import pytest


def exchange_sort(arr: list[int]) -> None:
    """Sorts an array in-place using exchange sort.

    Time: O(n^2)
    Space: O(1)
    """
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]


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
    exchange_sort(arr)
    assert arr == sorted(arr)
