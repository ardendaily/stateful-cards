'''

API for manipulating cards. Basically 
we're setting up a tidy namespace here.

'''

if __name__ == "__main__" and __package__ == None:

	'''
	Run from command line as script, awesome, 
	let's build an interactive shell. 
	'''

	import ardenshell
	shell = ardenshell.ArdenShell()

	cardfile = None
	cards = None

	if len(argv) < 2: 
		#if no card file given, assume default location
		cardfile = ".pycarddeck"
	else: 
		cardfile = argv[1]

	#load cards if file exists
	try:
		print("Loaded", cardfile)
		cards = utils.loadCardsFromFile(cardfile)
	except IOError:
		#otherwise, create file and initialize deck.
		utils.saveCardsToFile(cardfile, initCards())
		print("wrote new deck to",cardfile)

	shell.loop()