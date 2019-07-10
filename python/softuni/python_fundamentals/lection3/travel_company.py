# Write a program, which categorizes information about a travel company.
# Companies have various vehicles planned for different cities. 
# Every city has prepared several types of vehicles. 
# Each vehicle type has a different capacity.
# Example - I: Warsaw:bus-30,train-150,airplane-120; Warsaw 500;
# O: Warsaw -> all except 200 accommodated

data = input()

cities_dict = {}

while data != 'ready':
    city, vehicle_type = data.split(':')
    vehicle_type = vehicle_type.split(',') 
    # If city is not in dict, create an empty one with the city as a key
    if city not in cities_dict.keys():
        cities_dict[city] = {}
    # Fill in the city dictionary by creating another dictionary with a 
    # key vehicle type: value capacity
    for vehicle in vehicle_type:
        x, y = vehicle.split('-') # x is vehicle type, y is the capacity
        y = int(y)
        temp_dict = {x: y}
        cities_dict[city].update(temp_dict)
    
    data = input()
# Start accommodating groups of passengers 
data = input().split(' ')

while data[0] != 'travel':
    city, passengers_amount = data[0], int(data[1])
    total_capacity = 0

    for value in cities_dict[city].values():
        total_capacity += value

    if passengers_amount <= total_capacity:
        print(f"{city} -> all {passengers_amount} accommodated")
    else:
        print(f"{city} -> all except {abs(total_capacity - passengers_amount)} accommodated")

    data = input().split(' ')