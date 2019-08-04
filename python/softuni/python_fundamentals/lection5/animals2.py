from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def __str__(self):
        return f"{self.__class__.__name__}\n{self.name} {self.age} {self.gender}"


    @abstractmethod
    def produce_sound(self):
        pass

    # Age getter/setter
    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, value):
        if value < 0:
            raise Exception('Invalid input!')
        self.__age = value
    
    # Gender getter/setter
    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, value):
        if self.__class__.__name__ == 'Kitten':
            self.__gender = 'Female'
        elif self.__class__.__name__ == 'Tomcat':
            value = 'Male'
        self.__gender = value


class Dog(Animal):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
    
    def produce_sound(self):
        return 'Woof!'


class Cat(Animal):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
    
    def produce_sound(self):
        return 'Meow meow'


class Kitten(Cat):
    def __init__(self, name, age, gender='Female'):
        super().__init__(name, age, gender='Female')
        self.gender = 'Female'

    def produce_sound(self):
        return 'Meow'


class Tomcat(Cat):
    def __init__(self, name, age, gender='Male'):
        super().__init__(name, age, gender='Male')
        self.gender = 'Male'

    def produce_sound(self):
        return 'MEOW'


class Frog(Animal):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)

    def produce_sound(self):
        return 'Ribbit'

is_failed = False

while True:
    type_of_animal = input()
    
    if type_of_animal == 'Beast!':
        break

    name, age, gender = input().split()

    try:
        if type_of_animal == 'Dog':
            animal = Dog(name, int(age), gender)
        elif type_of_animal == 'Cat':
            animal = Cat(name, int(age), gender)
        elif type_of_animal == 'Frog':
            animal = Frog(name, int(age), gender)
        elif type_of_animal == 'Kitten':
            animal = Kitten(name, int(age), gender)
        elif type_of_animal == 'Tomcat':
            animal = Tomcat(name, int(age), gender)
        else:
            raise Exception
    except Exception as f:
        print('Invalid input!')
        continue

    print(animal)
    print(animal.produce_sound())