from collections import UserDict
from typing import Callable

from DAL.Entities.Record import Record
from DAL.IStorage import IStorage, T

class AddressBookStorage(UserDict, IStorage[str, Record]):
    def add(self, record: Record) -> Record:
        self.data[record.name.value] = record
        return record

    def update_item(self, record_name: str, new_record: Record) -> Record:
        self.data[record_name] = new_record
        return new_record

    def find(self, record_name: str) -> Record | None:
        return self.data.get(record_name)

    def all_values(self) -> list[T]:
        return list(self.data.values())

    def delete(self, record_name: str) -> None:
        self.pop(record_name)

    def has(self, record_name: str) -> bool:
        return record_name in self

    def filter(self, predicate: Callable[[Record], bool]) -> list[Record]:
        return [record for record in self.data.values() if predicate(record)]
