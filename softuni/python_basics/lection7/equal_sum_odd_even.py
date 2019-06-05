n1 = int(input())
n2 = int(input())

odd_sum = 0
even_sum = 0

for i in range(n1, n2 + 1):
    i = str(i)
    for pos in range(len(i)):
        pos_checker = int(i[pos])

        if pos % 2 != 0:
            odd_sum += pos_checker 
        else:
            even_sum += pos_checker 

    if odd_sum == even_sum:
        print(f"{i} ", end='')
    odd_sum = 0
    even_sum = 0