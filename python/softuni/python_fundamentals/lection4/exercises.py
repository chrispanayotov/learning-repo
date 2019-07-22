class Exercise:
    def __init__(self, topic, course_name, judge_contest_link, problems):
        self.topic = topic
        self.course_name = course_name
        self.judge_contest_link = judge_contest_link
        self.problems = problems


data = input()

exercises_list = []

while data != 'go go go':
    topic, course_name, link, problems = data.split(' -> ')
    problems = problems.split(', ')

    exercise = Exercise(topic, course_name, link, problems)
    exercises_list.append(exercise)

    data = input()

for exercise in exercises_list:
    print(f"Exercises: {exercise.topic}")
    print(
        f"Problems for exercises and homework for the \"{exercise.course_name}\" course @ SoftUni.")
    print(f"Check your solutions here: {exercise.judge_contest_link}")
    for index, problem in enumerate(exercise.problems):
        print(f"{index+1}. {problem}")
