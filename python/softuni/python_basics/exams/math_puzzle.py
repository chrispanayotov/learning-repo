key = int(input())

no_combinaitons = True

for num1 in range(1, 30 + 1):
    for num2 in range(1, 30 + 1):
        for num3 in range(1, 30 + 1):
            result_add =  num1 + num2 + num3
            result_mul = num1 * num2 * num3
            if num1 < num2 < num3 and result_add == key:
                print(f"{num1} + {num2} + {num3} = {key}")
                no_combinaitons = False
            if num1 > num2 > num3 and result_mul == key:
                print(f"{num1} * {num2} * {num3} = {key}")
                no_combinaitons = False

if no_combinaitons == True:
    print("No!")