from typing import Any

from returns.result import *

_ = Any


def test_is_ok_method_in_the_ok_state_must_return_true():
    result: Result[int, _] = Ok(1)
    assert result.is_ok()


def test_is_err_method_in_the_ok_state_must_return_false():
    result: Result[int, _] = Ok(1)
    assert not result.is_err()


def test_is_ok_method_in_the_err_state_must_return_false():
    result: Result[_, ValueError] = Err(ValueError("error"))
    assert not result.is_ok()


def test_is_err_method_in_the_err_state_must_return_true():
    result: Result[_, ValueError] = Err(ValueError("error"))
    assert result.is_err()


def test_map_method_in_the_ok_state_should_correctly_apply_the_passed_function():
    result: Result[int, _] = Ok(1)
    match result.map(lambda x: Ok(x + 2)):
        case Ok(value):
            assert value == 3
        case Err():
            assert False


def test_map_method_in_the_err_state_should_return_an_err_object():
    result: Result[_, ValueError] = Err(ValueError("error"))
    match result.map(lambda x: Ok(x + 2)):
        case Ok():
            assert False
        case Err():
            assert True
