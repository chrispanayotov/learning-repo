n = int(input())
l = int(input())

for i in range(1, n):
    for j in range(1, n):
        for symb_one in range(97, 97 + l):
            for symb_two in range(97, 97 + l):
                for k in range(i+1, n+1):
                    if k > i and k > j:
                        print(f"{i}{j}{chr(symb_one)}{chr(symb_two)}{k} ", end='')
                    else:
                        pass