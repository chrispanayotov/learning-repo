days = int(input())
room = input()
evaluation = input()

result = None
nights = days - 1
ONE_PERSON = 18.00
APARTMENT = 25.00
PRESIDENT = 35.00

if room == "room for one person":
    result = nights * ONE_PERSON
elif room == "apartment":
    result = nights * APARTMENT
    if days < 10:
        result -= (result * 0.30)
    elif 10 <= days <= 15:
        result -= (result * 0.35)
    else:
        result -= (result *0.50)
elif room == "president apartment":
    result = nights * PRESIDENT
    if days < 10:
        result -= (result * 0.10)
    elif 10 <= days <= 15:
        result -= (result * 0.15)
    else:
        result -= (result * 0.20) 

if evaluation == "positive":
    result += (result * 0.25)
elif evaluation == "negative":
    result -= (result * 0.10)

print(f"{result:.2f}")