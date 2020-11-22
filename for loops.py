
# with strings, it will take each letter
for letter in "Ellies house":
    print(letter)

# it'll take each item from an array
friends = ["Kristin", "Beth", "Eloise", "Charlotte"]
for friend in friends:
    print(friend)


# another way to do the above
for index in range(len(friends)):
    print(friends[index])

# it will print out each number in a range beginning with 10
nums = range(10)
print(nums)
for index in range(10):
    print(index)

for index in range(5):
    if index == 0:
        print("First")
    else:
        print("Not first")

