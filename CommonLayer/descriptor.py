from datetime import date


class LengthDescriptor:
    def __init__(self, max_character):
        self.__max_character = max_character

    def __set_name__(self, owner, name):
        self.__attribute_name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.__attribute_name]

    def __set__(self, instance, value):
        if not isinstance(value, str) or len(value) < self.__max_character:
            raise ValueError(f"Invalid Value Name = {self.__attribute_name}")
        else:
            instance.__dict__[self.__attribute_name] = value


class NationalCodeDescriptor:
    def __init__(self, min_character):
        self.__min_character = min_character

    def __set_name__(self, owner, name):
        self.__attribute_name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.__attribute_name]

    def __set__(self, instance, value):
        if not isinstance(value, int) or value < self.__min_character:
            return ValueError(f"Invalid Value = {self.__attribute_name}")
        else:
            instance.__dict__[self.__attribute_name] = value


class BirthdayDescriptor:
    def __set_name__(self, owner, name):
        self.__attribute_name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.__attribute_name]

    def __set__(self, instance, value):
        try:
            date_value = date.fromisoformat(value)
        except:
            raise ValueError(f"Invalid Value = {self.__attribute_name}")
        else:
            instance.__dict__[self.__attribute_name] = date_value


class PhoneNumerDescriptor:
    def __set_name__(self, owner, name):
        self.__attribute_name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.__attribute_name]

    def __set__(self, instance, value):
        if not isinstance(value, int) or value < 11:
            raise ValueError(f"Invalid Value  = {self.__attribute_name}")
        else:
            instance.__dict__[self.__attribute_name] = value


class SalaryDescriptor:
    def __init__(self, min_salary):
        self.__min_salary = min_salary

    def __set_name__(self, owner, name):
        self.__attribute_name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.__attribute_name]

    def __set__(self, instance, value):
        if not isinstance(value, float) or value < self.__min_salary:
            return ValueError(f"Invalid Value = {self.__attribute_name}")
        else:
            instance.__dict__[self.__attribute_name] = value
