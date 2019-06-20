n = int(input())

while n < 1 or n > 100:
    print("Invalid number")
    n = int(input())

print(f"The number is: {n}.")