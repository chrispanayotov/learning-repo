fruit = input()
weekday = input().lower()
quantity = float(input())

result = None

if weekday == "saturday" or weekday == "sunday":
    if fruit == "banana":
        result = quantity * 2.70
    elif fruit == "apple":
        result = quantity * 1.25
    elif fruit == "orange":
        result = quantity * 0.90
    elif fruit == "grapefruit":
        result = quantity * 1.60
    elif fruit == "kiwi":
        result = quantity * 3.00
    elif fruit == "pineapple":
        result = quantity * 5.60
    elif fruit == "grapes":
        result = quantity * 4.20
elif weekday == "monday" or weekday == "tuesday" or weekday == "wednesday" or weekday == "thursday" or weekday == "friday":
    if fruit == "banana":
        result = quantity * 2.50
    elif fruit == "apple":
        result = quantity * 1.20
    elif fruit == "orange":
        result = quantity * 0.85
    elif fruit == "grapefruit":
        result = quantity * 1.45
    elif fruit == "kiwi":
        result = quantity * 2.70
    elif fruit == "pineapple":
        result = quantity * 5.50
    elif fruit == "grapes":
        result = quantity * 3.85

if result:
    print(f"{result:.2f}")
else:
    print("error")