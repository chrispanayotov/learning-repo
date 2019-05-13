w = int(input())
l = int(input())
h = int(input())

free_space = w * l * h

while free_space > 0:
    boxes = input()

    if boxes == 'Done':
        print(f"{free_space} Cubic meters left.")
        break

    free_space -= int(boxes)

if boxes != 'Done':
    print(f"No more free space! You need {abs(free_space)} Cubic meters more.")