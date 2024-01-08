import pytest

from returns.result import *


def test_is_ok_method_in_the_ok_state_must_return_true():
    result: Result[int, Exception] = Ok(1)
    assert result.is_ok()


def test_is_err_method_in_the_ok_state_must_return_false():
    result: Result[int, Exception] = Ok(1)
    assert not result.is_err()


def test_is_ok_method_in_the_err_state_must_return_false():
    result: Result[int, Exception] = Err(Exception("error"))
    assert not result.is_ok()


def test_is_err_method_in_the_err_state_must_return_true():
    result: Result[int, Exception] = Err(Exception("error"))
    assert result.is_err()


def test_map_method_in_the_ok_state_should_correctly_apply_the_passed_function():
    result: Result[int, Exception] = Ok(1)
    match result.map(lambda x: Ok[int, Exception](x + 2)):
        case Ok(value):
            assert value == 3
        case Err():
            assert False


def test_map_method_in_the_err_state_should_return_an_err_object():
    result: Result[int, Exception] = Err(Exception("error"))
    match result.map(lambda x: Ok[int, Exception](x + 2)):
        case Ok():
            assert False
        case Err():
            assert True


def test_unwrap_it_is_expected_that_in_the_ok_state_the_value_will_be_returned():
    result: Result[int, Exception] = Ok(1)
    assert result.unwrap() == 1


def test_unwrap_it_is_expected_that_in_the_err_state_an_error_will_be_thrown():
    result: Result[int, Exception] = Err(Exception("error"))
    with pytest.raises(InvalidUnwrapError):
        result.unwrap()


def test_unwrap_err_it_is_expected_that_in_the_err_state_the_value_will_be_returned():
    result: Result[int, Exception] = Err(Exception("error"))
    assert isinstance(result.unwrap_err(), Exception)


def test_unwrap_err_it_is_expected_that_in_the_ok_state_an_error_will_be_thrown():
    result: Result[int, Exception] = Ok(1)
    with pytest.raises(InvalidUnwrapError):
        result.unwrap_err()
