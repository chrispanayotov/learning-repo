season = input().title()
group = input()
students = int(input())
nights = int(input())

if group == "boys" or group == "girls":
    if season == "Winter":
        result = (students * nights) * 9.60
        if group == "girls":
            sport = "Gymnastics"
        elif group == "boys":
            sport = "Judo"
    elif season == "Spring":
        result = (students * nights) * 7.20
        if group == "girls":
            sport = "Athletics"
        elif group == "boys":
            sport = "Tennis"
    else:
        result = (students * nights) * 15
        if group == "girls":
            sport = "Volleyball"
        elif group == "boys":
            sport = "Football"
elif group == "mixed":
    if season == "Winter":
        result = (students * nights) * 10
        sport = "Ski"
    elif season == "Spring":
        result = (students * nights) * 9.50
        sport = "Cycling"
    else:
        result = (students * nights) * 20
        sport = "Swimming"

if 10 <= students < 20:
    result -= result * .05
elif students >= 50:
    result -= result * .50
elif 20 <= students < 50:
    result -= result * .15

print(f"{sport} {result:.2f} lv.")