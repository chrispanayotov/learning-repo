n = int(input())

result = 0

for num in range(0, n + 1, 2):
    result = 2 ** num
    print(result)