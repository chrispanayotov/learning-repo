n_fish = int(input())

total = 0
fish_counter = 0

for i in range(1, n_fish+1):
    lost_money = 0
    profit = 0
    fish_name = input()

    if fish_name == "Stop":
        break

    fish_kg = float(input())
    fish_counter += 1

    for letter in range(len(fish_name)):
        if i % 3 == 0:
            profit += ord(fish_name[letter])
        else:
            lost_money += ord(fish_name[letter])

    if profit != 0:
        profit /= fish_kg
        total += profit
    elif lost_money != 0:
        lost_money /= fish_kg
        total -= lost_money
        
if fish_counter == n_fish:
    print(f"Lyubo fulfilled the quota!")

if total >= 0:
    print(f"Lyubo's profit from {fish_counter} fishes is {total:.2f} leva.")
else:
    print(f"Lyubo lost {abs(total):.2f} leva today.")