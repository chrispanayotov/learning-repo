# Need to find a way how to remove the comma after the 'and' word

def comma_code(word_list, cleaner):
    word_list.insert(len(word_list) -1, 'and')

    for char in cleaner:
        word_list = str(word_list).replace(char, "")
 
    return word_list

spam = ['apples', 'bananas', 'tofu', 'cats']
to_be_removed = "[]'"
print(comma_code(spam, to_be_removed))