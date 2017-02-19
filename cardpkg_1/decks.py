'''

Decks inherit shuffling, etc., from ArdenDeck
but implement initCards() and numToCardName()
to return appropriate suits, etc.  

'''

class standard52(ArdenDeck):
	def initCards(self):
		self.deck = {}
		self.deck['type'] = utils.STANDARD52
		self.deck['cards'] = []
		for number in range(0,52):
			deck['cards'].append( {} )
			deck['cards'][number]['name'] = self.numToCardName(number)
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

class rwtarot(ArdenDeck):
	def initCards(self):
		self.deck={}
		self.deck['type'] = utils.RWTAROT 
		self.deck['cards'] = []
		for number in range(0, 78):
			deck['cards'].append( {} )
			deck['cards'][number]['name'] = self.numToCardName(number)
			deck['cards'][number]['text'] = self.numToCardText(number)
			deck['cards'][number]['hp'] = 100

		return deck

	def numToCardName(self, num):
		majArcana = [
		'The Fool','The Magician','The High Priestess',
		'The Empress', 'The Emperor', 'The Hierophant',
		'The Lovers', 'The Chariot', 'Strength', 
		'The Hermit', 'Wheel of Fortune', 'Justice',
		'The Hanged Man', 'Death', 'Temperance', 
		'The Devil', 'The Tower', 'The Star', 
		'The Moon', 'The Sun', 'Judgment',
		'The World'
		]

		minArcanaSuits = ['Wands', 'Pentacles', 'Cups', 'Swords']
		
		minArcanaVals = [
		'Ace', 'Two', 'Three', 'Four', 'Five',
		'Six', 'Seven', 'Eight', 'Nine', 'Ten',
		'Page', 'Knight', 'Queen', 'King'
		]

		if num < 23:
			return majArcana[num]
		else:
			valIndex = num % len(minArcanaVals)
			suitIndex = int(num / len(minArcanaVals) -1)
			return "%s of %s" % ( minArcanaVals[valIndex], minArcanaSuits[suitIndex] )

		def numToCardText(self, num):
			'''
			Ultimately I'll write card descriptions here. 
			But not today.
			'''
			return None