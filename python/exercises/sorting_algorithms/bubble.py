# This simple sorting algorithm iterates over a list, comparing elements 
# in pairs and swapping them until the larger elements "bubble up" 
# to the end of the list, and the smaller elements stay at the "bottom".

def bubble_sort(nums):
    is_swapped = True
    while is_swapped:
        is_swapped = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
                is_swapped = True