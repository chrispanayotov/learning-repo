# Make a program that calculates how much money Pesho needs
# to purchase beer, wine, rakia and whiskey from the market

whiskey_price = float(input())
beer_litres = float(input()) 
wine_litres = float(input())
rakia_litres = float(input())
whiskey_litres = float(input())

rakia_price = whiskey_price - (whiskey_price * 0.5)
wine_price = rakia_price - (rakia_price * 0.4)
beer_price = rakia_price - (rakia_price * 0.8)
total_rakia = rakia_litres * rakia_price
total_wine = wine_litres * wine_price
total_beer = beer_litres * beer_price
total_whiskey = whiskey_litres * whiskey_price
result = total_beer + total_rakia + total_wine + total_whiskey
print(f"{result:.2f}")