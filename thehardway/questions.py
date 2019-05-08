# User needs to press enter to begin the test
input("Press <enter> to begin quesitonnaire!")
# Define the input for diferrent variables
name = str(input("What is your name? "))
age = int(input("How old are you? "))
sex = str(input("What is your sex? "))
animal = str(input("What is your favorite animal? "))
food = str(input("What is your favorite food? "))
element = str(input("Ice, fire, air or earth? "))

print("Your answers:")
print(f"""
Hi, there {name}, welcome!
So, you are a {sex} and you are {age} years old.
Your favorite animal is {animal} and you love {food}.
Your element is {element}!
""")
