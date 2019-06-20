money_required = float(input())
money_wallet = float(input())

days = 0
spending = 0

while money_wallet < money_required and spending != 5:
    spend_or_save = input()
    amount = float(input())
    days += 1

    if spend_or_save == "spend":
        spending += 1
        money_wallet -= amount
        if money_wallet < 0:
            money_wallet = 0
    elif spend_or_save == "save":
        money_wallet += amount
        spending = 0
    
if money_wallet >= money_required:
    print(f"You saved the money for {days} days.")
else:
    print(f"You can't save the money.")
    print(f"{days}")