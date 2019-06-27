# Read a list of integers on the first line of the console. 
# After that, find the smallest item in the list and print it on the console.
# Example I/O: 1 2 3 4 5 - > 1
import sys
nums = list(map(int, input().split()))

min_num = sys.maxsize

for i in nums:
    if i < min_num:
        min_num = i

print(f"{min_num}")