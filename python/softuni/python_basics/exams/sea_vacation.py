money_food = float(input())
money_gifts = float(input())
money_hotel = float(input())

money_gasoline = (420 / 100 * 7) * 1.85
money_food_gifts = (3 * money_food) + (3 * money_gifts)

day_one = money_hotel - (money_hotel * .10)
day_two = money_hotel - (money_hotel * .15)
day_three = money_hotel - (money_hotel * .20)

print(f"""Money needed: {money_gasoline + money_food_gifts + day_one 
        + day_two + day_three:.2f}""")