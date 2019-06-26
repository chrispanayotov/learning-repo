# Write a program to sum all adjacent equal numbers in a list of decimal numbers, starting from left to right.

data = list(map(float, input().split(" ")))

x = 0

while x < len(data) - 1:
    for i in data:
        if data[x] == data[x+1]:
            summed_num = data[x] + data[x+1]
            data[x] = summed_num
            data.remove(data[x+1])
            x = 0
        else:
            x += 1
            break

print(*data)