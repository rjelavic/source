input_alphabet = ... # arbitrary collection of characters, characters of the string you observe

def generate_all_programs():
	alphabet = [chr(i) for i in xrange(127)] # all ASCII characters
	strings = ['']
	while True:
		strings += [x + c for x in strings for c in alphabet]
	return strings

def exec_until_next_output(p):
	# executes p until it outputs something
	# for each p, remembers where it stopped executing it so it can continue there next time it's called with the same p
	# if p finishes without output, output.getvalue() will return an empty string
	...

def bin_str(n):
	# returns an integer n as a binary string, e.g. 5 -> '101'
	return '{0:b}'.format(n)

def transform(s):
	# e.g. 'abcd' -> '1110100abcd'
	# since len('abcd') = 4, which is '100' in binary, len('100') = 3 # '1' * 3 + '0' + '100' + 'abcd'
	return '1' * len(bin_str(len(s))) + '0' + bin_str(len(s)) + s

def len_of_prefix_string(s):
	bin_len_s = 7 * len(s) # ASCII character can be encoded with 7 bits
	return bin_len_s + 1 + 2 * (floor(log(bin_len_s, 2)) + 1)

def solomonoff(s):
	distribution = {}
	for p in generate_all_programs():
		p_output = ''
		while True:
			try:
				with stdoutIO() as output:
					exec_until_next_output(p)
			except:
				break
			else:
				p_output += output.getvalue()
				if not s.startswith(p_output):
					break
				if len(p_output) == len(s):
					distribution[p] = 2 ** (- len_of_prefix_string(p))
					break
	return distribution

def probability(outcome, s):
	# outcome: a character in input_alphabet
	d = solomonoff(s)
	ws = {c: 0 for c in output_alphabet}
	for p, w in d.items():
		try:
			with stdoutIO() as output:
				exec_until_next_output(p)
		except:
			pass
		else:
			ws[output.getvalue()] += w
	return ws[outcome] / sum(ws.values())
