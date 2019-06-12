vacation_days = int(input())
CAT_POWER = 30000

work_days = 365 - vacation_days
play_time = (work_days * 63) + (vacation_days * 127)

if play_time > CAT_POWER:
    print("Tom will run away")
    power_left = abs(CAT_POWER - play_time)
    h = power_left // 60
    m = power_left % 60
    print(f"{h} hours and {m} minutes more for play")
else:
    print("Tom sleeps well")
    total = abs(CAT_POWER - play_time)
    h = total // 60
    m = total % 60
    print(f"{h} hours and {m} minutes less for play")