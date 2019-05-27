money_singer = int(input())

guests = None
total_guests = 0
total = 0


while True:
    guests = input()
    if guests == "The restaurant is full":
        break
    guests = int(guests)
    total_guests += int(guests)
    if guests >= 5:
        total += guests * 70
    else:
        total += guests * 100

if total >= money_singer:
    print(f"You have {total_guests} guests and {abs(money_singer - total)} leva left.")
else:
    print(f"You have {total_guests} guests and {total} leva income, but no singer.")