# You will be given a single string, containing random ASCII characters. 
# Your task is to print every character, and how many times it has been used in the string.
# Example - Input: aaabbaaabbbccc; Output: a -> 6 b -> 5 c -> 3

data = input()

letter_counter = {letter: data.count(letter) for letter in data}

for k, v in letter_counter.items():
    print(f"{k} -> {v}")