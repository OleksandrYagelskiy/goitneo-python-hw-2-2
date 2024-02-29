def parse_input(user_input):  # Розбиває введений рядок на команду та аргументи
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Contact not found."
        except IndexError:
            return "Missing command arguments."

    return inner


@input_error
def add_contact(args, contacts):  # Додає новий контакт
    name, phone = args
    contacts[name] = phone
    return "Contact added."


@input_error
def change_contact(args, contacts):  # Змінює номер телефону вже існуючого контакту
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        raise KeyError


@input_error
def show_phone(args, contacts):  # Показує номер телефону для вказаного контакту
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        raise KeyError


def show_all(contacts):  # Показує всі контакти
    if contacts:
        return '\n'.join([f"{name}: {phone}" for name, phone in contacts.items()])
    else:
        return "No contacts found."


def main():  # Головна функція, яка взаємодіє з користувачем
    contacts = {}
    print("Welcome to the assistant bot!")

    while True:
        try:
            user_input = input("Enter a command: ")
            command, args = parse_input(user_input)

            if command in ["close", "exit"]:
                print("Good bye!")
                break

            elif command == "hello":
                print("How can I help you?")

            elif command == "add":
                print(add_contact(args, contacts))

            elif command == "change":
                print(change_contact(args, contacts))

            elif command == "phone":
                print(show_phone(args, contacts))

            elif command == "all":
                print(show_all(contacts))

            else:
                print("Invalid command.")

        except Exception as e:
            print(e)


if __name__ == "__main__":
    main()
