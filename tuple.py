
coordinates = (4, 5)

# unique because immutable - can't be changed or modified
# will throw an error if you attempt to re-assign
# access certain values with square bracke notation, again 0-indexed
print(coordinates[0])

# tuples vs lists
# lists use square brackets - you can reassign, add, delete etc
# tuples you cant do the above - in practical uses you'd
# use it gfor things that wont change
# you can have a list of tuples - you wont be able to
# change the value within the round brackets
# but can change the stuff inside just square brackets
list_of_tuples = [(1, 2), (3, 6), (16, 25)]
print(list_of_tuples)
list_of_tuples[1] = (4, 8)
print(list_of_tuples)
