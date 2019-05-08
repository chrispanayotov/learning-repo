import math
x = int(input()) # area of the land
y = float(input()) # grape per sq.m.
z = int(input()) # required litres of wine
amount_workers = int(input())

total_grape = x * y
produced_wine = ((total_grape / 2.5) * 40) / 100

if produced_wine >= z:
    print(f"Good harvest this year! Total wine: {math.floor(produced_wine)} liters.")
    wine_left = abs(produced_wine - z)
    wine_person = wine_left / amount_workers
    print(f"{math.ceil(wine_left)} liters left -> {math.ceil(wine_person)} liters per person.")
else:
    wine_left = abs(produced_wine - z)
    print(f"It will be a tough winter! More {math.floor(wine_left)} liters wine needed.")