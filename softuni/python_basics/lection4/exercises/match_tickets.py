budget = float(input())
category = input()
people = int(input())

if category == "Normal":
    price = people * 249.99
    if 1 <= people <= 4:
        budget -= budget * .75
    elif 5 <= people <= 9:
        budget -= budget * .60
    elif 10 <= people <= 24:
        budget -= budget * .50
    elif 25 <= people <= 49:
        budget -= budget * .40
    else:
        budget -= budget * .25
elif category == "VIP":
    price = people * 499.99
    if 1 <= people <= 4:
        budget -= budget * .75
    elif 5 <= people <= 9:
        budget -= budget * .60
    elif 10 <= people <= 24:
        budget -= budget * .50
    elif 25 <= people <= 49:
        budget -= budget * .40
    else:
        budget -= budget * .25

if price <= budget:
    total = abs(budget - price)
    print(f"Yes! You have {total:.2f} leva left.")
else:
    total = abs(budget - price)
    print(f"Not enough money! You need {total:.2f} leva.")