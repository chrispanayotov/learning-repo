import math
w = float(input())
l = float(input())
h = float(input())
astronaut_height = float(input()) # average

spaceship_size = w * l * h
room_size = (astronaut_height + 0.40) * 2 * 2
total_crew = spaceship_size / room_size

if 3 <= total_crew <= 10:
    print(f"The spacecraft holds {math.floor(total_crew)} astronauts.")
elif total_crew < 3:
    print("The spacecraft is too small.")
else:
    print("The spacecraft is too big.")