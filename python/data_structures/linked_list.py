"""Linked list."""

from __future__ import annotations

from collections.abc import Iterator


class ListNode:
    """Linked list node."""

    def __init__(self, data: int, next_node: ListNode | None = None) -> None:
        """Constructs a node with the given data and next node."""
        self.data = data
        self.next = next_node

    @classmethod
    def from_list(cls: type[ListNode], items: list[int]) -> ListNode:
        """Constructs a linked list from a list of integers."""
        if not items:
            raise ValueError
        head = cls(items[0])
        current = head
        for item in items[1:]:
            current.next = cls(item)
            current = current.next
        return head

    def __str__(self) -> str:
        """Returns a string representation of the list."""
        return "->".join(str(x) for x in self)

    def __iter__(self) -> Iterator[int]:
        """Iterates over the list."""
        current = self
        while current:
            yield current.data
            current = current.next


def test() -> None:
    """Run tests."""
    head = ListNode.from_list([1, 2, 3])
    assert str(head) == "1->2->3"
    assert list(head) == [1, 2, 3]
