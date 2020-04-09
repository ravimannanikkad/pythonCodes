# ************************************#
# Writen By Ravi Damodaran           #
# Python building a quiz       #
# Working with classes and Objects  #
# ************************************#

from Questions import Questions

#Displayed Questions and Answers choices
question_promts=[
    "What colors are Apple ? \n "
    "(a) Green \n "
    "(b) Red \n (c) "
    "Yellow \n\n",
    "What colors are Banana ? \n "
    "(a) Teal \n "
    "(b) Yellow \n "
    "(c) orange \n\n",
    "What colors are Blueberries ? \n "
    "(a) Yellow \n "
    "(b) Violet \n "
    "(c) Blue \n\n",
]

# This is the question answer array
question_answer_array=[
    Questions(question_promts[0],"a"),
    Questions(question_promts[1],"b"),
    Questions(question_promts[2],"c")
]

def run_app(question_answer_array):
    score =0
    for qus in question_answer_array:
        ans=input(qus.question)
        if ans == qus.answer:
            score+=1
    print("Your Score is "+ str(score)+"/"+str(len(question_promts)))

run_app(question_answer_array)

