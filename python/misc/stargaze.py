"""Stargaze problem.

Given a list of points, a starting position, and a field of view, determine
the angle that allows you to see the most points.
"""

from math import atan2, isclose, tau

Point = tuple[int, int]


def solve(pos: Point, points: list[Point], fov_radians: float) -> float:
    """Solves the stargaze problem."""
    if not points:
        return 0.0

    angles = []
    for x, y in points:
        dx = x - pos[0]
        dy = y - pos[1]
        angle = atan2(dy, dx)
        if angle < 0:
            angle += tau  # Normalize angle to [0, 2π]
        angles.append(angle)

    angles.sort()

    # Duplicate angles to handle wrap-around
    angles += [angle + tau for angle in angles]

    max_visible = 0
    optimal_start_angle = 0
    window_start = 0
    for window_end in range(len(angles)):
        while angles[window_end] - angles[window_start] > fov_radians:
            window_start += 1

        visible_points = window_end - window_start + 1
        if visible_points > max_visible:
            max_visible = visible_points
            optimal_start_angle = angles[window_start]

        if max_visible > len(points) // 2:
            # Optimization: can't do better than half the points
            break

    return optimal_start_angle % tau  # Normalize back to [0, 2π)


def test() -> None:
    """Runs test cases."""
    # Test case 1: Basic scenario
    pos = (0, 0)
    points = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    fov = tau / 4  # 90 degrees
    result = solve(pos, points, fov)
    assert isclose(result, 0.0)

    # Test case 2: All points in one direction
    points = [(1, 0), (2, 0), (3, 0), (4, 0)]
    result = solve(pos, points, fov)
    assert isclose(result, 0.0)

    # Test case 3: Points spread out
    points = [(1, 1), (-1, 1), (-1, -1), (1, -1)]
    result = solve(pos, points, fov)
    assert isclose(result, tau / 8)

    # Test case 4: Empty list of points
    points = []
    result = solve(pos, points, fov)
    assert result == 0.0

    # Test case 5: Single point
    points = [(1, 1)]
    result = solve(pos, points, fov)
    assert isclose(result, tau / 8)

    # Test case 6: Narrow FOV
    points = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    fov = tau / 8  # 45 degrees
    result = solve(pos, points, fov)
    assert (
        isclose(result, 0.0)
        or isclose(result, tau / 4)
        or isclose(result, tau / 2)
        or isclose(result, 3 * tau / 4)
    )
