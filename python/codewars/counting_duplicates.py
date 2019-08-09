# Write a function that will return the count of distinct case-insensitive 
# alphabetic characters and numeric digits that occur more than once in the 
# input string. The input string can be assumed to contain only alphabets 
# (both uppercase and lowercase) and numeric digits.


def duplicate_count(text):
    duplicates = []
    for letter in text:    
        if text.lower().count(letter) > 1 and letter not in duplicates:
            duplicates.append(letter)
    counter = len(duplicates)
    return counter


duplicate_count('abcde') # == 0
duplicate_count('Indivisibilities') # == 2; 'i' occurs seven times and 's' occurs twice