"""Count islands in a matrix.

Given a matrix of 1s and 0s, count the number of islands. An island is
surrounded by water and is formed by connecting adjacent lands horizontally
or vertically.
You may assume all four edges of the grid are all surrounded by water.

Example 1:
11110
11010
11000
00000
Answer: 1
Example 2:
11000
11000
00100
00011
Answer: 3

Found in:
    https://leetcode.com/problems/number-of-islands/
"""

import pytest


def count_islands(grid: list[list[str]]) -> int:
    """Returns the number rof islands in the grid.

    An island is a group of 1s that are horizontally and
    vertically adjacent.

    Modifies grid in place.

    Time: O(m*n)
    """

    def dfs(i: int, j: int) -> int:
        """Performs a depth first search in the grid at (i,j)."""
        if (
            i in range(len(grid))
            and j in range(len(grid[0]))
            and grid[i][j] == "1"
        ):
            grid[i][j] = "0"  # mark the cell as visited
            for pos in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                dfs(*pos)
            return 1
        return 0

    return sum(dfs(i, j) for i in range(len(grid)) for j in range(len(grid[0])))


@pytest.mark.parametrize(
    ("test_input", "expected"),
    [("11000\n11000\n00100\n00011", 3), ("11110\n11010\n11000\n00000", 1)],
)
def test(test_input: str, expected: int) -> None:
    """Runs test cases."""
    grid = [list(line) for line in test_input.splitlines()]
    assert count_islands(grid) == expected
