from math import ceil
data = input()

shells_dict = {}

while data != 'Aggregate':
    city, size = data.split(' ')

    if city not in shells_dict.keys():
            shells_dict[city] = []
            shells_dict[city].append(size)
    if size not in shells_dict[city]:
        shells_dict[city].append(size)

    data = input()

for city, size in shells_dict.items():
    sum_size = 0
    for num in size:
        sum_size += int(num)
        
    average = (sum_size) - ((sum_size) / (len(size)))
    print(f"{city} -> ", end='')
    print(*size, sep=', ', end=' ')
    print(f"({ceil(average)})", sep=', ')