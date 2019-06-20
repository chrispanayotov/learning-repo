budget = float(input())

counter = 0
purchases = 0

while budget >= 0:
    product_name = input()

    if product_name == "Stop":
        print(f"You bought {counter} products for {purchases:.2f} leva.")
        break
        
    product_price = float(input())
    counter += 1

    if counter % 3 == 0 and counter > 0:
        product_price /= 2

    purchases += product_price
    budget -= product_price
    
    if budget < 0:
        print("You don't have enough money!")
        print(f"You need {abs(budget):.2f} leva!")
