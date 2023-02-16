from enum import Enum


class Card:
    Suit = Enum('Suit', 'Hearts Clubs Diamonds Spades')
    Rank = Enum('Rank', '2 3 4 5 6 7 8 9 10 J Q K A')


class Deck(Card):
    def __init__(self):
        self.deck = []

    def add(self, Card):
        self.deck.append(Card)

    def draw_from_top(self):
        return self.deck.pop(0)

    def cut(self):
        sz = len(self.deck)
        top, bot = self.deck[:sz//2], self.deck[sz//2:]
        self.deck[:sz//2] = bot
        self.deck[sz//2:] = top
        return self.deck

    def shuffle(self, l1, l2):
        if not l1:
            return l2
        elif not l2:
            return l1
        return l1[0:1] + self.shuffle(l2, l1[1:])


'''
if __name__ == '__main__':
    d = Deck() # creating deck

    c = Card() # creating a card
    c.Suit = 'Hearts'
    c.Rank = '2'

    e = Card()
    e.Suit = 'Clubs'
    e.Rank = '5'

    f = Card()
    f.Suit = 'Diamonds'
    f.Rank = '10'

    g = Card()
    g.Suit = 'Spades'
    g.Rank = '7'

    d.add(c)   # adding card to deck
    d.add(e)   # adding card to deck
    d.add(f)   # adding card to deck
    d.add(g)   # adding card to deck

    shuff = d.shuffle(d.deck[:len(d.deck)//2],d.deck[len(d.deck)//2:])
    print(shuff[2].Suit)
    #print(d.deck[1].Rank)
'''
