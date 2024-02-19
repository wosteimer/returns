from __future__ import annotations

from collections.abc import Callable

from returns.errors import InvalidUnwrapError

type Result[T, E: Exception] = Ok[T, E] | Err[T, E]


class Ok[T, E: Exception]:
    __match_args__ = ("value",)

    def __init__(self, value: T):
        self.__value = value

    @property
    def value(self) -> T:
        return self.__value

    def map[U, R: Exception](self, fn: Callable[[T], Result[U, R]]) -> Result[U, R]:
        return fn(self.__value)

    def unwrap_err(self) -> E:
        raise InvalidUnwrapError()

    def unwrap(self) -> T:
        return self.value

    def is_ok(self) -> bool:
        return True

    def is_err(self) -> bool:
        return False 


class Err[T, E:Exception]:
    __match_args__ = ("value",)

    def __init__(self, value: E):
        self.__value = value

    @property
    def value(self) -> E:
        return self.__value

    def map[U, R: Exception](self, _: Callable[[T], Result[U, R]]) -> Result[U, E]: 
        return Err(self.__value)

    def unwrap(self) -> T:
        raise InvalidUnwrapError()

    def unwrap_err(self) -> E:
        return self.__value

    def is_ok(self) -> bool:
        return False

    def is_err(self) -> bool:
        return True
