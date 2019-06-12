import math
shape = str(input())

if shape == 'square':
    a = float(input())
    result = a * a
elif shape == 'rectangle':
    a = float(input())
    b = float(input())
    result = a * b
elif shape == 'circle':
    r = float(input())
    result = math.pi * r ** 2
elif shape == 'triangle':
    length = float(input())
    height = float(input())
    result = length * height / 2

print(f"{result:.3f}")