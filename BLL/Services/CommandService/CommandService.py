from typing import Optional

from BLL.Services.CommandService.ICommandService import ICommandService
from BLL.Services.RecordService.IRecordService import IRecordService
from DAL.Entities.Command import Command
from DAL.Entities.Record import Record
from DAL.Exceptions.ExitBotException import ExitBotException
from BLL.Decorators.CommandHandlerDecorator import command_handler_decorator

class CommandService(ICommandService):
    def __init__(self, record_service: IRecordService):
        self.record_service = record_service

        self.commands: dict[str, Command] = {
            'hello': Command('hello', self.hello, 'Greet the bot'),
            'add': Command('add', self.add_contact, 'Add a new contact: add [name] [phone]'),
            'add-phone': Command('add-phone', self.add_phone, "Add new phone to contact: add-phone [name] [new_phone]."),
            'phone': Command('phone', self.show_phone, "Show a contact's phone by name: phone [name]"),
            'all': Command('all', self.show_all, 'Show all contacts'),
            'help': Command('help', self.help_command, 'Show this help message'),
            'exit': Command('exit', self.exit_bot, 'Exit the program'),
            'close': Command('close', self.exit_bot, 'Exit the program'),
            'add-birthday': Command('add-birthday', self.add_birthday,"Add birthday to contact: add-birthday [name] [birthday]. Note it will replace birthday if exist"),
            'show-birthday': Command('show-birthday', self.show_birthday,"Show birthday to contact: show-birthday [name]"),
            'birthdays': Command('birthdays', self.birthdays, 'Show upcoming birthdays for next week'),
        }

    @command_handler_decorator
    def add_contact(self, arguments: list[str]) -> str:
        name, phone = arguments
        new_contact = Record(name, phone)
        self.record_service.save(new_contact)

        return f"Contact added. {new_contact}"

    @command_handler_decorator
    def add_phone(self, arguments: list[str]) -> str:
        name, new_phone = arguments

        contact = self.record_service.get_by_name(name)
        contact.add_phone(new_phone)

        return f"Contact updated. {contact}"

    @command_handler_decorator
    def show_phone(self, arguments: list[str]) -> str:
        name = arguments[0]
        contact = self.record_service.get_by_name(name)

        return ", ".join(p.value for p in contact.phones)

    @command_handler_decorator
    def add_birthday(self, arguments: list[str]) -> str:
        name, birthday = arguments
        contact = self.record_service.get_by_name(name)
        contact.add_birthday(birthday)
        self.record_service.update(name, contact)

        return f"Contact updated. {contact}"

    @command_handler_decorator
    def show_birthday(self, arguments: list[str]) -> str:
        name = arguments[0]
        contact = self.record_service.get_by_name(name)

        return f"Contact birthday: {contact.birthday}"

    @command_handler_decorator
    def birthdays(self) -> str:
        contacts_with_upcoming_birthdays = self.record_service.get_with_upcoming_birthdays()

        if not contacts_with_upcoming_birthdays:
            return "No birthdays this week 🎂"

        return "\n".join([f"Contact: {contact.name} - {contact.birthday}" for contact in contacts_with_upcoming_birthdays])

    @command_handler_decorator
    def show_all(self) -> str:
        contacts = self.record_service.get_all()

        if not contacts:
            return "No contacts found."

        return "\n".join([f"{contact}" for contact in contacts])

    @command_handler_decorator
    def hello(self) -> str:
        return "How can I help you?"

    @command_handler_decorator
    def help_command(self) -> str:
        lines = sorted(f" - {cmd.name}: {cmd.description}" for cmd in self.commands.values())
        return "Available commands:\n" + "\n".join(lines)

    @command_handler_decorator
    def exit_bot(self) -> None:
        raise ExitBotException("Good bye!")

    def get_command(self, command: str) -> Optional[Command]:
        return self.commands.get(command)
