from BLL.Services.RecordService.RecordService import RecordService
from DAL.AddressBookStorage import AddressBookStorage
from DAL.Entities.Record import Record

def test_end_to_end_scenario():
    # core init
    book = AddressBookStorage()
    service = RecordService(book)

    # data init
    john = Record("John", "1234567890")
    jane = Record("Jane", "9876543210")

    service.save(john)
    service.save(jane)

    # check if exist
    assert service.has("John")
    assert service.has("Jane")

    # update John phone
    john.update_phone("1234567890", "1112223333")
    service.update("John", john)

    # check changes
    updated = service.get_by_name("John")
    assert updated.phones[0].value == "1112223333"

    # rename John to Johnny
    renamed = service.rename("John", "Johnny")

    # check changes
    assert renamed.name.value == "Johnny"
    assert not service.has("John")
    assert service.has("Johnny")

    # delete Jane
    service.delete("Jane")

    # check changes
    assert not service.has("Jane")

    # final check
    all_records = service.get_all()
    assert len(all_records) == 1
    assert all_records[0].name.value == "Johnny"
