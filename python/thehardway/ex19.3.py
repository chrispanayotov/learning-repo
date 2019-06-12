def food(fruits, vegetables):
    print(f"You have {fruits} fruits in the fridge.")
    print(f"You have {vegetables} vegetables in the fridge.")
# Manually inputting the integers
food(10, 20)
# Using math
food(2 *5, 10 * 2)
# Using variables in the script
amount_of_fruits = 14
amounts_of_veggies = 36
food(amount_of_fruits, amounts_of_veggies)
# Combining variables with math
food(amount_of_fruits + 30, amounts_of_veggies + 40)
# Input from user
veggies = int(input("How many vegetables do you have in the fridge?"))
frutties = int(input("How many fruits do you have in the fridge?"))
food(veggies, frutties)
# Input from user using math
veggies = int(input("How many vegetables do you have in the fridge?"))
frutties = int(input("How many fruits do you have in the fridge?"))
food(veggies + 10, frutties + 12)
