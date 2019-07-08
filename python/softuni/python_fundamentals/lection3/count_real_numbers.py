# Read a list of real numbers and print them in ascending order along with their 
# number of occurrences.
# Example: Input: 8 2.5 2.5 8 2.5 Output: 2.5 -> 3 times; 8 -> 2 times

data = input().split(' ')

dict_counter = {float(num): data.count(num) for num in data}

for key, value in sorted(dict_counter.items()):
    print(f"{key} -> {value} times")