# https://www.practicepython.org/exercise/2014/04/02/09-guessing-game-one.html
import random

computer = random.randint(1,10)
people = int(input("Your number(1-10)? "))

if people == computer:
	print("You win!")
elif people > computer:
	print("Your number is " + str(people-computer) + " more.")
else:
	print("Your number is " + str(computer-people) + " less.")

print(computer)
