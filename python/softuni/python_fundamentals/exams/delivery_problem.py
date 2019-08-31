from math import pi

truck_width = float(input())
truck_depth = float(input())
truck_height = float(input())

truck_volume = truck_width * truck_depth * truck_height

n = int(input()) # Number of barrels

barrels_on_board = 0

for barrel in range(n):
	barrel_radius = float(input())
	barrel_height = float(input())

	current_barrel_volume = (barrel_radius ** 2) * barrel_height * pi

	truck_volume -= current_barrel_volume

	if truck_volume >= 0:
		barrels_on_board += 1
	else:
		print(f"Truck is full. {barrels_on_board} on board!")
		break


if barrels_on_board == n:
	print(f"All barrels on board. Capacity left - {truck_volume:.2f}.")