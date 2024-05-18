from .window import Page
from .login import LoginFrame
from .home import HomeFrame
from .employee_management import EmployeeManagementFrame
from .patient_management import PatientManagementFrame
from .employee_registration import EmployeeRegistration


class Mainview:
    def __init__(self):
        self.window = Page()

        self.frames = {}

        self.add_frame("employee_register", EmployeeRegistration(self, self.window))
        self.add_frame("patient_management", PatientManagementFrame(self, self.window))
        self.add_frame("employee_management", EmployeeManagementFrame(self, self.window))
        self.add_frame("home", HomeFrame(self, self.window))
        self.add_frame("login", LoginFrame(self, self.window))
        self.window.show()

    def add_frame(self, frame_name, frame):
        self.frames[frame_name] = frame
        self.frames[frame_name].grid(row=0, column=0, sticky="nsew")

    def switch(self, frame_name):
        self.frames[frame_name].tkraise()
        return self.frames[frame_name]
