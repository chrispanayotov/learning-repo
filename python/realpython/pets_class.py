class Pets:

	dogs = []

	def __init__(self, dogs):
		self.dogs = dogs


class Dog:
	species = 'mammal'
	is_hungry = True

	def __init__(self, name, age):
		self.name = name
		self.age = age
	

	def description(self):
		return f"{self.name} is {self.age} years old"


	def speak(self, sound):
		return f"{self.name} says {sound}"

	
	def eat(self):
		is_hungry = False

		
class RusselTerrier(Dog):
	def run(self, speed):
		return f"{self.name} runs {speed}"


class Bulldog(Dog):
	def run(self, speed):
		return f"{self.name} runs {speed}"


my_dogs = [
	Bulldog('Tom', 6),
	RusselTerrier('Fletcher', 7),
	Dog('Larry', 9)
]

my_pets = Pets(my_dogs)

print(f"I have {len(my_dogs)} dogs.")

for dog in my_pets.dogs:
	dog.eat()
	print(f"{dog.name} is {dog.age}")

print(f"And they are all {dog.species}, of course")

are_my_dogs_hungry = False

for dog in my_pets.dogs:
	if dog.is_hungry:
		are_my_dogs_hungry = True

if are_my_dogs_hungry:
	print("My dogs are hungry.")
else:
	print("My dogs are not hungry.")