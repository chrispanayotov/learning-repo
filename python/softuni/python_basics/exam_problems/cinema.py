capacity = int(input())

cinema_profit = 0

while True:
    command = input()

    if command == "Movie time!":
        print(f"There are {capacity} seats left in the cinema.")
        break
    
    current_visitors = int(command)

    if current_visitors > capacity:
        print(f"The cinema is full.")
        break
    else:
        capacity -= current_visitors

    cinema_profit += current_visitors * 5

    if current_visitors % 3 == 0:
        cinema_profit -= 5
    
    current_visitors = 0

print(f"Cinema income - {cinema_profit} lv.")