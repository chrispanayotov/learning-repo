# You have an array of numbers.
# Your task is to sort ascending odd numbers but even numbers must be on their places.
# Zero isn't an odd number and you don't need to move it. 
# If you have an empty array, you need to return it.
# Example: sort_array([5, 3, 2, 8, 1, 4]) == [1, 3, 2, 8, 5, 4]

def sort_array(source_array):
	even_positions = {v: i for i, v in enumerate(source_array) if v % 2 == 0}
	source_array = [num for num in sorted(source_array) if not num % 2 == 0]
	for k, v in even_positions.items():
		source_array.insert(v, k)
	return source_array

print(sort_array([5, 3, 2, 8, 1, 4]))