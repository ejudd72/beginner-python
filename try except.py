# number = int(input("Enter a number: "))
# print(number)

# try except will stop code from entirely breaking if it errors
# instead it will fall into an exception e.g. above is likely to error

try:
    # value = 10/0
    number = int(input("Enter a number"))
    print(number)
# #     different except blocks for different types of errors
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("Type a number")

