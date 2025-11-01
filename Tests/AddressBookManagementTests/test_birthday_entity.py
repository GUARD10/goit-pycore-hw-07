import pytest
from datetime import date, datetime, timedelta
from DAL.Entities.Birthday import Birthday

def test_valid_birthday_from_string():
    b = Birthday("05.11.2000")
    assert b.value == date(2000, 11, 5)

def test_valid_birthday_from_date():
    b = Birthday(date(2000, 11, 5))
    assert str(b) == "05.11.2000"

def test_valid_birthday_from_datetime():
    b = Birthday(datetime(2000, 11, 5, 12, 0))
    assert str(b) == "05.11.2000"

def test_future_birthday_raises():
    future = date.today() + timedelta(days=5)
    with pytest.raises(ValueError):
        Birthday(future)

def test_invalid_string_format_raises():
    with pytest.raises(ValueError):
        Birthday("2000/11/05")

def test_invalid_type_raises():
    with pytest.raises(TypeError):
        Birthday(12345)
