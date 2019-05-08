import time, random

dieMessage = ['You DIED! Thank goodness!', 'Good riddance.', 'My Condolences. You failed.', 'I will tell your parents that you died with honor.', 'I will tell your parents that you died for nothing.', 'Will somebody clean this up?']
surviveMessage = ['YEEEHAW! I ain\'t gon die today!', 'Thank heavens! You didn\'t get your brains blown out!', 'You have not died... YET.', 'This is getting intense.', 'Dang.', 'Maybe next time...']

while True:
    # Display the welcome message:
    print('Welcome to Russian Roulette!')
    time.sleep(2)

    while True:
        peopleCount = int(input('How many people are playing? (2-6): '))
        if 2 <= peopleCount <= 6:
            break
        # This code runs if the player entered a number not in between 2 and 6:
        print('You must have at least 2 people and at most 6 people to play!')
        time.sleep(2)

    print('Please state your friends names, one at a time')
    choosePerson = []
    for i in range(peopleCount):
        name = input(f'Person #{i + 1}: ')
        choosePerson.append(name)

    print(f'Welcome, {", ".join(choosePerson[:-1])} , and {choosePerson[-1]}!')
    choosePersonNum = random.randint(0, peopleCount - 1)

    # Play the game:
    for i in range(6):
        if i == 0:
            print('Ok! Let\'s begin!')
            time.sleep(2)
        print('It\'s ' + choosePerson[choosePersonNum] + '\'s turn')
        time.sleep(2)

        number = random.randint(0, 5 - i)
        if number == 0:
            print('BAM!')
            time.sleep(2)
            print(random.choice(dieMessage))
            time.sleep(4)
            break
        else:
            print('click.')
            time.sleep(2)
            print(random.choice(surviveMessage))
            time.sleep(4)
            choosePersonNum = (choosePersonNum + 1) % peopleCount

    print('Would you like to play again?')
    playAgain = input().upper()
    if not (playAgain in ('YES', 'Y')):
        break