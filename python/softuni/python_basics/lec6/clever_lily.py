n = int(input()) # Age of lilly
washing_machine = float(input())
toy_price = int(input())

bday_money = 0
total_money = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        bday_money = bday_money + 10
        total_money += bday_money - 1
    else:
        total_money += 1 * toy_price

if total_money >= washing_machine:
    print(f"Yes! {abs(total_money - washing_machine):.2f}")
else:
    print(f"No! {abs(total_money - washing_machine):.2f}")