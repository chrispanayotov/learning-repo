# Write a program that extracts from a given sequence of words all elements that
# present in it odd number of times (case-insensitive).
# Example I/O: Java C# PHP PHP JAVA C java -> java, c#, c
data = input().lower().split(' ')

# Solution 1 - basic
dict_count = {}
list_count = []

for word in data:
    dict_count[word] = data.count(word)

for key, value in dict_count.items():
    if value % 2 == 1:
        list_count.append(key)

print(', '.join(list_count))

# Soltuion 2 - using dict comprehension
dict_count = {word: data.count(word) for word in data}
list_count = []

for key, value in dict_count.items():
    if value % 2 == 1:
        list_count.append(key)

print(', '.join(list_count))