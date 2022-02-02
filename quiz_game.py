## COMPUTER QUIZ GAME

print("Welcome to my computer quiz!")

variable = input("Do you want to play? Y/N : ")

if variable != "Y".lower():
    quit()

print("Okay! Let's play :)")

score = 0

questions_dictionary = {"What does CPU stand for? ": "central processing unit", 
                        "What does GPU stand for? ": "graphics processing unit", 
                        "What is the capital of germany? ": "Berlin"}


def questions(questions_dictionary):
    global score
    for key, value in questions_dictionary.items():
        answer = input(key)
        if answer == value:
            print("Correct")
            score += 1
        else:
            print("Incorrect)")

questions(questions_dictionary)
