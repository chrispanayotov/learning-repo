n1 = int(input())
n2 = int(input())

left_sum = 0
middle_num = 0
right_sum = 0

for i in range(n1, n2 + 1):
    i = str(i)
    for pos in range(len(i)):
        pos_checker = int(i[pos])
        
        if pos == 0 or pos == 1:
            left_sum += pos_checker
        elif pos == 3 or pos == 4:
            right_sum += pos_checker
        else:
            middle_num += pos_checker

    if left_sum != right_sum and left_sum < right_sum:
        left_sum += middle_num
    elif left_sum != right_sum and left_sum > right_sum:
        right_sum += middle_num
            
    if left_sum == right_sum:
        print(f"{i} ", end='')

    left_sum = 0
    middle_num = 0
    right_sum = 0