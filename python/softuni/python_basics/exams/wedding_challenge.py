import sys
male_clients = int(input())
female_clients = int(input())
max_tables = int(input())

current_table = 0

while True:
    for male_n in range(1, male_clients + 1):
        for female_n in range(1, female_clients + 1):
            print(f"({male_n} <-> {female_n})", end=' ')
            current_table += 1
            if current_table >= max_tables:
                sys.exit()
    break