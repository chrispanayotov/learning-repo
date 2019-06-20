import sys
n = int(input())

total = 0
max_number = -sys.maxsize-1

for num in range(1, n + 1):
    current_num = int(input())
    max_number = current_num
    total += current_num

if total - max_number == max_number:
    print("Yes")
    print(f"Sum = {max_number}")
else:
    print("No")
    print(f"Diff = {abs(max_number - (total - max_number))}")