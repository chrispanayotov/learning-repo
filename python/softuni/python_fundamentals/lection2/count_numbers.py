# Read a list of integers in range [0…1000] and print them in ascending order along with their number of occurrences.
# Example I/O: I:8 2 2 8 2 2 3 7 O:2 -> 4, 3 -> 1, 7 -> 1, 8 -> 2

# Solution 1 - using built-in methods
nums = list(map(int, input().split()))

nums.sort()

y = 0

for i in nums:
    if y == i:
        pass
    else:
        x = nums.count(i)
        print(f"{i} -> {x}")
        y = i

# Solution 2 - without built-ins - Counting Occurrences after sorting with Bubble sort
nums = list(map(int, input().split()))

# Using Bubble sort algorithm to sort the numbers in ascending order
is_swapped = True
while is_swapped:
    is_swapped = False
    for i in range(len(nums) - 1):
        if nums[i] > nums[i+1]:
            nums[i], nums[i+1] = nums[i+1], nums[i]
            is_swapped = True

# Counting the occurances of each number in the sorted list
index = 0
for i in nums:
    count = 0
    current_num = nums[index]
    for j in nums:
        if current_num == j:
            count += 1
            index += 1

    print(f"{current_num} -> {count}")

    if index == len(nums):
        break