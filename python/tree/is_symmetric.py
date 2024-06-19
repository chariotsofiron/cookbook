"""Returns True if a binary tree is symmetric."""

from __future__ import annotations

from typing import NamedTuple


class TreeNode(NamedTuple):
    """Tree data structure."""

    data: int
    left: TreeNode | None
    right: TreeNode | None


def is_symmetric(root1: TreeNode | None, root2: TreeNode | None) -> bool:
    """Returns True if the tree is symmetric."""
    if root1 is None and root2 is None:
        return True
    if root1 is not None and root2 is not None:
        return is_symmetric(root1.left, root2.right) and is_symmetric(
            root1.right, root2.left
        )
    return False


def is_symmetric2(root: TreeNode) -> bool:
    """Returns True if the tree is symmetric."""
    stack = [(root.left, root.right)]

    while stack:
        left, right = stack.pop()
        if left is None != right is None:
            return False
        if left is None and right is None:
            continue
        if left is not None and right is not None:
            stack.append((left.left, right.right))
            stack.append((left.right, right.left))

    return True
