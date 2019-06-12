# This is a Guess the Number game
import random

guessesTaken = 0
guessesLeft = 6 

print("Hello! What is your name?")
playerName = input()

number = random.randint(1, 50)
print("Well, " + playerName + ", I am thinking of a number between 1 and 50.")
print(f"Can you guess it in {guessesLeft} tries?")

for guessesTaken in range(6):
    guess = input('> ')
    guess = int(guess)
    
    if guess < number:
        print("Your guess is too low.")
    
    if guess > number:
        print("Your guess is too high.")

    guessesLeft -= 1
    print(f"You have {guessesLeft} guesses left.")

    if guess == number:
        break

if guess == number:
    guessesTaken = str(guessesTaken + 1)
    print("Good job, " + playerName + "! You guessed my number in " + 
            guessesTaken + " guesses!")

if guess != number:
    number = str(number)
    print("The number I was thinking of was " + number + '.')
