command = input()

prime = 0
non_prime = 0

while command != "stop":

    command = int(command)

    if command < 0:
        print("Number is negative.")
        command = input()
        continue

    counter = 0

    for i in range(1, command+1):
        if command % i == 0:
            counter += 1
    
    if counter == 2:
        prime += command
    else:
        non_prime += command

    command = input()

print(f"Sum of all prime numbers is: {prime}")
print(f"Sum of all non prime numbers is: {non_prime}")

# Other solution
# for j in range(2, number // 2 + 1):
#   if number % j == 0:
#       is_prime = False