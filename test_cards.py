from cards import Card, Deck
import unittest
from copy import deepcopy

class TestDeck(unittest.TestCase):
	def test_add(self):
		# test if add(Card) increases size of deck
		d = Deck() # creating deck
		c = Card() # creating a card
		c.Suit = 'Hearts'
		c.Rank = '2'
		d.add(c)   # adding card to deck
		len1 = len(d.deck)
		
		e = Card()
		e.Suit = 'Clubs'
		e.Rank = '5'
		d.add(e)
		len2 = len(d.deck)
		
		self.assertGreater(len2, len1)
	
	def test_draw_from_top(self):
		# test if draw_from_top() decreases size of deck
		d = Deck() # creating deck
		
		c = Card() # creating a card
		c.Suit = 'Hearts'
		c.Rank = '2'
		d.add(c)   # adding card to deck
		
		e = Card()
		e.Suit = 'Clubs'
		e.Rank = '5'
		d.add(e)
		
		len1 = len(d.deck)
		
		h = d.draw_from_top()
		len2 = len(d.deck)
		
		self.assertGreater(len1, len2)
		
	def test_cut(self):
		# test if cut() retains card order of each half of deck
		d = Deck() # creating deck
		
		c = Card() # creating a card
		c.Suit = 'Hearts'
		c.Rank = '2'
		d.add(c)   # adding card to deck
		
		e = Card()
		e.Suit = 'Clubs'
		e.Rank = '5'
		d.add(e)
		
		f = Card()
		f.Suit = 'Clubs'
		f.Rank = 'J'
		d.add(f)
		
		g = Card()
		g.Suit = 'Spades'
		g.Rank = 'A'
		d.add(g)
		
		# so far: 2H, 5C, JC, AS
		ori_d = Deck()
		ori_d.deck = deepcopy(d.deck)
		
		d.cut()
		# after cut: JC, AS, 2H, 5C
	
		self.assertEqual(d.deck[0].Suit, ori_d.deck[2].Suit) and self.assertEqual(d.deck[0].Rank, ori_d.deck[2].Rank)
		self.assertEqual(d.deck[1].Suit, ori_d.deck[3].Suit) and self.assertEqual(d.deck[1].Rank, ori_d.deck[3].Rank)
		self.assertEqual(d.deck[2].Suit, ori_d.deck[0].Suit) and self.assertEqual(d.deck[2].Rank, ori_d.deck[0].Rank)
		self.assertEqual(d.deck[3].Suit, ori_d.deck[1].Suit) and self.assertEqual(d.deck[3].Rank, ori_d.deck[1].Rank)
		
	def test_shuffle(self):
		# test if shuffle() keeps top card near top and bottom card near bottom
		
		d = Deck() # creating deck
		
		c = Card() # creating a card
		c.Suit = 'Hearts'
		c.Rank = '2'
		d.add(c)   # adding card to deck
		
		e = Card()
		e.Suit = 'Clubs'
		e.Rank = '5'
		d.add(e)
		
		f = Card()
		f.Suit = 'Clubs'
		f.Rank = 'J'
		d.add(f)
		
		g = Card()
		g.Suit = 'Spades'
		g.Rank = 'A'
		d.add(g)
		
		ori_d = Deck()
		ori_d.deck = deepcopy(d.deck)
		
		shuff = d.shuffle(d.deck[:len(d.deck)//2],d.deck[len(d.deck)//2:])
		self.assertAlmostEqual(ori_d.deck.index(ori_d.deck[0]) - shuff.index(shuff[0]),0)
		self.assertAlmostEqual(ori_d.deck.index(ori_d.deck[3]) - shuff.index(shuff[3]),0)
