# Write a program to read a list of integers, find the smallest item and print it.

# Basic Solution - Checks every i in the list and compares it with the initial
# value of the same list
str_list = list(map(int, input().split(" ")))

min_num = str_list[0]

for i in str_list:
    if i < min_num:
        min_num = i

print(min_num)

# Advanced Solution 1 - Sorts the list from min to max
str_list = list(map(int, input().split(" ")))

min_num = sorted(str_list)
print(min_num[0])

# Advanced Solution 2 - Directly use the min function
str_list = list(map(int, input().split(" ")))

print(min(str_list))