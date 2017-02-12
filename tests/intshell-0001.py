'''

an interactive shell that relays state information.
think text-based video game. 

should ultimately tie into cards, but for now let's just 
work on back-and-forth directions.

'''

out1 = ""
out2 = ""
out3 = ""

def treat( _input ):

	commands = ['shuffle','deal','cut']

	_input = _input.split(" ")

	if _input[0] in commands:
		#bind to functions??
		out1 = "ok"

	else:
		out2 = "did not understand"

if __name__ == "__main__":

	out1 = "hello world"

	while True:
		#IO loop
		try:
			print "%s%s%s" % (out1, out2, out3)
			user_in = raw_input(">")
			treat(user_in)

		except KeyboardInterrupt:
			#save and exit
			exit()