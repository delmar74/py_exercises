# https://www.practicepython.org/exercise/2014/03/05/05-list-overlap.html
import random

def randomNum():
	return random.randint(5,30)

count1 = randomNum()
count2 = randomNum()

while count1 == count2:
	count2 = randomNum


l1 = []
l2 = []

while len(l1) < count1:
	l1.append(random.randint(1,50))

while len(l2) < count2:
	l2.append(random.randint(1,50))

print(l1)
print(l2)

###
l3 = []
l4 = []
for i1 in l1:
	for i2 in l2:
		if i1 == i2:
			if not (i1 in l3):
				l3.append(i1)

l3 = sorted(l3)
print(l3)
