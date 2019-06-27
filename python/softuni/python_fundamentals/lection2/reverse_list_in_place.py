# Reverse a list of integers in-place
# Example I/O: 1 2 3 4 5 -> 5 4 3 2 1

nums = list(map(int, input().split()))
# Solution 1

nums.reverse()
print(*nums)

# Solution 2
x = len(nums) / 2
for i in range(int(x)):
    nums[i], nums[-1-i] = nums[-1-i], nums[i]

print(*nums)

# Reverse list
nums[::-1]
