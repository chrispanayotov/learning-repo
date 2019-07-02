# This algorithm segments the list into sorted and unsorted parts. 
# It iterates over the unsorted segment, and inserts the element being viewed
# into the correct position of the sorted list.

def insertion_sort(nums):
    # Start on the second element as we assume the first element is sorted
    for i in range(1, len(nums)):
        item_to_insert = nums[i]

        # Keep a reference of the index of the previous element
        j = i - 1

        # Move all items of the sorted segment forward if they are larger than 
        # the item to insert
        while j >= 0 and nums[j] > item_to_insert:
            nums[j + 1] = nums[j]
            j -= 1
        
        # Insert the item
        nums[j + 1] = item_to_insert

def insertion_sort_reverse(nums):
    # Sorts the numbers in descending order
     for i in range(1, len(nums)):
        item_to_insert = nums[i]
        j = i - 1

        while j >= 0 and nums[j] < item_to_insert:
            nums[j + 1] = nums[j]
            j -= 1

        nums[j + 1] = item_to_insert