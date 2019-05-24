n_freights = int(input())

weight = 0
bus_weight = 0
truck_weight = 0
train_weight = 0

total_weight = 0
total_price = 0

for i in range(n_freights):
    weight = int(input())
    if weight <= 3:
        total_weight += weight
        bus_weight += weight
        total_price += weight * 200
    elif weight <= 11:
        total_weight += weight
        truck_weight += weight
        total_price += weight * 175
    else:
        total_weight += weight
        train_weight += weight
        total_price += weight * 120

print(f"{total_price / total_weight:.2f}")
print(f"{(bus_weight / total_weight) * 100:.2f}%")
print(f"{(truck_weight / total_weight) * 100:.2f}%")
print(f"{(train_weight / total_weight) * 100:.2f}%")