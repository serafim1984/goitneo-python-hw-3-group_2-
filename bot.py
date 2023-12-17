import address_book_manager
from collections import UserDict

contacts = address_book_manager.AddressBook()

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (ValueError, KeyError, IndexError):
            return """Please give me correct input\n
                      To add contact >>> 'add' <name> <phone number>\n
                      To change contact >>> 'change' <name> <phone number old> <phone number new>\n
                      To see a phone number of a contact >>> 'phone' <name>\n
                      To see all contacts >>> 'all'\n
                      To add birthday to contact >>> 'add' <name> <birthday date in forman DD.MM.YYYY>\n
                      To show all birthdays in next week >>> 'birthdays'\n
                      To show birthday of a person >>> 'show-birthday' <name>\n
                      To close me >>> 'close' or 'exit'\n
                      """

    return inner


@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts):
    name, phone = args
    new_record = address_book_manager.Record(name)
    new_record.add_phone(phone)
    contacts.add_record(new_record)
    return "Contact added."

@input_error
def add_birthday(args, contacts):
    name, birthday = args
    contacts.find_record(name).add_birthday(birthday)
    return "Birthday added."

@input_error
def show_birthday(args, contacts):
    name = args
    return contacts.find_record(name).birthday()

@input_error
def birthdays():
    contacts.get_birthdays()

@input_error
def change_contact(args, contacts):
    name, phone_1, phone_2 = args
 
    
    contacts.find_record(name).edit_phone(phone_1, phone_2)

    return "Contact changed."

@input_error
def phone_contact(args, contacts):
    name = args
    contacts.find_record(name).find_phone_name()

@input_error
def all_contact():

    for name, record  in contacts.data.items():
        print(record)



def main():
    global contacts
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

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
            print(phone_contact(args, contacts))
        elif command == "all":
            print(all_contact())
        elif command == "add-birthday":
            print(add_birthday(args, contacts))
        elif command == "show-birthday":
            print(show_birthday(args, contacts))
        elif command == "birthdays":
            birthdays()
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
