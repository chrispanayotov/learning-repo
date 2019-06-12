player_1 = input()
player_2 = input()

points_p1 = 0
points_p2 = 0
is_end_of_game = False

while True:
    card_p1 = input()
    
    if card_p1 == "End of game":
        is_end_of_game = True
        break

    card_p1 = int(card_p1)
    card_p2 = int(input())

    if card_p1 > card_p2:
        points_p1 += abs(card_p1 - card_p2)
    elif card_p2 > card_p1:
        points_p2 += abs(card_p2 - card_p1)
    else:
        print("Number wars!")
        card_p1 = int(input())
        card_p2 = int(input())

        if card_p1 > card_p2:
            print(f"{player_1} is winner with {points_p1} points")
            break
        elif card_p2 > card_p1:
            print(f"{player_2} is winner with {points_p2} points")
            break

if is_end_of_game == True:
    print(f"{player_1} has {points_p1} points")
    print(f"{player_2} has {points_p2} points")