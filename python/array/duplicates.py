"""Find duplicates."""

from collections.abc import Iterable, MutableSequence

import pytest


def solve_bounded(nums: MutableSequence[int]) -> int | None:
    """Returns the first duplicate element if it exists.

    Precondition: 1 <= x <= len(nums) for all x in nums

    Uses the sign of a number to mark it as seen

    - We can shift the bound by making the list longer if needed
    - e.g. if bound is n, append extra zeroes as necessary
    - Modifies the list. Can be restored with an additional pass that
    makes every number positive

    Time: O(n)
    Space: O(1)
    """
    assert all(1 <= x <= len(nums) for x in nums)

    for x in (abs(x) for x in nums):
        if nums[x - 1] < 0:
            return x
        nums[x - 1] *= -1
    return None


def solve_set(nums: Iterable[int]) -> int | None:
    """Returns the first duplicate element of an iterable.

    Time: O(n)
    Space: O(n)
    """
    seen = set()
    for num in nums:
        if num in seen:
            return num
        seen.add(num)
    return None


@pytest.mark.parametrize(
    ("nums", "index"),
    [
        ([], None),
        ([1], None),
        ([1, 2], None),
        ([2, 2], 2),
        ([1, 2, 1], 1),
        ([1, 1, 2], 1),
        ([2, 1, 3, 1], 1),
    ],
)
def test_solve_bounded(nums: list[int], index: int | None) -> None:
    """Run tests."""
    assert solve_bounded(nums) == index
