budget = float(input())
season = input().lower()

destination = None
stay = None

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        stay = "Camp"
        budget *= 0.30
    elif season == "winter":
        stay = "Hotel"
        budget *=  0.70
elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        stay = "Camp"
        budget *= 0.40
    elif season == "winter":
        stay = "Hotel"
        budget *= 0.80
else:
    destination = "Europe"
    stay = "Hotel"
    budget *= 0.90

print(f"Somewhere in {destination}")
print(f"{stay} - {budget:.2f}")
