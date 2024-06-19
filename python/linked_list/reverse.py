"""Reverse a linked list."""

from data_structures.linked_list import ListNode


def reverse(head: ListNode) -> ListNode:
    """Reverses a linked list in one pass.

    Time: O(n)
    """
    prev = None
    sentinel = head
    while sentinel:
        current = sentinel
        sentinel = sentinel.next
        current.next = prev
        prev = current
    assert prev is not None
    return prev


def test() -> None:
    """Runs test cases."""
    head = ListNode.from_list([5, 3, 2])
    assert list(reverse(head)) == [2, 3, 5]
