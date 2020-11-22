
# list with a grid-like structure
number_grid = [
    [1, 2, 3],
    [4, 6, 5],
    [7, 8, 9],
    [0]
]

print(number_grid[2][1])

# nested for loop
for row in number_grid:
    for col in row:
        print(col)


def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            translation = translation + "g"
        else:
            translation = translation + letter
    return translation


print(translate(input("Enter a phrase: ")))