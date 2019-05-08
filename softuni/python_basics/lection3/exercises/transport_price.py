km_distance = int(input())
day_or_night = input()

if km_distance < 20 and day_or_night == "day":
    cheapest_price = 0.70 + (0.79 * km_distance)
elif km_distance < 20 and day_or_night == "night":
    cheapest_price = 0.70 + (0.90 * km_distance)

if km_distance >= 20 and km_distance < 100:
    cheapest_price = 0.09 * km_distance
elif km_distance >= 100:
    cheapest_price = 0.06 * km_distance

print(f"{cheapest_price:.2f}")