"""Generate a random permutation of a finite sequence."""

import random


def shuffle_std(arr: list[int]) -> None:
    """Shuffles an array using the standard library in-place."""
    random.shuffle(arr)


def shuffle_fischer_yates(arr: list[int]) -> None:
    """Shuffles an array in-place using Fisher-Yates algorithm.

    Time: O(n)
    Space: O(1)

    - <https://en.wikipedia.org/wiki/Fisher-Yates_shuffle>
    """
    for i, item in enumerate(arr):
        rand_idx = random.randrange(i, len(arr))
        arr[i], arr[rand_idx] = arr[rand_idx], item
