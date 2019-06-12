# Make a program that reads a value of an angle in radians (rad)
# And converts it to degrees (deg). Round to the nearest number
import math

rad = float(input())
deg = rad * 180 / math.pi
print(round(deg))