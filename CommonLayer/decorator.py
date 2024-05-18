import functools
import time
from .get_employee_clicker import EmployeeClicker


def performance_logger_decorator(function):
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        present_time = time.ctime()
        start_time = time.time()
        result = function(*args, **kwargs)
        ent_time = time.time() - start_time
        name_function = function.__name__

        if EmployeeClicker.employee_clicker:
            print(present_time + " " + f"{ent_time}" + " " + name_function + " " + EmployeeClicker.employee_clicker)

        return result

    return wrapper
