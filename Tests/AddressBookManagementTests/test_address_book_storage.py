import pytest
from DAL.AddressBookStorage import AddressBookStorage
from DAL.Entities.Record import Record

@pytest.fixture
def storage():
    return AddressBookStorage()

def test_add_and_find_record(storage):
    rec = Record("John", "1234567890")
    storage.add(rec)
    assert storage.find("John") == rec

def test_update_record(storage):
    rec = Record("John", "1234567890")
    storage.add(rec)
    new_rec = Record("John", "0987654321")
    updated = storage.update_item("John", new_rec)
    assert updated.phones[0].value == "0987654321"

def test_delete_record(storage):
    rec = Record("Jane", "1112223333")
    storage.add(rec)
    storage.delete("Jane")
    assert not storage.has("Jane")

def test_all_values(storage):
    storage.add(Record("A", "1234567890"))
    storage.add(Record("B", "0987654321"))
    values = storage.all_values()
    assert len(values) == 2
    assert any(v.name.value == "A" for v in values)

def test_has_method(storage):
    rec = Record("John", "1234567890")
    storage.add(rec)
    assert storage.has("John")
    assert not storage.has("Ghost")
