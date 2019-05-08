# Make a program that takes order for tailoring of covers and squares for tables
# Calculate the price in USD and BGN

amount_table = int(input())
lenght_table = float(input())
width_table = float(input())

area_rectangle = amount_table * (lenght_table + 2 * 0.30) * (width_table + 2 * 0.30)
area_square = amount_table * (lenght_table / 2) ** 2
price_usd = area_rectangle * 7 + area_square * 9
price_bgn = price_usd * 1.85
print(f"{price_usd:.2f} USD")
print(f"{price_bgn:.2f} BGN")
