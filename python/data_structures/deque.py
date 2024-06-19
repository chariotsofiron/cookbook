"""Double-ended deque.

Can be made a circular queue by popping when getting to a certain size.
"""

from typing import Iterator


class Deque:
    """Double ended deque."""

    def __init__(self) -> None:
        """Constructs a deque with a capacity of 0."""
        self.items = []
        self.front: int = 0
        self.back: int = 0
        self.size: int = 0

    def __len__(self) -> int:
        """Returns the number of items in the deque."""
        return self.size

    def is_empty(self) -> bool:
        """Returns `true` if the deque contains no items."""
        return self.size == 0

    def _is_full(self) -> bool:
        return self.size == len(self.items)

    def resize(self, capacity: int) -> None:
        """Resizes the deque with the given capacity."""
        tmp = list(iter(self))
        tmp.extend([0] * capacity)
        self.items = tmp
        self.front = 0
        self.back = self.size

    def push_back(self, item: int) -> None:
        """Pushes an item to the back of the deque."""
        if self._is_full():
            self.resize(max(len(self.items) * 2, 1))

        self.items[self.back] = item
        self.back = (self.back + 1) % len(self.items)
        self.size += 1

    def push_front(self, item: int) -> None:
        """Pushes an item to the front of the deque."""
        if self._is_full():
            self.resize(max(len(self.items) * 2, 1))

        self.front = (self.front - 1) % len(self.items)
        self.items[self.front] = item
        self.size += 1

    def pop_back(self) -> int | None:
        """Pop an item from the back of the deque."""
        if self.is_empty():
            return None
        self.back = (self.back - 1) % len(self.items)
        item = self.items[self.back]
        self.size -= 1
        return item

    def pop_front(self) -> int | None:
        """Pop an item from the front of the deque."""
        if self.is_empty():
            return None
        item = self.items[self.front]
        self.front = (self.front + 1) % len(self.items)
        self.size -= 1
        return item

    def __getitem__(self, index: int) -> int | None:
        """Returns the item at the given index from the front of the deque."""
        if self.is_empty():
            return None

        return self.items[self.front + index]

    def __iter__(self) -> Iterator[int]:
        """Iterates through the items starting from the front."""
        i = self.front
        for _ in range(len(self)):
            yield self.items[i]
            i = (i + 1) % len(self.items)


def test() -> None:
    """Runs test cases."""
    deque = Deque()
    deque.push_back(1)
    deque.push_back(2)
    deque.push_back(3)
    deque.push_back(4)
    assert list(iter(deque)) == [1, 2, 3, 4]

    deque = Deque()
    deque.push_front(2)
    deque.push_back(3)
    deque.push_front(1)
    deque.push_back(4)
    assert list(iter(deque)) == [1, 2, 3, 4]

    deque.pop_front()
    deque.pop_back()
    assert list(iter(deque)) == [2, 3]
