
# while loops in python
# i = 1
# while i <= 10 :
#     print(i)
#     i += 1
#
# print("Done with loop")

# A basic guessing game
secret_word = "doosty"
guess = ""
tries = 0
out_of_tries = False
try_limit = 5


def user_correct():
    return guess == secret_word


while not user_correct() and not out_of_tries:
    print("You have " + str(try_limit - tries) + " attempts left.")
    if tries < try_limit:
        guess = input("What is the secret word? ")
        tries += 1
    else:
        out_of_tries = True


if out_of_tries:
    print("Out of guesses, you lose :(")
else:
    print("Congratulations... the secret word was " + secret_word)