import sys
n_kozunaks = int(input())

top_chef = None
top_points = -sys.maxsize-1
current_points = 0

for kozunak in range(n_kozunaks):
    chef_name = input()

    while True:
        rating = input()

        if rating == "Stop":
            break
        else:
            current_points += int(rating)
    
    print(f"{chef_name} has {current_points} points.")
    if current_points > top_points:
        top_points = current_points
        top_chef = chef_name
        print(f"{chef_name} is the new number 1!")

    current_points = 0

print(f"{top_chef} won competition with {top_points} points!")