import pytest

from returns.errors import InvalidUnwrapError
from returns.option import *
from returns.result import Err, Ok


def test_is_some_method_in_the_some_state_must_return_true():
    option: Option[int] = Some(1)
    assert option.is_some()


def test_is_nothing_method_in_the_some_state_must_return_false():
    option: Option[int] = Some(1)
    assert not option.is_nothing()


def test_is_some_method_in_the_nothing_state_must_return_false():
    option: Option[int] = Nothing()
    assert not option.is_some()


def test_is_nothing_method_in_the_nothing_state_must_return_true():
    option: Option[int] = Nothing()
    assert option.is_nothing()


def test_map_method_in_the_some_state_should_correctly_apply_the_passed_function():
    option: Option[int] = Some(1)
    match option.map(lambda x: Some(x + 2)):
        case Some(value):
            assert value == 3
        case Nothing():
            assert False


def test_map_method_in_the_nothing_state_should_return_an_nothing_object():
    option: Option[int] = Nothing[int]()
    match option.map(lambda x: Some(x + 2)):
        case Some():
            assert False
        case Nothing():
            assert True


def test_to_result_it_is_expected_to_return_an_ok_type_when_in_the_state_some():
    option: Option[int] = Some(1)
    assert isinstance(option.to_result(ValueError()), Ok)


def test_to_result_it_is_expected_to_return_an_err_type_when_in_the_state_nothing():
    option: Option[int] = Nothing()
    assert isinstance(option.to_result(ValueError()), Err)


def test_unwrap_it_is_expected_that_in_the_some_state_the_value_will_be_returned():
    option: Option[int] = Some(1)
    assert option.unwrap() == 1


def test_unwrap_it_is_expected_that_in_the_nothing_state_an_error_will_be_thrown():
    option: Option[int] = Nothing()
    with pytest.raises(InvalidUnwrapError):
        option.unwrap()
