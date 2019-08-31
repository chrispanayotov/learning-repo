command = input()

array = list(map(int, command.split()))
rounds_played = 0

while True:
    command = input().split()

    if command[0] == 'exhausted':
        print(f"I beat It for {rounds_played} rounds!")
        break

    if command[0] == 'set':
        if len(array) == len(set(array)):
            print('It is a set')
        else:
            uniques = []
            for x in array:
                if x not in uniques:
                    uniques.append(x)
            print(uniques)

    elif command[0] == 'filter':
        if command[1] == 'odd':
            odds = [num for num in array if not num % 2 == 0]
            if len(odds) > 0:
                print(odds)
        else:
        	evens = [num for num in array if num % 2 == 0]
        	if len(evens) > 0:
        		print(evens)
    
    elif command[0] == 'multiply':
        multiplied_array = [num * int(command[1]) for num in array]
        if len(multiplied_array) > 0:
            print(multiplied_array)

    elif command[0] == 'divide':
        try:
            divided_array = [num / int(command[1]) for num in array]
            print(divided_array)
        except:
            print('ZeroDivisionError caught')
    
    elif command[0] == 'slice':
        n = int(command[1])
        m = int(command[2])+1
        try:
            array[n]
            array[m]
            sliced_array = array[n:m]
            print(sliced_array)
        except:
            is_caught = True
            print('IndexError caught')
    
    elif command[0] == 'sort':
        print(sorted(array))
    elif command[0] == 'reverse':
        print(array[::-1])

    rounds_played += 1