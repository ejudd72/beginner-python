num1 = float(input("Enter first number: "))
op = input("Enter operator: ")
num2 = float(input("Enter second number: "))

print(op)
if op.lower == "+" or op.lower == "add" or op.lower == "plus":
     print(num1 + num2)
if op.lower == "-" or op.lower == "minus" or op.lower == "subtract":
    print(num1 - num2)
elif op.lower == "*" or op.lower == "x" or op.lower == "multiply" or op.lower == "times":
     print(num1 * num2)
elif op.lower == "/" or op.lower == "division" or op.lower == "divided by":
     print("division section!")
     print(num1, num2, num1 / num2)
     print(num1 / num2)
else:
    print("invalid operator")
