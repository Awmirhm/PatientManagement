import sqlite3
from CommonLayer.employees import Employee
from CommonLayer.patient import Patient


class EmployeeDataAccess:
    def __init__(self):
        self.data_base_name = "PatientManagement.db"

    def get_employee(self, username, password):
        with sqlite3.connect(self.data_base_name) as connection:
            cursor = connection.cursor()
            data = cursor.execute("""
                    SELECT id,
                           first_name,
                           last_name,
                           username,
                           birthday,
                           gender_id,
                           salary,
                           role_id,
                           active
                    FROM Employee
                    WHERE  username = ?
                    AND    password = ? """, [username, password]).fetchone()
            if data:
                employee = Employee.create_with_tuple(data)
                return employee
            else:
                return None

    def get_employees(self, current_user_id):
        employees = []
        with sqlite3.connect(self.data_base_name) as connection:
            cursor = connection.cursor()
            data = cursor.execute("""
                SELECT id,
                       first_name,
                       last_name,
                       username,
                       birthday,
                       gender_id,
                       salary,
                       role_id,
                       active
                FROM Employee
                WHERE  id != ?""", [current_user_id]).fetchall()

            for item in data:
                employee = Employee.create_with_list(item)
                employees.append(employee)

            return employees

    def update_status(self, active, employee_username):
        with sqlite3.connect(self.data_base_name) as connection:
            cursor = connection.cursor()
            cursor.execute("""
                UPDATE Employee
                SET     active = ? 
                WHERE   username = ?""", [active, employee_username])

            connection.commit()

    def delete_employee(self, employee_username):
        with sqlite3.connect(self.data_base_name) as connection:
            cursor = connection.cursor()
            cursor.execute("""
                DELETE FROM Employee
                WHERE username = ?""", [employee_username])

            connection.commit()

    def search_employee(self, employee_last_name):
        employee_searched = []
        with sqlite3.connect(self.data_base_name) as connection:
            cursor = connection.cursor()
            data = cursor.execute("""
                    SELECT id,
                           first_name,
                           last_name,
                           username,
                           birthday,
                           gender_id,
                           salary,
                           role_id,
                           active
                    FROM Employee
                    WHERE  last_name like ?""", [employee_last_name]).fetchall()
            for item in data:
                all_employee = Employee.create_with_list(item)
                employee_searched.append(all_employee)
            return employee_searched

    def return_all_last_name(self):
        all_last_name = []
        with sqlite3.connect(self.data_base_name) as connection:
            cursor = connection.cursor()
            data = cursor.execute("""
                    SELECT id,
                           first_name,
                           last_name,
                           username,
                           birthday,
                           gender_id,
                           salary,
                           role_id,
                           active
                    FROM Employee""").fetchall()
            for item in data:
                all_last_name.append(item[2])
            return all_last_name

    def create_employee(self, firstname, lastname, username, password, birthday, gender, salary):
        with sqlite3.connect(self.data_base_name) as connection:
            cursor = connection.cursor()
            cursor.execute("""
                        INSERT INTO Employee (
                                     first_name,
                                     last_name,
                                     username,
                                     password,
                                     birthday,
                                     gender_id,
                                     salary,
                                     role_id,
                                     active
                                 )
                                 VALUES (
                                     ?,
                                     ?,
                                     ?,
                                     ?,
                                     ?,
                                     ?,
                                     ?,
                                    '2',
                                    '0'
                                 )""", [firstname, lastname, username, password, birthday, gender, salary])
            connection.commit()

    def return_all_password(self):
        passwords = []
        with sqlite3.connect(self.data_base_name) as connection:
            cursor = connection.cursor()
            data = cursor.execute("""
                    SELECT id,
                           first_name,
                           last_name,
                           username,
                           password,
                           birthday,
                           gender_id,
                           salary,
                           role_id,
                           active
                    FROM Employee""").fetchall()
            for item in data:
                passwords.append(item[4])
            return passwords

    def return_all_username(self):
        usernames = []
        with sqlite3.connect(self.data_base_name) as connection:
            cursor = connection.cursor()
            data = cursor.execute("""
                    SELECT id,
                           first_name,
                           last_name,
                           username,
                           birthday,
                           gender_id,
                           salary,
                           role_id,
                           active
                    FROM Employee""").fetchall()
            for item in data:
                usernames.append(item[3])
            return usernames
