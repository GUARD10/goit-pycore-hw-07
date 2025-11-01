## 🤖 AI Usage Disclaimer / Дісклеймер щодо використання ШІ

🇬🇧 **Note:** Artificial Intelligence (AI) was used **only** for writing this README file and for general consultation and documentation.  
All source code, algorithms, and logic were **written and designed by the author**.

🇺🇦 **Примітка:** Штучний інтелект (AI) використовувався **лише** для створення цього README-файлу та отримання консультацій й оформлення.  
Увесь код, алгоритми та логіка були **написані й продумані автором**.

---

# 🧠 Address Book Assistant Bot (goit-pycore-hw-07)

<p align="center">
  <a href="#-description">🇬🇧 English</a> |
  <a href="#-опис-проєкту">🇺🇦 Українська</a>
</p>

---

# 🇬🇧 **Description**

This console application is a **contact management assistant bot**, built as part of the **GOIT Python Core – Homework 7 (Advanced OOP)**.  
It allows you to manage contacts, phone numbers, and birthdays using simple text commands.

### 🔧 Features:
- Add, update, or delete contacts
- Store birthdays in format `DD.MM.YYYY`
- Show upcoming birthdays within a week
- Safe exit with `exit` or `close`
- Friendly validation and clear error messages

---

## ⚙️ **Architecture**


The project follows **Clean Architecture principles** and is divided into three layers:

```
📦 goit-pycore-hw-07
┣━━ .gitignore
┣━━ BLL
┃   ┣━━ Decorators
┃   ┃   ┗━━ CommandHandlerDecorator.py
┃   ┣━━ Helpers
┃   ┃   ┗━━ DateHelper.py
┃   ┗━━ Services
┃       ┣━━ CommandService
┃       ┃   ┣━━ CommandService.py
┃       ┃   ┗━━ ICommandService.py
┃       ┣━━ InputService
┃       ┃   ┣━━ IInputService.py
┃       ┃   ┗━━ InputService.py
┃       ┗━━ RecordService
┃           ┣━━ IRecordService.py
┃           ┗━━ RecordService.py
┣━━ DAL
┃   ┣━━ AddressBookStorage.py
┃   ┣━━ Entities
┃   ┃   ┣━━ Birthday.py
┃   ┃   ┣━━ Command.py
┃   ┃   ┣━━ Field.py
┃   ┃   ┣━━ Name.py
┃   ┃   ┣━━ Phone.py
┃   ┃   ┗━━ Record.py
┃   ┣━━ Exceptions
┃   ┃   ┣━━ AlreadyExistException.py
┃   ┃   ┣━━ ExitBotException.py
┃   ┃   ┣━━ InvalidException.py
┃   ┃   ┗━━ NotFoundException.py
┃   ┗━━ IStorage.py
┣━━ main.py
┣━━ README.md
┗━━ Tests
    ┣━━ AddressBookManagementTests
    ┃   ┣━━ test_address_book_storage.py
    ┃   ┣━━ test_birthday_entity.py
    ┃   ┣━━ test_end_to_end_address_book.py
    ┃   ┣━━ test_field_name_phone.py
    ┃   ┣━━ test_record_entity.py
    ┃   ┗━━ test_record_service.py
    ┣━━ BotTests
    ┃   ┣━━ test_command_service.py
    ┃   ┣━━ test_end_to_end_bot_flow.py
    ┃   ┗━━ test_input_service.py
    ┗━━ test_date_helper.py
```

---

## 💬 **User Commands**

| Command | Description |
|----------|-------------|
| `hello` | Greet the bot |
| `add [name] [phone]` | Add a new contact |
| `add-phone [name] [new_phone]` | Add another phone to an existing contact |
| `phone [name]` | Show all phones for a contact |
| `add-birthday [name] [DD.MM.YYYY]` | Add a birthday |
| `show-birthday [name]` | Show a contact’s birthday |
| `birthdays` | Show all birthdays within the next week |
| `all` | Show all contacts |
| `exit` / `close` | Exit the program safely |

---

## 🧪 **Testing**

Run all tests with coverage:
```bash
pytest --cov=BLL --cov=DAL --cov=Tests --cov-report=term-missing
```

---

## 🚀 **Run the bot**

```bash
python main.py
```

---

## 🧠 **Demo Example**

```
Welcome to the assistant bot!
Enter a command: add John +380991112233
Contact added.
Enter a command: add-birthday John 05.11.2000
Contact updated.
Enter a command: birthdays
Contact: John - 05.11.2000
Enter a command: exit
Good bye!
```

---

## 👨‍💻 **Author**
**Kulchitskiy Roman**  
Full Stack Developer (.NET / Python)  
[LinkedIn Profile](https://www.linkedin.com/in/kulchitskiy-r)

---

## 🇺🇦 **Опис проєкту**

Цей консольний застосунок — **бот-асистент для роботи з адресною книгою**, створений у рамках курсу **GOIT Python Core (Модуль 7 – Розширене ООП)**.  
Він дозволяє зручно керувати контактами, номерами телефонів і днями народження через команди.

### 🔧 Основні можливості:
- Додавання, оновлення, видалення контактів
- Додавання днів народження у форматі `DD.MM.YYYY`
- Перегляд усіх контактів
- Вивід днів народження, що наближаються протягом наступного тижня
- Коректне завершення роботи командою `exit` або `close`

---

## ⚙️ **Архітектура проєкту**

Проєкт реалізовано за принципами **Clean Architecture (чистої архітектури)**, з чітким розділенням на рівні:

```
📦 goit-pycore-hw-07
┣━━ .gitignore
┣━━ BLL
┃   ┣━━ Decorators
┃   ┃   ┗━━ CommandHandlerDecorator.py
┃   ┣━━ Helpers
┃   ┃   ┗━━ DateHelper.py
┃   ┗━━ Services
┃       ┣━━ CommandService
┃       ┃   ┣━━ CommandService.py
┃       ┃   ┗━━ ICommandService.py
┃       ┣━━ InputService
┃       ┃   ┣━━ IInputService.py
┃       ┃   ┗━━ InputService.py
┃       ┗━━ RecordService
┃           ┣━━ IRecordService.py
┃           ┗━━ RecordService.py
┣━━ DAL
┃   ┣━━ AddressBookStorage.py
┃   ┣━━ Entities
┃   ┃   ┣━━ Birthday.py
┃   ┃   ┣━━ Command.py
┃   ┃   ┣━━ Field.py
┃   ┃   ┣━━ Name.py
┃   ┃   ┣━━ Phone.py
┃   ┃   ┗━━ Record.py
┃   ┣━━ Exceptions
┃   ┃   ┣━━ AlreadyExistException.py
┃   ┃   ┣━━ ExitBotException.py
┃   ┃   ┣━━ InvalidException.py
┃   ┃   ┗━━ NotFoundException.py
┃   ┗━━ IStorage.py
┣━━ main.py
┣━━ README.md
┗━━ Tests
    ┣━━ AddressBookManagementTests
    ┃   ┣━━ test_address_book_storage.py
    ┃   ┣━━ test_birthday_entity.py
    ┃   ┣━━ test_end_to_end_address_book.py
    ┃   ┣━━ test_field_name_phone.py
    ┃   ┣━━ test_record_entity.py
    ┃   ┗━━ test_record_service.py
    ┣━━ BotTests
    ┃   ┣━━ test_command_service.py
    ┃   ┣━━ test_end_to_end_bot_flow.py
    ┃   ┗━━ test_input_service.py
    ┗━━ test_date_helper.py
```

---

## 🧩 **Основні класи**
| Клас | Призначення |
|------|--------------|
| `Record` | Представляє контакт (ім’я, телефони, день народження) |
| `Phone` | Валідує телефонні номери |
| `Birthday` | Зберігає дату народження, перевіряє формат |
| `RecordService` | Бізнес-логіка для керування записами |
| `CommandService` | Обробляє усі команди користувача |
| `InputService` | Приймає введення користувача і маршрутизує до потрібної команди |
| `AddressBookStorage` | Зберігає всі записи у пам’яті |
| `DateHelper` | Обробляє дати, визначає наближені дні народження |

---

## 💬 **Команди користувача**

| Команда | Опис |
|----------|------|
| `hello` | Привітання з ботом |
| `add [name] [phone]` | Додає новий контакт |
| `add-phone [name] [new_phone]` | Додає ще один номер до контакту |
| `phone [name]` | Показує всі телефони контакту |
| `add-birthday [name] [DD.MM.YYYY]` | Додає день народження |
| `show-birthday [name]` | Показує день народження контакту |
| `birthdays` | Показує список контактів із днями народження на наступному тижні |
| `all` | Показує всі контакти |
| `exit` / `close` | Завершує роботу програми |

---

## 🧪 **Тестування**

Використовується `pytest` із повним покриттям:
```bash
pytest --cov=BLL --cov=DAL --cov=Tests --cov-report=term-missing
```

---

## 🚀 **Як запустити**

1. Клонуй репозиторій:
   ```bash
   git clone https://github.com/<your_username>/goit-pycore-hw-07.git
   cd goit-pycore-hw-07
   ```

2. Створи віртуальне середовище:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # для Linux / Mac
   .venv\Scripts\activate     # для Windows
   ```

3. Встанови залежності:
   ```bash
   pip install -r requirements.txt
   ```

4. Запусти бота:
   ```bash
   python main.py
   ```

---

## 🧠 **Приклад роботи**

```
Welcome to the assistant bot!
Enter a command: add John +380991112233
Contact added. Contact name: John, phones: +380991112233
Enter a command: add-birthday John 05.11.2000
Contact updated. Contact name: John, phones: +380991112233, birthday: 05.11.2000
Enter a command: birthdays
Contact: John - 05.11.2000
Enter a command: exit
Good bye!
```

---

## 🧾 **Автор**
**Kulchitskiy Roman**  
.NET / Python Full Stack Developer  
[LinkedIn Profile](https://www.linkedin.com/in/kulchitskiy-r)

---
