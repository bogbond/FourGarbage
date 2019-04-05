import pygame, sys, random
from pygame.locals import *

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
playerPos = [8, 7]

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
        if title ==BIN_GLASS:
            trash_Pos.append(rw)
            trash_Pos.append(cl)
            #trash_Pos.remove(1)
        #print('hello')
pygame.init()
pygame.display.set_caption("Garbage truck")
TILWSIZE1 = 125
DISPLAYSURF = pygame.display.set_mode((MAPWIDTH*TILWSIZE1, MAPHIGHT*TILWSIZE))
DISPLAYSURF.fill((255, 255, 255))

#scr = pygame.display.set_mode((MAPWIDTH*TILWSIZE, MAPHIGHT*TILWSIZE))
#scr.fill((255, 255, 255))

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

while True:
#    scr.blit(BackGround.image, BackGround.rect)
    DISPLAYSURF.blit(BackGround.image, BackGround.rect)
    pygame.draw.rect(DISPLAYSURF, (GREEN), (800, 700, 100, 100))
    pygame.draw.rect(DISPLAYSURF, (BROWN), (800, 400, 100, 100))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


        elif event.type == KEYDOWN:
            if event.key == K_RIGHT and (playerPos[0] < MAPWIDTH - 1 or (playerPos[0]==7 and playerPos[1]==4)):
                playerPos[0] +=1
                Q_player +=1
            if event.key == K_LEFT and playerPos[0] > 0:
                playerPos[0] -=1
                Q_player +=1
            if event.key == K_UP and playerPos[1] > 0 and playerPos[0] < MAPWIDTH:
                playerPos[1] -=1
                Q_player +=1
            if event.key == K_DOWN and playerPos[1] < MAPHIGHT - 1 and playerPos[0] < MAPWIDTH:
                playerPos[1] +=1
                Q_player +=1

    for row in range(MAPHIGHT):
        for column in range(MAPWIDTH):
            #trash_Pos
            DISPLAYSURF.blit(textures[tilemap[row][column]], (column*TILWSIZE, row*TILWSIZE))
            #if title == BIN_GLASS or title == BIN_PAPER:
            #trash_Pos.append(row)
            #trash_Pos[column]= column
    TILWSIZE2 = 10
    #print(trash_Pos)
    for p in range(0, len(trash_Pos)-1):
        if(playerPos[0]==trash_Pos[p] and playerPos[1]==trash_Pos[p+1]):
            trashcounter +=1
            print(playerPos[0], playerPos[1], trash_Pos[p], trash_Pos[p+1])
            print(trash_Pos)

    pygame.time.delay(10)
    DISPLAYSURF.blit(PLAYER, (playerPos[0]*TILWSIZE, playerPos[1]*TILWSIZE))
    #DISPLAYSURF.blit(PLAYER, (playerPos[0]*400, playerPos[1]*500))
#    print('Player Position:  ', playerPos)
    print(trashcounter)

    textsurface6 = myfont.render("STEPS: "+str(Q_player),True,BLACK)
    DISPLAYSURF.blit(textsurface0,(805,5))
    DISPLAYSURF.blit(textsurface,(805,35))
    DISPLAYSURF.blit(textsurface1,(805,65))
    DISPLAYSURF.blit(textsurface2,(805,95))
    DISPLAYSURF.blit(textsurface3,(805,125))
    DISPLAYSURF.blit(textsurface4,(805,155))
    DISPLAYSURF.blit(textsurface5,(805,185))
    DISPLAYSURF.blit(textsurface7,(800,650))
    DISPLAYSURF.blit(textsurface8,(800,350))

    pygame.draw.rect(DISPLAYSURF, WHITE, (805, 248, 180, 42))
    DISPLAYSURF.blit(textsurface6,(805,250))

    pygame.display.update()
