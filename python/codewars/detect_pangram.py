# A pangram is a sentence that contains every single letter of the alphabet at 
# least once (case is irrelevant).

# Given a string, detect whether or not it is a pangram. 
# Return True if it is, False if not. Ignore numbers and punctuation.


def is_pangram(str_array):
	alphabet = []
	for letter in str_array.lower():
		if not letter in alphabet and letter.isalpha():
			alphabet.append(letter)
	return len(alphabet) >= 26


print(is_pangram("The quick, brown fox jumps over the lazy dog!")) # == True