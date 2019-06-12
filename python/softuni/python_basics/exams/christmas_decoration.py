budget = int(input())

price = 0

while budget >= 0:
    item = input()

    if item == "Stop":
        print(f"Money left: {budget}")
        break
    
    for letter in range(len(item)):
        price += ord(item[letter])
    
    if price <= budget:
        budget -= price
        print("Item successfully purchased!")
        price = 0
    else:
        print("Not enough money!")
        break