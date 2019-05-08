screening_type = input().lower()
rows = int(input())
columns = int(input())

cinema_hall = rows * columns
result = None

if screening_type == "premiere":
    result = cinema_hall * 12.00
elif screening_type == "normal":
    result = cinema_hall * 7.50
elif screening_type == "discount":
    result = cinema_hall * 5.00

print(f"{result:.2f} leva")