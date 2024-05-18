from DataAccessLayer.employee_data_access import EmployeeDataAccess
from CommonLayer.active_data_type import Status
from CommonLayer.role_data_type import Role
from datetime import date
from passlib.hash import pbkdf2_sha256


class EmployeeBusiness:
    def __init__(self):
        self.employee_data_access = EmployeeDataAccess()
        self.employee = None

    def login(self, username, password):
        passwords = self.employee_data_access.return_all_password()

        if len(username) < 3 or len(password) < 3:
            return [None, "Invalid Request"]
        else:
            for item in passwords:
                if pbkdf2_sha256.verify(password, item):
                    self.employee = self.employee_data_access.get_employee(username, item)
                    break

            if self.employee:
                data_status = self.employee.active
                active = Status(data_status)
                if active == Status.DEACTIVE:
                    return [None, "Your Account Deactivate"]
                else:
                    return [self.employee, None]
            else:
                return [None, "Invalid Username or Password"]

    def get_employees(self, current_employee, sort, search_by_last_name):
        all_last_name = self.employee_data_access.return_all_last_name()

        data_role = int(current_employee.role_id)
        role = Role(data_role)
        data_status = current_employee.active
        active = Status(data_status)
        if role != Role.BOSS:
            return [None, "Invalid Access"]
        if active == Status.DEACTIVE:
            return [None, "Your Account Deactivate"]
        if search_by_last_name:
            for item in all_last_name:
                if search_by_last_name in item:
                    employee_searches = self.employee_data_access.search_employee(search_by_last_name)
                    return [employee_searches, None]
            return [None, "There is no one with this last name"]
        else:
            employees = self.employee_data_access.get_employees(current_employee.id)
            if sort == "Name":
                sort_by_name = sorted(employees, key=lambda name: name.firstname)
                return [sort_by_name, None]
            elif sort == "Birthday":
                sort_by_birthday = sorted(employees, key=lambda birthday: birthday.birthday)
                return [sort_by_birthday, None]
            elif sort == "Salary":
                sort_by_salary = sorted(employees, key=lambda salary: salary.salary)
                return [sort_by_salary, None]
            return [employees, None]

    def update_to_active(self, current_employee, employee_username):
        data_role = int(current_employee.role_id)
        role = Role(data_role)
        data_status = current_employee.active
        active = Status(data_status)
        if role != Role.BOSS:
            return "Invalid Access"
        if active == Status.DEACTIVE:
            return "Your Account Deactivate"
        else:
            self.employee_data_access.update_status(1, employee_username)
            return None

    def update_to_deactivate(self, current_employee, employee_username):
        data_role = int(current_employee.role_id)
        role = Role(data_role)
        data_status = current_employee.active
        active = Status(data_status)
        if role != Role.BOSS:
            return "Invalid Access"
        if active == Status.DEACTIVE:
            return "Your Account Deactivate"
        else:
            self.employee_data_access.update_status(0, employee_username)
            return None

    def delete_employee(self, current_employee, employee_username):
        data_role = int(current_employee.role_id)
        role = Role(data_role)
        data_status = current_employee.active
        active = Status(data_status)
        if role != Role.BOSS:
            return "Invalid Access"
        if active == Status.DEACTIVE:
            return "Your Account Deactivate"
        else:
            self.employee_data_access.delete_employee(employee_username)
            return None

    def create_employee(self, firstname, lastname, username, user_password, birthday, gender, salary):
        usernames = self.employee_data_access.return_all_username()

        if len(firstname) < 3 or len(username) < 3:
            return [None, "Length should be least 3"]

        if any(char.isdigit() for char in firstname):
            return [None, "The First Name does not have a number"]

        if len(lastname) < 4:
            return [None, "Length should be least 3"]

        if any(char.isdigit() for char in lastname):
            return [None, "The Last Name does not have a number"]

        if not isinstance(user_password, str):
            return [None, "The password_user must be a string"]

        if len(user_password) < 6:
            return [None, f"length should be at least 6"]

        if len(user_password) > 20:
            return [None, f"length should be not be greater than 20"]

        if not any(char.isdigit() for char in user_password):
            return [None, "Password should have at least one numeral"]

        if not any(char.isupper() for char in user_password):
            return [None, "Password should have at least one uppercase letter"]

        if not any(char.islower() for char in user_password):
            return [None, "Password should have at least one lowercase letter"]

        password_hash = pbkdf2_sha256.hash(user_password)

        if gender == 0:
            return [None, "Please specify your gender"]

        if not isinstance(salary, int) or salary < 10000000:
            return [None, "Salary should least 1,000,000"]
        try:
            date_value = date.fromisoformat(birthday)
        except:
            return [None, "Invalid Birthday"]
        else:
            for item in usernames:
                if username == item:
                    return [None, "Duplicate Username"]

            self.employee_data_access.create_employee(firstname, lastname, username, password_hash, date_value,
                                                      gender,
                                                      salary)
