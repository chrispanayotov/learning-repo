a = int(input())
b = int(input())
c = int(input())
d = int(input())

for x1 in range(a, b + 1):
    for x2 in range(a, b + 1):
        for y1 in range(c, d + 1):
            for y2 in range(c, d + 1):
                if (x1 + y2) == (x2 + y1) and x1 != x2 and y1 != y2:
                    print(f"{x1}{x2}")
                    print(f"{y1}{y2}\n")