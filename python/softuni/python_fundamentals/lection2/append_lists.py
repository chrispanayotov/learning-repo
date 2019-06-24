# Write a program to append several lists of numbers.
# Lists are separated by ‘|’.
# Values are separated by spaces (‘ ’, one or several)
# Order the lists from the last to the first, and their values from left to right.

# Solution 1
data = input().split("|")

pure_list = []
b = "[]' ,"

for i in range(len(data), 0, -1):
    pure_list.append(data[i-1])

pure_list = str(pure_list)

for char in b:
    pure_list = pure_list.replace(char, "")

pure_list = list(map(int, pure_list))
print(*pure_list)

# Solution 2
data = input().split("|")

pure_list = []

for i in range(len(data), 0, -1):
    x = data[i-1].split()
    for char in x:
        if char != " ":
            pure_list.append(char)
            
print(*pure_list)