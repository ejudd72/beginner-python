
# creating a list like a normal variable, square brackets,
# python doesn't mind if the list holds multiple types
friends = ["Kevin", "Karen", "Jim"]
print(friends)

# selecting specific item by index (like javascript)
print(friends[0])
# Kevin

# select items from list STARTING FROM THE END OF THE LIST using negative
print (friends[-1])
# Jim

# Get all elements after a certain index:
print(friends[1:])
# Karen, Jim

# Get all elements within a range (not inclusive of second value)
print(friends[0:2])
# Kevin, Karen

# modify element by its index
friends[1] = "mike"
print(friends)

# =======================
# list functions
lucky_numbers = [4, 8, 15, 16, 23, 42, 7, 5]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Fred"]
str_friends = ["Kevin", "Karen", "Jim", "Oscar", "Fred"]
print(friends)

# extend will append another list to a list - changes the original variable
friends.extend(lucky_numbers)
print(friends)

# append you can add another data item to the end fo the list
friends.append("Chris")
print(friends)

# insert you can add an item to a specific index - first
# parameter must be the desired index position,
# param 2 is the value
friends.insert(3, "Robert")
print(friends)

# remove a specific item (by value) from the list
friends.remove("Robert")
print(friends)

# like javascript, pop will remove the last item from the list
last_item = friends.pop()
print(last_item)
print(friends)

# check the index of an item in the list
# (it will throw an error if not)
print(friends.index("Karen"))

# check how many items are similar in a list
print(friends.count("Jim"))

# sort list to be in alphabetical order/numerical order
# throws an error for multi-typed lists
# doesn't return anything to print
str_friends.sort()
print(str_friends)
lucky_numbers.sort()
print(lucky_numbers)

# reverse
friends.reverse()
print(friends)
# copy a list, it will have same attributes
friends2 = friends.copy()
print(friends2)
# remove everything from the list
friends.clear()
print(friends)

