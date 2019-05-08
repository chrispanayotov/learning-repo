##Now, go through this piece of code and replace each ##?? comment 
# with a comment that says whether 
# the next line represents an is-a or a has-a relationship 
# and what that relationship is.
# Remember, is-a is the relationship between fish and salmon, 
# while has-a is the relationship between salmon and gills.



## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## ??
Class Dog(Animal):

    def __init__(self, name):
        ## ??
        self.name = name

# ??
class Cat(Animal):

    def __init(self, name):
        ## ??
        self.name = name

## ??
class Person(object):
    def __init__(self, name):
        ##??
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## ??
class Employee(Person):

    def __init__(self, name, salary):
        ## ?? hmm what is this strange magic?
        super(Employee, self).__init__(name)
        ## ??
        self.salary = salary

## ??
class Fish(object):
    pass

## ??
class Salmon(Fish):
    pass

# ??
class Halibut(Fish):
    pass

# rover is-a Dog
rover = Dog("Rover")

# ??
satan = Cat("Satan")

## ??
mary = Person("Mary")

# ??
mary.pet = satan

# ??
frank = Employee("Frank", 120000)

## ??
frank.pet = rover

## ??
flipper = Fish()

# ??
crouse = Salmon()

##??
harry = Halibut()
