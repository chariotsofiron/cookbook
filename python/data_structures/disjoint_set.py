"""Disjoint set.

It provides operations for
- adding new sets
- merging sets (replacing them by their union)
- finding a representative member of a set.

The last operation makes it possible to find out efficiently if any two
elements are in the same or different sets.

- <https://en.wikipedia.org/wiki/Disjoint-set_data_structure>
"""


class DisjointSet:
    """Disjoint set."""

    def __init__(self) -> None:
        """Constructs an empty DisjointSet."""
        self.parents = {}

    def find(self, w: int) -> int:
        """Returns the parent of this item."""
        words_traversed = []
        if w not in self.parents:
            self.parents[w] = w
            return w
        while self.parents[w] != w:
            words_traversed.append(w)
            w = self.parents[w]
        for word in words_traversed:
            self.parents[word] = w
        return w

    def union(self, w1: int, w2: int) -> None:
        """Union by rank.

        Replaces the set containing x and the set containing y
        with their union.
        """
        if w1 not in self.parents:
            self.parents[w1] = w1
        if w2 not in self.parents:
            self.parents[w2] = w2

        w1_root = self.find(w1)
        w2_root = self.find(w2)
        if w1_root < w2_root:
            w1_root, w2_root = w2_root, w1_root
        self.parents[w2_root] = w1_root

    def are_synonymous(self, w1: int, w2: int) -> bool:
        """Returns true if the items are part of the same set."""
        return self.find(w1) == self.find(w2)


def test() -> None:
    """Run test cases."""
    box = DisjointSet()
    box.union(1, 2)
    assert box.are_synonymous(1, 2)
    assert not box.are_synonymous(2, 3)
    box.union(2, 3)
    assert box.are_synonymous(1, 3)
    box.union(4, 5)
    box.union(6, 7)
    box.union(5, 6)
    box.union(2, 6)
    assert box.are_synonymous(1, 6)
