# Read a list of integers on the first line of the console. After that, 
# sort the list, using the Insertion Sort algorithm, but instead of doing it 
# in-place, add the result one by one to a list.
import copy
data = list(map(int, input().split()))
nums = data.copy()

# Insertion sort
for i in range(1, len(nums)):
    item_to_insert = nums[i]
    j = i - 1

    while j >= 0 and nums[j] > item_to_insert:
        nums[j + 1] = nums[j]
        j -= 1
    
    nums[j + 1] = item_to_insert

print(*nums)