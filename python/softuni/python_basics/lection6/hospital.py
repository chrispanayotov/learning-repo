days = int(input())

doctors = 7
new_patients = 0
total_treated_patients = 0
total_untreated_patients = 0
treated_patients = 0
untreated_patients = 0

for day in range(1, days + 1):
    new_patients += int(input())
    if day % 3 == 0 and total_untreated_patients > total_treated_patients:
        doctors += 1

    if new_patients > doctors:
        untreated_patients += new_patients - doctors
        total_untreated_patients += new_patients - doctors
        new_patients -= untreated_patients
        untreated_patients = 0
    if new_patients <= doctors:
        total_treated_patients += new_patients
        new_patients = 0

print(f"Treated patients: {total_treated_patients}.")
print(f"Untreated patients: {total_untreated_patients}.")