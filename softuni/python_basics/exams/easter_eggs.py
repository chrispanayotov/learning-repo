import sys
painted_eggs = int(input())

red = 0
orange = 0
blue = 0
green = 0
max_egg = -sys.maxsize-1
max_egg_name = None

for egg in range(painted_eggs):
    egg_color = input()

    if egg_color == "red":
        red += 1
        if red > max_egg:
            max_egg = red
            max_egg_name = "red"
    elif egg_color == "orange":
        orange += 1
        if orange > max_egg:
            max_egg = orange
            max_egg_name = "orange"
    elif egg_color == "blue":
        blue += 1
        if blue > max_egg:
            max_egg = blue
            max_egg_name = "blue"
    else:
        green += 1
        if green > max_egg:
            max_egg = green
            max_egg_name = "green"

print(f"Red eggs: {red}")
print(f"Orange eggs: {orange}")
print(f"Blue eggs: {blue}")
print(f"Green eggs: {green}")
print(f"Max eggs: {max_egg} -> {max_egg_name}")