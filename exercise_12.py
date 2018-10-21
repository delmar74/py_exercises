# https://www.practicepython.org/exercise/2014/04/25/12-list-ends.html
import random

mylist = random.sample(range(1,100),10)

def f(list):
    return list[0], list[-1]

first, last = f(mylist)
print(mylist, first, last)
