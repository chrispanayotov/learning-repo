def for_loop(number):
    numbers_list = []
    numbers = range(1, 10)
    for i in numbers:
        print(f"At the top i is {i}: ")
        #i = i + 1
        print(f"Numbers now: ", numbers_list)
        print(f"At the bottom i is {i}...")
        numbers_list.append(i)

for_loop(1)

