passengers = int(input())
stops = int(input())

for i in range (1, stops + 1):
    passengers_off = int(input())
    passengers_on = int(input())
    if i % 2 != 0:
        passengers_on += 2
        passengers = (passengers - passengers_off) + passengers_on
        passengers_on = 0
    else:
        passengers -= 2
        passengers = (passengers - passengers_off) + passengers_on

print(f"The final number of passengers is : {passengers}")