student = 0
standard = 0
kid = 0
total_tickets = 0

while True:
    movie_name = input()

    if movie_name == "Finish":
        break

    free_space = int(input())

    for space in range(1, free_space + 1):
        ticket = input()

        if ticket == "End":
            space -= 1
            break
        elif ticket == "student":
            student += 1
        elif ticket == "standard":
            standard += 1
        elif ticket == "kid":
            kid += 1

        total_tickets += 1

    vacancy = (space / free_space) * 100
    print(f"{movie_name} - {vacancy:.2f}% full.")

print(f"Total tickets: {total_tickets}")
print(f"{student / total_tickets * 100:.2f}% student tickets.")
print(f"{standard / total_tickets * 100:.2f}% standard tickets.")
print(f"{kid / total_tickets * 100:.2f}% kids tickets.")