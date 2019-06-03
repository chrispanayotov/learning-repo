n_bakes = int(input())
bake_count = 0

flour, eggs, sugar = False, False, False

while bake_count < n_bakes:

    command = input()

    while command != "Bake!":
        if command == "flour":
            flour = True
        elif command == "eggs":
            eggs = True
        elif command == "sugar":
            sugar = True

        command = input()

    if command == "Bake!" and (flour == False or eggs == False or sugar == False):
        print("The batter should contain flour, eggs and sugar!")
    else:
        bake_count += 1
        print(f"Baking batch number {bake_count}...")
        flour, eggs, sugar = False, False, False