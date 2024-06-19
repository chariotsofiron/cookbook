"""Median in linear time."""

import random


def quickselect_median(arr: list[int]) -> float:
    """Quickselect median."""
    if len(arr) % 2 == 1:
        return quickselect(arr, len(arr) // 2)

    return 0.5 * (
        quickselect(arr, len(arr) // 2 - 1) + quickselect(arr, len(arr) // 2)
    )


def quickselect(arr: list[int], k: int) -> int:
    """Select the kth element in l (0 based)."""
    if len(arr) == 1:
        assert k == 0
        return arr[0]

    pivot = random.choice(arr)

    lows = [el for el in arr if el < pivot]
    highs = [el for el in arr if el > pivot]
    pivots = [el for el in arr if el == pivot]

    if k < len(lows):
        return quickselect(lows, k)

    if k < len(lows) + len(pivots):
        # We got lucky and guessed the median
        return pivots[0]

    return quickselect(highs, k - len(lows) - len(pivots))


def test() -> None:
    """Runs test cases."""
    arr = [1, 3, 2, 7, 5, 4, 6, 8]
    median = 4.5
    assert quickselect_median(arr) == median
