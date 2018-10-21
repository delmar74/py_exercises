# https://www.practicepython.org/exercise/2014/05/28/16-password-generator.html
import random
import string

password_level = 2 # 1 (low) - 2 (strong)

password_list = ["table", "game", "first", "cow", "secret", "son", "my"]

def generate():
    count = random.randint(6,20)
    char_set = string.ascii_letters + string.digits + string.punctuation
    res = ''.join(random.sample(char_set, count))
    return res

if password_level == 1:
    password = "_".join(random.sample(password_list, 2))
elif password_level == 2:
    password = generate()

print(password)
