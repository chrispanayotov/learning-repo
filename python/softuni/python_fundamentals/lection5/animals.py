class Animal:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
    

class Dog(Animal):
    def __init__(self, name, age, number_of_legs: int):
        Animal.__init__(self, name, age)
        self.number_of_legs = number_of_legs
    

    def produce_sound(self):
        return "I'm a Distinguishedog, and I will now produce a distinguished sound! Bau Bau."
    
    def __str__(self):
        return f"Dog: {self.name}, Age: {self.age}, Number of Legs: {self.number_of_legs}"


class Cat(Animal):
    def __init__(self, name, age, iq: int):
        Animal.__init__(self, name, age)
        self.iq = iq


    def produce_sound(self):
        return "I'm an Aristocat, and I will now produce an aristocratic sound! Myau Myau."
    

    def __str__(self):
        return f"Cat: {self.name}, Age: {self.age}, IQ: {self.iq}"


class Snake(Animal):
    def __init__(self, name, age, cruelty_coeff):
        Snake.__init__(self, name, age)
        self.cruelty = cruelty_coeff
    

    def produce_sound(self):
        return "I'm a Sophistisnake, and I will now produce a sophisticated sound! Honey, I'm home."
    

    def __str__(self):
        return f"Snake: {self.name}, Age: {self.age}, Cruely: {self.cruelty}"


data = input()
animals_list = []

while data[0] != "I":
    if data[0:4] != 'talk':
        class_, name, age, parameter = data.split(' ')
        age, parameter = int(age), int(parameter)

        str_class_instance = f"{class_}(\"{name}\", {age}, {parameter})"
        current_animal = eval(str_class_instance)

        animals_list.append(current_animal)
            
    data = input()

dogs = filter(lambda x: isinstance(x, Dog), animals_list)
cats = filter(lambda x: isinstance(x, Cat), animals_list)
snakes = filter(lambda x: isinstance(x, Snake), animals_list)
sorted_animals = dogs + cats + snakes

for animal in sorted_animals:
    pass
