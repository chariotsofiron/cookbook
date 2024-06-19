"""Two sum.

Given an array of integers, return indices of the two numbers
such that they add up to a specific target.
You may assume that each input would have exactly one solution,
and you may not use the same element twice.

# Example

Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return (0, 1)

# Links

- <https://en.wikipedia.org/wiki/Subset_sum_problem>
- <https://leetcode.com/problems/two-sum/>
"""

import pytest


def two_sum_naive(arr: list[int], target: int) -> tuple[int, int] | None:
    """Returns two indices for numbers that sum to the target.

    Naive brute-force solution.

    Time: O(n^2)
    Space: O(1)
    """
    for i, val1 in enumerate(arr):
        for j, val2 in enumerate(arr):
            if i != j and val1 + val2 == target:
                return i, j
    return None


def two_sum_dict(arr: list[int], target: int) -> tuple[int, int] | None:
    """Returns two indices for numbers that sum to the target.

    Use a dictionary to store targets.

    Time: O(n)
    Space: O(n)
    """
    complement: dict[int, int] = {}
    for i, num in enumerate(arr):
        if num in complement:
            return complement[num], i
        complement[target - num] = i
    return None


@pytest.mark.parametrize(
    ("arr", "target", "expected"),
    [([], 0, None), ([1], 1, None), ([2, 7, 11, 15], 9, (0, 1))],
)
def test(arr: list[int], target: int, expected: tuple[int, int]) -> None:
    """Runs the test case."""
    assert two_sum_naive(arr, target) == expected
    assert two_sum_dict(arr, target) == expected
