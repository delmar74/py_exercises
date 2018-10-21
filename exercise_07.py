# https://www.practicepython.org/exercise/2014/03/19/07-list-comprehensions.html
import random

#a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
a = random.sample(range(0, 35), 30)

b = []

for i in a:
    if (i % 2 == 0):
        b.append(i)
print(a)
print(sorted(b))
