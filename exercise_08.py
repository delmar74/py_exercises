# https://www.practicepython.org/exercise/2014/03/26/08-rock-paper-scissors.html
import random

choices = ['rock', 'scissors', 'papper']

def newgame():
    return random.choice(choices), random.choice(choices)

def resultgame(people1, people2):

    result = 0

    if people1 == "rock":
        if people2 == "scissors":
            result = 1
        elif people2 == "papper":
            result = 2
    if people1 == "scissors":
        if people2 == "rock":
            result = 2
        elif people2 == "papper":
            result = 1
    if people1 == "papper":
        if people2 == "rock":
            result = 1
        elif people2 == "scissors":
            result = 2

    return result


res = 0
while res == 0:
    people1, people2 = newgame()
    print(people1, people2)

    res = resultgame(people1, people2)
    if res == 1:
        print("Win People1")
    elif res == 2:
        print("Win People2")
