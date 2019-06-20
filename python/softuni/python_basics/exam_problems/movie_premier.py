projeciton = input()
package = input().title()
tickets_amount = int(input())

result = 0

if projeciton == "John Wick":
    if package == "Drink":
        result += tickets_amount * 12
    elif package == "Popcorn":
        result += tickets_amount * 15
    else:
        result += tickets_amount * 19
elif projeciton == "Star Wars":
    if package == "Drink":
        result += tickets_amount * 18
    elif package == "Popcorn":
        result += tickets_amount * 25
    else:
        result += tickets_amount * 30
elif projeciton == "Jumanji":
    if package == "Drink":
        result += tickets_amount * 9
    elif package == "Popcorn":
        result += tickets_amount * 11
    else:
        result += tickets_amount * 14

if projeciton == "Star Wars" and tickets_amount >= 4:
    result -= result * .30
elif projeciton == "Jumanji" and tickets_amount == 2:
    result -= result * .15

print(f"Your bill is {result:.2f} leva.")