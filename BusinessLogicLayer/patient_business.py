from CommonLayer.role_data_type import Role
from CommonLayer.active_data_type import Status
from DataAccessLayer.patient_access import PatientDataAccess
from datetime import date


class PatientBusiness:
    def __init__(self):
        self.patient_data_access = PatientDataAccess()

    def get_patients(self, current_employee, sort, search_by_nationality_code):
        all_national_code = self.patient_data_access.return_all_patient_national_code()

        data_role = int(current_employee.role_id)
        role = Role(data_role)
        data_status = current_employee.active
        active = Status(data_status)
        if role != Role.BOSS and role != Role.SECRETARY:
            return [None, "Invalid Access"]
        if active == Status.DEACTIVE:
            return [None, "Your Account Deactivate"]
        if search_by_nationality_code:
            for item in all_national_code:
                if search_by_nationality_code == item:
                    patient_search = self.patient_data_access.search_with_national_code(search_by_nationality_code)
                    return [patient_search, None]
            return [None, "There is no one with this last name"]

        else:
            patients = self.patient_data_access.get_patients()
            if sort == "Name":
                sort_by_name = sorted(patients, key=lambda name: name.firstname)
                return [sort_by_name, None]
            elif sort == "Gender":
                sort_by_gender = sorted(patients, key=lambda gender: gender.gender)
                return [sort_by_gender, None]
            elif sort == "Birthday":
                sort_by_birthday = sorted(patients, key=lambda birthday: birthday.birthday)
                return [sort_by_birthday, None]
            return [patients, None]

    def create_new_patient(self, firstname, lastname, national_code: int, birthday, gender, phone_number: int, address,
                           disease_name, treating_physician):
        if (len(firstname) < 3 or len(lastname) < 3 or national_code == 9 or len(
                lastname) < 3 or phone_number < 10 or len(address) < 6 or len(disease_name) < 4 or
                len(treating_physician) < 3):
            return "Fill in the blank fields"
        if gender == 0:
            return "Please specify your gender"
        try:
            data_value = date.fromisoformat(birthday)
        except:
            return "Invalid Birthday"
        else:
            self.patient_data_access.create_patient(firstname, lastname, national_code, data_value, gender,
                                                    phone_number, address, disease_name, treating_physician)
            return None

    def delete_patient(self, current_employee, patient_national_code):
        data_role = int(current_employee.role_id)
        role = Role(data_role)
        data_status = current_employee.active
        status = Status(data_status)
        if role != Role.BOSS and role != Role.SECRETARY:
            return "Invalid Access"
        if status == Status.DEACTIVE:
            return "Your Account Deactivate"
        else:
            self.patient_data_access.delete_patient(patient_national_code)
            return None
