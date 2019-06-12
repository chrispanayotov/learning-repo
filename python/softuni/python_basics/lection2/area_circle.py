# Calculate perimeter and area of a circle
import math
r = float(input())
area = math.pi * r ** 2
perimeter = 2 * math.pi * r

print(f"Area is: {area:.2f}")
print(f"Perimeter is: {perimeter:.2f}")