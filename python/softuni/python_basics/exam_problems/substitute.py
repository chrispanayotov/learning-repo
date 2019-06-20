import sys
k = int(input())
l = int(input())
m = int(input())
n = int(input())

counter = 0

for x1 in range(k, 9):
    for x2 in range(9, l-1, -1):
        for y1 in range(m, 9):
            for y2 in range(9, n-1, -1):
                if x1 % 2 == 0 and x2 % 2 != 0 and y1 % 2 == 0 and y2 % 2 != 0:
                    if x1 == y1 and x2 == y2:
                        print(f"Cannot change the same player.")
                    else:
                        print(f"{x1}{x2} - {y1}{y2}")
                        counter += 1
                    if counter == 6:
                        sys.exit()