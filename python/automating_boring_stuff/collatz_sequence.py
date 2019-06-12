def collatz(number):
    if number % 2 == 0:
        return number // 2
    elif number % 2 != 0:
        return 3 * number + 1

while True:
    try:
        usr_input = int(input("Please enter a number bigger than 1: "))
        if usr_input <= 1:
            print("Number must be > 1!")
            continue
        else:
            break
    except ValueError:
        print("Please enter a valid number!")

while usr_input != 1:
    usr_input = collatz(usr_input)
    print(usr_input)