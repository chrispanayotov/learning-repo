stadium_capacity = int(input())
total_fans = int(input())

A = 0
B = 0
V = 0
G = 0

for i in range(1, total_fans + 1):
    sector = input().upper()
    if sector == "A":
        A += 1
    elif sector == "B":
        B += 1
    elif sector == "V":
        V += 1
    else:
        G += 1

print(f"{(A / total_fans) * 100:.2f}%")
print(f"{(B / total_fans) * 100:.2f}%")
print(f"{(V / total_fans) * 100:.2f}%")
print(f"{(G / total_fans) * 100:.2f}%")
print(f"{(total_fans / stadium_capacity) * 100:.2f}%")