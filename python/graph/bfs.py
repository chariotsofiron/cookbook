"""Breadth first search.

- <https://en.wikipedia.org/wiki/Breadth-first_search>
"""
import typing

V = typing.TypeVar("V")


def bfs(graph: dict[V, list[V]], start: V) -> list[V]:
    """Breadth first search.

    Time: O(|V| + |E|)
    """
    seen = set()
    path = []
    queue = [start]
    while queue:
        current = queue.pop(0)
        if current not in seen:
            seen.add(current)
            path.append(current)
            queue.extend(graph[current])
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
    assert bfs(graph, "C") == ["C", "A", "F", "B", "E", "D"]


if __name__ == "__main__":
    test()
