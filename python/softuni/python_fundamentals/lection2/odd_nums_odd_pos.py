# Write a program to read a list of integers and find how many odd numbers at odd positions the list holds. 
# If there are no numbers, which match this criterion, do not print anything

data = list(map(int, input().split(" ")))

odd_nums = 0
counter = 0

for i in data:
    if i % 2 != 0 and counter % 2 != 0:
        print(f"Index {counter} -> {i}")
    counter += 1