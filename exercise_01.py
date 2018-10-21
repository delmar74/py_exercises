# Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year that they will turn 100 years old.
import datetime

name = input("Name? ")
print(name)

age = int(input("Enter your age: "))
print(str(age))

now_year = int(datetime.datetime.now().year)
year_100 = now_year - age + 100

print("In " + str(year_100) + " your age will be 100.")
