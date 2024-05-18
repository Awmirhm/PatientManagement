from .descriptor import LengthDescriptor
from .descriptor import BirthdayDescriptor
from .descriptor import SalaryDescriptor
from datetime import date


class Employee:
    hospital = ""
    firstname = LengthDescriptor(3)
    lastname = LengthDescriptor(3)
    username = LengthDescriptor(3)
    birthday = BirthdayDescriptor()
    salary = SalaryDescriptor(10000)

    def __init__(self, id, firstname, lastname, username, password, birthday, gender, salary, role_id, active):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.password = password
        self.birthday = birthday
        self.gender = gender
        self.salary = salary
        self.role_id = role_id
        self.active = active

    def calculate_age(self):
        year = date.today().year
        return year - self.birthday.yaer

    @classmethod
    def create_with_tuple(cls, data: tuple):
        return cls(data[0], data[1], data[2], data[3], None, data[4], data[5], data[6], data[7], data[8])

    @classmethod
    def create_with_list(cls, data: list):
        return cls(data[0], data[1], data[2], data[3], None, data[4], data[5], data[6], data[7], data[8])
