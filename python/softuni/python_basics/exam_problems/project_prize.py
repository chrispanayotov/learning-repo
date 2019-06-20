project_size = int(input())
money_prize = float(input())

total_points = 0 

for part in range(1, project_size + 1):
    current_points = int(input())

    if part % 2 == 0:
        total_points += current_points * 2
    else:
        total_points += current_points

total = total_points * money_prize
print(f"The project prize was {total:.2f} lv.")