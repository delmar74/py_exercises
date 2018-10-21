# Palindrome
# https://www.practicepython.org/exercise/2014/03/12/06-string-lists.html

word = "21a Bc  11c ba12"
word = word.replace(" ", "")
word = word.lower()

length = len(word)
half = length // 2

check = True

for i in range(0,half):
    k = length - i - 1
    print(word[i], word[k])
    if word[i] != word[k]:
        check = False

# answer
print(word, check)
