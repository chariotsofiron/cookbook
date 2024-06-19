"""Implementation of Bresenham's line drawing algorithm.

- <https://en.wikipedia.org/wiki/Bresenham's_line_algorithm>
- <https://rosettacode.org/wiki/Bitmap/Bresenham%27s_line_algorithm#C++>
"""

from typing import Iterator

import pytest


def line(x1: int, y1: int, x2: int, y2: int) -> Iterator[tuple[int, int]]:
    """Plot a line using Bresenham's algorithm. Supports all octants."""
    steep = abs(y2 - y1) > abs(x2 - x1)
    if steep:
        x1, y1 = y1, x1
        x2, y2 = y2, x2

    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1

    dx = x2 - x1
    dy = abs(y2 - y1)
    error = dx // 2
    ystep = 1 if y1 < y2 else -1
    count = dx

    while True:
        if steep:
            yield y1, x1
        else:
            yield x1, y1

        error -= dy
        if error < 0:
            y1 += ystep
            error += dx
        x1 += 1

        if count == 0:
            break
        count -= 1


@pytest.mark.parametrize(("test_input", "expected"), [((0, 1, 6, 4), 7)])
def test(test_input: list[int], expected: int) -> None:
    """Run test cases."""
    assert len(list(line(*test_input))) == expected
