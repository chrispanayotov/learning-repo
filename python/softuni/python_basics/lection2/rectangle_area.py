# Calculate the area and perimeter of a 2D rectangle

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

length = abs(x1 - x2)
width = abs(y1 - y2)

area = length * width
perimeter = (length + width) * 2

print(f"{area:.2f}")
print(f"{perimeter:.2f}")