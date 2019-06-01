player1_eggs = int(input())
player2_eggs = int(input())

command = input()
is_end = True

while command != "End of battle":
    if command == "one":
        player2_eggs -= 1
        if player2_eggs <= 0:
            print(f"Player two is out of eggs. Player one has {player1_eggs} eggs left.")
            is_end = False
            break
    elif command == "two":
        player1_eggs -= 1
        if player1_eggs <= 0:
            print(f"Player one is out of eggs. Player two has {player2_eggs} eggs left.")
            is_end = False
            break
    
    command = input()

if is_end == True:
    print(f"Player one has {player1_eggs} eggs left.")
    print(f"Player two has {player2_eggs} eggs left.")