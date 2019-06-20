name = input()

grade = 1
result = 0

while grade <= 12:
    gpa = float(input())

    if gpa >= 4:
        result += gpa
        grade += 1
    else:
        print(f"{name} has been excluded at {grade} grade")
        break

if grade > 12:
    result /= 12
    print(f"{name} graduated. Average grade: {result:.2f}")