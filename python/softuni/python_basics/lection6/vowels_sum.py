word = input()

result = 0

for i in range(0, len(word)):
    if word[i] == "a":
        result += 1
    elif word[i] == "e":
        result += 2
    elif word[i] == "i":
        result += 3
    elif word[i] == "o":
        result += 4
    elif word[i] == "u":
        result += 5

print(result)