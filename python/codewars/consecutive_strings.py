# You are given an array strarr of strings and an integer k. Your task is 
# to return the first longest string consisting of k consecutive strings taken in the array.
# n being the length of the string array, if n = 0 or k > n or k <= 0 return "".

def longest_consec(strarr, k):
	longest_consec = ''
	current_longest = ''
	
	if len(strarr) == 0 or k > len(strarr) or k <= 0:
		return longest_consec

	for i in range(len(strarr)):
		range_ = strarr[i:k]
		current_longest = ''.join(range_)
		if len(current_longest) > len(longest_consec):
			longest_consec = current_longest
		k += 1

	return longest_consec


longest_consec(["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"], 2) # == "abigailtheta"