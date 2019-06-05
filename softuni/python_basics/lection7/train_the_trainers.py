n_jury = int(input())

presentation = input()
grade_counter = 0
total_grade = 0

while presentation != "Finish":
    current_grade = 0

    for i in range(n_jury):
        grade = float(input())
        current_grade += grade
        total_grade += grade
        grade_counter += 1

    print(f"{presentation} - {current_grade / n_jury:.2f}.")

    presentation = input()

print(f"Student's final assessment is {total_grade / grade_counter:.2f}.")