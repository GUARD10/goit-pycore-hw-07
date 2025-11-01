from BLL.Services.CommandService.CommandService import CommandService
from BLL.Services.InputService.InputService import InputService
from BLL.Services.RecordService.RecordService import RecordService
from DAL.AddressBookStorage import AddressBookStorage
from DAL.Exceptions.AlreadyExistException import AlreadyExistException
from DAL.Exceptions.ExitBotException import ExitBotException
from DAL.Exceptions.InvalidException import InvalidException
from DAL.Exceptions.NotFoundException import NotFoundException

def main():
    book_storage = AddressBookStorage()
    record_service = RecordService(book_storage)
    command_service = CommandService(record_service)
    input_service = InputService(command_service)

    print('Welcome to the assistant bot!')

    while True:
        try:
            user_input = input('Enter a command: ')

            if not user_input:
                continue

            print(input_service.handle(user_input))

        except InvalidException as ic:
            print(ic)
            continue
        except AlreadyExistException as aee:
            print(aee)
        except NotFoundException as nf:
            print(nf)
        except ExitBotException as eb:
            print(eb)
            break
        except Exception as ex:
            print(f'An error occurred: {ex}. Please try again.')
            break

if __name__ == "__main__":
    main()
