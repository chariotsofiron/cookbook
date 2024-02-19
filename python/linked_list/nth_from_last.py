"""Nth from last."""
from data_structures.linked_list import ListNode


def get_nth_from_end(head: ListNode, n: int) -> int | None:
    """Gets the nth node from the end of the list."""
    front = head
    for _ in range(n):
        if front.next is None:
            return None
        front = front.next
    end = head

    while front.next is not None:
        front = front.next  # type: ignore[reportOptionalMemberAccess]
        end = end.next  # type: ignore[reportOptionalMemberAccess]
    return end.data  # type: ignore[reportOptionalMemberAccess]


def test() -> None:
    """Runs test cases."""
    head = ListNode.from_list([4, 0, 2, 3])
    assert get_nth_from_end(head, 2) == 0
