n = int(input())

counter = 1

for row in range(1, n + 1):
    for num in range(1, row + 1):
        print(f"{counter} ", end='')
        counter += 1
        
        if counter > n:
            exit(0)
    print()