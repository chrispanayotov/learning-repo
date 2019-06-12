season = input().title()
km_month = float(input())

if km_month <= 5000:
    if season == "Spring" or season == "Autumn":
        result = km_month * 0.75
    elif season == "Summer":
        result = km_month * 0.90
    else:
        result = km_month * 1.05
elif 5000 < km_month <= 10000:
    if season == "Spring" or season == "Autumn":
        result = km_month * 0.95
    elif season == "Summer":
        result = km_month * 1.10
    else:
        result = km_month * 1.25
elif 10000 < km_month <= 20000:
    result = km_month * 1.45

result *= 4
result -= result * .10

print(f"{result:.2f}")