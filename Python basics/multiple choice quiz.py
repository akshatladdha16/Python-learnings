from question import question
question_prompt=[
    "number of hrs in a day?\n(a)21\n(b)22\n(c)23\n(d)24\n\n",
    "earth revolve around sun in ?\n(a)343\n(b)365\n(c)366\n(d)365 and 1/2\n\n",
    "Who won 2019 cricket world cup\n(a)India\n(b)South Africa\n(c)England\n(d)Australia\n"
]
questions=[
    question(question_prompt[0],"d"),
    question(question_prompt[1],"d"),
    question(question_prompt[2],"c")
]
def run_test(questions):
    score=0
    for question in questions:
        answer=input(question.prompt)#here you want user to give input based on question prompt
        if answer== question.ans:
            score = score + 1
    print("you got "+str(score)+"/"+ str(len(questions))+" correct .")
run_test(questions)
