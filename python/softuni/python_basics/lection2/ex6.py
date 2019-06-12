# Make a program that calculates how many hours will be needed
# for an architect to complete a project. 1 project = 3 hours

architectName = str(input())
projectsAmount = int(input())
hoursRequired = projectsAmount * 3

print(f"The architect {architectName} will need {hoursRequired} hours to"
      f"to complete {projectsAmount} project/s.")

