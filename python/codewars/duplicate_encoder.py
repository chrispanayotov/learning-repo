# The goal of this exercise is to convert a string to a new string where each 
# character in the new string is "(" if that character appears only once in the 
# original string, or ")" if that character appears more than once in the 
# original string. Ignore capitalization when determining if a character is a duplicate.

def duplicate_encode(word):
	result = ''
	word = word.lower()
	for symbol in word:
		if word.count(symbol) == 1:
			result += '('
		else:
			result += ')'
	return result


duplicate_encode('Success') # Should return -> ")())())"