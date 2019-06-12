flowers = input()
flowers_amount = int(input())
budget = int(input())

result = None

if flowers == "Roses":
    result = flowers_amount * 5
    if flowers_amount > 80:
        result -= (result * 0.10)
elif flowers == "Dahlias":
    result = flowers_amount * 3.80
    if flowers_amount > 90:
        result -= (result * 0.15)
elif flowers == "Tulips":
    result = flowers_amount * 2.80
    if flowers_amount > 80:
        result -= (result * 0.15)
elif flowers == "Narcissus":
    result = flowers_amount * 3
    if flowers_amount < 120:
        result += (result * 0.15)
elif flowers == "Gladiolus":
    result = flowers_amount * 2.50
    if flowers_amount < 80:
        result += (result * 0.20)

if result <= budget:
    result = abs(result - budget)
    print(f"Hey, you have a great garden with {flowers_amount} {flowers} and {result:.2f} leva left.")
elif result > budget:
    result = abs(result - budget)
    print(f"Not enough money, you need {result:.2f} leva more.")