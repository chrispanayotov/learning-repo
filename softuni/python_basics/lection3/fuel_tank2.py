fuel_type = input().lower()
fuel_amount = float(input())
club_card = input().lower()

if club_card == "yes":
    gasoline = 2.22 - 0.18
    diesel = 2.33 - 0.12
    gas = 0.93 - 0.08
else:
    gasoline = 2.22 # per lt.
    diesel = 2.33 # per lt.
    gas = 0.93 # per lt.

if fuel_type == "gasoline":
    total = fuel_amount * gasoline
elif fuel_type == "diesel":
    total = fuel_amount * diesel
elif fuel_type == "gas":
    total = fuel_amount * gas

if 20 <= fuel_amount <= 25:
    total -= (total * 0.08)
elif fuel_amount > 25:
    total -= (total * 0.10)

print(f"{total:.2f} lv.")
