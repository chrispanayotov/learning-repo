class Dog:
    def __init__(self, name, age, number_of_legs):
        self.name = name
        self.age = age
        self.number_of_legs = number_of_legs
    

    def produce_sound(self):
        return "I'm a Distinguishedog, and I will now produce a distinguished sound! Bau Bau."


class Cat:
    def __init__(self, name, age, iq):
        self.name = name
        self.age = age
        self.iq = iq


    def produce_sound(self):
        return "I'm an Aristocat, and I will now produce an aristocratic sound! Myau Myau."


class Snake:
    def __init__(self, name, age, cruelty_coeff):
        self.name = name
        self.age = age
        self.cruelty = cruelty_coeff
    

    def produce_sound(self):
        return "I'm a Sophistisnake, and I will now produce a sophisticated sound! Honey, I'm home."


data = input()
dogs = []
cats = []
snakes = []

while data[0] != "I":
    # Starts creating objects when the if check passes
    if data[0:4] != 'talk':
        class_, name, age, parameter = data.split(' ')
        age, parameter = int(age), int(parameter)

        if class_ == "Dog":
            dog = Dog(name, age, parameter)
            dogs.append(dog)
        elif class_ == "Cat":
            cat = Cat(name, age, parameter)
            cats.append(cat)
        else:
            snake = Snake(name, age, parameter)
            snakes.append(snake)
        
        data = input()
    # When the if check doesn't pass starts calling methods from each class
    else:
        data = data.split(' ')
        for dog in dogs:
            if data[1] == dog.name:
                print(dog.produce_sound())
        for cat in cats:
            if data[1] == cat.name:
                print(cat.produce_sound())
        for snake in snakes:
            if data[1] == snake.name:
                print(snake.produce_sound())
        
        data = input()

for dog in dogs:
    print(f"Dog: {dog.name}, Age: {dog.age}, Number Of Legs: {dog.number_of_legs}")
for cat in cats:
    print(f"Cat: {cat.name}, Age: {cat.age}, IQ: {cat.iq}")
for snake in snakes:
    print(f"Snake: {snake.name}, Age: {snake.age}, Cruelty: {snake.cruelty}")