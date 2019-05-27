days = int(input())
hours = int(input())

money_day = 0
total = 0

for day in range(1, days + 1):
    for hour in range(1, hours + 1):
        if day % 2 == 0 and hour % 2 != 0:
            money_day += 2.50
            total += 2.50
        elif day % 2 != 0 and hour % 2 == 0:
            money_day += 1.25
            total += 1.25
        else:
            money_day += 1
            total += 1

    print(f"Day: {day} - {money_day:.2f} leva")
    money_day = 0        

print(f"Total: {total:.2f} leva")
