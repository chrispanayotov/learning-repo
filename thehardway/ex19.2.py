def work_hours(day, week, month):
    print(f"A normal daily workload is {day} hours.")
    print(f"That means {week} hours per week.")
    print(f"Which is {month} hours per month...")
    #print(f"... and {year} hours per year.")

work_hours(8, 8*5, 8*20)

day = int(input("Please write how many hours you work per day."))
print(f"""
So, you work {day} hours per day,
which is {day * 5} hours a week,
{day * 20} hours a month,
and {day * 240} a year!
""")

day = 8
week = 40
month = 160
print(f"Workload is {day} hours per day, {week} h/week, {month} h/mo.")
work_hours(day, week, month)
