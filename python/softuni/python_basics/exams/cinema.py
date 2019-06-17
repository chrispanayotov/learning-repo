import sys
cinema_capacity = int(input())

total_profit = 0
visitors = 0
current_visitors = 0
current_profit = 0

while visitors < cinema_capacity:
    command = input()

    if command == "Movie time!":
        print(f"There are {abs(visitors - cinema_capacity)} seats left in the cinema.")
        print(f"Cinema income - {total_profit} lv.")
        sys.exit()

    visitors += int(command)
    current_visitors += int(command)
    current_profit += current_visitors * 5

    if current_visitors % 3 == 0:
        current_profit -= 5

    total_profit += current_profit
    current_visitors = 0
    current_profit = 0

print(f"Cinema income - {total_profit} lv.")