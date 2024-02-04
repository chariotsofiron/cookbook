"""Check if a tree is a BST."""
from __future__ import annotations

from typing import NamedTuple


class TreeNode(NamedTuple):
    """Tree data structure."""

    data: int
    left: TreeNode | None
    right: TreeNode | None


def is_bst(
    root: TreeNode | None,
    left: TreeNode | None = None,
    right: TreeNode | None = None,
) -> bool:
    """Returns true if the tree is a binary search tree."""
    if root is None:
        return True

    if left is not None and root.data <= left.data:
        return False

    if right is not None and root.data >= right.data:
        return False

    return is_bst(root.left, left, root) and is_bst(root.right, root, right)


def test() -> None:
    """Run test cases."""
    root = TreeNode(
        3,
        TreeNode(2, None, None),
        TreeNode(5, TreeNode(1, None, None), TreeNode(4, None, None)),
    )
    assert not is_bst(root)

    root = TreeNode(
        5,
        TreeNode(3, TreeNode(2, None, None), TreeNode(4, None, None)),
        TreeNode(7, TreeNode(6, None, None), TreeNode(8, None, None)),
    )
    assert is_bst(root)


if __name__ == "__main__":
    test()
