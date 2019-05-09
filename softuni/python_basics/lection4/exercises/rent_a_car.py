budget = float(input())
season = input().title()

car_class = None
car_type = None

if budget <= 100:
    car_class = "Economy class"
    if season == "Summer":
        car_type = "Cabrio"
        budget = budget * .35
    elif season == "Winter":
        car_type = "Jeep"
        budget = budget * .65
elif 100 < budget <= 500:
    car_class = "Compact class"
    if season == "Summer":
        car_type = "Cabrio"
        budget = budget * .45
    elif season == "Winter":
        car_type = "Jeep"
        budget = budget * .80
else:
    car_class = "Luxury class"
    car_type = "Jeep"
    budget = budget * .90

print(f"{car_class}")
print(f"{car_type} - {budget:.2f}")