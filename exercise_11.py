# https://www.practicepython.org/exercise/2014/04/16/11-check-primality-functions.html
import random

mynum = random.randint(2,1000)

def issimple(num):
    check = []

    for i in range(2,num):
        if num % i == 0:
            check.append(i)

    return check


check = issimple(mynum)

print(mynum, check)

if len(check) == 0:
    print(str(mynum) + " is simple.")
else:
    print(str(mynum) + " is not simple.")
