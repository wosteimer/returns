__all__ = ("Some", "Nothing", "Option")

from typing import Callable

from .errors import InvalidUnwrapError
from .result import Err, Ok, Result

type Option[T] = Some[T] | Nothing[T]


class Some[T]:
    __match_args__ = ("value",)

    def __init__(self, value: T):
        self.__value = value

    @property
    def value(self) -> T:
        return self.__value

    def map[U](self, fn: Callable[[T], Option[U]]) -> Option[U]:
        return fn(self.__value)
    
    def unwrap(self) -> T:
        return self.value

    def is_some(self) -> bool:
        return True

    def is_nothing(self) -> bool:
        return False 

    def to_result[E: Exception](self, _: E) -> Result[T, E]:
        return Ok(self.__value)

class Nothing[T]:
    __match_args__ = ("value",)

    @property
    def value(self) -> None:
        return None 

    def map[U](self, _: Callable[[T], Option[U]]) -> Option[U]:
        return Nothing() 

    def unwrap(self) -> T:
        raise InvalidUnwrapError()

    def is_some(self) -> bool:
        return False 

    def is_nothing(self) -> bool:
        return True 

    def to_result[E: Exception](self, error: E) -> Result[T, E]:
        return Err(error)
