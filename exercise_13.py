# https://www.practicepython.org/exercise/2014/04/30/13-fibonacci.html
import random

mynum = random.randint(2,300)

def Fibonnachi(num):
    list = []
    for i in range(num):
        if i == 0:
            list.append(i)
        elif i == 1:
            list.append(i)
        else:
            list.append(list[-1]+list[-2])
    return list

l = Fibonnachi(mynum)

print(mynum)
print(l)
print(l[-1])
