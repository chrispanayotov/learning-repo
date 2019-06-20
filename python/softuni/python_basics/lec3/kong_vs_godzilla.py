total_budget = float(input())
actors_amount = int(input())
price_clothes = float(input()) # per 1 actor

decor = (total_budget * 10) / 100

if actors_amount >= 150:
    price_clothes -= (price_clothes * 10) / 100

total_clothes = actors_amount * price_clothes
#movie_price = decor + total_clothes
total_price = decor + total_clothes

if total_budget < total_price:
    print("Not enough money!")
    print(f"Wingard needs {abs(total_budget - total_price):.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {abs(total_budget - total_price):.2f} leva left.")