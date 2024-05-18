from ttkbootstrap import Frame, Labelframe, Label, Entry, Button, Treeview, Scrollbar, END, Combobox, IntVar, \
    DateEntry, Radiobutton, DANGER, Text, WARNING, OUTLINE, DARK, LIGHT, SECONDARY, SUCCESS, VERTICAL, StringVar, \
    READONLY
from datetime import date
from BusinessLogicLayer.patient_business import PatientBusiness
from ttkbootstrap.dialogs import Messagebox
from CommonLayer.gnder_data_type import Gender


class PatientManagementFrame(Frame):
    def __init__(self, view, window):
        super().__init__(window)

        self.patient_business = PatientBusiness()

        self.search_by_nationality_code = None

        self.sort = None

        self.current_employee = None

        self.view = view

        self.treeview_items = []

        self.patient_national_code = None
        self.patient_phone_number = None

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=1)

        self.header = Labelframe(self, text="Create a New Patient", bootstyle=DANGER)
        self.header.grid_columnconfigure(1, weight=1)
        self.header.grid(row=0, column=0, padx=(10, 10), pady=(10, 10), sticky="nsew")

        # First Name
        self.patient_first_name_label = Label(self.header, text="First Name  :")
        self.patient_first_name_label.grid(row=0, column=0, padx=(10, 10), pady=(10, 10), sticky="w")

        self.patient_first_name_entry = Entry(self.header, bootstyle=DARK)
        self.patient_first_name_entry.grid(row=0, column=1, padx=(0, 10), pady=(10, 10), sticky="ew")

        # Last Name
        self.patient_last_name_label = Label(self.header, text="Last Name  :")
        self.patient_last_name_label.grid(row=1, column=0, padx=(10, 10), pady=(10, 10), sticky="w")

        self.patient_last_name_entry = Entry(self.header, bootstyle=DARK)
        self.patient_last_name_entry.grid(row=1, column=1, padx=(0, 10), pady=(10, 10), sticky="ew")

        # National Code
        self.patient_national_code_label = Label(self.header, text="National Code  :")
        self.patient_national_code_label.grid(row=2, column=0, padx=(10, 10), pady=(10, 10), sticky="w")

        self.patient_national_code_entry = Entry(self.header, bootstyle=DARK)
        self.patient_national_code_entry.grid(row=2, column=1, padx=(0, 10), pady=(10, 10), sticky="ew")

        # Birthdate
        self.patient_birth_data_label = Label(self.header, text="Birth Date  :")
        self.patient_birth_data_label.grid(row=3, column=0, padx=(10, 10), pady=(10, 10), sticky="w")

        self.patient_birth_data_entry = DateEntry(self.header, dateformat="%Y-%m-%d", startdate=date(2000, 1, 1),
                                                  bootstyle=DARK)
        self.patient_birth_data_entry.grid(row=3, column=1, padx=(0, 10), pady=(10, 10), sticky="ew")

        # Gender
        self.patient_gender_label = Label(self.header, text="Gender  : ")
        self.patient_gender_label.grid(row=4, column=0, padx=(10, 10), pady=(10, 10), sticky="w")

        self.patient_gender_radio_button_var = IntVar(value=0)
        self.patient_gender_radio_button_for_male = Radiobutton(self.header, value=1,
                                                                variable=self.patient_gender_radio_button_var,
                                                                text="Male")
        self.patient_gender_radio_button_for_male.grid(row=4, column=1, padx=(10, 10), pady=(10, 10), sticky="w")

        self.patient_gender_radio_button_for_female = Radiobutton(self.header, value=2,
                                                                  variable=self.patient_gender_radio_button_var,
                                                                  text="Female", bootstyle=DANGER)
        self.patient_gender_radio_button_for_female.grid(row=4, column=1, padx=(80, 10), pady=(10, 10), sticky="w")

        # Phone Number
        self.patient_phone_number_label = Label(self.header, text="Phone Number  :")
        self.patient_phone_number_label.grid(row=5, column=0, padx=(10, 10), pady=(10, 10), sticky="w")

        self.patient_phone_number_entry = Entry(self.header, bootstyle=DARK)
        self.patient_phone_number_entry.grid(row=5, column=1, padx=(0, 10), pady=(10, 10), sticky="ew")

        # Address
        self.patient_address_label = Label(self.header, text="Address  :")
        self.patient_address_label.grid(row=6, column=0, padx=(10, 10), pady=(10, 10), sticky="w")

        self.patient_address_entry = Entry(self.header, bootstyle=DARK)
        self.patient_address_entry.grid(row=6, column=1, padx=(0, 10), pady=(10, 10), sticky="ew")

        # Disease Name
        self.patient_disease_name_label = Label(self.header, text="Disease Name  :")
        self.patient_disease_name_label.grid(row=7, column=0, padx=(10, 10), pady=(10, 10), sticky="w")

        self.patient_disease_name_entry = Entry(self.header, bootstyle=DARK)
        self.patient_disease_name_entry.grid(row=7, column=1, padx=(0, 10), pady=(10, 10), sticky="ew")

        # Treating Physician
        self.treating_physician_label = Label(self.header, text="Treating Physician")
        self.treating_physician_label.grid(row=8, column=0, padx=(10, 10), pady=(10, 10), sticky="w")

        self.treating_physician_entry = Entry(self.header, bootstyle=DARK)
        self.treating_physician_entry.grid(row=8, column=1, padx=(0, 10), pady=(10, 10), sticky="ew")

        # Save Button
        self.save_button = Button(self.header, text="Save", bootstyle=OUTLINE + SUCCESS,
                                  command=self.save_button_clicked)
        self.save_button.grid(row=9, column=1, padx=(0, 10), pady=(10, 10), sticky="w")

        # Search Box
        self.search_box = Labelframe(self, text="Search with Nationality Code", bootstyle=WARNING)
        self.search_box.grid_columnconfigure(1, weight=1)
        self.search_box.grid(row=1, column=0, padx=(10, 10), pady=(10, 10), sticky="nsew")

        self.search_label = Label(self.search_box, text="Search  : ")
        self.search_label.grid(row=0, column=0, padx=(10, 10), pady=(10, 10), sticky="w")

        self.search_entry = Entry(self.search_box, bootstyle=DARK)
        self.search_entry.grid(row=0, column=1, padx=(0, 10), pady=(10, 10), sticky="ew")

        self.search_button = Button(self.search_box, text="Search", command=self.search_button_clicked)
        self.search_button.grid(row=0, column=2, padx=(0, 10), pady=(10, 10), sticky="w")

        # Treeview
        self.table_frame = Labelframe(self, text="Patient information", bootstyle=SUCCESS)
        self.table_frame.grid_rowconfigure(0, weight=1)
        self.table_frame.grid_columnconfigure(0, weight=1)
        self.table_frame.grid(row=2, column=0, padx=(10, 10), pady=(10, 10), sticky="nsew")

        # Delete
        self.delete_button = Button(self.table_frame, text="Delete Patient", bootstyle=DANGER,
                                    command=self.delete_button_clicked)
        self.delete_button.grid(row=1, column=0, padx=(10, 10), pady=(10, 10), sticky="e")

        # Sort
        self.sort_combobox_var = StringVar(value="None")
        self.sort_combobox = Combobox(self.table_frame, values=["Name", "Gender", "Birthday"],
                                      textvariable=self.sort_combobox_var, state=READONLY)
        self.sort_combobox.grid(row=1, column=0, padx=(10, 10), pady=(10, 10), sticky="w")

        self.sort_button = Button(self.table_frame, text="Sort by", bootstyle=LIGHT + OUTLINE,
                                  command=self.sort_button_clicked)
        self.sort_button.grid(row=2, column=0, padx=(10, 10), pady=(10, 10), sticky="w")

        self.y_scrollbar = Scrollbar(self.table_frame, orient=VERTICAL)
        self.y_scrollbar.grid(row=0, column=1, padx=(10, 10), pady=(10, 10), sticky="ns")

        self.columns = ["first_name", "last_name", "national_code", "birthday", "gender", "phone_number", "address",
                        "disease_name", "treating_physician"]

        self.table = Treeview(self.table_frame, columns=self.columns, bootstyle=LIGHT,
                              yscrollcommand=self.y_scrollbar.set)

        self.table.heading("#0", text="NO")
        self.table.heading("first_name", text="First Name")
        self.table.heading("last_name", text="Last Name")
        self.table.heading("national_code", text="National Code")
        self.table.heading("birthday", text="Birthday")
        self.table.heading("gender", text="Gender")
        self.table.heading("phone_number", text="Phone Number")
        self.table.heading("address", text="Address")
        self.table.heading("disease_name", text="Disease Name")
        self.table.heading("treating_physician", text="Treating Physician")

        self.table.grid(row=0, column=0, padx=(10, 10), pady=(10, 10), sticky="nsew")

        self.y_scrollbar.config(command=self.table.yview)

        # Back To Home Button
        self.back_to_home_page_button = Button(self, text="Back To Home Page", bootstyle=WARNING,
                                               command=self.back_to_home_page_button_clicked)
        self.back_to_home_page_button.grid(row=3, column=0, padx=(10, 10), pady=(10, 10), sticky="ew")

    def load_patient_data(self, current_employee):
        for item in self.treeview_items:
            self.table.delete(item)
        self.treeview_items.clear()

        self.current_employee = current_employee
        result = self.patient_business.get_patients(self.current_employee, self.sort, self.search_by_nationality_code)
        patients = result[0]
        error_message = result[1]

        if error_message:
            Messagebox.show_error(title="Error", message=error_message, alert=True)
        else:
            row_number = 1
            for item in patients:
                data_gender = int(item.gender)
                gender = Gender(data_gender)

                items = self.table.insert("", END, iid=item.national_code, text=str(row_number), values=(
                    item.firstname,
                    item.lastname,
                    item.national_code,
                    item.birthday,
                    f"{gender.name if gender == Gender.MALE else gender.name}",
                    item.phone_number,
                    item.address,
                    item.disease_name,
                    item.treating_physician
                ))
                row_number += 1
                self.treeview_items.append(items)

            self.table.column("#0", width=200, anchor="w")
            for column in self.columns:
                self.table.column(column, width=300, anchor="center")

    def sort_button_clicked(self):
        sort = self.sort_combobox_var.get()
        if sort == "Name":
            self.sort = sort
            self.sort_button.config(text=f"Sort by {self.sort_combobox_var.get()}")
        if sort == "Gender":
            self.sort = sort
            self.sort_button.config(text=f"Sort by {self.sort_combobox_var.get()}")
        if sort == "Birthday":
            self.sort = sort
            self.sort_button.config(text=f"Sort by {self.sort_combobox_var.get()}")
        self.load_patient_data(self.current_employee)

    def search_button_clicked(self):
        search = int(self.search_entry.get())
        if search == "":
            Messagebox.show_error(title="Error", message="Please Enter Your Desired Last Name")
        else:
            self.search_by_nationality_code = search
            self.load_patient_data(self.current_employee)

    def back_to_home_page_button_clicked(self):
        self.view.switch("home")
        self.patient_first_name_entry.delete(0, END)
        self.patient_last_name_entry.delete(0, END)
        self.patient_national_code_entry.delete(0, END)
        self.patient_birth_data_entry.entry.delete(0, END)
        self.patient_phone_number_entry.delete(0, END)
        self.patient_address_entry.delete(0, END)
        self.patient_disease_name_entry.delete(0, END)
        self.treating_physician_entry.delete(0, END)
        self.search_by_nationality_code = None

    def save_button_clicked(self):
        patient_first_name = str(self.patient_first_name_entry.get())
        patient_last_name = str(self.patient_last_name_entry.get())
        try:
            self.patient_national_code = int(self.patient_national_code_entry.get())
        except:
            pass

        patient_birthday = str(self.patient_birth_data_entry.entry.get())
        patient_gender = self.patient_gender_radio_button_var.get()
        try:
            self.patient_phone_number = int(self.patient_phone_number_entry.get())
        except:
            pass

        patient_address = str(self.patient_address_entry.get())
        patient_disease_name = str(self.patient_disease_name_entry.get())
        treating_physician = self.treating_physician_entry.get()

        error_message = self.patient_business.create_new_patient(patient_first_name, patient_last_name,
                                                                 self.patient_national_code,
                                                                 patient_birthday, patient_gender,
                                                                 self.patient_phone_number,
                                                                 patient_address, patient_disease_name,
                                                                 treating_physician)

        if error_message:
            Messagebox.show_error(title="Error", message=error_message, alert=True)
        else:
            self.load_patient_data(self.current_employee)

    def delete_button_clicked(self):
        for national_code in self.table.selection():
            error_message = self.patient_business.delete_patient(self.current_employee, national_code)

            if error_message:
                Messagebox.show_error(title="Error", message=error_message, alert=True)
            else:
                self.load_patient_data(self.current_employee)
