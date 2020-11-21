
# keyword def in python to create a function -
# you must indent instead of using bracket blocks
# pass in parameters just like in javascript
def say_hello(name):
    print("Hello " + name)


# call function - leave 2 blank lines before
# will throw an error if not given a parameter
say_hello("Ellie")


# using return
def cube_number(num):
    return num * num


print(cube_number(5))


# if statements
def eat_breakfast():
    if hungry:
        print("eating breakfast")
    else:
        print("no breakfast for me today")


hungry = False
eat_breakfast()


hungry = True
eat_breakfast()


has_food = True
# or keyword
if hungry or has_food:
    print("Lets eat!")
else:
    print("Later on...")

has_food = False
# and keyword
if hungry and has_food:
    print("yum")
# checking not conditions and elif (elseif)
elif hungry and not(has_food):
    print("Go to the shops...")
else:
    print("Later on...")

