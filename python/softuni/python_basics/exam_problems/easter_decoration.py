n_clients = int(input())

shopping_cart = 0
current_total = 0
total = 0

for client in range(n_clients):
    while True:
        product = input()
        
        if product == "Finish":
            if shopping_cart % 2 == 0:
                current_total -= current_total * .20

            print(f"You purchased {shopping_cart} items for {current_total:.2f} leva.")

            total += current_total
            current_total = 0
            shopping_cart = 0

            break
        elif product == "basket":
            current_total += 1.50
        elif product == "wreath":
            current_total += 3.80
        else:
            current_total += 7

        shopping_cart += 1

print(f"Average bill per client is: {total / n_clients:.2f} leva.")