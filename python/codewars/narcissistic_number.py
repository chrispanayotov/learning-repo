# A Narcissistic Number is a number which is the sum of its own digits, 
# each raised to the power of the number of digits in a given base. 
# Your code must return true or false depending upon whether the given number
# is a Narcissistic number in base 10.
# 7 == True; 153 == True; 122 == False; 4887 == False;

def narcissistic(number):
	total = 0
	for i in str(number):
		total += int(i) ** len(str(number))
	return total == number

print(narcissistic(122))