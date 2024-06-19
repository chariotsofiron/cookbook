"""Base conversion.

- <https://bradfieldcs.com/algos/stacks/converting-number-bases/>
"""

import pytest

SYMBOLS = "0123456789abcdefghijklmnopqrstuvwxyz"


def convert_to_base(number: int, base: int) -> str:
    """Converts a decimal number to a different base."""
    remainder_stack = []
    while number > 0:
        remainder = number % base
        remainder_stack.append(remainder)
        number = number // base

    new_digits = (SYMBOLS[digit] for digit in reversed(remainder_stack))
    return "".join(new_digits)


@pytest.mark.parametrize(
    ("number", "base", "expected"), [(25, 2, "11001"), (25, 16, "19")]
)
def test(number: int, base: int, expected: str) -> None:
    """Runs test cases."""
    assert convert_to_base(number, base) == expected
