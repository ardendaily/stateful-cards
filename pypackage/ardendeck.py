'''

TO DO:
abstract into class. 
add decks. 

'''

from sys import argv
from random import choice
import pickle

class ArdenDeck:

	def __init__(self, deckType):
		self.deck = {}

	def setDeck(self, deck):
		self.deck = deck

	def initCards(self):
		self.deck = {}
		self.deck['type'] = "standard"
		self.deck['cards'] = []
		for number in range(0,52):
			deck['cards'].append( {} )
			deck['cards'][number]['name'] = numToCardName(number)
			deck['cards'][number]['hp'] = 100

		return deck 

	def numToCardName(self, num):
		values = ['ace', 'two', 'three', 'four', 'five', 
		'six', 'seven', 'eight', 'nine', 'ten', 
		'jack', 'queen', 'king']

		suits = ['spades','clubs','hearts','diamonds']

		if num < 52:
			valIndex = num % len(values)
			suitIndex = int(num / len(values) - 1)

			return "%s of %s" % ( values[valIndex], suits[suitIndex] )
		else:
			return "joker"

	def bridgeShuffle(self):
		'''

		fold a deck onto itself 

		'''

		final_pile = []

		#halve the deck, poorly
		splitpoint = len(self.deck['cards']) / 2 + choice(range(-7, 7))
		subdeck_a = self.deck['cards'][0:splitpoint]
		subdeck_b = self.deck['cards'][splitpoint:]

		#drop cards from subdecks into a pile, close to one at a time
		while len(final_pile) != len(self.deck['cards']):
			maxcards_a = choice(range(1,3))
			for num in range(1,maxcards_a):
				if ( len(subdeck_a) >= num ): 
					final_pile.append(subdeck_a.pop(-1))

			maxcards_b = choice(range(1,3))
			for num in range(1,maxcards_b):
				if ( len(subdeck_b) >= num ):
					final_pile.append(subdeck_b.pop(-1))

		#massage data 
		newdeck = self.deck.copy()
		newdeck['cards'] = final_pile

		self.deck = newdeck

	def drawTopCard(self):
		card = self.deck['cards'].pop(0)
		card['hp'] -= 0.1
		return card

	def putCardIntoDeck(self, card, location="mid"):
		if location == "top":
			self.deck['cards'].insert(0, card)
		elif location == "bot":
			self.deck['cards'].insert(-1, card)
		elif location == "mid":
			maxrange = int( len(self.deck['cards']) / 8 )
			offby = choice( range( -maxrange, maxrange ) )
			location = len(deck['cards']) / 2 + offby
			self.deck['cards'].insert(location, card)
		else:
			#location is an index
			self.deck['cards'].insert(location, card)