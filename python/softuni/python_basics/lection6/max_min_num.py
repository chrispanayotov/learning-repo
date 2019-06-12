import sys
n = int(input())

max_num = -sys.maxsize-1
min_num = sys.maxsize

for num in range(0, n):
    current_num = int(input())
    if current_num > max_num:
        max_num = current_num

    if current_num < min_num:
        min_num = current_num

print(f"Max number: {max_num}")
print(f"Min number: {min_num}")