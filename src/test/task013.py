def p(g):
	do_transpose = False
	if len(g) > len(g[0]):
		do_transpose = True
		g = [*zip(*g)]  # transpose

	# so now find the nonzero elements
	nonzero = []  # (col, number)
	for col in range(len(g[0])):
		tmp = g[0][col] or g[-1][col]
		if tmp:
			nonzero.append((col, tmp))
	# now use those to fill in extra lines below
	g = [*zip(*g)]
	i = 0
	dif = nonzero[1][0] - nonzero[0][0]
	while i*dif + nonzero[0][0] < len(g):
		g[i*dif + nonzero[0][0]] = [nonzero[i%2][1]] * len(g[0])
		i += 1
	g = [list(r) for r in zip(*g)] 

	if do_transpose:
		g = [list(r) for r in zip(*g)]
	return g
