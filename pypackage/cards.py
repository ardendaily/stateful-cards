'''

TO DO:
abstract into class. 
add decks. 

'''

from sys import argv
from random import choice
import pickle

def loadCardsFromFile(file):
	with open(file, "r") as cardfile:
		cards = pickle.load(cardfile)
	return cards

def saveCardsToFile(file, cards):
	with open(file, "w") as cardfile:
		pickle.dump(cards, cardfile)

def initCards():
	deck = {}
	deck['type'] = "standard"
	deck['cards'] = []
	for number in range(0,52):
		deck['cards'].append( {} )
		deck['cards'][number]['name'] = numToCardName(number)
		deck['cards'][number]['hp'] = 100

	return deck 

def numToCardName(num):
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

def bridgeShuffle(deck):
	'''

	fold a deck onto itself 

	'''

	final_pile = []

	#halve the deck, poorly
	splitpoint = len(deck['cards']) / 2 + choice(range(-7, 7))
	subdeck_a = deck['cards'][0:splitpoint]
	subdeck_b = deck['cards'][splitpoint:]

	#drop cards from subdecks into a pile, close to one at a time
	while len(final_pile) != len(deck['cards']):
		maxcards_a = choice(range(1,5))
		for num in range(1,maxcards_a):
			if ( len(subdeck_a) >= num ): 
				final_pile.append(subdeck_a.pop(-1))

		maxcards_b = choice(range(1,5))
		for num in range(1,maxcards_b):
			if ( len(subdeck_b) >= num ):
				final_pile.append(subdeck_b.pop(-1))

	#massage data 
	newdeck = deck.copy()
	newdeck['cards'] = final_pile

	return newdeck

def cutDeckNTimes(deck, num):
	'''

	drop parts of a deck into piles 

	'''
	pass


def drawTopCard(deck):
	card = deck['cards'].pop(0)
	card['hp'] -= 0.1
	return card

def putCardIntoDeck(deck, card, location="mid"):
	if location == "top":
		deck['cards'].insert(0, card)
	elif location == "bot":
		deck['cards'].insert(-1, card)
	elif location == "mid":
		maxrange = int( len(deck['cards']) / 8 )
		offby = choice( range( -maxrange, maxrange ) )
		location = len(deck['cards']) / 2 + offby
		deck['cards'].insert(location, card)
	else:
		#location is an index
		deck['cards'].insert(location, card)

if __name__ == "__main__":
	cardfile = None
	cards = None

	if len(argv) < 2: 
		#if no card file given, assume default location
		cardfile = ".pycarddeck"
	else: 
		cardfile = argv[1]

	#load cards if file exists
	try:
		cards = loadCardsFromFile(cardfile)
		print "loaded %s" % cardfile
		print ""
		# print "shuffling."
		# cards = bridgeShuffle(cards)
		print cards
		# print "done. saving."
		# saveCardsToFile(cardfile, cards)
	except IOError:
		#otherwise, create file and initialize deck.
		saveCardsToFile(cardfile, initCards())
		print("wrote new deck to %s" % (cardfile))