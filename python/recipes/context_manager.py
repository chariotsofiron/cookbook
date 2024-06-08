"""Example custom context manager.

- <https://bbc.github.io/cloudfit-public-docs/asyncio/asyncio-part-3.html>

with blah as a:
    stuff
"""
from types import TracebackType
from typing import Self


class Foo:
    """Sync context manager."""

    def __init__(self) -> None:
        """Init."""

    def __enter__(self) -> Self:
        """Called on entering."""
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None,
        traceback: TracebackType | None,
    ) -> None:
        """Called on exit."""


class AsyncFoo:
    """Async context manager.

    async with AsyncFoo as foo:
        blah
    """

    def __init__(self) -> None:
        """Init."""

    async def __aenter__(self) -> Self:
        """You can call await in here."""
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None,
        traceback: TracebackType | None,
    ) -> bool:
        """Returns True if the exception was handled, False otherwise."""
        return False
