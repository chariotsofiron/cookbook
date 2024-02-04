"""Different traversals of a binary tree."""
from __future__ import annotations

from typing import Iterator, NamedTuple


class TreeNode(NamedTuple):
    """Tree data structure."""

    data: int
    left: TreeNode | None
    right: TreeNode | None


def pre_order(root: TreeNode | None) -> Iterator[int]:
    """Pre-order traversal."""
    if root:
        yield root.data
        yield from in_order(root.left)
        yield from in_order(root.right)


def in_order(root: TreeNode | None) -> Iterator[int]:
    """In-order traversal."""
    if root:
        yield from in_order(root.left)
        yield root.data
        yield from in_order(root.right)


def post_order(root: TreeNode | None) -> Iterator[int]:
    """Post-order traversal."""
    if root:
        yield from in_order(root.left)
        yield from in_order(root.right)
        yield root.data


def level_order(root: TreeNode) -> Iterator[int]:
    """Level-order traversal."""
    queue = [root]
    next_level = []
    while queue:
        current = queue.pop(0)
        yield current.data
        for child in (current.left, current.right):
            if child is not None:
                next_level.append(child)
        if not queue:
            queue.extend(next_level)
            next_level = []


def test() -> None:
    """Run test cases."""
    root = TreeNode(
        5,
        TreeNode(3, TreeNode(2, None, None), TreeNode(4, None, None)),
        TreeNode(7, TreeNode(6, None, None), TreeNode(8, None, None)),
    )

    assert list(pre_order(root)) == [5, 2, 3, 4, 6, 7, 8]
    assert list(in_order(root)) == [2, 3, 4, 5, 6, 7, 8]
    assert list(post_order(root)) == [2, 3, 4, 6, 7, 8, 5]


if __name__ == "__main__":
    test()
