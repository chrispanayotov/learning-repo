# Read a list of integers on the first line of the console. On the next line, 
# you will receive an integer N. After that, find and print the largest N items
# the list, sorted in descending order.
# Example I/O: 5 3 4 1 2, N = 3 -> 5 4 3

nums = list(map(int, input(). split()))
n = int(input())
result = []

# Using Insertion sort in reverse
for i in range(1, len(nums)):
    item_to_insert = nums[i]
    j = i - 1

    while j >= 0 and nums[j] < item_to_insert:
        nums[j + 1] = nums[j]
        j -= 1

    nums[j + 1] = item_to_insert

for i in range(n):
    result.append(nums[i])

print(*result)