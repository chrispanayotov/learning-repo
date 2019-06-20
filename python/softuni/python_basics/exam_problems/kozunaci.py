import sys
import math
n_kozunaci = int(input())

max_flour = -sys.maxsize-1
max_sugar = -sys.maxsize-1
total_sugar = 0
total_flour = 0

while True:
    for kozunak in range(n_kozunaci):
        sugar = int(input())
        flour = int(input())

        total_sugar += sugar
        total_flour += flour

        if sugar > max_sugar:
            max_sugar = sugar
        if flour > max_flour:
            max_flour = flour
    
    sugar_packets = math.ceil(total_sugar / 950)
    flour_packets = math.ceil(total_flour / 750)
    break

print(f"Sugar: {sugar_packets}")
print(f"Flour: {flour_packets}")
print(f"Max used flour is {max_flour} grams, max used sugar is {max_sugar} grams.")