from sys import argv

food, fruit, vegetable, meat = argv
input("Press <enter> to begin")
print(f"""
    This is a script called {food}, which is going to ask you
    couple of quick questions, about your favorite foods!
""")

fruit = input("What is your favorite fruit? ")
vegetable = input("What is your favorite vegetable? ")
meat = input("What is your favourite meat? ")
quant_fruit = int(input("How many fruits do you eat per day? "))
quant_vege = int(input("How many vegetables do you eat per day? "))
quant_meat = str(input("How much meat do you eat per day? "))

print("Your favorite fruit is: ", fruit)
print("Your favorite vegetable is: ", vegetable)
print("Your favorite meat is: ", meat)
print(f"You eat {quant_fruit} fruits a day!")
print(f"You eat {quant_vege} vegetables a day!")
print(f"And you eat {quant_meat} meat a day!")
