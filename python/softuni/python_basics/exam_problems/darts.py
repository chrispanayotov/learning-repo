player_name = input()

POINTS = 301
successfull_hits = 0
failed_hits = 0
is_retired = False

while POINTS != 0:
    target = input()
    
    if target == "Retire":
        is_retired = True
        break

    hit_points = int(input())

    if target == "Triple":
        hit_points *= 3
    elif target == "Double":
        hit_points *= 2

    if hit_points <= POINTS:
        successfull_hits += 1
        POINTS -= hit_points
    else:
        failed_hits += 1

if is_retired == False:
    print(f"{player_name} won the leg with {successfull_hits} shots.")
else:
    print(f"{player_name} retired after {failed_hits} unsuccessful shots.")