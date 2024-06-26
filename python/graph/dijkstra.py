"""Dijkstra's algorithm.

Dijkstra's algorithm is for finding the shortest paths between nodes in a
graph.

Using a priority queue, it is the fastest known single-source
shortest-path algorithm for arbitrary directed graphs with unbounded
non-negative weights.

Dijkstra's original algorithm found the shortest path between two given
nodes,[4] but a more common variant fixes a single node as the "source" node
and finds shortest paths from the source to all other nodes in the graph,
producing a shortest-path tree.

Conditions:
- positive edge weights

- <https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm>
"""

import heapq
from typing import TypeVar

V = TypeVar("V")


def dijkstra(graph: dict[V, dict[V, int]], start: V) -> dict[V, V]:
    """Dijkstra's algorithm, implemented using a priority queue.

    Includes practical optimizations.
    Worst case performance: O(|E| + |V|log|V|)
    """
    dist_from_start = {start: 0}
    previous = {}
    heap: list[tuple[int, V]] = [(0, start)]
    while heap:
        current = heapq.heappop(heap)[1]
        for neighbour, cost in graph[current].items():
            alt_cost = dist_from_start[current] + cost
            if alt_cost < dist_from_start.get(neighbour, float("inf")):
                heapq.heappush(heap, (alt_cost, neighbour))
                dist_from_start[neighbour] = alt_cost
                previous[neighbour] = current
    return previous


def get_path(prev: dict[V, V], target: V) -> list[V]:
    """Get path."""
    path = []
    while target in prev:
        path.insert(0, target)
        target = prev[target]
    return path


def test() -> None:
    """Run test cases."""
    graph = {
        "A": {"C": 2, "D": 6},
        "B": {"D": 10, "A": 3},
        "C": {"D": 7, "E": 5},
        "D": {"E": 1},
        "E": {},
    }
    prev = dijkstra(graph, "B")
    assert get_path(prev, "D") == ["A", "D"]
    assert get_path(prev, "E") == ["A", "C", "E"]

    graph = {
        1: {2: 3, 3: 8, 5: 2},
        2: {4: 1, 5: 7},
        3: {2: 4},
        4: {1: 2, 3: 2},
        5: {4: 6},
    }
    prev = dijkstra(graph, 1)
    assert get_path(prev, 5) == [5]
    assert get_path(prev, 3) == [2, 4, 3]
