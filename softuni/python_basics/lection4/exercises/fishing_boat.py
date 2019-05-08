budget = int(input())
season = input().title()
fishermen = int(input())

if season == "Spring":
    result = 3000
elif season == "Winter":
    result = 2600
elif season == "Autumn" or season == "Summer":
    result = 4200

if fishermen <= 6:
    result -= (result * 0.10)
elif 7 <= fishermen <= 11:
    result -= (result * 0.15)
else:
    result -= (result * 0.25)

if (season == "Spring" or season == "Summer" or season == "Winter") and (fishermen % 2 == 0): 
    result -= (result * 0.05)

if result <= budget:
    result = abs(result - budget)
    print(f"Yes! You have {result:.2f} leva left.")
else:
    result = abs(result - budget)
    print(f"Not enough money! You need {result:.2f} leva.")