eggs_in_stock = int(input())

eggs_sold = 0
command = input()

while command != "Close":
    eggs_amount = int(input())

    if command == "Buy":
        if eggs_amount <= eggs_in_stock:
            eggs_in_stock -= eggs_amount
            eggs_sold += eggs_amount
        else:
            print("Not enough eggs in store!")
            print(f"You can buy only {eggs_in_stock}.")
            break
             
    elif command == "Fill":
        eggs_in_stock += eggs_amount

    command = input()

    if command == "Close":
        print("Store is closed!")
        print(f"{eggs_sold} eggs sold.")