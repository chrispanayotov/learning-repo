n = int(input())

valid_combos = 0

for x1 in range(n + 1):
    for x2 in range(n + 1):
        for x3 in range(n + 1):
            for x4 in range(n + 1):
                for x5 in range(n + 1):
                    if x1 + x2 + x3 + x4 + x5 == n:
                        valid_combos += 1

print(f"{valid_combos}")