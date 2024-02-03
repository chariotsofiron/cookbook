"""Flood fill."""


def floodfill(
    grid: list[list[int]], i: int, j: int, before: int, after: int
) -> None:
    """Flood fills a matrix in-place.

    Time: O(n) where n is the number of cells in the grid
    """
    if grid[i][j] == before:
        grid[i][j] = after
        if i > 0:
            floodfill(grid, i - 1, j, before, after)
        if i < len(grid[j]) - 1:
            floodfill(grid, i + 1, j, before, after)
        if j > 0:
            floodfill(grid, i, j - 1, before, after)
        if j < len(grid) - 1:
            floodfill(grid, i, j + 1, before, after)


def test() -> None:
    """Runs test cases."""
    grid = [
        [0, 2, 0, 2, 2, 2],
        [0, 0, 0, 0, 0, 0],
        [0, 2, 2, 0, 2, 2],
        [2, 0, 2, 0, 0, 2],
        [0, 2, 0, 0, 2, 0],
        [0, 0, 2, 0, 0, 0],
    ]

    floodfill(grid, 4, 2, 0, 1)
    assert grid[1][5] == 1
