import pytest
from BLL.Services.InputService.InputService import InputService
from BLL.Services.CommandService.CommandService import CommandService
from BLL.Services.RecordService.RecordService import RecordService
from DAL.AddressBookStorage import AddressBookStorage
from DAL.Entities.Record import Record
from DAL.Exceptions.ExitBotException import ExitBotException


@pytest.fixture
def full_bot():
    storage = AddressBookStorage()
    record_service = RecordService(storage)
    command_service = CommandService(record_service)
    input_service = InputService(command_service)
    return input_service, record_service


def test_full_bot_flow(full_bot):
    input_service, record_service = full_bot

    # 1️⃣ Add 2 contacts
    result = input_service.handle("add John +380991112233")
    assert "John" in result and "+380991112233" in result

    result = input_service.handle("add Jane +380987654321")
    assert "Jane" in result and "+380987654321" in result

    # 2️⃣ Add birthdays
    result = input_service.handle("add-birthday John 05.11.2000")
    assert "birthday" in result.lower()
    assert "2000-11-05" in result

    result = input_service.handle("add-birthday Jane 29.02.1996")
    assert "birthday" in result.lower()
    assert "1996-02-29" in result

    # 3️⃣ Check birthdays
    result = input_service.handle("show-birthday John")
    assert "05.11.2000" in result or "2000-11-05" in result

    # 4️⃣ Add another phone to John
    result = input_service.handle("add-phone John +380990001122")
    john = record_service.get_by_name("John")
    assert len(john.phones) == 2
    assert any(p.value == "+380990001122" for p in john.phones)

    # 5️⃣ Show all contacts
    result = input_service.handle("all")
    assert "John" in result and "Jane" in result
    assert "birthday" in result.lower()

    # 6️⃣ Show upcoming birthdays
    result = input_service.handle("birthdays")
    assert isinstance(result, str)
    assert "Contact" in result or result.strip() == ""

    # 7️⃣ Show help
    result = input_service.handle("help")
    assert "available commands" in result.lower()
    assert "add" in result.lower()
    assert "exit" in result.lower()

    # 8️⃣ Check greeting
    result = input_service.handle("hello")
    assert "how can i help" in result.lower()

    # 9️⃣ Check exit
    with pytest.raises(ExitBotException):
        input_service.handle("exit")

    # 🔟 Check data integrity
    all_records = record_service.get_all()
    assert len(all_records) == 2

    john = record_service.get_by_name("John")
    assert isinstance(john, Record)
    assert len(john.phones) == 2
    assert john.birthday is not None
    assert john.birthday.value.year == 2000

    jane = record_service.get_by_name("Jane")
    assert jane.birthday is not None
    assert jane.birthday.value.year == 1996
