hall_rent = int(input())

statues = hall_rent - (hall_rent * .30)
service = statues - (statues * .15)
sound = service / 2
total = statues + service + sound + hall_rent

print(f"{total:.2f}")