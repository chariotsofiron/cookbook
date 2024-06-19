"""LRU Cache."""

from collections import deque
from typing import Iterator


class Cache:
    """LRU cache."""

    def __init__(self, capacity: int) -> None:
        """Constructs an LRU cache with a specfic capacity."""
        self.queue = deque(maxlen=capacity)
        self.present = set()

    def refer(self, item: int) -> None:
        """Refer to an element and update the cache."""
        if item not in self.present:
            if len(self.queue) == self.queue.maxlen:
                last = self.queue.pop()
                self.present.remove(last)
        else:
            self.queue.remove(item)

        self.queue.appendleft(item)
        self.present.add(item)

    def __len__(self) -> int:
        """Returns the number of elements in the cache."""
        return len(self.queue)

    def __iter__(self) -> Iterator[int]:
        """Returns an iterator over the items in most recently seen order."""
        return iter(self.queue)


def test() -> None:
    """Tests LRU cache operations."""
    cache = Cache(4)
    cache.refer(1)
    cache.refer(2)
    cache.refer(3)
    cache.refer(1)
    cache.refer(4)
    cache.refer(5)

    assert list(cache) == [5, 4, 1, 3]
