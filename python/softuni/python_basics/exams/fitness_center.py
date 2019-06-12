visitors = int(input())

training = 0
purchased = 0
back = 0
chest = 0
legs = 0
abs_m = 0
prot_shake = 0
prot_bar = 0

for i in range(visitors):
    activity = input().title()

    if activity == "Back":
        training += 1
        back += 1
    elif activity == "Chest":
        training += 1
        chest += 1
    elif activity == "Legs":
        training += 1
        legs += 1
    elif activity == "Abs":
        training += 1
        abs_m += 1
    elif activity == "Protein Shake":
        purchased += 1
        prot_shake += 1
    else:
        purchased += 1
        prot_bar += 1

print(f"{back} - back")
print(f"{chest} - chest")
print(f"{legs} - legs")
print(f"{abs_m} - abs")
print(f"{prot_shake} - protein shake")
print(f"{prot_bar} - protein bar")
print(f"{training / visitors * 100:.2f}% - work out")
print(f"{purchased / visitors * 100:.2f}% - protein")