# List of variables for cars
cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
# Cars not driven = the number of cars minus the number of drivers
cars_not_driven = cars - drivers
# Cars driven = the number of drivers
cars_driven = drivers
# Carpool capacity = multiply the cars driven by the space in a car
carpool_capacity = cars_driven * space_in_a_car
# Average passenger per car = passengers divided by the cars driven
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
print "Hey %s there."
