students = int(input())

top = 0
four_five = 0
three_four = 0
fail = 0
gpa_total = 0

for i in range(1, students + 1):
    gpa = float(input())
    if gpa >= 5.00:
        top += 1
        gpa_total += gpa
    elif gpa >= 4.00:
        four_five += 1
        gpa_total += gpa
    elif gpa >= 3.00:
        three_four += 1
        gpa_total += gpa
    else:
        fail += 1
        gpa_total += gpa

print(f"Top students: {(top / students) * 100:.2f}%")
print(f"Between 4.00 and 4.99: {(four_five / students) * 100:.2f}%")
print(f"Between 3.00 and 3.99: {(three_four / students) * 100:.2f}%")
print(f"Fail: {(fail / students) * 100:.2f}%")
print(f"Average: {gpa_total / students:.2f}")