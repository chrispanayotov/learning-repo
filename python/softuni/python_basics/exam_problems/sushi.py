import math
sushi_type = input()
restaurant = input()
portions = int(input())
delivery = input().upper()

total = 0

if restaurant == "Sushi Zone":
    if sushi_type == "sashimi":
        total += portions * 4.99
    elif sushi_type == "maki":
        total += portions * 5.29
    elif sushi_type == "uramaki":
        total += portions * 5.99
    else:
        total += portions * 4.29
elif restaurant == "Sushi Time":
    if sushi_type == "sashimi":
        total += portions * 5.49
    elif sushi_type == "maki":
        total += portions * 4.69
    elif sushi_type == "uramaki":
        total += portions * 4.49
    else:
        total += portions * 5.19
elif restaurant == "Sushi Bar":
    if sushi_type == "sashimi":
        total += portions * 5.25
    elif sushi_type == "maki":
        total += portions * 5.55
    elif sushi_type == "uramaki":
        total += portions * 6.25
    else:
        total += portions * 4.75
elif restaurant == "Asian Pub":
    if sushi_type == "sashimi":
        total += portions * 4.50
    elif sushi_type == "maki":
        total += portions * 4.80
    elif sushi_type == "uramaki":
        total += portions * 5.50
    else:
        total += portions * 5.50
else:
    print(f"{restaurant} is invalid restaurant!")

if delivery == "Y":
    total += total * .20
if total != 0:
    print(f"Total price: {math.ceil(total)} lv.")