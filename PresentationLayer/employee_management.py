from ttkbootstrap import Frame, Treeview, Button, Label, Entry, END, Scrollbar, VERTICAL, SUCCESS, WARNING, OUTLINE, \
    DANGER, Combobox, StringVar, READONLY, LIGHT, DARK
from ttkbootstrap.dialogs import Messagebox
from BusinessLogicLayer.employee_business import EmployeeBusiness
from CommonLayer.gnder_data_type import Gender
from CommonLayer.role_data_type import Role
from CommonLayer.active_data_type import Status


class EmployeeManagementFrame(Frame):
    def __init__(self, view, window):
        super().__init__(window)

        self.employee_business = EmployeeBusiness()

        self.sort = None

        self.view = view

        self.search_by_last_name = None

        self.current_employee = None

        self.treeview_items = []

        self.delete_button = None
        self.active_button = None
        self.deactive_button = None

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)

        self.header = Label(self, text="Employee Management")
        self.header.grid(row=0, column=0, padx=(10, 10), pady=(10, 10), sticky="w")

        # Search Box
        self.search_entry = Entry(self)
        self.search_entry.grid(row=0, column=1, padx=(0, 10), pady=(10, 10), sticky="ew")

        self.search_button = Button(self, text="Search", command=self.search_button_clicked)
        self.search_button.grid(row=0, column=2, padx=(0, 10), pady=(10, 10), sticky="w")

        # For Sore
        self.sort_combobox_var = StringVar(value="None")
        self.sort_combobox = Combobox(self, values=["Name", "Birthday", "Salary"], textvariable=self.sort_combobox_var,
                                      state=READONLY, bootstyle=DARK)
        self.sort_combobox.grid(row=3, column=1, padx=(10, 10), pady=(10, 10))

        self.sort_button = Button(self, text=f"Sort By {self.sort_combobox_var.get()}",
                                  command=self.sort_button_clicked, bootstyle=OUTLINE + LIGHT)
        self.sort_button.grid(row=4, column=1, padx=(10, 10), pady=(10, 10))

        # Scrollbar
        self.y_scrollbar = Scrollbar(self, orient=VERTICAL)
        self.y_scrollbar.grid(row=2, column=2, padx=(0, 10), pady=(10, 10), sticky="ns")

        # Back To Home Page
        self.back_to_home_pag_button = Button(self, text="Back To Home Page", bootstyle=WARNING,
                                              command=self.back_to_home_pag_button_clicked)
        self.back_to_home_pag_button.grid(row=3, column=0, padx=(10, 10), pady=(10, 10), sticky="w")

        # Treeview
        self.columns = ("first_name", "last_name", "username", "birthday", "gender", "salary", "role", "status")

        self.table = Treeview(self, columns=self.columns, yscrollcommand=self.y_scrollbar.set, bootstyle=WARNING)

        self.y_scrollbar.config(command=self.table.yview)

        self.table.heading("#0", text="NO")
        self.table.heading("first_name", text="First Name")
        self.table.heading("last_name", text="Last Name")
        self.table.heading("username", text="Username")
        self.table.heading("birthday", text="Birthday")
        self.table.heading("gender", text="Gender")
        self.table.heading("salary", text="NO")
        self.table.heading("role", text="Role")
        self.table.heading("status", text="Status")

        self.table.grid(row=2, column=1, padx=(0, 10), pady=(10, 10), sticky="nsew")

    def load_data(self, current_employee):
        for item in self.treeview_items:
            self.table.delete(item)
        self.treeview_items.clear()

        self.current_employee = current_employee
        result = self.employee_business.get_employees(self.current_employee, self.sort, self.search_by_last_name)
        employees = result[0]
        error_message = result[1]

        if error_message:
            Messagebox.show_error(title="Error", message=error_message, alert=True)
        else:
            row_number = 1
            for item in employees:
                data_gender = int(item.gender)
                gender = Gender(data_gender)
                data_role = int(item.role_id)
                role = Role(data_role)
                data_status = int(item.active)
                active = Status(data_status)

                items = self.table.insert("", END, iid=item.username, text=str(row_number), values=(
                    item.firstname,
                    item.lastname,
                    item.username,
                    item.birthday,
                    f"{gender.name if gender == Gender.MALE else gender.name}",
                    item.salary,
                    f"{role.name if role == Role.BOSS else role.name}",
                    f"{active.name if active == Status.ACTIVE else active.name}"
                ))
                row_number += 1
                self.treeview_items.append(items)

            self.table.column("#0", width=220, anchor="w")
            for columns in self.columns:
                self.table.column(columns, width=300, anchor="center")

            data_role_1 = int(self.current_employee.role_id)
            role_1 = Role(data_role_1)
            if role_1 == Role.BOSS:
                self.active_button = Button(self, text="Active", bootstyle=OUTLINE + SUCCESS,
                                            command=self.active_button_clicked)
                self.active_button.grid(row=1, column=1, padx=(0, 10), pady=(10, 10), sticky="e")
                self.deactive_button = Button(self, text="Deactive", bootstyle=OUTLINE + DANGER,
                                              command=self.deactive_button_clicked)
                self.deactive_button.grid(row=1, column=1, padx=(0, 10), pady=(10, 10), sticky="w")
            else:
                self.active_button.destroy()
                self.deactive_button.destroy()
                self.active_button = None
                self.deactive_button = None

            # Delete Employee
            if role_1 == Role.BOSS:
                self.delete_button = Button(self, text="Delete Employee", bootstyle=DANGER,
                                            command=self.delete_button_clicked)
                self.delete_button.grid(row=3, column=2, padx=(10, 10), pady=(10, 10), sticky="w")
            else:
                self.delete_button.destroy()
                self.delete_button = None

    def back_to_home_pag_button_clicked(self):
        self.view.switch("home")
        self.search_by_last_name = None

    def active_button_clicked(self):
        for employee_username in self.table.selection():
            error_message = self.employee_business.update_to_active(self.current_employee, employee_username)

            if error_message:
                Messagebox.show_error(title="Error", message=error_message, alert=True)
            else:
                self.load_data(self.current_employee)

    def deactive_button_clicked(self):
        for employee_username in self.table.selection():
            error_message = self.employee_business.update_to_deactivate(self.current_employee, employee_username)

            if error_message:
                Messagebox.show_error(title="Error", message=error_message, alert=True)
            else:
                self.load_data(self.current_employee)

    def delete_button_clicked(self):
        for employee_username in self.table.selection():
            error_message = self.employee_business.delete_employee(self.current_employee, employee_username)

            if error_message:
                Messagebox.show_error(title="Error", message=error_message, alert=True)
            else:
                self.load_data(self.current_employee)

    def sort_button_clicked(self):
        sort_by = self.sort_combobox_var.get()
        if sort_by == "Name":
            self.sort = "Name"
            self.sort_button.config(text=f"Sort by {self.sort_combobox_var.get()}")

        elif sort_by == "Birthday":
            self.sort = "Birthday"
            self.sort_button.config(text=f"Sort by {self.sort_combobox_var.get()}")

        elif sort_by == "Salary":
            self.sort = "Salary"
            self.sort_button.config(text=f"Sort by {self.sort_combobox_var.get()}")

        self.load_data(self.current_employee)

    def search_button_clicked(self):
        search = self.search_entry.get()
        if search == "":
            Messagebox.show_error(title="Error", message="Please Enter Your Desired Last Name")
        else:
            self.search_by_last_name = search
            self.load_data(self.current_employee)
