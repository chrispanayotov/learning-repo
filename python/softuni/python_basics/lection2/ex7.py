# Calculate the area and perimeter of a circle with a radius r
# Format the output to the second decimal point
import math
r = float(input("Enter radius: "))
area = math.pi * r ** 2
perimeter = math.pi * 2 * r

print(f"Area is: {area:.2f}")
print(f"Perimeter is: {perimeter:.2f}")
