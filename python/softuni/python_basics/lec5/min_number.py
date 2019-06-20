import sys
n = int(input())

counter = 0
min_number = sys.maxsize

while counter < n:
    current_number = int(input())
    if min_number < current_number:
        min_number = current_number
    
    counter += 1

print(min_number)