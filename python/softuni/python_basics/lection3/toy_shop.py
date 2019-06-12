vacation_price = float(input())
puzzles_amount = int(input())
dolls_amount = int(input())
bears_amount = int(input())
minions_amount = int(input())
trucks_amount = int(input())

total_price_toys = ((puzzles_amount * 2.60 ) + (dolls_amount * 3) + 
                    (bears_amount * 4.10) + 
                    (minions_amount * 8.20) + (trucks_amount * 2))
amount_toys = (puzzles_amount + dolls_amount + bears_amount + 
                minions_amount + trucks_amount)

if amount_toys >= 50:
    total_price_toys -= total_price_toys * 0.25

total_price_toys -= total_price_toys * 0.10
profit = abs(total_price_toys - vacation_price)

if total_price_toys >= vacation_price:
    print(f"Yes! {profit:.2f} lv left.")
else:
    print(f"Not enough money! {profit:.2f} lv needed.")
    