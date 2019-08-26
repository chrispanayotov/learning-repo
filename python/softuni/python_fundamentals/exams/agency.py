from abc import ABC, abstractmethod

class Apartment(ABC):
	def __init__(self, id_, rooms, baths, sq_m, price):
		self.id_ = id_
		self.rooms = int(rooms)
		self.baths = int(baths)
		self.sq_m = float(sq_m)
		self.price = float(price)
		self.is_taken = False

	@abstractmethod
	def __str__(self):
		return f"{self.rooms} rooms place with {self.baths} bathroom/s.\n{self.sq_m} sq. meters for {self.price} lv."


class LivingApartment(Apartment):
	def __init__(self, id_, rooms, baths, sq_m, price):
		super().__init__(id_, rooms, baths, sq_m, price)


	def __str__(self):
		return Apartment.__str__(self)


class OfficeApartment(Apartment):
	def __init__(self, id_, rooms, baths, sq_m, price):
		super().__init__(id_, rooms, baths, sq_m, price)


	def __str__(self):
		return Apartment.__str__(self)


data = input()
apartments_list = []

while not data == 'start_selling':
	try:
		current_apartment = eval(data)
		apartments_list.append(current_apartment)
	except Exception as a:
		print(a)

	data = input()

data_list = input().split()
ids_list = list(map(lambda a: a.id_, apartments_list))


while not (data_list[0] == 'free' or data_list[0] == 'taken'):
	command = data_list[0]
	id_ = data_list[1]

	if id_ in ids_list:
		current_apartment = list(filter(lambda a: a.id_ == id_, apartments_list))[0]
		if current_apartment.is_taken:
			print(f"Apartment with id - {id_} is already taken!")
		elif command == 'rent' and isinstance(current_apartment, LivingApartment):
			print(f"Apartment with id - {id_} is only for selling!")
		elif command == 'buy' and isinstance(current_apartment, OfficeApartment):
			print(f"Apartment with id - {id_} is only for renting!")
		else:
			current_apartment.is_taken = True
	else:
		print(f"Apartment with id - {id_} does not exist!")

	data_list = input().split()


if data_list[0] == 'taken':
	taken_aparts = list(filter(lambda a: a.is_taken == True, apartments_list))
	for apartment in sorted(taken_aparts, key=lambda a: (a.price, -a.sq_m)):
		print(apartment)

if data_list[0] == 'free':
	taken_aparts = list(filter(lambda a: a.is_taken == False, apartments_list))
	for apartment in sorted(taken_aparts, key=lambda a: (-a.price, a.sq_m)):
		print(apartment)

if len(taken_aparts) == 0:
	print("No information for this query")
