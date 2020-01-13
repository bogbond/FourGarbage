class State():
    
    def __init__(self, coordX,coordY, orientation):
        self.x = coordX
        self.y = coordY
        self.ori = orientation
    
    def __eq__ (self, other):
        return self.x == other.x and self.y == other.y


class Node():

    def __init__(self, parent, state, action):
        self.parent = parent
        self.state = state
        self.action = action
        self.priority = 0

def goal_test(state):
    if state == (0,0,WEST) or (0,0,NORTH):
        return True
    else:
        return False

def succ(state):
#Corners
    if state.x == 7 and state.y ==7:
        actions.append(State(6,7,NORTH))
        actions.append(State(7,6,WEST))
    elif state.x == 0 and state.y == 7:
        actions.append(State(1,7,SOUTH))
        actions.append(State(0,6,WEST))
    elif state.x == 7 and state.y == 0:
        actions.append(State(7,1,EAST))
        actions.append(State(0,6,NORTH))
#Borders
    elif 0 < state.x < 7 and state.y == 0:
        actions.append(State(state.x, 1, EAST))
        actions.append(State(state.x - 1, 0, NORTH))
        actions.append(State(state.x +1,0,SOUTH))
    elif 0 < state.x < 7 and state.y == 7:
        actions.append(State(state.x, 6, WEST))
        actions.append(State(state.x - 1, 7, NORTH))
        actions.append(State(state.x +1,7,SOUTH))
    elif 0 < state.y < 7 and state.x == 0:
        actions.append(State(1, state.y, SOUTH))
        actions.append(State(0, state.y - 1, WEST))
        actions.append(State(0, state.y +1,EAST))
    elif 0 < state.y < 7 and state.x == 7:
        actions.append(State(6, state.y, NORTH))
        actions.append(State(7, state.y - 1, WEST))
        actions.append(State(7, state.y +1,EAST))
#Middle
    else:
        actions.append(State(state.x+1, state.y, SOUTH)
        actions.append(State(stae.x -1, state.y, NORTH))
        actions.append(State(state.x, state.y - 1, WEST))
        actions.append(State(state.x, state.y +1,EAST))

    return actions


def graphsearch(fringe, explored, istate, succ, goaltest, f):

	fringe.append(Node(None, istate, istate))

	while True:

		if len(fringe) == 0:
			return False

		elem = fringe.pop()

		if goal_test(elem.state): 
            while elem.state != istate: 
                actions.append(elem.action)
                elem = elem.parent
            return actions
			#return sequence of actions indicated by the parent and action fields of nodes

		explored.append(elem)

        #WE don't know what state is exactly
		for (action, state) in succ(elem.state):

			x = Node(elem,state, action)
			x.priority = f(x)
        
        if x.state not in fringe and x.state not in explored
#		if state is not in fringe and is not in explored
            if x.priority > fringe(0).pripority:
                fringe.append(x)
            else:
                #order the list by priority (bigger priority at the end
		else if there is node y in fringe such that y.state == state and y.priority > x.priority
			remove y from fringe and insert x into fringe

def main():

    maze = tilemap

    actions = graphsearch(fringe, explored, State(7,7,WEST), goaltest, f)
    actions.reverse()


   # path = astar(maze, start, end)
    print(len(actions))
    print(actions)


    textsurface6 = myfont.render("STEPS: "+str(len(path)),True,BLACK)
    DISPLAYSURF.blit(textsurface6,(805,250))
    
    for pos in path:
        DISPLAYSURF.blit(PLAYER, (pos[0]*TILWSIZE, pos[1]*TILWSIZE))        
        pygame.display.update()
        pygame.time.delay(200)

    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()


if __name__ == '__main__':
    main()

