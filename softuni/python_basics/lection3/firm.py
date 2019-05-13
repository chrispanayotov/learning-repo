import math
required_h = int(input()) 
days = int(input()) 
overtime_employees = int(input()) # amount of employees that work overtime

education = days - (days * 0.10) # 10% of the days are for education
hours_after_education = education * 8
overtime_hours = overtime_employees * (2 * days)
total_h = math.floor(hours_after_education + overtime_hours)

if total_h >= required_h:
    x = abs(total_h - required_h)
    print(f"Yes!{x} hours left.")
else:
    x = abs(total_h - required_h)
    print(f"Not enough time!{x} hours needed.")