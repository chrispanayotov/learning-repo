hrizantemi = int(input())
roses = int(input())
tulips = int(input())
season = input().title()
holiday = input()

if season == "Spring" or season == "Summer":
    result = (hrizantemi * 2.00) + (roses * 4.10) + (tulips * 2.50)
    if holiday == "Y":
        result += result * .15
    if tulips > 7 and season == "Spring":
        result -= result * .05
    if hrizantemi + roses + tulips > 20:
        result -= result * .20
elif season == "Autumn" or season == "Winter":
    result = (hrizantemi * 3.75) + (roses * 4.50) + (tulips * 4.15)
    if holiday == "Y":
        result += result * .15
    if roses >= 10 and season == "Winter":
        result -= result * .10
    if hrizantemi + roses + tulips > 20:
        result -= result * .20

result += 2

print(f"{result:.2f}")