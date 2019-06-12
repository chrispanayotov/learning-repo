period = input()
contract_type = input().title()
internet = input()
months = int(input())

result = 0

if period == "one":
    if contract_type == "Small":
        result = 9.98
    elif contract_type == "Middle":
        result = 18.99
    elif contract_type == "Large":
        result = 25.98
    else:
        result = 35.99
else:
    if contract_type == "Small":
        result = 8.58
    elif contract_type == "Middle":
        result = 17.09
    elif contract_type == "Large":
        result = 23.59
    else:
        result = 31.79

if internet == "yes":
    if result <= 10.00:
        result += 5.50
    elif result <= 30.00:
        result += 4.35
    else:
        result += 3.85

if period == "two":
    result -= result * 3.75 / 100

result *= months
print(f"{result:.2f} lv.")