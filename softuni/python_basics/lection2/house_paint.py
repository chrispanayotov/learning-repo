# Calculate how many litres of paint will be needed to paint a house

x = float(input()) # Height of the house
y = float(input()) # Width  of house
h = float(input()) # Height of triangle roof

# Dimensions of the house without roof
window = 1.5 ** 2 # square 
door = 1.2 * 2  # rectangle 
total_sides = (x * y) * 2 - 2 * (window)
total_backfront = (x * x) * 2 - (door)
total_house_area = total_sides + total_backfront
green_paint = total_house_area / 3.4 # 1 litre per 3.4sq.m.

# Dimensions of the roof
roof_rectangles = 2 * (x * y)
roof_triangles = 2 * (x * h / 2)
total_roof_area = roof_rectangles + roof_triangles
red_paint = total_roof_area / 4.3 # 1 litre per 4.3sq.m.

print(f"{green_paint:.2f}")
print(f"{red_paint:.2f}")