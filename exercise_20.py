# https://www.practicepython.org/exercise/2014/11/11/20-element-search.html
import random


mylist = sorted(random.sample(range(1,100), 20))
mynum = random.randint(1,100)

print("List: " + str(mylist))
print("Number: " + str(mynum))

def bin_search(list, x):
    lower = 0
    upper = len(list)
    while lower != upper:
        compared_value = (lower + upper) // 2
        if x == list[compared_value]:
            return True
        elif x < list[compared_value]:
            upper = compared_value
        else:
            lower = compared_value + 1
    return False

print("Result: " + str(bin_search(mylist, mynum)))
