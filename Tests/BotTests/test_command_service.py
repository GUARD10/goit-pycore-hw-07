import pytest
from BLL.Services.CommandService.CommandService import CommandService
from DAL.Entities.Record import Record
from DAL.Exceptions.ExitBotException import ExitBotException

class FakeRecordService:
    def __init__(self):
        self.records = {}

    def save(self, record):
        self.records[record.name.value] = record

    def update(self, name, record):
        self.records[name] = record

    def get_by_name(self, name):
        return self.records.get(name)

    def get_with_upcoming_birthdays(self):
        return [r for r in self.records.values() if r.birthday]

    def get_all(self):
        return list(self.records.values())

def test_add_contact():
    service = CommandService(FakeRecordService())
    result = service.add_contact(["John", "1234567890"])
    assert "Contact added" in result

def test_add_phone():
    fake = FakeRecordService()
    rec = Record("John", "1234567890")
    fake.save(rec)

    svc = CommandService(fake)
    res = svc.add_phone(["John", "1112223333"])
    assert "Contact updated" in res
    assert len(fake.records["John"].phones) == 2

def test_add_birthday():
    fake = FakeRecordService()
    rec = Record("John", "1234567890")
    fake.save(rec)

    svc = CommandService(fake)
    res = svc.add_birthday(["John", "05.11.2000"])
    assert "Contact updated" in res
    assert rec.birthday is not None

def test_show_birthday():
    fake = FakeRecordService()
    rec = Record("John", "1234567890", birthday="05.11.2000")
    fake.save(rec)
    svc = CommandService(fake)
    result = svc.show_birthday(["John"])
    assert "05.11.2000" in result

def test_birthdays_command():
    fake = FakeRecordService()
    rec = Record("John", "1234567890", birthday="05.11.2000")
    fake.save(rec)
    svc = CommandService(fake)
    result = svc.birthdays()
    assert "John" in result

def test_show_all_empty():
    svc = CommandService(FakeRecordService())
    result = svc.show_all()
    assert "No contacts" in result

def test_show_all_with_data():
    fake = FakeRecordService()
    fake.save(Record("John", "1234567890"))
    fake.save(Record("Jane", "0987654321"))
    svc = CommandService(fake)
    result = svc.show_all()
    assert "John" in result and "Jane" in result

def test_hello_and_help():
    svc = CommandService(FakeRecordService())
    assert "help" in svc.help_command().lower()
    assert "how can i help" in svc.hello().lower()

def test_exit_bot():
    svc = CommandService(FakeRecordService())
    with pytest.raises(ExitBotException):
        svc.exit_bot()

def test_get_command_exists():
    svc = CommandService(FakeRecordService())
    cmd = svc.get_command("add")
    assert cmd is not None
    assert cmd.name == "add"

def test_get_command_missing():
    svc = CommandService(FakeRecordService())
    assert svc.get_command("unknown") is None
