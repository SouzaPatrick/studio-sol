import pytest

from app.validate_password import (
    validate_min_size,
    count_char,
    validate_no_repeted,
    validate_min_digit,
    validate_min_low_case,
    validate_min_special_chars,
    validate_min_upper_case
)


@pytest.fixture
def password():
    return 'T2esteSenhaForte!123&'


def test_validate_min_size(password):
    count_min_size: bool = validate_min_size(password=password, value=21)
    assert count_min_size is True


def test_validate_no_repeted(password):
    assert validate_no_repeted(password) is True


def test_validate_repeted():
    password: str = 'T22esteSenhaForte!123&'
    assert validate_no_repeted(password) is False


def test_validate_min_digit(password):
    assert validate_min_digit(password=password, value=4) is True


def test_validate_min_low_case(password):
    assert validate_min_low_case(password=password, value=12) is True


def test_validate_min_upper_case(password):
    assert validate_min_upper_case(password=password, value=3) is True


def test_validate_min_special_chars(password):
    assert validate_min_special_chars(password=password, value=2) is True


@pytest.mark.parametrize(
    'data',
    [
        {
            'function': str.isdigit,
            'result': 4
        },
        {
            'function': str.isalpha,
            'result': 15
        },
        {
            'function': str.islower,
            'result': 12
        },
        {
            'function': str.isupper,
            'result': 3
        }
    ],
)
def test_count_char(password, data):
    assert count_char(password=password, function=data['function']) == data['result']