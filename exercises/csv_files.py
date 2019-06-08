import csv

with open("/home/uriel/smarterway/potions.csv") as f:
    text_to_read = csv.reader(f)
    potions_list = []

    for i in text_to_read:
        potions_list += i

target = potions_list.index("Draught of Peace")
pot_effect = target + 1
print(potions_list[pot_effect])