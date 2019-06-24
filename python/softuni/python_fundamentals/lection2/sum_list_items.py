# Write a program, which reads a list of integers, calculates its sum and prints it.

n = int(input())

sum_num = 0

for i in range(1, n+1):
    numbers = int(input())
    sum_num += numbers

print(sum_num)