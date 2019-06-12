while True:
    destination = input()

    if destination == "End":
        break

    money_req = float(input())

    saved_money = 0

    while saved_money < money_req:
        current_money = float(input())
        saved_money += current_money

    print(f"Going to {destination}!")