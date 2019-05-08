import math
days = int(input())
total_food = int(input()) # in kg
dog_food = float(input())
cat_food = float(input())
turtle_food = float(input()) # in grams

req_food_dog = days * dog_food
req_food_cat = days * cat_food
req_food_turtle = (days * turtle_food) / 1000
result = req_food_cat + req_food_dog + req_food_turtle

if result <= total_food:
    result = math.floor(abs(total_food - result))
    print(f"{result} kilos of food left.")
else:
    result = math.ceil(abs(total_food - result))
    print(f"{result} more kilos of food are needed.")