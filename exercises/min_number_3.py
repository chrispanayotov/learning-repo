n = int(input())
nums = list()
for i in range(0, n):
    nums.append(int(input()))
nums = sorted(nums)
count = min(len(nums), 3)
for i in range(0, count):
    print(nums[i])
