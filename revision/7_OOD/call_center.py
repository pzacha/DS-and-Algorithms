import unittest

class Employee:
    """
    A class used to represent an employee

    Attributes
    ----------
    position : str
    name : str
    free : bool
        0 - busy, 1 - free

    Methods
    -------
    says(sound=None)
        Prints the animals name and what sound it makes
    """
    def __init__(self, position: str = "respondent", name: str):
        self.position = position
        self.name = name
        self.free = 1
    
    def is_free(self):
        return self.free

def dispatch_call(self):
    for employee in employees:
        if employee.position == "respondent" and employee.is_free():
            employee.free = 0
            break
        else:    
            for employee in employees:
                if employee.position == "manager" and employee.is_free():
                    employee.free = 0
                    break


