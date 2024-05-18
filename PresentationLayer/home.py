from ttkbootstrap import Frame, Label, Button, OUTLINE, WARNING, INFO, LIGHT,SUCCESS
from CommonLayer.role_data_type import Role


class HomeFrame(Frame):
    def __init__(self, view, window):
        super().__init__(window)

        self.grid_columnconfigure(1, weight=1)

        self.view = view

        self.current_employee = None

        self.employee_button = None
        self.employee_register_button = None
        self.patient_button = None

        self.header = Label(self, text="Wellcome")
        self.header.grid(row=0, column=1, padx=(10, 10), pady=(10, 10), sticky="w")

        # Login Button
        self.logout_button = Button(self, text="Logout", bootstyle=WARNING, command=self.logout_button_clicked)
        self.logout_button.grid(row=5, column=1, padx=(10, 10), pady=(10, 10), sticky="ew")

    def set_current_employee(self, employee):
        self.current_employee = employee
        data = int(self.current_employee.role_id)
        role = Role(data)
        self.header.config(
            text=f"Wellcome , {self.current_employee.firstname} {self.current_employee.lastname} ({role.name})")

        # Employee Button
        if role == Role.BOSS:
            if not self.employee_button or self.employee_register_button:
                self.employee_button = Button(self, text="Employee List", bootstyle=OUTLINE + INFO,
                                              command=self.show_employees)
                self.employee_button.grid(row=1, column=1, padx=(10, 10), pady=(10, 10), sticky="ew")

                self.employee_register_button = Button(self, text="Employee Register",
                                                       command=self.employee_register_button_clicked , bootstyle = OUTLINE+LIGHT)
                self.employee_register_button.grid(row=2, column=1, padx=(10, 10), pady=(10, 10), sticky="ew")
        else:
            if self.employee_button and self.employee_register_button:
                self.employee_button.destroy()
                self.employee_register_button.destroy()
                self.employee_button = None
                self.employee_register_button = None

        # Patient Button
        if role == Role.BOSS or role == Role.SECRETARY:
            if not self.patient_button:
                self.patient_button = Button(self, text="Patients List", bootstyle=OUTLINE + SUCCESS,
                                             command=self.patient_button_clicked)
                self.patient_button.grid(row=3, column=1, padx=(10, 10), pady=(10, 10), sticky="ew")
        else:
            if self.patient_button:
                self.patient_button.destroy()
                self.patient_button = None

    def logout_button_clicked(self):
        self.view.switch("login")

    def show_employees(self):
        employee_management = self.view.switch("employee_management")
        employee_management.load_data(self.current_employee)

    def patient_button_clicked(self):
        patient_management = self.view.switch("patient_management")
        patient_management.load_patient_data(self.current_employee)

    def employee_register_button_clicked(self):
        self.view.switch("employee_register")
