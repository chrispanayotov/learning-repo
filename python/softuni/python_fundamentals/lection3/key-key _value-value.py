# Write a program, which searches for a key and value inside of 
# several key-value pairs.
target_key = input()
target_value = input()
n = int(input())

for i in range(n):
    data = input()
    key, value = data.split(' => ')
    value = value.split(';')

    if target_key in key:
        print(f"{key}:")
        for v in value:
            for char in v:
                if target_value == char or target_value in v:
                    print(f"-{v}")
                    break