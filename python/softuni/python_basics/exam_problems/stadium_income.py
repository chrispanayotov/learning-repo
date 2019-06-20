n_sectors = int(input())
stadium_capacity = int(input())
ticket_price = float(input())

profit_per_sector = (stadium_capacity * ticket_price) / n_sectors
total_profit = profit_per_sector * n_sectors
charity = (total_profit - (profit_per_sector * 0.75)) / 8

print(f"Total income - {total_profit:.2f} BGN")
print(f"Money for charity - {charity:.2f} BGN")