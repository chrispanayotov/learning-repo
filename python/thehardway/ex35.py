from sys import exit

def gold_room():
    print("." * 60)
    print("""
    You open the door and you see a room full of gold. 
    How much do you take?"""[1:])

    choice = input("> ")
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print("Nice, you're not greedy, you win!")
        exit(0)
    else:
        dead("You greedy bastard!")


def bear_room():
    print("." * 60)
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear?")
    bear_moved = False

    while True:
        choice = input("> ")

        if choice == "take honey" or choice == "poke bear" or choice == "hit bear" or choice == "hit" or choice == "kick" or choice == "attack":
            dead("The bear looks at you then slaps your face off.")
        elif choice == "taunt bear" or choice == "taunt" or choice == "scream" or choice == "shout" and not bear_moved:
            print("." * 60)
            print("The bear has moved from the door.")
            print("You can go through it now.")
            bear_moved = True
        elif choice == "taunt bear" or choice == "taunt" or choice == "scream" or choice == "shout" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif choice == "open door" or choice == "go to door" or choice == "go" and bear_moved:
            gold_room()
        else:
            print("I have no idea what that means.")


def cthulhu_room():
    print("." * 60)
    print("Here you see the great evil Cthulhu.")
    print("He, it, whatever, stares at you and you go insane.")
    print("Do you flee for your life or eat your head?")

    choice = input("> ")

    if choice == "flee" or choice == "run" or choice == "escape":
        print("." * 60)
        print("Unbelievably, but you flee successfuly from CTHULHU.")
        print("." * 60)
        return_beginning()
    elif choice == "head" or choice == "eat head" or choice == "eat my head":
        dead("""
        With Cthulhu's eye focused upon you, somehow you manage to eat your own head. 
        Well that was tasty!"""[1:])
    else:
        cthulhu_room()


def dead(why):
    print("." * 60)
    print(why, "Game Over!")
    print("." * 60)
    start()

def start():
    print("You are in a dark room.")
    print("There is a door to your right and left.")
    print("Which one do you take?")

    choice = input("> ")

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")

def return_beginning():
    print("You return back to the dark room.")
    print("There is a door to your right and left.")
    print("Which one do you take?")

    choice = input("> ")

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")


#play_again = "yes"
#while play_again == "yes" or play_again == "y":
    #start()
    #play_again = input("Do you want to play again?")

start()



