# # Find 10 examples of things in the real world that would fit in a list.
# Try writing some scripts to work with them.

# A classic deck of cards consists of 52 cards.
# It can be divided into 4 categories by suit (Spades, Hearts, Diamonds and Clubs)

spades = ["2", "3", "4", "5", "6", "7", "8", "9", "10",
         "Jack", "Queen", "King", "Ace"]
hearts = ["2", "3", "4", "5", "6", "7", "8", "9", "10",
          "Jack", "Queen", "King", "Ace"]
diamonds = ["2", "3", "4", "5", "6", "7", "8", "9", "10",
            "Jack", "Queen", "King", "Ace"]
clubs = ["2", "3", "4", "5", "6", "7", "8", "9", "10",
         "Jack", "Queen", "King", "Ace"]

print("The number of spades in a deck of cards are: {}".format(len(spades)))

print("The number of all cards in a deck is: {}".format(len(
        spades + hearts + diamonds + clubs)))

# It can also be divided into 13 categories by number (from 2 to Ace)

twos = ["Spades", "Hearts", "Diamonds", "Clubs"]
threes = ["Spades", "Hearts", "Diamonds", "Clubs"]
fours = ["Spades", "Hearts", "Diamonds", "Clubs"]
fives = ["Spades", "Hearts", "Diamonds", "Clubs"]
sixes = ["Spades", "Hearts", "Diamonds", "Clubs"]
sevens = ["Spades", "Hearts", "Diamonds", "Clubs"]
eights = ["Spades", "Hearts", "Diamonds", "Clubs"]
nines = ["Spades", "Hearts", "Diamonds", "Clubs"]
tens = ["Spades", "Hearts", "Diamonds", "Clubs"]
jacks = ["Spades", "Hearts", "Diamonds", "Clubs"]
queens = ["Spades", "Hearts", "Diamonds", "Clubs"]
kings = ["Spades", "Hearts", "Diamonds", "Clubs"]
aces = ["Spades", "Hearts", "Diamonds", "Clubs"]
print("The total number of cards in a standard deck is: {}".
        format(len(twos +  threes + fours + fives + sixes + sevens + eights + 
        nines + tens + jacks + queens + kings + aces)))
