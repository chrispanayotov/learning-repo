##Now, go through this piece of code and replace each ##?? comment 
# with a comment that says whether 
# the next line represents an is-a or a has-a relationship 
# and what that relationship is.
# Remember, is-a is the relationship between fish and salmon, 
# while has-a is the relationship between salmon and gills.



## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

# class Dog is-a class of type Animal
class Dog(Animal):
    pass
    def __init__(self, name):
        # Dog has-a attribute called name
        self.name = name

# Cat is-a class of type Animal
class Cat(Animal):

    def __init(self, name):
        # Cat has-a attribute called name
        self.name = name

# Person is-a class of type object
class Person(object):
    def __init__(self, name):
        # Person has-a attribute called name
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

# Employee is-a class of type Person
class Employee(Person):

    def __init__(self, name, salary):
        # Employee has-a attribute called name
        super(Employee, self).__init__(name)
        # Employee has-a attribute called salary
        self.salary = salary

# Fish is-a class of type object
class Fish(object):
    pass

# Salmon is-a class of type Fish
class Salmon(Fish):
    pass

# Halibut is-a class of type Fish
class Halibut(Fish):
    pass

# rover is-a Dog
rover = Dog("Rover")

# satan is-a Cat
satan = Cat("Satan")

# mary is-a Person
mary = Person("Mary")

# mary has-a pet called satan
mary.pet = satan

# frank is-a Employee that has-a name "Frank" and has-a salary of 120000
frank = Employee("Frank", 120000)

# frank has-a pet called rover
frank.pet = rover

# flipper is-a object of class Fish
flipper = Fish()

# crouse is-a object of class Salmon
crouse = Salmon()

# harry is-a object of class Halibut
harry = Halibut()
