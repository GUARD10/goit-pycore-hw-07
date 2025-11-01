import pytest
from datetime import date, datetime

from DAL.Entities.Record import Record
from DAL.Entities.Phone import Phone
from DAL.Entities.Birthday import Birthday
from DAL.Exceptions.AlreadyExistException import AlreadyExistException
from DAL.Exceptions.InvalidException import InvalidException
from DAL.Exceptions.NotFoundException import NotFoundException


def test_create_record_with_multiple_phones():
    record = Record("John", "+380991112233", "+380665554433")
    assert record.name.value == "John"
    assert len(record.phones) == 2
    assert all(isinstance(p, Phone) for p in record.phones)


def test_add_phone_successfully():
    record = Record("John")
    record.add_phone("+380991112233")
    assert len(record.phones) == 1
    assert record.phones[0].value == "+380991112233"


def test_add_duplicate_phone_raises():
    record = Record("John", "+380991112233")
    with pytest.raises(AlreadyExistException):
        record.add_phone("+380991112233")


def test_update_phone_replaces_correctly():
    record = Record("John", "+380991112233")
    record.update_phone("+380991112233", "+380665554433")
    assert record.phones[0].value == "+380665554433"


def test_remove_existing_phone():
    record = Record("John", "+380991112233", "+380665554433")
    record.remove_phone("+380665554433")
    assert len(record.phones) == 1
    assert record.phones[0].value == "+380991112233"


def test_remove_nonexistent_phone_raises():
    record = Record("John", "+380991112233")
    with pytest.raises(NotFoundException):
        record.remove_phone("+380665554433")


def test_find_existing_phone_returns_object():
    record = Record("John", "+380991112233")
    found = record.find_phone("+380991112233")
    assert isinstance(found, Phone)
    assert found.value == "+380991112233"


def test_find_missing_phone_raises():
    record = Record("John", "+380991112233")
    with pytest.raises(NotFoundException):
        record.find_phone("+380123456789")


def test_has_phone_validations():
    record = Record("John", "+380991112233")
    assert record.has_phone("+380991112233")
    with pytest.raises(InvalidException):
        record.has_phone(None)


def test_add_birthday_from_string():
    record = Record("John")
    record.add_birthday("05.11.2000")
    assert isinstance(record.birthday, Birthday)
    assert record.birthday.value == date(2000, 11, 5)


def test_add_birthday_from_datetime():
    record = Record("John")
    dt = datetime(1990, 7, 14, 12, 0)
    record.add_birthday(dt)
    assert record.birthday.value == date(1990, 7, 14)


def test_add_birthday_from_date():
    record = Record("John")
    record.add_birthday(date(1988, 1, 1))
    assert record.birthday.value == date(1988, 1, 1)


def test_str_representation_contains_birthday_and_phones():
    record = Record("John", "+380991112233", birthday="05.11.2000")
    text = str(record)
    assert "John" in text
    assert "+380991112233" in text
    assert "birthday" in text.lower()
    assert "2000" in text


def test_equality_logic_between_records():
    r1 = Record("John", "+380991112233")
    r2 = Record("John", "+380991112233")
    r3 = Record("Jane", "+380991112233")

    assert r1 == r2
    assert r1 != r3
    assert r1 == "John"
    assert r1 != "Jane"


def test_record_initialization_with_birthday_and_phones():
    record = Record("Jane", "+380991112233", "+380665554433", birthday="29.02.1996")
    assert record.name.value == "Jane"
    assert len(record.phones) == 2
    assert isinstance(record.birthday, Birthday)
    assert record.birthday.value == date(1996, 2, 29)
