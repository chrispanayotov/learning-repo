class Dog:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age

sharo = Dog("Sharo", 5)
balkan = Dog("Balkan", 7)
rex = Dog("Rex", 9)

print("{} is {} years old and {} is {} years old.".format(
    sharo.name, sharo.age, balkan.name, balkan.age))

if sharo.species == "mammal":
    print("{0} is a {1}!".format(sharo.name, sharo.species))

def oldest_dog(*args):
    return max(args)

testvar = "The oldest dog is {} years old".format(
    oldest_dog(sharo.age, balkan.age, rex.age))

testvar_two = " and his name is {}".format(rex.name)

print(testvar + testvar_two)