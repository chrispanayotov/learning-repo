allowed_mistakes = int(input())

problems_solved = 0
bad_grades = 0
result = 0

while bad_grades < allowed_mistakes:
    problem = input()

    if problem == "Enough":
        break

    grade = int(input())
    if grade <= 4:
        bad_grades += 1

    result += grade
    last_problem = problem
    problems_solved += 1

if problem == "Enough":
    result /= problems_solved
    print(f"Average score: {result:.2f}")
    print(f"Number of problems: {problems_solved}")
    print(f"Last problem: {last_problem}")
else:
    print(f"You need a break, {bad_grades} poor grades.")