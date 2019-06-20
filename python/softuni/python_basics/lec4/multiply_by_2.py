n = float(input())

while n != None:
    if n < 0:
        print("Negative number!")
        break
    elif n >= 0:
        y = n * 2
        print(f"Result: {y:.2f}")
        n = float(input())