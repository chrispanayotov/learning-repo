budget = float(input())
season = input().title()

if season == "Summer":
    location = "Alaska"
else:
    location = "Morocco"

if budget <= 1000:
    stay = "Camp"
    if season == "Summer":
        budget = budget * .65
    elif season == "Winter":
        budget = budget * .45
elif 1000 < budget <= 3000:
    stay = "Hut"
    if season == "Summer":
        budget = budget * .80
    elif season == "Winter":
        budget = budget * .60
elif budget > 3000:
    stay = "Hotel"
    budget = budget * .90

print(f"{location} - {stay} - {budget:.2f}")