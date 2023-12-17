import re
import get_birthdays_per_week
from collections import UserDict

class PhoneNumberLenthException(Exception):
    pass

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass

class Phone(Field):
    def __init__(self, value):
        super().__init__(value)

        self.__value = None
        self.phone = value

    @property
    def phone(self):
        return self.__value
    
    @phone.setter
    def phone(self, value):
        if len(self.value) == 10: 
            self.__value = value
            
        else:
            raise ValueError('Number must be 10 digits long - please try once more')
        
class Birthday(Field):
    def __init__(self, value):
        super().__init__(value)

        self.__value = None
        self.birthday = value

    @property
    def birthday(self):
        return self.__value
    
    @birthday.setter
    def birthday(self, value):
        if re.search('\d{2}.\d{2}.\d{4}', value): 
            self.__value = value
            
        else:
            raise ValueError('Date of birthday must be exactly in format: DD.MM.YYYY - please try once more')
        

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_phone(self, phone):
        return self.phones.append(Phone(phone))
    
    def add_birthday(self, birthday):  
        self.birthday = Birthday(birthday)
        return self.birthday
    
    def remove_phone(self, phone):
        return self.phones.remove(phone)
    
    def edit_phone(self, phone, new_phone):
        for ph in self.phones:
            if str(ph) == phone:
                self.phones[self.phones.index(ph)] = Phone(new_phone)
            return self
    
    def find_phone(self, phone): 
        for ph in self.phones:
            if str(ph) == phone:
                found_phone = phone
        return found_phone
    
    def find_phone_name(self):
        for phone in self.phones:
            print(phone)

    def show_birthday(self):
        print(str(self.birthday))
    
    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}, birthday: {self.birthday}"

class AddressBook(UserDict):

    def add_record(self, record):
        self.update({record.name : record})

    def find_record(self, name):
        for name_dict, record in self.data.items():
            if str(name_dict) == name:
                return Record(record)

    def delete(self, name):
        for name_dict, record in self.data.items():
            if str(name_dict) == name:
                to_remove = name_dict
        self.data.pop(to_remove) 

    def get_birthdays(self):
        
        colleagues_list = self.values()

        print(colleagues_list)
        
        return get_birthdays_per_week.get_birthdays_per_week(colleagues_list)


'''        
# реалізація класу
# Створення нової адресної книги
book = AddressBook()

john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

# Додавання запису John до адресної книги
book.add_record(john_record)

# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Виведення всіх записів у книзі
for name, record in book.data.items():
    print(record)

# Знаходження та редагування телефону для John
john = book.find("John")

print(john)

john.edit_phone("1234567890", "1112223333")

print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

# Видалення запису Jane
book.delete("Jane")

# Виведення всіх записів у книзі (перевірка видалення)
for name, record in book.data.items():
    print(record)

john_record.add_birthday("18.12.2001")

for name, record in book.data.items():
    print(record)

roman_record = Record("Roman")
roman_record.add_phone("0501614466")
book.add_record(roman_record)

for name, record in book.data.items():
    print(record)

roman_record.add_birthday("15.06.1984")

book.get_birthdays()
'''
