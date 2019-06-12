n_floors = int(input())
n_rooms = int(input())

room_number = n_floors * 10
new_line = "\n"

for floor in range(n_floors, 0, -1):
    for room in range(n_rooms):
        if floor == n_floors:
            print(f"L{room_number + room}", end=' ')
        elif floor % 2 == 0:
            print(f"O{room_number + room}", end=' ')
        elif floor % 2 != 0:
            print(f"A{room_number + room}", end=' ')
    
    print(new_line.strip())
    room_number -= 10