nums_list = list(map(int, input().split()))

command = input()
valid_commands = 0

def get_divisible_by(array, num):
	return [i for i in array if i % num == 0]


while command != 'end':
	if command[:4] == 'swap':
		#Splits the input into separate indices and casts them to int
		_, index1, index2 = command.split()
		index1, index2 = int(index1), int(index2)

		# When index1 and index2 are in range of nums_list swap the values
		if 0 <= index1 < len(nums_list) and 0 <= index2 < len(nums_list):
			nums_list[index1], nums_list[index2] = nums_list[index2], nums_list[index1]
			print(nums_list)
			valid_commands += 1
		else:
			print(nums_list)
			valid_commands += 1
	elif command == 'enumerate_list':
		# Returns a list with nested tuples that show the index and value
		enumerated_list = [(i, v) for i, v in enumerate(nums_list)]
		print(enumerated_list)
		valid_commands += 1
	elif command == 'max':
		print(max(nums_list))
		valid_commands += 1
	elif command == 'min':
		print(min(nums_list))
		valid_commands += 1
	elif command[:4] == 'get_':
		x, _, num = command.split()
		if x == 'get_divisible':
			print(get_divisible_by(nums_list, int(num)))
			valid_commands += 1
	
	command = input()

print(valid_commands)