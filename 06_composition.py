# Composition!

# Define a Teacher class. Each teacher has a name and a subject they teach.
class Teacher:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject

    def get_details(self):
        return f"{self.name} teaches {self.subject}."


# Define composite Department class
# A department is composed of multiple teachers.
# Thus, we use composition to include instances of Teacher within a Department.

class Department:
    def __init__(self, name):
        self.name = name
        self.teachers = []  # Composition happens here

    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    def get_department_details(self):
        details = f"Department: {self.name}\n"
        details += "Teachers:\n"
        for teacher in self.teachers:
            details += f"- {teacher.get_details()}\n"
        return details


# Creating teacher instances
teacher1 = Teacher("Alice Smith", "Mathematics")
teacher2 = Teacher("Bob Johnson", "Science")
teacher3 = Teacher("Mary Jane", "Art")
print(teacher1.get_details())
print(teacher2.get_details())
print(teacher3.get_details())

# Creating a math and science department and adding teachers to it
math_science_department = Department("Math & Science")
# math_science_department.add_teacher(teacher1)
# math_science_department.add_teacher(teacher2)
# art_department.add_teacher(teacher3)

# Creating an Art department and adding teachers to it
art_department = Department("Art")

# Displaying department details
# print(math_science_department.get_department_details())
