'''

Internal datahandling functions.
Load cards, save cards, etc.

'''

def loadCardsFromFile(self, file):
	with open(file, "r") as cardfile:
		self.deck.setDeck( 
			pickle.load(cardfile)
			)
	# return cards

def saveCardsToFile(self, file):
	with open(file, "w") as cardfile:
		pickle.dump(self.deck.dump(), cardfile)