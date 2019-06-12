GOAL = 10000
steps = 0

while steps < GOAL:
    command = input()

    if command == "Going home":
        steps += int(input())
        break
            
    steps += int(command)

if steps >= GOAL:
    print("Goal reached! Good job!")
else:
    print(f"{abs(GOAL - steps)} more steps to reach goal.")