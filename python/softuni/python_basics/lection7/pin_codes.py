n1 = int(input()) # 1 to 9
n2 = int(input())
n3 = int(input())

for i in range(1, n1+1):
    for k in range(2, n2+1):
        for j in range(1, n3+1):
            if i % 2 == 0 and j % 2 == 0:
                if k == 2 or k == 3 or k == 5 or k == 7:
                    print(f"{i} {k} {j}")