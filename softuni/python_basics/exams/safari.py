budget = float(input())
fuel = float(input()) * 2.10
day = input().title()

total = fuel + 100 # price of a guide

if day == "Saturday":
    total -= total * .10
elif day == "Sunday":
    total -= total * .20

if total <= budget:
    print(f"Safari time! Money left: {abs(budget - total):.2f} lv.")
else:
    print(f"Not enough money! Money needed: {abs(budget - total):.2f} lv.")