# In this kata you are required to, given a string, 
# replace every letter with its position in the alphabet.
# If anything in the text isn't a letter, ignore it and don't return it.
# "a" = 1, "b" = 2, etc.

def alphabet_position(text):
    alphabet_dict = {chr(letter): index for index, letter in enumerate(range(97, 123), 1)}
    number_list = []

    for letter in text.lower():
        if alphabet_dict.get(letter) != None:
            number_list.append(alphabet_dict.get(letter))
    
    return ' '.join(map(str, number_list))


alphabet_position("The sunset sets at twelve o' clock.")
# Should return:
#  "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11" (as a string)