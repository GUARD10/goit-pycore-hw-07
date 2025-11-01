from typing import Union

from BLL.Helpers.DateHelper import DateHelper
from DAL.Entities.Birthday import Birthday
from DAL.Entities.Name import Name
from DAL.Entities.Phone import Phone
from DAL.Exceptions.AlreadyExistException import AlreadyExistException
from DAL.Exceptions.InvalidException import InvalidException
from DAL.Exceptions.NotFoundException import NotFoundException
from datetime import datetime, date

class Record:
    def __init__(self, name: str, *phone_numbers: str, birthday: str | datetime | date |  None = None):
        self.name = Name(name)
        self.phones: list[Phone] = []
        self.birthday: Birthday | None = None

        if birthday is not None:
            self.add_birthday(birthday)

        for phone_number in phone_numbers:
            self.add_phone(phone_number)

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}" + (f", birthday: {self.birthday.value}" if self.birthday else "")

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name.value == other
        if not isinstance(other, Record):
            return NotImplemented
        return self.name == other.name and self.phones == other.phones

    def add_phone(self, phone: str | Phone) -> None:
        if self.has_phone(phone):
            raise AlreadyExistException(f"Record {self.name} already have {phone} phone")

        phone = phone if isinstance(phone, Phone) else Phone(phone)
        self.phones.append(phone)

    def update_phone(self, old_phone: str | Phone, new_phone: str | Phone) -> None:
        self.remove_phone(old_phone)
        self.add_phone(new_phone)

    def remove_phone(self, phone: str | Phone) -> None:
        if not self.has_phone(phone):
            raise NotFoundException(f"Record {self.name} do not have {phone} phone")

        self.phones.remove(phone)

    def has_phone(self, phone: str | Phone) -> bool:
        if not phone:
            raise InvalidException("Phone cannot be None")

        return phone in self.phones

    def find_phone(self, phone: str | Phone) -> Phone:
        if not self.has_phone(phone):
            raise NotFoundException(f"Record {self.name} do not have {phone} phone")

        return next((p for p in self.phones if p == phone), None)

    def add_birthday(self, birthday: Union[str, datetime, date]) -> None:
        birthday_value = DateHelper.parse_to_date(birthday)
        self.birthday = Birthday(birthday_value)

