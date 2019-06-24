# Read a list of integers, an integer p, multiply each item by p and print the resulting list.

# Basic Solution 1
str_list = input().split(" ")
p = int(input())

int_list = []
result = []

for i in range(len(str_list)):
    int_list.append(int(str_list[i]))
    result.append(p * int_list[i])
    print(result[i], end=' ')

# Basic Solution 2
str_list = input().split(" ")
p = int(input())

int_list = []

for i in str_list:
    int_list.append(int(i) * p)

print(int_list, end=' ')

# Advanced Solution - call the function and use a for-loop in a list comprehension
def multiply(element, p):
    return element * p


str_list = list(map(int, input().split(" ")))
p = int(input())

result = [multiply(i, p) for i in str_list]

print(" ".join(map(str, result)))