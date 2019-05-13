import math
world_record = float(input()) # in seconds
distance_meters = float(input())
time_per_meter = float(input()) # in seconds for 1 meter

distance_in_seconds = distance_meters * time_per_meter
resistance = math.floor(distance_meters / 15) * 12.5 # every 15 meter adds 12.5 seconds 

total_time = distance_in_seconds + resistance
if total_time >= world_record:
    time_needed = abs(world_record - total_time)
    print(f"No, he failed! He was {time_needed:.2f} seconds slower.")
elif total_time < world_record:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")