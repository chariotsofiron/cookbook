"""Depth first search.

- <https://en.wikipedia.org/wiki/Depth-first_search>
"""

import typing

V = typing.TypeVar("V")


def dfs(graph: dict[V, list[V]], start: V) -> list[V]:
    """Depth first search.

    Time: O(|V| + |E|)
    """
    seen = set()
    path = []
    stack = [start]
    while stack:
        current = stack.pop()
        if current not in seen:
            seen.add(current)
            path.append(current)
            stack.extend(graph[current])
    return path


def test() -> None:
    """Run test cases."""
    graph = {
        "A": ["B", "C"],
        "B": ["A", "D", "E"],
        "C": ["A", "F"],
        "D": ["B"],
        "E": ["B", "F"],
        "F": ["C", "E"],
    }
    assert dfs(graph, "C") == ["C", "F", "E", "B", "D", "A"]


if __name__ == "__main__":
    test()
