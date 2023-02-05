
# 2. get the occurence of all vowels and consonent from the large given string.

def vowelsConsonants(val, lst):
    vowels = 0
    consonants = 0
    for i in val:
        if i in lst:
            vowels += 1
        else:
            consonants += 1

    print("Vowels: ", vowels)
    print("Consonant: ", consonants)

lst = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
val = input("Please Enter your String: ")
vowelsConsonants(val, lst)
