def exec_one_instruction(p):
	# executes p for just one instruction forward 
	# remembers where it stopped using a hashmap so it can continue from there next time
	...

outputs = {} # partial outputs of all programs we ran so far

def kolmogorov(s, n):
    # the string s has a null character at the end of it, which denotes the end of the string, and the program p outputs the null character when it stops
	alphabet = [chr(i) for i in xrange(127)] # all ASCII characters
	strings = ['']
	while n:
		strings += [x + c for x in strings for c in alphabet]
		for p in strings:
			try:
				with stdoutIO() as output:
					exec_one_instruction(p)
			except:
				pass
			else:
				if p in outputs:
					outputs[p] += output.getvalue()
				else:
					outputs[p] = output.getvalue()
				if outputs[p] == s:
					return len(p)
		n -= 1
