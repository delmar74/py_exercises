# Create a program that asks the user for a number and then prints out a list of all the divisors of that number.

#num = int(input("Your number? "))
num = 110

for i in range(2, num):
    if (num % i == 0):
	       print(str(i))
