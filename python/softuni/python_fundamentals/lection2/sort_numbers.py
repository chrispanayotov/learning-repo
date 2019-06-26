# Read a list of integers and sort them in ascending order.

data = list(map(int, input().split(" ")))

data.sort()

for i in range(len(data)):
    if len(data) - i == 1:
        print(f"{data[i]}", end='')
        break
    print(f"{data[i]}" + " <= ", end='')