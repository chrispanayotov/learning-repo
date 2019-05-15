w = int(input())
l = int(input())

cake_size = w * l
result = 0

while cake_size >= result:
    cake_piece = input()
    if cake_piece == "STOP":
        break
    
    result += int(cake_piece)

if result >= cake_size:
    print(f"No more cake left! You need {abs(cake_size - result)} pieces more.")
else:
    print(f"{abs(cake_size - result)} pieces are left.")