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
                      To change contact >>> 'change' <name> <phone number>\n
                      To see a phone number of a contact >>> 'phone' <name>\n
                      To see all contacts >>> 'all'\n
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
    #contacts[name] = name
    new_record = address_book_manager.Record(name)
    new_record.add_phone(phone)
    contacts.add_record(new_record)
    return "Contact added."

@input_error
def add_birthday(args, contacts):
    name, birthday = args
    #contacts[name] = name
    contacts.find_record(name).add_birthday(birthday)
    return "Birthday added."

@input_error
def change_contact(args, contacts):
    name, phone_1, phone_2 = args
    #contacts[name] = name
    
    contacts.find_record(name).edit_phone(phone_1, phone_2)

    return "Contact changed."

@input_error
def phone_contact(args, contacts):
    name = args
    #contact_phone = contacts[name]
    contacts.find_record(name).find_phone_name()

@input_error
def all_contact():

    for name, record  in contacts.data.items():
        print(record)

    '''global contacts
    all_contacts = ""
    for name, phone in contacts.items():
        all_contacts = all_contacts + name + " " + phone + "\n"
    return all_contacts[:-1]'''



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
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
