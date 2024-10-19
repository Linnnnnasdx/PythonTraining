# 問答程式
from question import Question

test = [
    "1+1=?\n(a) 2\n(b) 3\n(c) 4\n(d) 5\n\n",
    "1公尺等於幾公分?\n(a) 10\n(b) 100\n(c) 500\n(d) 1000\n\n"
]

questions = [
    Question(test[0],"a"),
    Question(test[1],"b")
]


def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.description)
        if answer == question.answer:
            score += 1

    print("你得到" + str(score) + "分，共" + str(len(questions)) + "題")

run_test(questions)