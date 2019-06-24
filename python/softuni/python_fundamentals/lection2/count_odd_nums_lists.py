# Write a program to read a list of integers and find how many odd items it holds.

# Basic solution
nums = list(map(int, input().split(" ")))

odd_nums = 0

for i in nums:
    if i % 2 != 0:
        odd_nums += 1

print(odd_nums)

# Advanced solution - list comprehension

nums = list(map(int, input().split(" ")))

odd_nums = [i for i in nums if i % 2 != 0]
print(len(odd_nums))