def number_of_hours(h_week, h_month, h_year):
    print(f"You need to work {h_week} hours per week.")
    print(f"You need to work {h_month} hours per month.")
    print(f"You need to work {h_year} hours per year.")

print("We'll just put the numbers manually:")
number_of_hours(40, 160, 1920)

print("We'll use math to calculate the workload")
number_of_hours(40, 40 * 4, 160 * 12)

print("We'll define each variable separately:")
hours_week = 40
hours_month = 160
hours_year = 1920
number_of_hours(hours_week, hours_month, hours_year)

print(input("Press <Enter> to input what is your workload!"))
hours_week = int(input("How many hours do you work per week?:"))
hours_month = (hours_week * 4)
hours_year = (hours_month * 12)
print(f"""
So you work {hours_week} hours per week, {hours_month} hours per month and
{hours_year} hours per year!
""")
