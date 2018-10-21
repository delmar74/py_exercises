# https://www.practicepython.org/exercise/2014/05/15/14-list-remove-duplicates.html
import random

def generate_list(num):
    random_list = []
    for i in range(num):
        random_list.append(random.randint(1,20))
    return random_list

mylist = generate_list(10)

def list_without_duplicate(list):
    new_list = []
    for element in list:
        if not (element in new_list):
            new_list.append(element)
    return new_list

res_list = list_without_duplicate(mylist)
print(mylist)
print(res_list)
