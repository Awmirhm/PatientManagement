import sqlite3
from CommonLayer.patient import Patient


class PatientDataAccess:
    def __init__(self):
        self.data_base_name = "PatientManagement.db"

    def get_patients(self):
        patients = []
        with sqlite3.connect(self.data_base_name) as connection:
            cursor = connection.cursor()
            data = cursor.execute("""
                    SELECT id,
                           first_name,
                           last_name,
                           national_code,
                           birthday,
                           gender_id,
                           phone_number,
                           address,
                           disease_name,
                           treating_physician
                    FROM Patient""").fetchall()
            for item in data:
                patient = Patient.create_with_list(item)
                patients.append(patient)

            return patients

    def search_with_national_code(self, patient_national_code):
        patient_searched = []
        with sqlite3.connect(self.data_base_name) as connection:
            cursor = connection.cursor()
            data = cursor.execute("""
                    SELECT id,
                           first_name,
                           last_name,
                           national_code,
                           birthday,
                           gender_id,
                           phone_number,
                           address,
                           disease_name,
                           treating_physician
                    FROM Patient
                    WHERE national_code like ?""", [patient_national_code]).fetchall()
            for item in data:
                patient = Patient.create_with_list(item)
                patient_searched.append(patient)
            return patient_searched

    def return_all_patient_national_code(self):
        all_national_code = []
        with sqlite3.connect(self.data_base_name) as connection:
            cursor = connection.cursor()
            data = cursor.execute("""
                    SELECT id,
                           first_name,
                           last_name,
                           national_code,
                           birthday,
                           gender_id,
                           phone_number,
                           address,
                           disease_name,
                           treating_physician       
                    FROM Patient""").fetchall()
            for item in data:
                all_national_code.append(item[3])
            return all_national_code

    def create_patient(self, firstname, lastname, national_code, birthday, gender, phone_number, address, disease_name,
                       treating_physician):
        with sqlite3.connect(self.data_base_name) as connection:
            cursor = connection.cursor()
            cursor.execute("""
                    INSERT INTO Patient (
                                first_name,
                                last_name,
                                national_code,
                                birthday,
                                gender_id,
                                phone_number,
                                address,
                                disease_name,
                                treating_physician            
                            )
                            VALUES (
                                ?,
                                ?,
                                ?,
                                ?,
                                ?,
                                ?,
                                ?,
                                ?,
                                ?
                            )""",
                           [firstname, lastname, national_code, birthday, gender, phone_number, address, disease_name,
                            treating_physician])
            connection.commit()

    def delete_patient(self, national_code):
        with sqlite3.connect(self.data_base_name) as connection:
            cursor = connection.cursor()
            cursor.execute("""
                    DELETE FROM Patient
                    WHERE  national_code = ?""", [national_code])
            connection.commit()
