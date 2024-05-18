from .descriptor import LengthDescriptor
from .descriptor import NationalCodeDescriptor
from .descriptor import BirthdayDescriptor
from .descriptor import PhoneNumerDescriptor
from datetime import date


class Patient:
    Hospital_name = ""
    firstname = LengthDescriptor(3)
    lastname = LengthDescriptor(4)
    national_code = NationalCodeDescriptor(9)
    birthday = BirthdayDescriptor()
    phone_number = PhoneNumerDescriptor()
    address = LengthDescriptor(6)
    disease_name = LengthDescriptor(2)
    treating_physician = LengthDescriptor(3)

    def __init__(self, id, firstname, lastname, national_code: int, birthday, gender, phone_number: int, address,
                 disease_name, treating_physician):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.national_code = national_code
        self.birthday = birthday
        self.gender = gender
        self.phone_number = phone_number
        self.address = address
        self.disease_name = disease_name
        self.treating_physician = treating_physician

    def calculate_age(self):
        year = date.today().year
        return year - self.birthday.yaer

    @classmethod
    def create_with_tuple(cls, data: tuple):
        return cls(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9])

    @classmethod
    def create_with_list(cls, data: list):
        return cls(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9])
