n = int(input())

for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            for l in range(1, 10):
                if (n % (i + j)) == 0 and (n % (k + l)) == 0:
                    if (i + j == k + l) and (i < 10 and j < 10 and k < 10 and l < 10):
                        print(f"{i}{j}{k}{l} ", end='')