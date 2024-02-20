"""Fibonacci sequence.

The Fibonacci sequence is defined as a recurrence relation.
fn+1 = fn + fn-1, with f(0) = 1, and f(1) = 1
0,1,1,2,3,5,8,13,21,34,55,89,144,233,...

- <https://en.wikipedia.org/wiki/Fibonacci_number>
"""
import functools
import math

import pytest


def fibonacci_recursive(n: int) -> int:
    """Returns the nth fibonacci number.

    Uses recursion. Does plenty of redundant work.

    Time: (2^n), more precisely O((1+sqrt(5))/2)^n)
    Space: O(n)
    """
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def fibonacci_iterative(n: int) -> int:
    """Returns the nth fibonacci number.

    Uses iteration.

    Time: O(n)
    """
    last, curr = 0, 1
    for _ in range(n):
        last, curr = curr, last + curr
    return last


@functools.lru_cache
def fibonacci_memoized(n: int) -> int:
    """Returns the nth fibonacci number.

    Memoization refers to remembering results of method calls based on the
    method inputs and then returning the remembered result rather than
    computing the result again.

    time: O(n)
    space O(n)
    """
    if n <= 1:
        return n
    return fibonacci_memoized(n - 1) + fibonacci_memoized(n - 2)


def fibonacci_closed(n: int) -> int:
    """Returns the nth fibonacci number.

    We can calculate a closed form representation, as taught in introductory
    discrete structure courses.
    Approach: http://discrete.openmathbooks.org/dmoi2/sec_recurrence.html

    time: O(1)
    space: O(1)
    """
    golden_ratio = (1 + math.sqrt(5)) / 2
    return int(round(golden_ratio**n / math.sqrt(5)))


@pytest.mark.parametrize(
    ("n", "expected"), [(0, 0), (1, 1), (2, 1), (3, 2), (4, 3), (5, 5), (6, 8)]
)
def test(n: int, expected: int) -> None:
    """Runs test cases."""
    assert fibonacci_recursive(n) == expected
    assert fibonacci_iterative(n) == expected
    assert fibonacci_memoized(n) == expected
    assert fibonacci_closed(n) == expected
