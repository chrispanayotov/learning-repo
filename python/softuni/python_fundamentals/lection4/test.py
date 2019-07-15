class Pet:
    def __init__(self, species, name, age, character):
        self.species = species
        self.name = name
        self.age = age
        self.character = character

    def speak(self, sound):
        return f"{self.name} says {sound}."

juji = Pet('dog', 'Juji', 15, 'strong')
moly = Pet('dog', 'Moly', 8, 'scared')
mini = Pet('cat', 'Mini', 0.5, 'kind')
tommy = Pet('cat', 'Tommy', 0.5, 'curious')

def oldest_pet(*args):
    return max(*args)


print(f'The oldest pet is {oldest_pet(juji.age, moly.age, mini.age, tommy.age)} years old.')
print(juji.speak('Woof'))