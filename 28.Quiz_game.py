# we are gonna work on a small quiz using multiple choices

from _28Questions import Question

questions_prompts = [
    "What is the color of sky?\n (a)Blue\n (b)Green\n (C)Pink\n\n",
    "how many times do you brush your teeth? \n (a)Once per day\n (b)Twice per day\n (c)we do not brush\n\n",
    "Is Greeting someone you meet important?\n (a)Yes\n (b)No\n\n" 
]


question = [
    Question(questions_prompts[0],"a" ),
    Question(questions_prompts[1],"b" ),
    Question(questions_prompts[2],"a" )
]


def run_test(question):
    score = 0
    for question in question:
        answer = input(question.prompt)
        if answer == question.answer:
            score +=1
    print("you got "+ str(score) + " correct answer")
    
run_test(question)