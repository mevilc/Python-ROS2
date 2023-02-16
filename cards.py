from enum import Enum

class Card:
    Suit = Enum('Suit','Hearts Clubs Diamonds Spades')
    Rank = Enum('Rank','2 3 4 5 6 7 8 9 10 J Q K A')

class Deck:
    def __init__(self):
        self.deck = [] # to add cards
	
    def add(self, Card):
    	# Adds a Card object to deck list
        self.deck.append(Card)

    def draw_from_top(self):
    	# Returns first Card object fron deck list
        return self.deck.pop(0)

    def cut(self):
    	# Cuts deck list. Bottom half comes up and vice-versa.
        sz = len(self.deck)
        top, bot = self.deck[:sz//2], self.deck[sz//2:]
        self.deck[:sz//2] = bot
        self.deck[sz//2:] = top
        return self.deck

    def shuffle(self, l1, l2):
    	# Returns a riffle shuffled card deck list
        if not l1: return l2
        elif not l2: return l1
        return l1[0:1] + self.shuffle(l2,l1[1:])

