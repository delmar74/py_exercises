# https://www.practicepython.org/exercise/2014/05/21/15-reverse-word-order.html

sentence = "My name is Michele"

list = sentence.split()
reverse_list = list[::-1]
reverse_sentence = " ".join(reverse_list)

print(reverse_sentence)
