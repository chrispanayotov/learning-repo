# Your goal in this exercise is to implement two classes, Card  and Deck .
from random import shuffle

class Card:
    """Class creates an unique card with a corresponding suit and value."""
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
    

    def __repr__(self):
        return f"{self.value} {self.suit}"


class Deck:
    """Class creates a deck with 52 unique cards. Has an integrated shuffle method 
    that utilizes pseudo-randomization with the random.shuffle function.
    Can also deal a single card or a hand with size n"""

    def __init__(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        self.cards = [Card(value, suit) for value in values for suit in suits]


    def __repr__(self):
        return f"Deck of {self.count()} cards"


    def count(self):
        return len(self.cards)
    

    def _deal(self, num):
        count = self.count()
        # Checks if the deck is empty or if user is trying to deal more cards
        # than whats left in the deck. If that is the case - raise ValueError
        if count == 0 or num > count:
            raise ValueError("All cards have been dealt")
        cards_to_deal = min([count, num])
        delt_cards = []
        for i in range(cards_to_deal):
            current_card = self.cards.pop()
            delt_cards.append(current_card)
        return delt_cards
    
    
    def deal_card(self):
        return self._deal(1)[0]


    def deal_hand(self, cards_to_deal):
        return self._deal(cards_to_deal)


    def shuffle(self):
        # Returns a list of pseudo-random shuffled deck
        if self.count() < 52:
            raise ValueError("Only full decks can be shuffled")
        return shuffle(self.cards)