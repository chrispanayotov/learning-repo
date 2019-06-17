cinema_capacity = int(input())

current_visitors = 0
total_visitors = 0
profit = 0
is_full = False
command = input()

while total_visitors <= cinema_capacity:
    if command == "Movie time!":
        print(f"There are {abs(cinema_capacity - total_visitors)} seats left in the cinema.")
        break

    command = int(command)

    if total_visitors <= cinema_capacity:
        current_visitors += command
        total_visitors += command
        profit += current_visitors * 5

        if command % 3 == 0:
            profit -= 5

    elif total_visitors >= cinema_capacity:
        print("The cinema is full.")
        break

    current_visitors = 0
    command = input()

print(f"Cinema income - {profit} lv.")