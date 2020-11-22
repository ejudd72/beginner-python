
# open the file, 1st param is path to file,
# second is open type
# r = read
# w = write
# r+ = read and write
#a = appending to file
employee_file = open("employees.txt", "r")

# check file is readable
print(employee_file.readable())

# spit out information from file
print(employee_file.read())

# spit out information from file, line by line
print(employee_file.readline())  # first line
print(employee_file.readline())  # second line

# spit out information from file, line by line
print(employee_file.readlines())  # each line, as in an array
# print(employee_file.readlines()[0])  # each line, access by index of line

# close file too - make sure you always do this
employee_file.close()

# Appending to files
employee_file = open("employees.txt", "a")
employee_file.write("\nToby - Human Resources")
employee_file.write("\nKelly - Customer SErvice")

employee_file.close()

# # Writing files entirely - this will overwrite everything
employee_file = open("employees.txt", "w")
employee_file.write("Kelly - Customer service")

employee_file.close()

# # Writing files entirely - this will overwrite everything
html_file = open("index.html", "w")
html_file.write("<p>Hello world</p>")

employee_file.close()



