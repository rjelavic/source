rule, step, i, x, successor, total, current = [0,1,1,1,0,1,1,0], 0, 0, 0, [], [], [0] * 99 + [1]
total = [current]
while step < 100:
	while i < 99:
		successor.append(rule[4*x + 2*current[i] + current[i+1]])
		i, x = i + 1, current[i]
	successor.append(rule[4*x + 2*current[i] + 0])
	total.append(successor)
	current, successor, i, x, step = successor, [], 0, 0, step + 1

i1, j1, i2, j2 = 50, 50, 100, 100 # indexical info
for i in range(i1, i2):
	for j in range(j1, j2):
		print(total[i][j],end='') # encoding
