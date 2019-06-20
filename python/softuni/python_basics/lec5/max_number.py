import sys
n = int(input())

counter = 0
max_number = -sys.maxsize-1

while counter < n:
    current_number = int(input())
    if max_number > current_number:
        max_number = current_number
    
    counter += 1

print(max_number)