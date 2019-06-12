moves = int(input())

points = 0
result = 0
r1 = 0
r2 = 0
r3 = 0
r4 = 0
r5 = 0
r6 = 0

for i in range(moves):
    num = int(input())
    if 0 <= num <= 9:
        points += num * .20
        r1 += 1
    elif 10 <= num <= 19:
        points += num * .30
        r2 += 1
    elif 20 <= num <= 29:
        points += num * .40
        r3 += 1
    elif 30 <= num <= 39:
        points += 50
        r4 += 1
    elif 40 <= num <= 50:
        points += 100
        r5 += 1
    else:
        result /= 2
        r6 += 1
    result += points
    points = 0

print(f"{result:.2f}")
print(f"From 0 to 9: {(r1 / moves) * 100:.2f}%")
print(f"From 10 to 19: {(r2 / moves) * 100:.2f}%")
print(f"From 20 to 29: {(r3 / moves) * 100:.2f}%")
print(f"From 30 to 39: {(r4 / moves) * 100:.2f}%")
print(f"From 40 to 50: {(r5 / moves) * 100:.2f}%")
print(f"Invalid numbers: {(r6 / moves) * 100:.2f}%")