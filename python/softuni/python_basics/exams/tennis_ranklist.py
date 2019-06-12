import math
n_tournaments = int(input())
starting_points = int(input())

W = 2000
F = 1200
SF = 720

total_points = 0
avg_points = 0
wins = 0

for i in range(n_tournaments):
    position = input()

    if position == "W":
        total_points += W
        wins += 1
    elif position == "F":
        total_points += F
    else:
        total_points += SF

print(f"Final points: {total_points + starting_points}")
print(f"Average points: {math.floor(total_points / n_tournaments)}")
print(f"{(wins / n_tournaments) * 100:.2f}%")