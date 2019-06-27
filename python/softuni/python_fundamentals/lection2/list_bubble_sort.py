# Sort a list of integers using bubble sort algorithm
# Example I/O: 5 3 4 1 2 -> 1 2 3 4 5

nums = list(map(int, input().split()))

is_swapped = True
while is_swapped:
    is_swapped = False
    for i in range(len(nums) - 1):
        if nums[i] > nums[i+1]:
            nums[i], nums[i+1] = nums[i+1], nums[i]
            is_swapped = True

print(*nums)