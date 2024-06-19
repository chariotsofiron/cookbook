"""Check if parentheses in a string are balanced.

Links:
    https://bradfieldcs.com/algos/stacks/balanced-parentheses/
"""

import pytest


def is_balanced(text: str) -> bool:
    """Checks if parentheses are balanced.

    Args:
    ----
    text: A string consisting only of parentheses.

    Time: O(n)
    Space: O(n)

    """
    stack = []
    braces = {")": "(", "]": "[", "}": "{"}
    for char in text:
        if char in braces.values():
            stack.append(char)
        elif not stack or stack.pop() != braces[char]:
            return False
    return not stack


@pytest.mark.parametrize(
    ("test_input", "expected"),
    [
        ("", True),
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([)]", False),
        ("{[]}", True),
        ("((()))", True),
        ("(()", False),
        ("())", False),
    ],
)
def test(test_input: str, expected: bool) -> None:  # noqa: FBT001
    """Runs the test cases."""
    assert is_balanced(test_input) == expected
