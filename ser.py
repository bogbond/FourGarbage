def graphsearch(fringe, explored, istate, succ, goaltest, f)
	fringe.append(node(istate))
	while True
		if len(fringe) == 0:
			return False
		elem = fringe(node)
		if goal_test(elem.state)
			return sequence of actions indicated by the parent and action fields of nodes
		explored.append(elem)
		for (action, state) in succ(elem.state)
			x = new node(state)
			x.parent = elem
			x.action = action
			x.priority = f(x)
		if state is not in fringe and is not in explored
			insert x into fringe according to x.priority
		else if there is node y in fringe such that y.state == state and y.priority > x.priority
			remove y from fringe and insert x into fringe