from ttkbootstrap import Frame, LabelFrame, Label, Entry, Button, END, INFO, DARK, OUTLINE, SUCCESS
from ttkbootstrap.dialogs import Messagebox
from BusinessLogicLayer.employee_business import EmployeeBusiness
from CommonLayer.decorator import performance_logger_decorator
from CommonLayer.get_employee_clicker import EmployeeClicker


class LoginFrame(Frame):
    def __init__(self, view, window):
        super().__init__(window)
        self.grid_columnconfigure(0, weight=1)

        self.employee_business = EmployeeBusiness()

        self.view = view

        self.header = LabelFrame(self, text="Login with your Account", bootstyle=INFO)
        self.header.grid_columnconfigure(1, weight=1)
        self.header.grid(row=0, column=0, padx=(10, 10), pady=(10, 10), sticky="nsew")

        # Username
        self.username_label = Label(self.header, text="Username  : ", foreground="gray")
        self.username_label.grid(row=0, column=0, padx=(10, 10), pady=(10, 10), sticky="w")

        self.username_entry = Entry(self.header, bootstyle=DARK)
        self.username_entry.grid(row=0, column=1, padx=(0, 10), pady=(10, 10), sticky="ew")

        # Password
        self.password_label = Label(self.header, text="Password  : ", foreground="gray")
        self.password_label.grid(row=1, column=0, padx=(10, 10), pady=(0, 10), sticky="w")

        self.password_entry = Entry(self.header, bootstyle=DARK, show="*")
        self.password_entry.grid(row=1, column=1, padx=(0, 10), pady=(0, 10), sticky="ew")

        # Login Button
        self.login_button = Button(self.header, text="Login", bootstyle=OUTLINE + SUCCESS,
                                   command=self.login_button_clicked)
        self.login_button.grid(row=2, column=1, padx=(0, 10), pady=(0, 10), sticky="w")

    @performance_logger_decorator
    def login_button_clicked(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        result = self.employee_business.login(username, password)
        employee = result[0]
        error_message = result[1]

        if employee:
            EmployeeClicker.employee_clicker = employee.username

        if error_message:
            Messagebox.show_error(title="Error", message=error_message, alert=True)
        else:
            self.username_entry.delete(0, END)
            self.password_entry.delete(0, END)
            home_frame = self.view.switch("home")
            home_frame.set_current_employee(employee)
