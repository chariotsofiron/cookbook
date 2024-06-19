"""Simple limit order book implementation.

- <https://en.wikipedia.org/wiki/Central_limit_order_book>
"""

import dataclasses


@dataclasses.dataclass
class Fill:
    """A fill in the book."""

    order_id: int
    quantity: int
    price: int
    is_done: bool


@dataclasses.dataclass
class Order:
    """An order in the book."""

    order_id: int
    quantity: int
    price: int
    is_buy: bool


class Orderbook:
    """A matching engine for a limit order book."""

    def __init__(self) -> None:
        """Constructs an empty order book."""
        # buys sorted from least to most marketable
        self.buys: list[Order] = []
        # sells sorted from least to most marketable
        self.sells: list[Order] = []

    def add(self, order: Order) -> list[Fill]:
        """Submits an order to the book and returns fills."""
        if order.is_buy:
            return self._match_with_sells(order)
        return self._match_with_buys(order)

    def _match_with_buys(self, order: Order) -> list[Fill]:
        fills = []

        while self.buys:
            buy = self.buys[-1]
            if order.price > buy.price:
                break

            qty = min(buy.quantity, order.quantity)
            buy.quantity -= qty
            order.quantity -= qty

            fills.append(Fill(buy.order_id, qty, buy.price, buy.quantity == 0))

            if buy.quantity == 0:
                self.buys.pop()
            if order.quantity == 0:
                break

        if order.quantity != 0:
            self.sells.append(order)
            self.sells.sort(key=lambda x: x.price, reverse=True)

        return fills

    def _match_with_sells(self, order: Order) -> list[Fill]:
        fills = []
        while self.sells:
            sell = self.sells[-1]
            if order.price < sell.price:
                break

            qty = min(sell.quantity, order.quantity)
            sell.quantity -= qty
            order.quantity -= qty

            fills.append(
                Fill(sell.order_id, qty, sell.price, sell.quantity == 0)
            )

            if sell.quantity == 0:
                self.sells.pop()
            if order.quantity == 0:
                break

        if order.quantity != 0:
            self.buys.append(order)
            self.buys.sort(key=lambda x: x.price)

        return fills

    def remove(self, order_id: int) -> Order | None:
        """Removes an order from the book."""
        for order in self.buys:
            if order.order_id == order_id:
                self.buys.remove(order)
                return order

        for order in self.sells:
            if order.order_id == order_id:
                self.sells.remove(order)
                return order
        return None


def test() -> None:
    """Run tests."""
    book = Orderbook()
    fills = book.add(Order(1, 10, 2, True))
    assert not fills
    fills = book.add(Order(2, 1, 1, False))
    assert fills == [Fill(1, 1, 2, False)]
