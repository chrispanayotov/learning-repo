# Make a program that calculates how many dancers can fit in 
# a dancing hall and can move freely
# Import the math library
import math
# Inputs from the user
lenght_room = float(input())
width_room = float(input())
square_wardrobe = float(input()) * 100
# Calculations
room_area_cm = (lenght_room * 100) * (width_room * 100)
wardrobe_area = (square_wardrobe ** 2)
bench_area = (room_area_cm / 10)
free_space = room_area_cm - bench_area - wardrobe_area
dancers = free_space / (40 + 7000)
# Total number of dancers that can fit in the hall rounded to the nearest low
print(math.floor(dancers))