from ttkbootstrap import Frame, Labelframe, Label, Entry, Button, DateEntry, Radiobutton, IntVar, WARNING, OUTLINE, \
    DARK, LIGHT, SUCCESS, END, DANGER
from ttkbootstrap.dialogs import Messagebox
from datetime import date
from BusinessLogicLayer.employee_business import EmployeeBusiness


class EmployeeRegistration(Frame):
    def __init__(self, view, window):
        super().__init__(window)

        self.view = view

        self.employee_business = EmployeeBusiness()

        self.salary = None

        self.grid_columnconfigure(0, weight=1)

        self.header = Labelframe(self, text="Employee Registration", bootstyle=SUCCESS)
        self.header.grid_columnconfigure(1, weight=1)
        self.header.grid(row=0, column=0, padx=(10, 10), pady=(10, 10), sticky="nsew")

        # First Name
        self.employee_firstname_label = Label(self.header, text="First Name :")
        self.employee_firstname_label.grid(row=0, column=0, padx=(10, 10), pady=(10, 10), sticky="w")

        self.employee_firstname_entry = Entry(self.header, bootstyle=DARK)
        self.employee_firstname_entry.grid(row=0, column=1, padx=(0, 10), pady=(10, 10), sticky="ew")

        # Last Name
        self.employee_lastname_label = Label(self.header, text="Last Name :")
        self.employee_lastname_label.grid(row=1, column=0, padx=(10, 10), pady=(10, 10), sticky="w")

        self.employee_lastname_entry = Entry(self.header, bootstyle=DARK)
        self.employee_lastname_entry.grid(row=1, column=1, padx=(0, 10), pady=(10, 10), sticky="ew")

        # Username
        self.employee_username_label = Label(self.header, text="Username :")
        self.employee_username_label.grid(row=2, column=0, padx=(10, 10), pady=(10, 10), sticky="w")

        self.employee_username_entry = Entry(self.header, bootstyle=DARK)
        self.employee_username_entry.grid(row=2, column=1, padx=(0, 10), pady=(10, 10), sticky="ew")

        # Password
        self.employee_password_label = Label(self.header, text="Password :")
        self.employee_password_label.grid(row=3, column=0, padx=(10, 10), pady=(10, 10), sticky="w")

        self.employee_password_entry = Entry(self.header, bootstyle=DARK)
        self.employee_password_entry.grid(row=3, column=1, padx=(0, 10), pady=(10, 10), sticky="ew")

        # Birthday
        self.birthday_label = Label(self.header, text="Birthday  :")
        self.birthday_label.grid(row=4, column=0, padx=(10, 10), pady=(10, 10), sticky="w")

        self.birthday_entry = DateEntry(self.header, dateformat="%Y-%m-%d", startdate=date(2000, 1, 1), bootstyle=DARK)
        self.birthday_entry.grid(row=4, column=1, padx=(0, 10), pady=(10, 10), sticky="ew")

        # Gender
        self.gender_label = Label(self.header, text="Gender  :")
        self.gender_label.grid(row=5, column=0, padx=(10, 10), pady=(10, 10), sticky="w")

        self.gender_radio_button_var = IntVar(value=0)
        self.gender_radio_button_for_male = Radiobutton(self.header, value=1, text="Male",
                                                        variable=self.gender_radio_button_var)
        self.gender_radio_button_for_male.grid(row=5, column=1, padx=(0, 10), pady=(10, 10), sticky="ew")

        self.gender_radio_button_for_female = Radiobutton(self.header, value=2, text="Female",
                                                          variable=self.gender_radio_button_var, bootstyle=DANGER)
        self.gender_radio_button_for_female.grid(row=5, column=1, padx=(70, 10), pady=(10, 10), sticky="ew")

        # Salary
        self.salary_label = Label(self.header, text="Salary  :")
        self.salary_label.grid(row=6, column=0, padx=(10, 10), pady=(10, 10), sticky="w")

        self.salary_entry = Entry(self.header, bootstyle=DARK)
        self.salary_entry.grid(row=6, column=1, padx=(0, 10), pady=(10, 10), sticky="ew")

        # Save Button
        self.sava_button = Button(self.header, text="Save", bootstyle=OUTLINE + SUCCESS,
                                  command=self.sava_button_clicked)
        self.sava_button.grid(row=7, column=1, padx=(0, 10), pady=(10, 10), sticky="w")

        # Back To Home Page
        self.back_to_home_page_button = Button(self, text="Back To Home Page",
                                               command=self.back_to_home_page_button_clicked, bootstyle=WARNING)
        self.back_to_home_page_button.grid(row=1, column=0, padx=(10, 10), pady=(10, 10), sticky="ew")

    def back_to_home_page_button_clicked(self):
        self.view.switch("home")
        self.employee_firstname_entry.delete(0, END)
        self.employee_lastname_entry.delete(0, END)
        self.employee_username_entry.delete(0, END)
        self.employee_password_entry.delete(0, END)
        self.salary_entry.delete(0, END)

    def sava_button_clicked(self):
        firstname = str(self.employee_firstname_entry.get())
        lastname = str(self.employee_lastname_entry.get())
        username = str(self.employee_username_entry.get())
        password = str(self.employee_password_entry.get())
        birthday = str(self.birthday_entry.entry.get())
        gener = int(self.gender_radio_button_var.get())
        try:
            self.salary = int(self.salary_entry.get())
        except:
            pass

        result = self.employee_business.create_employee(firstname, lastname, username, password, birthday, gener,
                                                        self.salary)
        save_message = result[0]
        error_message = result[1]

        if error_message:
            Messagebox.show_error(title="Error", message=error_message, alert=True)
        else:
            Messagebox.show_info(title="Info", message=save_message, alert=True)
