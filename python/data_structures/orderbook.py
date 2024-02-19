"""Simple limit order book implementation.

- <https://en.wikipedia.org/wiki/Central_limit_order_book>
"""
import dataclasses


@dataclasses.dataclass
class Order:
    """An order in the book."""

    order_id: int
    size: int
    price: int


class MatchingEngine:
    """A matching engine for a limit order book."""

    def __init__(self) -> None:
        """Constructs an empty order book."""
        self.buys: list[Order] = []
        self.sells: list[Order] = []

    def buy(self, order: Order) -> None:
        """Submits a buy order to the book."""
        self.buys.append(order)
        self.buys.sort(key=lambda x: x.price)
        self._match()

    def sell(self, order: Order) -> None:
        """Submits a sell order to the book."""
        self.sells.append(order)
        self.sells.sort(key=lambda x: x.price, reverse=True)
        self._match()

    def _match(self) -> None:
        while self.buys and self.sells:
            buy = self.buys[-1]
            sell = self.sells[-1]
            if buy.price >= sell.price:
                qty = min(buy.size, sell.size)
                buy.size -= qty
                sell.size -= qty
                if buy.size == 0:
                    self.buys.pop()
                if sell.size == 0:
                    self.sells.pop()


def test() -> None:
    """Run tests."""
    book = MatchingEngine()
    book.buy(Order(0, 100, 10))
    book.buy(Order(1, 100, 11))
    book.sell(Order(2, 200, 10))
