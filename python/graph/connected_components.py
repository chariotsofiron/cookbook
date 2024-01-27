"""Find all the connected components in a directed graph."""
from typing import Iterator, TypeVar

V = TypeVar("V")


def connected(graph: dict[V, list[V]]) -> Iterator[list[V]]:
    """Returns an iterator over lists of connected components.

    Time: O(|V| + |E|)
    """
    seen = set()

    def dfs(node: V) -> list[V]:
        path = []
        stack = [node]
        while stack:
            current = stack.pop()
            if current not in seen:
                seen.add(current)
                path.append(current)
                stack.extend(graph[current])
        return path

    for node in graph:
        if node not in seen:
            yield dfs(node)


def test() -> None:
    """Run test cases."""
    graph = {
        "a": ["c"],
        "b": ["c", "e"],
        "c": ["a", "b", "d", "e"],
        "d": ["c"],
        "e": ["c", "b"],
        "f": [],
    }
    graph = {"a": ["b"], "b": [], "c": ["d", "e"], "d": [], "e": []}

    assert list(connected(graph)) == [["a", "b"], ["c", "e", "d"]]


if __name__ == "__main__":
    test()
