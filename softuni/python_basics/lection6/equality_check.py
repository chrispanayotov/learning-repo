n = int(input())

left_result = 0
right_result = 0

for i in range(1, n + 1):
    num = int(input())
    left_result += num

for i in range(1, n + 1):
    num = int(input())
    right_result += num

if left_result == right_result:
    print(f"Yes, sum = {left_result}")
else:
    print(f"No, diff = {abs(left_result - right_result)}")