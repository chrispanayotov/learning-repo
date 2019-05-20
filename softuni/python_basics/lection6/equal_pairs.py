n = int(input())

curr_sum = 0
prev_sum = 0
max_diff = 0

for i in range(n):
    num1 = int(input())
    num2 = int(input())

    if i == 0:
        prev_sum = num1 + num2
    else:
        curr_sum = num1 + num2
        diff = abs(prev_sum - curr_sum)
        if max_diff < diff:
            max_diff = diff
        prev_sum = curr_sum

if max_diff == 0:
    print(f"Yes, value={prev_sum}")
else:
    print(f"No, maxdiff={max_diff}")