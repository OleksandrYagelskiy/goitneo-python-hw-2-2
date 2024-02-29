from collections import UserDict

class Field: # Базовий клас для полів запису
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field): # Клас для зберігання імені контакту. Обов'язкове поле.
    def __init__(self, value):
        super().__init__(value)

class Phone(Field): # Клас для зберігання номера телефону. Має валідацію формату (10 цифр).
    def __init__(self, value):
        if not self._validate_phone(value):
            raise ValueError("Invalid phone number format")
        super().__init__(value)

    def _validate_phone(self, value):
        return len(value) == 10 and value.isdigit()

class Record: # Клас для зберігання інформації про контакт, включаючи ім'я та список телефонів.
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        self.phones = [p for p in self.phones if str(p) != phone]

    def edit_phone(self, old_phone, new_phone):
        for i, phone in enumerate(self.phones):
            if str(phone) == old_phone:
                self.phones[i] = Phone(new_phone)

    def find_phone(self, phone):
        for p in self.phones:
            if str(p) == phone:
                return p

    def __str__(self): # реалізація класу
        phones_str = "; ".join(str(p) for p in self.phones)
        return f"Contact name: {self.name}, phones: {phones_str}"

class AddressBook(UserDict): # реалізація класу
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        del self.data[name]

book = AddressBook() # Створення нової адресної книги

john_record = Record("John") # Створення запису для John
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

book.add_record(john_record) # Додавання запису John до адресної книги

jane_record = Record("Jane") # Створення та додавання нового запису для Jane
jane_record.add_phone("9876543210")
book.add_record(jane_record)

for name, record in book.data.items(): # Виведення всіх записів у книзі
    print(record)

john = book.find("John") # Знаходження та редагування телефону для John
john.edit_phone("1234567890", "1112223333")
print(john)  # Виведення:
