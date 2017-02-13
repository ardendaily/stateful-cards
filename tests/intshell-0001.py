'''

an interactive shell that relays state information.
think text-based video game. 

should ultimately tie into cards, but for now let's just 
work on back-and-forth directions.


TO DO:
	further abstract the working(!!) call-and-response code,
	and add helper functions to bind keywords to functions across libraries. 



'''
import sys
global pcresponse

class ArdenShell:
	'''
	Container for IO and function binding
	'''

	bindCommands = {}
	exitText = "Bye!"
	pcresponse = ""

	def userin(self, _input):
		''' Handle user input '''
		return _input

	def die(self):
		print exitText
		exit()

	def bindCommand( comString, methString):
		''' construct table linking commands to methods in namespace '''
		pass

	def loop(self):
		''' Input loop. Call after setting everything up. '''
		while True:
			try:
				print pcresponse
				user = raw_input("> ")
				pcresponse = userin( user )
			except KeyboardInterrupt:
				# Catch 
				die()

def parseUserInput( _input ):
	commands = ["shuffle","deal","cut", "help"]
	dieC = ['exit','quit','die']

	_input = _input.lower()
	_input = _input.split(" ")

	if _input[0] in dieC:
		exit()

	if _input[0] in commands:
		index = commands.index(_input[0])
		args = _input[0:].pop()
		pcresponse = getattr(sys.modules[__name__], commands[index])(args)

	else:
		pcresponse = "did not understand. need HELP?"

	return pcresponse

def shuffle( args ):
	return "shuffle", args
	
def deal( args ):
	return "deal", args

def cut( args ):
	return "cut", args

def help( args ):
	return """

SHUFFLE 5 will bridge-shuffle the deck 5 times.
CUT 3 will cut the deck into 3 piles
DEAL 3 will deal three cards off the deck. 
DEAL 1 3 will deal one card off the third pile.

""" 

if __name__ == "__main__":

	#initialize globals
	pcresponse = "CARDS. you can SHUFFLE, CUT, or DEAL"

	while True:
		#IO loop
		try:
			print pcresponse
			user_in = raw_input(">")
			pcresponse = parseUserInput(user_in)

		except KeyboardInterrupt:
			#save and exit
			exit()