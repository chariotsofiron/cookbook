"""Common prefix.

Found in:
    https://leetcode.com/problems/longest-common-prefix/
"""

import pytest


def common_prefix(strings: list[str]) -> str:
    """Returns the longest common prefix string in an array of strings.

    Gets first and last string by alphabetical sorting and return the
    common prefix.

    time: O(n)
    space: O(1)
    """
    if not strings:
        return ""
    first = min(strings)  # first string by alphabetical sorting
    last = max(strings)  # last string by alphabetical sorting
    for i, char in enumerate(first):
        if char != last[i]:
            return first[:i]
    return first


@pytest.mark.parametrize(
    ("test_input", "expected"),
    [
        ([], ""),
        (["a", "b", "c"], ""),
        (["a", "a", "a"], "a"),
        (["flower", "flow", "flight"], "fl"),
    ],
)
def test(test_input: str, expected: str) -> None:
    """Runs the test cases."""
    assert common_prefix(test_input) == expected
