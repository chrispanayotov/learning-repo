n1 = int(input())
n2 = int(input())

for i in range(n1, n2+1):
    for j in range(n1, n2+1):
        for k in range(n1, n2+1):
            for l in range(n1, n2+1):
                if (i % 2 == 0 and l % 2 != 0) or (i % 2 != 0 and l % 2 == 0):
                    if i > l and (j + k) % 2 == 0:
                        print(f"{i}{j}{k}{l} ", end='')