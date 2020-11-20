# add a newline inside string
print("I am a \n  \n \n \nstring")

# add a quotation into string
print("I am a \"string\"")

# create a string variable
phrase = "I am a string"
print(phrase)

# concatenation
print(phrase + " and I am really cool")

# common string functions
print(phrase.lower())
print(phrase.upper())
# check if string is entirely lower/uppercase
print(phrase.isupper())
print(phrase.islower())
print(phrase.upper().isupper())
print(phrase.lower().islower())

# get string length (!)
print(len(phrase))

# get individual string characters (zero-indexed)
print(phrase[0])

# find where a specific character is located inside our string
# but it errors if it's not found, rather than giving undefined
print(phrase.index("s"))

# replacing, parameter 1 with 2
print(phrase.replace("string", "very silly boy"))



