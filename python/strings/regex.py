"""Regex.

Implement regex operators: .+*
"""

import pytest


def match(pattern: str, string: str) -> bool:
    """Returns True if the string matches the pattern."""
    dp = [[False] * (len(pattern) + 1) for _ in range(len(string) + 1)]
    dp[0][0] = True

    for i in range(len(string) + 1):
        for j in range(1, len(pattern) + 1):
            if pattern[j - 1] == "*":
                dp[i][j] = dp[i][j - 2] or (
                    i > 0
                    and dp[i - 1][j]
                    and (
                        pattern[j - 2] == string[i - 1] or pattern[j - 2] == "."
                    )
                )
            elif i > 0 and (
                pattern[j - 1] == string[i - 1] or pattern[j - 1] == "."
            ):
                dp[i][j] = dp[i - 1][j - 1]

    return dp[len(string)][len(pattern)]


@pytest.mark.parametrize(
    ("pattern", "string", "expected"),
    [
        ("a.*b", "ab", True),
        ("a.*b", "aab", True),
        ("a.*b", "acb", True),
        ("a.*b", "a", False),
    ],
)
def test(pattern: str, string: str, expected: bool) -> None:  # noqa: FBT001
    """Runs the test cases."""
    assert match(pattern, string) == expected
