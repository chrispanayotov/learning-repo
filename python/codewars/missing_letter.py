# #Find the missing letter
# Write a function that takes an array of consecutive (increasing) letters as 
# input and that returns the missing letter in the array.
# You will always get an valid array. And it will be always exactly one letter 
# be missing. The length of the array will always be at least 2.

def find_missing_letter(chars):
	# Transform the characters to numbers from ASCII 
	nums = [ord(char) for char in chars]
	# Find the missing number and return a character using chr()
	return chr(sum(range(nums[0], nums[-1]+1)) - sum(nums))


print(find_missing_letter(['a','b','c','d','f']))