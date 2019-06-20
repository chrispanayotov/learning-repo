import math
income = float(input())
gpa = float(input())
minSalary = float(input())

socialScholarship = 0
excellentScholarship = 0
if income < minSalary and gpa > 4.5:
    socialScholarship = (minSalary * 35) / 100

if gpa >= 5.5:
    excellentScholarship = gpa * 25

if socialScholarship == 0 and excellentScholarship == 0:
    print("You cannot get a scholarship!")
elif socialScholarship > excellentScholarship:
    print(f"You get a Social scholarship {math.floor(socialScholarship)} BGN")
else:
    print(f"You get a scholarship for excellent results {math.floor(excellentScholarship)} BGN")

    