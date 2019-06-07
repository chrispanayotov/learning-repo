l1 = ord(input())
l2 = ord(input())
ignore = ord(input())

combinations = 0

for i in range(l1, l2+1):
    for j in range(l1, l2+1):
        for k in range(l1, l2+1):
            if i == ignore or j == ignore or k == ignore:
                pass
            else:
                combinations += 1
                i, j, k = chr(i), chr(j), chr(k)
                print(f"{i}{j}{k} ", end='')
                i, j, k = ord(i), ord(j), ord(k)

print(f"{combinations}")