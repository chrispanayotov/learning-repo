dog_food = int(input())

dog_food *= 1000
food_eaten = None

while True:
    food_eaten = input()

    if food_eaten == "Adopted":
        break
    food_eaten = int(food_eaten)
    dog_food -= food_eaten

if dog_food >= 0:
    print(f"Food is enough! Leftovers: {dog_food} grams.")
else:
    print(f"Food is not enough. You need {abs(dog_food)} grams more.")