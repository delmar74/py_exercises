# https://www.practicepython.org/exercise/2014/11/30/21-write-to-a-file.html

def save_to_file(file_name, text):
    file = open(file_name, 'w')
    file.write(text)
    file.close()

my_file_name = "exercise_21.txt"
my_text = "aaab"

save_to_file(my_file_name, my_text)
