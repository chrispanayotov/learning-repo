m = int(input())

counter = 0
password = False
pass_num = 0

for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            for d in range(1, 10):
                if (a*b + c*d == m) and (a < b and c > d):
                    print(f"{a}{b}{c}{d} ", end='')
                    counter += 1
                    if counter == 4:
                        password = True
                        x, y, z, j = a, b, c, d
if password == True:
    print()
    print(f"Password: {x}{y}{z}{j}")
else:
    print()
    print("No!")