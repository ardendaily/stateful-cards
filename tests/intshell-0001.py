'''

baaaaarebones interactive shell with function binding

'''
import sys

class ArdenShell:
	'''
	Container for IO and function binding
	'''
	def __init__(self, _exitText="Bye!"):
		self.bindCommands = {}
		self.exitText = _exitText
		self.pcresponse = ""
		self.banner = "" #displays once at start of program
		self.eBanner = "" #displays after every interaction.


	def userin(self, _input):
		''' Handle user input '''
		_input = _input.lower()
		_input = _input.split(" ")
		if _input[0] in self.bindCommands.keys():
			if len(_input) > 1:
				return self.bindCommands[_input[0]]( _input[1:]) 
			else:
				return self.bindCommands[_input[0]]()
		else:
			return "MISUNDERSTOOD. do you require HELP"

	def die(self):
		print ""
		print ""
		print self.exitText
		exit()

	def bindCommand( self, comStrings, methString, namespace=sys.modules[__name__]):
		''' 
		construct table linking commands to 
		methods in program namespace 
		'''

		#accept either single key or list of keys
		if not isinstance( comStrings, list ):
			comStrings = [comStrings]
			
		for key in comStrings:
			methObject = getattr(namespace, methString)
			self.bindCommands[key] = methObject

	def setBanner( self, banner):
		self.banner = banner

	def loop(self):
		print ""
		print ""
		print self.banner
		print ""
		print ""

		while True:
			try:
				print self.pcresponse
				print self.eBanner
				user = raw_input("> ")
				self.pcresponse = self.userin( user )
			except KeyboardInterrupt:
				# Catch 
				self.die()


def shuffle( args=[] ):
	return "shuffle", args
	
def deal( args=[] ):
	return "deal", args

def cut( args=[] ):
	return "cut", args

def help( args=[] ):
	return """

SHUFFLE N 	bridge-shuffle the deck N times.
CUT N 		cut the deck into N piles
DEAL N 		deal N cards off the deck. 
DEAL N R 	deal N cards off the Rth pile.

""" 

if __name__ == "__main__":
	shell = ArdenShell()
	shell.setBanner("WELCOME TO CARDS.")
	shell.bindCommand(["shuffle","shuf", "s"], "shuffle")
	shell.bindCommand(["help", "halp", "h"], "help")
	shell.loop()
