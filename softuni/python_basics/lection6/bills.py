months = int(input())

water = 20 * months
internet = 15 * months
electricity = 0
others = 0
average = 0

for i in range(1, months + 1):
    electricity += float(input())

others += (electricity + water + internet) * .20
total = water + internet + electricity + others
average = (water + internet + electricity + total) / months

print(f"Electricity: {electricity:.2f} lv")
print(f"Water: {water:.2f} lv")
print(f"Internet: {internet:.2f} lv")
print(f"Other: {total:.2f} lv")
print(f"Average: {average:.2f} lv")