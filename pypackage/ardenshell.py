'''

baaaaarebones interactive shell with function binding

'''
import sys

class ArdenShell:
	'''
	Container for IO and function binding
	'''
	def __init__(self):
		self.bindCommands = {}
		self.exitText = "Bye!"
		self.pcresponse = ""
		self.err = "Command not found."
		self.banner = "Welcome" #displays once at start of program
		self.eBanner = "" #displays after every interaction.
		self.reticule = "> " #beckon input

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

	def setErrorText( self, _errtext):
		self.err = _errtext

	def setExitText( self, _exittext):
		self.exitText = _exittext

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
				user = raw_input(self.reticule)
				self.pcresponse = self.userin( user )
			except KeyboardInterrupt:
				# Catch 
				self.die()