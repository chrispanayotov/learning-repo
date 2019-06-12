n_groups = int(input())

musala = 0
monblan = 0
kilimandjaro = 0
k2 = 0
everest = 0
total_people = 0

for group in range(n_groups):
    group_amount = int(input())

    if group_amount <= 5:
        musala += group_amount
    elif group_amount <= 12:
        monblan += group_amount
    elif group_amount <= 25:
        kilimandjaro += group_amount
    elif group_amount <= 40:
        k2 += group_amount
    else:
        everest += group_amount
        
    total_people += group_amount

print(f"{musala / total_people * 100:.2f}%")
print(f"{monblan / total_people * 100:.2f}%")
print(f"{kilimandjaro / total_people * 100:.2f}%")
print(f"{k2 / total_people * 100:.2f}%")
print(f"{everest / total_people * 100:.2f}%")