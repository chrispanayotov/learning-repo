# Read a list of integers and extract all square numbers from it and print them in descending order. 

# Solution 1
from math import sqrt
data_input = list(map(int, input().split()))

sqrt_list = []

for i in data_input:
    if sqrt(i) == int(sqrt(i)):
        sqrt_list.append(i)

sqrt_list = sorted(*[sqrt_list], reverse=True)
print(*sqrt_list)


# Solution 2 - Using list comprehension
data_input = map(int, input().split())

data_input = [i for i in data_input if i > 0 and i**0.5 == int(i**0.5)]

data_input.sort(reverse=True)
print(*data_input)