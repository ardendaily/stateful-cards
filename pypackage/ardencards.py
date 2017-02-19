'''

TO DO:
abstract into class. 
add decks. 

'''

#Card API
from ardendeck import ArdenDeck
import pickle

class ArdenCards:

	def __init__(self, deckType="standard52"):
		#is this how you do that 
		self.deck = ArdenDeck(deckType)

	def loadCardsFromFile(self, file):
		with open(file, "r") as cardfile:
			self.deck.setDeck( 
				pickle.load(cardfile)
				)
		# return cards

	def saveCardsToFile(self, file):
		with open(file, "w") as cardfile:
			pickle.dump(self.deck.dump(), cardfile)

	def shuffle(self):
		self.deck.bridgeShuffle()

	def deal(self, num):
		for num in range(0, num):
			print self.deck.drawTopCard(num)


if __name__ == "__main__" and __package__ == None:

	'''
	Run from command line as script, awesome, 
	let's build an interactive shell. 
	'''

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