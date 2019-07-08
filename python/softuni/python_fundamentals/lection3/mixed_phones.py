# Sort in alphabetical order an input of names: phone numbers in a dictionary
# Example - Input: Gosho : 088423123 14284124 : Alex
# Output: Alex -> 14284124 Gosho -> 88423123

data = input().split(' : ')

phone_book = {}

while data[0] != 'Over':
    if data[0].isdigit():
        phone_book[data[1]] = str(data[0])
    else:
        phone_book[data[0]] = str(data[1])

    data = input().split(' : ')

for k, v in sorted(phone_book.items()):
    print(f"{k} -> {v}")