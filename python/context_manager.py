from __future__ import annotations

from typing import BaseException, Optional, TracebackType, Type


class Foo:
    def __init__(self) -> None:
        pass

    def __enter__(self) -> Foo:
        return self

    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_value: Optional[BaseException],
        traceback: Optional[TracebackType],
    ) -> None:
        pass


class AsyncFoo:
    def __init__(self) -> None:
        pass

    async def __aenter__(self) -> AsyncFoo:
        return self

    async def __aexit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_value: Optional[BaseException],
        traceback: Optional[TracebackType],
    ) -> bool:
        """Returns True if the exception was handled, False otherwise."""
        return False
