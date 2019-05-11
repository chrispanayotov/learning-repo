payments = int(input())

counter = 0
balance = 0

while counter < payments:
    amount = float(input())

    if amount < 0:
        print(f"Invalid operation!")
        break
    else:
        print(f"Increase: {amount:.2f}")
        balance += amount
        counter += 1

print(f"Total: {balance:.2f}")