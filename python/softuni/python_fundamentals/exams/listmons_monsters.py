from abc import ABC, abstractmethod

class BaseMonster(ABC):
    @abstractmethod
    def __init__(self, name, id_, strength, ugliness):
        self.name = name
        self.id_ = int(id_)
        self.strength = int(strength)
        self.ugliness = int(ugliness)


    def __str__(self):
        pass

class Hydralisk(BaseMonster):

    hydralisks_spawned = 0
    
    def __init__(self, name, id_, strength, ugliness, range):
        super().__init__(name, id_, strength, ugliness)
        self.range = range

    def __str__(self):
        return BaseMonster.__str__(self)

    
    @property   
    def range(self):
        return self.__range
    
    @range.setter
    def range(self, value):
        if isinstance(value, str):
            Hydralisk.hydralisks_spawned += 1
            self.__range = value
        else:
            raise Exception('Range must be string')
    

class Zergling(BaseMonster):

    zerglings_spawned = 0

    def __init__(self, name, id_, strength, ugliness, speed):
        super().__init__(name, id_, strength, ugliness)
        self.speed = speed

    def __str__(self):
        return BaseMonster.__str__(self)
        
    @property
    def speed(self):
        return self.__speed
    
    @speed.setter
    def speed(self, value):
        if isinstance(value, int):
            Zergling.zerglings_spawned += 1
            self.__speed = int(value)
        else:
            raise Exception('Speed must be integer')


data = input()
monsters_list = []

while not data == 'stopAddingArmy':
    try:
        current_monster = eval(data)
        monsters_list.append(current_monster)
    except Exception as x:
        print(x)

    data = input()

zerg_speed = 0
army_strength = 0

for monster in monsters_list:
    if isinstance(monster, Zergling):
        zerg_speed += monster.speed
    army_strength += monster.strength

print(f"Overall speed of army: {zerg_speed}")
print(f"Overall stength: {army_strength}")
print(f"Hydralisk: {Hydralisk.hydralisks_spawned}; Zergling: {Zergling.zerglings_spawned}")