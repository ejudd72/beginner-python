from student import Student
# from refers to file, import refers to class

student1 = Student("Jim", "Business", 3.1, False)
student2 = Student("Pam", "Admin", 6.7, True)


print(student1.gpa)
print(student2.name)

student2.name_to_upper()
print(student2.name)