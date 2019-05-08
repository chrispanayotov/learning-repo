product = input()
city = input().lower()
amount = float(input())

if city == "sofia":
    if product == "coffee":
        result = amount * 0.5
    elif product == "water":
        result = amount * 0.8
    elif product == "beer":
        result = amount * 1.2
    elif product == "sweets":
        result = amount * 1.45
    else:
        result = amount * 1.6
elif city == "plovdiv":
    if product == "coffee":
        result = amount * 0.4
    elif product == "water":
        result = amount * 0.7
    elif product == "beer":
        result = amount * 1.15
    elif product == "sweets":
        result = amount * 1.3
    else:
        result = amount * 1.5
else:
    if product == "coffee":
        result = amount * 0.45
    elif product == "water":
        result = amount * 0.7
    elif product == "beer":
        result = amount * 1.1
    elif product == "sweets":
        result = amount * 1.35
    else:
        result = amount * 1.55
print(result)