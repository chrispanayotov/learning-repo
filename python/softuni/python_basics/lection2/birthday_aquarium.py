# Make a program that calculates the volume of an aquarium 
# with and without the items that are in it

length = int(input())
width = int(input())
height = int(input())
percentage_occupied = float(input()) / 100

volume = length * width * height
litres_decimeter = volume * 0.001
volume_litres = litres_decimeter * (1 - percentage_occupied)

print(f"{volume_litres:.3f}")