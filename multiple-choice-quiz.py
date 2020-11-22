from Question import Question

question_prompts = [
    "What colour are apples? \n(a) Red/Green\n(b) Purple\n(c) Orange \n\n",
    "What colour are bananas? \n(a) Red/Green\n(b) Purple\n(c) Yellow \n\n",
    "What colour are strawberries? \n(a) Red/Green\n(b) Red\n(c) Yellow \n\n",
 ]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b"),
]


def run_test(qs):
    score = 0
    for question in qs:
        answer = input(question.prompt)
        if answer.lower() == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct.")


run_test(questions)