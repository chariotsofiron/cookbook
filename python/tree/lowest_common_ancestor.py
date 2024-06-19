"""Lowest common ancestor.

find lowest common ancestor of two nodes in a tree
"""

from __future__ import annotations

from typing import NamedTuple


class TreeNode(NamedTuple):
    """Tree data structure."""

    data: int
    left: TreeNode | None
    right: TreeNode | None


def lowest_common_ancestor(
    root: TreeNode | None, i: TreeNode, j: TreeNode
) -> TreeNode | None:
    """Finds the lowest common ancestor in a tree.

    We traverse to the bottom, and once we reach a node which matches one
    of the two nodes, we pass it up to its parent. The parent would then test
    its left and right subtree if each contain one of the two nodes. If yes,
    then the parent must be the LCA and we pass its parent up to the root. If
    not, we pass the lower node which contains either one of the two nodes
    (if the left or right subtree contains either p or q), or NULL (if both
    the left and right subtree does not contain either p or q) up.

    Time: O(n)
    """
    if root is None or root.data in (i.data, j.data):
        return root

    left = lowest_common_ancestor(root.left, i, j)
    right = lowest_common_ancestor(root.right, i, j)

    if left and right:
        return root

    return left if left else right


def test() -> None:
    """Run test cases."""
    a = TreeNode(2, None, None)
    b = TreeNode(6, None, None)
    root = TreeNode(
        5,
        TreeNode(3, a, TreeNode(4, None, None)),
        TreeNode(7, b, TreeNode(8, None, None)),
    )

    lca = lowest_common_ancestor(root, a, b)
    assert lca is not None
    assert lca.data == root.data
