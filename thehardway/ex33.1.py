def while_loop(var_number, increment):
    i = 0
    numbers = []
    while i <= var_number:
        print(f"At the top i is {i}")
        numbers.append(i)
        i = i + increment

        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")

while_loop(21, 5)

