from collections.abc import Callable

type Result[T, R: Exception] = Ok[T] | Err[T, R]

class Ok[T]:
    __match_args__ = ("value",)

    def __init__(self, value: T):
        self.__value = value

    @property
    def value(self) -> T:
        return self.__value

    def map[U, B: Exception](self, fn: Callable[[T], Result[U, B]]) -> Result[U, B]:
        return fn(self.__value)

    def is_ok(self) -> bool:
        return True

    def is_err(self) -> bool:
        return False 


class Err[T, R: Exception]:
    __match_args__ = ("value",)

    def __init__(self, value: R):
        self.__value = value

    @property
    def value(self) -> R:
        return self.__value

    def map[U, B: Exception](self, _: Callable[[T], Result[U, B]]) -> Result[U, R]:
        return Err(self.__value)

    def is_ok(self) -> bool:
        return False

    def is_err(self) -> bool:
        return True
