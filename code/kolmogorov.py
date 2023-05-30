import sys
from io import StringIO
import contextlib

@contextlib.contextmanager
def stdoutIO(stdout=None):
	old = sys.stdout
	if stdout is None:
		stdout = StringIO()
	sys.stdout = stdout
	yield stdout
	sys.stdout = old

def kolmogorov(s):
	alphabet = [chr(i) for i in xrange(127)] # all ASCII characters
	strings = ['']
	while True:
		strings = [x + c for x in strings for c in alphabet]
		for p in strings:
			try:
				with stdoutIO() as output:
					exec(p)
			except:
				pass
			else:
				if output.getvalue() == s:
					return len(p)
