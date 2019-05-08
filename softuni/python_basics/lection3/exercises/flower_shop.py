import math
magnolii_amount = int(input())
zumbuli_amount = int(input())
roses_amount = int(input())
cactus_amount = int(input())
gift_price = float(input())
# Pricelist
MAGNOLII = 3.25
ZUMBULI = 4
CACTUS = 8
ROSES = 3.50

total = (magnolii_amount * MAGNOLII + zumbuli_amount * ZUMBULI + 
        cactus_amount * CACTUS + roses_amount * ROSES)
total -= (total * 0.05) # after taxes

if total >= gift_price:
    total = math.floor(abs(gift_price - total))
    print(f"She is left with {total} leva.")
else:
    total = math.ceil(abs(gift_price - total))
    print(f"She will have to borrow {total} leva.")
