import pygame, sys, random, heapq
from pygame.locals import *
from enum import Enum

#colours
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BROWN = (153, 76, 0)
WHITE = (255, 255,255)

#tipes
HOME = 0
BIN_PLASTIC = 1
BIN_PAPER = 2
BIN_GLASS = 3
BIN_ORGANIC = 4
BIN_WASTE = 5

trash_Pos =[]
trashcounter=0

class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

BackGround = Background('background.jpg', [0,0])
textures = {
HOME : pygame.image.load('home.png'),
BIN_PLASTIC : pygame.image.load('plastic.png'),
BIN_PAPER : pygame.image.load('paper.png'),
BIN_GLASS : pygame.image.load('glass.png'),
BIN_ORGANIC : pygame.image.load('organic.png'),
BIN_WASTE : pygame.image.load('waste.png')
}
TILWSIZE =100
MAPWIDTH = 8
MAPHIGHT = 8

PLAYER = pygame.image.load('GT.png')
playerPos = [7, 7]

resourses = [HOME, BIN_PLASTIC, BIN_PAPER, BIN_GLASS, BIN_ORGANIC, BIN_WASTE]
Q_homes=0
Q_glass=0
Q_paper=0
Q_plastic=0
Q_organic=0
Q_waste=0

tilemap = [ [HOME for w in range(MAPWIDTH)] for h in range(MAPHIGHT)]
for rw in range(MAPHIGHT):
    for cl in range(MAPWIDTH):
        randomNumber = random.randint(0, 14)
        if randomNumber == 1 or randomNumber == 2:
            title = BIN_GLASS
            Q_glass +=1
        elif randomNumber == 3 or randomNumber == 4:
            title = BIN_PAPER
            Q_paper +=1
        elif randomNumber ==5 or randomNumber ==6:
            title = BIN_PLASTIC
            Q_plastic +=1
        elif randomNumber ==7 or randomNumber ==8:
            title = BIN_ORGANIC
            Q_organic +=1
        elif randomNumber ==9 or randomNumber ==10:
            title = BIN_WASTE
            Q_waste +=1
        else:
            title = HOME
            Q_homes +=1


        tilemap[rw][cl] = title

tilemap[0][0] = HOME
tilemap[7][7] = HOME

pygame.init()
pygame.display.set_caption("Garbage truck")
TILWSIZE1 = 125
DISPLAYSURF = pygame.display.set_mode((MAPWIDTH*TILWSIZE1, MAPHIGHT*TILWSIZE))
DISPLAYSURF.fill((255, 255, 255))

pygame.font.init() # you have to call this at the start,
                   # if you want to use this module.
myfont = pygame.font.SysFont('Comic Sans MS', 30)

textsurface0 = myfont.render('Quantity of', False, (0, 0, 0))
textsurface = myfont.render("HOMES: "+str(Q_homes),True,BLACK)
textsurface1 = myfont.render("GLASS: "+str(Q_glass),True,BLACK)
textsurface2 = myfont.render("PAPER: "+str(Q_paper),True,BLACK)
textsurface3 = myfont.render("PLASTIC: "+str(Q_plastic),True,BLACK)
textsurface4 = myfont.render("ORGANIC: "+str(Q_organic),True,BLACK)
textsurface5 = myfont.render("WASTE: "+str(Q_waste),True,BLACK)
textsurface7 = myfont.render("GARAGE",True,BLACK)
textsurface8 = myfont.render("LANDFILL",True,BLACK)


Q_player=0

for row in range(MAPHIGHT):
    for column in range(MAPWIDTH):
            #trash_Pos
        DISPLAYSURF.blit(textures[tilemap[row][column]], (column*TILWSIZE, row*TILWSIZE))
            #if title == BIN_GLASS or title == BIN_PAPER:
            #trash_Pos.append(row)
            #trash_Pos[column]= column
TILWSIZE2 = 10

pygame.time.delay(10)
DISPLAYSURF.blit(PLAYER, (playerPos[0]*TILWSIZE, playerPos[1]*TILWSIZE))
    #DISPLAYSURF.blit(PLAYER, (playerPos[0]*400, playerPos[1]*500))
#    print('Player Position:  ', playerPos)
print(trashcounter)

# textsurface6 = myfont.render("STEPS: "+str(len(path)),True,BLACK)
DISPLAYSURF.blit(textsurface0,(805,5))
DISPLAYSURF.blit(textsurface,(805,35))
DISPLAYSURF.blit(textsurface1,(805,65))
DISPLAYSURF.blit(textsurface2,(805,95))
DISPLAYSURF.blit(textsurface3,(805,125))
DISPLAYSURF.blit(textsurface4,(805,155))
DISPLAYSURF.blit(textsurface5,(805,185))
DISPLAYSURF.blit(textsurface7,(700,700))
DISPLAYSURF.blit(textsurface8,(0,5))

pygame.draw.rect(DISPLAYSURF, WHITE, (805, 248, 180, 42))
# DISPLAYSURF.blit(textsurface6,(805,250))

pygame.display.update()


class Action(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3

class State():
    
    def __init__(self, coordX,coordY):
        self.x = coordX
        self.y = coordY
    
    def __eq__ (self, other):
        return self.x == other.x and self.y == other.y


class Node():

    def __init__(self, parent, state, action):
        self.parent = parent
        self.state = state
        self.action = action
        self.cost = 0

    def __eq__(self,other):
        return self.state == other.state
	
    def __le__(self, other):
        return self.cost <= other.cost
    def __lt__(self,other):
        return self.cost < other.cost

def goal_test(state):
    return state == State(0,0)

#tuple of states and actions
def succ(state):
    actions = []

    if 0 < state.x <= 7:
        actions.append((State(state.x-1,state.y),Action.UP))
    if 0 <= state.x < 7:
        actions.append((State(state.x+1,state.y),Action.DOWN))
    if 0 < state.y <= 7:
        actions.append((State(state.x,state.y-1),Action.LEFT))
    if 0 <= state.y < 7:
        actions.append((State(state.x,state.y+1),Action.RIGHT))



    return actions

def f(node):
    #if there is a house it shouldn't choose that way
    #bigger cost, more expensive
    if tilemap[node.state.x][node.state.y] == HOME:
        g = node.parent.cost + 50
    #it should go through the bins
    else: g = node.parent.cost + 1

    #heuristic just the way missing till the end
    h = (node.state.x ** 2) + (node.state.y ** 2)
    f = g + h

    return f


def graphsearch(fringe, istate, explored):
	
    heapq.heappush(fringe, Node(None,istate,None))
   # fringe.append(Node(None, istate, None))

    while True:

        if len(fringe) == 0:
            return False

        #Select elem from fringe -- REVISAR 
        elem = heapq.heappop(fringe)

        if goal_test(elem.state):
            actions = []
            while elem.state != istate:
                actions.append(elem.action)
                elem = elem.parent
            return actions
			#return sequence of actions indicated by the parent and action fields of nodes

        explored.append(elem)

        #(Action, state is a tuple, succ is a list of tuples)
        for (state, action) in succ(elem.state):

            x = Node(elem, state, action)
            x.cost = f(x)
        
            existFringe = False
            existExplored = False

            for st in fringe:
                if st.state == state:
                    existFringe = True
                    y = st

            for stt in explored:
                if stt.state == state:
                    existExplored = True

            # if state is not in fringe and is not in explored
            if existFringe == False and existExplored == False:
            # insert x into fringe according to x.cost
                heapq.heappush(fringe,x)
               # fringe.append(x)
            # else if there is node y in fringe such that y.state == state
            # and y.cost > x.cost
            elif existFringe == True and existExplored == False and y.state == state and y.cost > x.cost:                
            # remove y from fringe and insert x into fringe
                fringe.remove(y)
                heapq.heappush(fringe,x)
                #fringe.append(x)

       

def main():
    fringe = []
    explored = []

    actions = graphsearch(fringe,State(7,7), explored)
    actions.reverse()


   # path = astar(maze, start, end)
    print(len(actions))
    print(actions)


    textsurface6 = myfont.render("STEPS: "+str(len(actions)),True,BLACK)
    DISPLAYSURF.blit(textsurface6,(805,250))
    
    pos = (7,7)

    for act in actions:
        if act == Action.UP:
            pos = tuple(map(lambda x,y: x-y, pos,(0,1)))
        elif act == Action.LEFT:
            pos = tuple(map(lambda x,y: x-y, pos,(1,0)))
        elif act == Action.RIGHT:
            pos = tuple(map(lambda x,y: x+y, pos,(1,0)))
        elif act == Action.DOWN:
            pos = tuple(map(lambda x,y: x+y, pos,(0,1)))
        else:
            pos = pos

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