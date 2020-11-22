
# classes and objects

class Student:

    # initialised function - like a constructor
    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation

    def name_to_upper(self):
        self.name = self.name.upper()

