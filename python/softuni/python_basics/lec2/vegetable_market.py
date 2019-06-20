# Calculate the profit of a villager who sells his produce on the market
# The profit must be in euro
kg_vegetables = float(input())
kg_fruits = float(input())
total_vegetables = float(input())
total_fruits = float(input())

price_vegetables = kg_vegetables * total_vegetables
price_fruits = kg_fruits * total_fruits
euro = (price_vegetables + price_fruits) / 1.94
if euro > 100:
    print(round(euro))
elif euro < 100:
    print(f"{euro:.13f}")
else:
    pass