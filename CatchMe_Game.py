import pygame, sys, random
from pygame.locals import *

WINDOWWIDTH = 800
WINDOWHEIGHT = 600
FPS = 250
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
NUMBER = random.randint(1, 4)
START = 0
A = 0
B = 0
UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'
STOP = 'stop'


def main():
    global FPSCLOCK, DISPLAYSURF, FONT
    pygame.init()
    FONT = pygame.font.Font('D:/18110168_GITHUBS/ZZZChayThu/CatchMeGame-master/verdanab.ttf', 15)
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption("Catch Coins Game")
    while True:
        gameplay_start()


def gameplay_HUMANvsAI():
    n = 1
    PLYRscore = 0
    BOTscore = 0
    move = STOP
    # startx = random.randint(0,WINDOWWIDTH)
    # starty = random.randint(0,WINDOWHEIGHT)
    midx = WINDOWWIDTH / 2
    midy = WINDOWHEIGHT / 2
    enemyCoord = getRandomLocation()  # [{'x':startx, 'y':starty}]
    playerACoord = [{'x': midx, 'y': midy}]
    botCoord = [{'x': midx, 'y': midy}]
    if NUMBER == 1:
        direction = UP
    elif NUMBER == 2:
        direction = DOWN
    elif NUMBER == 3:
        direction = LEFT
    elif NUMBER == 4:
        direction = RIGHT

    while True:
        DISPLAYSURF.fill(WHITE)
        textSurf = FONT.render('MODE : Human VS AI', True, BLACK)
        textRect = textSurf.get_rect()
        textRect.topleft = (20, 10)
        DISPLAYSURF.blit(textSurf, textRect)
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            elif event.type == KEYDOWN:
                if event.key in (K_w, K_UP):
                    move = UP
                elif event.key in (K_s, K_DOWN):
                    move = DOWN
                elif event.key in (K_a, K_LEFT):
                    move = LEFT
                elif event.key in (K_d, K_RIGHT):
                    move = RIGHT
                elif event.key == K_SPACE:
                    move = STOP
            elif event.type == KEYUP:
                pass  # move = STOP
            elif event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                if pygame.Rect(10, WINDOWHEIGHT - Y_MENU - 10, X_MENU, Y_MENU).collidepoint(mousex, mousey):
                    return
                elif pygame.Rect(WINDOWWIDTH - X_EXIT - 10, WINDOWHEIGHT - Y_EXIT - 10, X_EXIT, Y_EXIT).collidepoint(
                        mousex, mousey):
                    terminate()

        if -25 < playerACoord[A]['x'] - enemyCoord[START]['x'] < 25 and -25 < playerACoord[A]['y'] - enemyCoord[START][
            'y'] < 25:
            enemyCoord = getRandomLocation()
            # pygame.time.delay(500)
            PLYRscore += 1
        if -25 < botCoord[A]['x'] - enemyCoord[START]['x'] < 25 and -25 < botCoord[A]['y'] - enemyCoord[START][
            'y'] < 25:
            BOTscore += 1
            # pygame.time.delay(500)
            enemyCoord = getRandomLocation()

        if move == UP:
            newMOVE = {'x': playerACoord[A]['x'], 'y': playerACoord[A]['y'] - n}
        elif move == DOWN:
            newMOVE = {'x': playerACoord[A]['x'], 'y': playerACoord[A]['y'] + n}
        elif move == LEFT:
            newMOVE = {'x': playerACoord[A]['x'] - n, 'y': playerACoord[A]['y']}
        elif move == RIGHT:
            newMOVE = {'x': playerACoord[A]['x'] + n, 'y': playerACoord[A]['y']}
        elif move == STOP:
            newMOVE = {'x': playerACoord[A]['x'], 'y': playerACoord[A]['y']}

        if playerACoord[A]['x'] < 25 or playerACoord[A]['x'] > WINDOWWIDTH - 25 or playerACoord[A]['y'] < 25 or \
                playerACoord[A]['y'] > WINDOWHEIGHT - 25:
            move = STOP

        if direction == UP:
            newPLACE = {'x': enemyCoord[START]['x'] - n, 'y': enemyCoord[START]['y'] - n}
        elif direction == DOWN:
            newPLACE = {'x': enemyCoord[START]['x'] + n, 'y': enemyCoord[START]['y'] + n}
        elif direction == LEFT:
            newPLACE = {'x': enemyCoord[START]['x'] - n, 'y': enemyCoord[START]['y'] + n}
        elif direction == RIGHT:
            newPLACE = {'x': enemyCoord[START]['x'] + n, 'y': enemyCoord[START]['y'] - n}

        if ((enemyCoord[START]['x'] < 0) and (direction == UP)):
            direction = RIGHT
        elif ((enemyCoord[START]['x'] < 0) and (direction == LEFT)):
            direction = DOWN
        elif ((enemyCoord[START]['x'] > WINDOWWIDTH) and (direction == RIGHT)):
            direction = UP
        elif ((enemyCoord[START]['x'] > WINDOWWIDTH) and (direction == DOWN)):
            direction = LEFT
        elif ((enemyCoord[START]['y'] < 0) and (direction == RIGHT)):
            direction = DOWN
        elif ((enemyCoord[START]['y'] < 0) and (direction == UP)):
            direction = LEFT
        elif ((enemyCoord[START]['y'] > WINDOWHEIGHT) and (direction == DOWN)):
            direction = RIGHT
        elif (enemyCoord[START]['y'] > WINDOWHEIGHT) and (direction == LEFT):
            direction = UP
        # AI program
        if direction == UP and botCoord[START]['x'] > enemyCoord[START]['x'] and botCoord[START]['y'] > \
                enemyCoord[START]['y']:
            BOTmove = {'x': botCoord[START]['x'] - n, 'y': botCoord[START]['y']}
        elif direction == UP and botCoord[START]['x'] > enemyCoord[START]['x'] and botCoord[START]['y'] < \
                enemyCoord[START]['y']:
            BOTmove = {'x': botCoord[START]['x'], 'y': botCoord[START]['y'] + n}
        elif direction == UP and botCoord[START]['x'] < enemyCoord[START]['x'] and botCoord[START]['y'] > \
                enemyCoord[START]['y']:
            BOTmove = {'x': botCoord[START]['x'], 'y': botCoord[START]['y'] - n}
        elif direction == UP and botCoord[START]['x'] < enemyCoord[START]['x'] and botCoord[START]['y'] < \
                enemyCoord[START]['y']:
            BOTmove = {'x': botCoord[START]['x'], 'y': botCoord[START]['y'] + n}

        elif direction == DOWN and botCoord[START]['x'] > enemyCoord[START]['x'] and botCoord[START]['y'] > \
                enemyCoord[START]['y']:
            BOTmove = {'x': botCoord[START]['x'], 'y': botCoord[START]['y'] - n}
        elif direction == DOWN and botCoord[START]['x'] > enemyCoord[START]['x'] and botCoord[START]['y'] < \
                enemyCoord[START]['y']:
            BOTmove = {'x': botCoord[START]['x'], 'y': botCoord[START]['y'] + n}
        elif direction == DOWN and botCoord[START]['x'] < enemyCoord[START]['x'] and botCoord[START]['y'] > \
                enemyCoord[START]['y']:
            BOTmove = {'x': botCoord[START]['x'] + n, 'y': botCoord[START]['y']}
        elif direction == DOWN and botCoord[START]['x'] < enemyCoord[START]['x'] and botCoord[START]['y'] < \
                enemyCoord[START]['y']:
            BOTmove = {'x': botCoord[START]['x'] + n, 'y': botCoord[START]['y']}

        elif direction == LEFT and botCoord[START]['x'] > enemyCoord[START]['x'] and botCoord[START]['y'] > \
                enemyCoord[START]['y']:
            BOTmove = {'x': botCoord[START]['x'] - n, 'y': botCoord[START]['y']}
        elif direction == LEFT and botCoord[START]['x'] > enemyCoord[START]['x'] and botCoord[START]['y'] < \
                enemyCoord[START]['y']:
            BOTmove = {'x': botCoord[START]['x'] - n, 'y': botCoord[START]['y']}
        elif direction == LEFT and botCoord[START]['x'] < enemyCoord[START]['x'] and botCoord[START]['y'] > \
                enemyCoord[START]['y']:
            BOTmove = {'x': botCoord[START]['x'] + n, 'y': botCoord[START]['y']}
        elif direction == LEFT and botCoord[START]['x'] < enemyCoord[START]['x'] and botCoord[START]['y'] < \
                enemyCoord[START]['y']:
            BOTmove = {'x': botCoord[START]['x'], 'y': botCoord[START]['y'] + n}

        elif direction == RIGHT and botCoord[START]['x'] > enemyCoord[START]['x'] and botCoord[START]['y'] > \
                enemyCoord[START]['y']:
            BOTmove = {'x': botCoord[START]['x'], 'y': botCoord[START]['y'] - n}
        elif direction == RIGHT and botCoord[START]['x'] > enemyCoord[START]['x'] and botCoord[START]['y'] < \
                enemyCoord[START]['y']:
            BOTmove = {'x': botCoord[START]['x'] - n, 'y': botCoord[START]['y']}
        elif direction == RIGHT and botCoord[START]['x'] < enemyCoord[START]['x'] and botCoord[START]['y'] > \
                enemyCoord[START]['y']:
            BOTmove = {'x': botCoord[START]['x'], 'y': botCoord[START]['y'] - n}
        elif direction == RIGHT and botCoord[START]['x'] < enemyCoord[START]['x'] and botCoord[START]['y'] < \
                enemyCoord[START]['y']:
            BOTmove = {'x': botCoord[START]['x'] + n, 'y': botCoord[START]['y']}
        else:
            BOTmove = {'x': botCoord[START]['x'], 'y': botCoord[START]['y']}

        del botCoord[-1]
        del enemyCoord[-1]
        del playerACoord[-1]

        botCoord.insert(0, BOTmove)
        enemyCoord.insert(0, newPLACE)
        playerACoord.insert(0, newMOVE)
        drawplayerAScore(PLYRscore)
        drawbotScore2(BOTscore)
        drawEnemy(enemyCoord)
        drawPlayerA(playerACoord)
        drawBOT2(botCoord)
        drawMENU()
        drawexit()
        pygame.display.update()
        FPSCLOCK.tick(FPS)


def gameplay_HUMANsolo():
    n = 1
    PLYRscore = 0
    move = STOP
    midx = WINDOWWIDTH / 2
    midy = WINDOWHEIGHT / 2
    enemyCoord = getRandomLocation()  # [{'x':startx, 'y':starty}]
    playerACoord = [{'x': midx, 'y': midy}]
    if NUMBER == 1:
        direction = UP
    elif NUMBER == 2:
        direction = DOWN
    elif NUMBER == 3:
        direction = LEFT
    elif NUMBER == 4:
        direction = RIGHT

    while True:
        DISPLAYSURF.fill(WHITE)
        textSurf = FONT.render('MODE : Human solo player', True, BLACK)
        textRect = textSurf.get_rect()
        textRect.topleft = (20, 10)
        DISPLAYSURF.blit(textSurf, textRect)
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            elif event.type == KEYDOWN:
                if event.key in (K_w, K_UP):
                    move = UP
                elif event.key in (K_s, K_DOWN):
                    move = DOWN
                elif event.key in (K_a, K_LEFT):
                    move = LEFT
                elif event.key in (K_d, K_RIGHT):
                    move = RIGHT
                elif event.key == K_SPACE:
                    move = STOP
            elif event.type == KEYUP:
                pass  # move = STOP
            elif event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                if pygame.Rect(10, WINDOWHEIGHT - Y_MENU - 10, X_MENU, Y_MENU).collidepoint(mousex, mousey):
                    return
                elif pygame.Rect(WINDOWWIDTH - X_EXIT - 10, WINDOWHEIGHT - Y_EXIT - 10, X_EXIT, Y_EXIT).collidepoint(
                        mousex, mousey):
                    terminate()

        if -25 < playerACoord[A]['x'] - enemyCoord[START]['x'] < 25 and -25 < playerACoord[A]['y'] - enemyCoord[START][
            'y'] < 25:
            enemyCoord = getRandomLocation()
            PLYRscore += 1

        if move == UP:
            newMOVE = {'x': playerACoord[A]['x'], 'y': playerACoord[A]['y'] - n}
        elif move == DOWN:
            newMOVE = {'x': playerACoord[A]['x'], 'y': playerACoord[A]['y'] + n}
        elif move == LEFT:
            newMOVE = {'x': playerACoord[A]['x'] - n, 'y': playerACoord[A]['y']}
        elif move == RIGHT:
            newMOVE = {'x': playerACoord[A]['x'] + n, 'y': playerACoord[A]['y']}
        elif move == STOP:
            newMOVE = {'x': playerACoord[A]['x'], 'y': playerACoord[A]['y']}

        if playerACoord[A]['x'] < 25 or playerACoord[A]['x'] > WINDOWWIDTH - 25 or playerACoord[A]['y'] < 25 or \
                playerACoord[A]['y'] > WINDOWHEIGHT - 25:
            move = STOP

        if direction == UP:
            newPLACE = {'x': enemyCoord[START]['x'] - n, 'y': enemyCoord[START]['y'] - n}
        elif direction == DOWN:
            newPLACE = {'x': enemyCoord[START]['x'] + n, 'y': enemyCoord[START]['y'] + n}
        elif direction == LEFT:
            newPLACE = {'x': enemyCoord[START]['x'] - n, 'y': enemyCoord[START]['y'] + n}
        elif direction == RIGHT:
            newPLACE = {'x': enemyCoord[START]['x'] + n, 'y': enemyCoord[START]['y'] - n}

        if ((enemyCoord[START]['x'] < 0) and (direction == UP)):
            direction = RIGHT
        elif ((enemyCoord[START]['x'] < 0) and (direction == LEFT)):
            direction = DOWN
        elif ((enemyCoord[START]['x'] > WINDOWWIDTH) and (direction == RIGHT)):
            direction = UP
        elif ((enemyCoord[START]['x'] > WINDOWWIDTH) and (direction == DOWN)):
            direction = LEFT
        elif ((enemyCoord[START]['y'] < 0) and (direction == RIGHT)):
            direction = DOWN
        elif ((enemyCoord[START]['y'] < 0) and (direction == UP)):
            direction = LEFT
        elif ((enemyCoord[START]['y'] > WINDOWHEIGHT) and (direction == DOWN)):
            direction = RIGHT
        elif ((enemyCoord[START]['y'] > WINDOWHEIGHT) and (direction == LEFT)):
            direction = UP
        del enemyCoord[-1]
        del playerACoord[-1]

        enemyCoord.insert(0, newPLACE)
        playerACoord.insert(0, newMOVE)
        drawplayerAScore(PLYRscore)
        drawEnemy(enemyCoord)
        drawPlayerA(playerACoord)
        drawMENU()
        drawexit()
        pygame.display.update()
        FPSCLOCK.tick(FPS)


def gameplay_start():
    n = 1
    BOTscore = 0
    BOTscore2 = 0
    BOTscore3 = 0
    enemyCoord = getRandomLocation()
    botCoord = getRandomLocation()
    botCoord2 = getRandomLocation()
    botCoord3 = getRandomLocation()
    if NUMBER == 1:
        direction = UP
    elif NUMBER == 2:
        direction = DOWN
    elif NUMBER == 3:
        direction = LEFT
    elif NUMBER == 4:
        direction = RIGHT

    while True:
        DISPLAYSURF.fill(WHITE)
        textSurf = FONT.render("Catch ME! the Heaven's Ruby", True, BLACK)
        textRect = textSurf.get_rect()
        textRect.topleft = (20, 10)
        DISPLAYSURF.blit(textSurf, textRect)
        textSurf = FONT.render('version 2.01.0000', True, BLACK)
        textRect = textSurf.get_rect()
        textRect.topleft = (20, 20 + textSurf.get_height())
        DISPLAYSURF.blit(textSurf, textRect)

        if -25 < botCoord[START]['x'] - enemyCoord[START]['x'] < 25 and -25 < botCoord[START]['y'] - enemyCoord[START][
            'y'] < 25:
            BOTscore += 1
            enemyCoord = getRandomLocation()
        if -25 < botCoord2[START]['x'] - enemyCoord[START]['x'] < 25 and -25 < botCoord2[START]['y'] - \
                enemyCoord[START]['y'] < 25:
            BOTscore2 += 1
            enemyCoord = getRandomLocation()
        if -25 < botCoord3[START]['x'] - enemyCoord[START]['x'] < 25 and -25 < botCoord3[START]['y'] - \
                enemyCoord[START]['y'] < 25:
            BOTscore3 += 1
            enemyCoord = getRandomLocation()

        if direction == UP:
            newPLACE = {'x': enemyCoord[START]['x'] - n, 'y': enemyCoord[START]['y'] - n}
        elif direction == DOWN:
            newPLACE = {'x': enemyCoord[START]['x'] + n, 'y': enemyCoord[START]['y'] + n}
        elif direction == LEFT:
            newPLACE = {'x': enemyCoord[START]['x'] - n, 'y': enemyCoord[START]['y'] + n}
        elif direction == RIGHT:
            newPLACE = {'x': enemyCoord[START]['x'] + n, 'y': enemyCoord[START]['y'] - n}

        if ((enemyCoord[START]['x'] < 0) and (direction == UP)):
            direction = RIGHT
        elif ((enemyCoord[START]['x'] < 0) and (direction == LEFT)):
            direction = DOWN
        elif ((enemyCoord[START]['x'] > WINDOWWIDTH) and (direction == RIGHT)):
            direction = UP
        elif ((enemyCoord[START]['x'] > WINDOWWIDTH) and (direction == DOWN)):
            direction = LEFT
        elif ((enemyCoord[START]['y'] < 0) and (direction == RIGHT)):
            direction = DOWN
        elif ((enemyCoord[START]['y'] < 0) and (direction == UP)):
            direction = LEFT
        elif ((enemyCoord[START]['y'] > WINDOWHEIGHT) and (direction == DOWN)):
            direction = RIGHT
        elif ((enemyCoord[START]['y'] > WINDOWHEIGHT) and (direction == LEFT)):
            direction = UP
        # AI program red
        if direction == UP and botCoord[START]['x'] > enemyCoord[START]['x'] and botCoord[START]['y'] > \
                enemyCoord[START]['y']:
            BOTmove = {'x': botCoord[START]['x'] - n, 'y': botCoord[START]['y']}
        elif direction == UP and botCoord[START]['x'] > enemyCoord[START]['x'] and botCoord[START]['y'] < \
                enemyCoord[START]['y']:
            BOTmove = {'x': botCoord[START]['x'], 'y': botCoord[START]['y'] + n}
        elif direction == UP and botCoord[START]['x'] < enemyCoord[START]['x'] and botCoord[START]['y'] > \
                enemyCoord[START]['y']:
            BOTmove = {'x': botCoord[START]['x'], 'y': botCoord[START]['y'] - n}
        elif direction == UP and botCoord[START]['x'] < enemyCoord[START]['x'] and botCoord[START]['y'] < \
                enemyCoord[START]['y']:
            BOTmove = {'x': botCoord[START]['x'] + n, 'y': botCoord[START]['y']}

        elif direction == DOWN and botCoord[START]['x'] > enemyCoord[START]['x'] and botCoord[START]['y'] > \
                enemyCoord[START]['y']:
            BOTmove = {'x': botCoord[START]['x'] - n, 'y': botCoord[START]['y']}
        elif direction == DOWN and botCoord[START]['x'] > enemyCoord[START]['x'] and botCoord[START]['y'] < \
                enemyCoord[START]['y']:
            BOTmove = {'x': botCoord[START]['x'], 'y': botCoord[START]['y'] + n}
        elif direction == DOWN and botCoord[START]['x'] < enemyCoord[START]['x'] and botCoord[START]['y'] > \
                enemyCoord[START]['y']:
            BOTmove = {'x': botCoord[START]['x'] + n, 'y': botCoord[START]['y']}
        elif direction == DOWN and botCoord[START]['x'] < enemyCoord[START]['x'] and botCoord[START]['y'] < \
                enemyCoord[START]['y']:
            BOTmove = {'x': botCoord[START]['x'] + n, 'y': botCoord[START]['y']}

        elif direction == LEFT and botCoord[START]['x'] > enemyCoord[START]['x'] and botCoord[START]['y'] > \
                enemyCoord[START]['y']:
            BOTmove = {'x': botCoord[START]['x'] - n, 'y': botCoord[START]['y']}
        elif direction == LEFT and botCoord[START]['x'] > enemyCoord[START]['x'] and botCoord[START]['y'] < \
                enemyCoord[START]['y']:
            BOTmove = {'x': botCoord[START]['x'], 'y': botCoord[START]['y'] + n}
        elif direction == LEFT and botCoord[START]['x'] < enemyCoord[START]['x'] and botCoord[START]['y'] > \
                enemyCoord[START]['y']:
            BOTmove = {'x': botCoord[START]['x'] + n, 'y': botCoord[START]['y']}
        elif direction == LEFT and botCoord[START]['x'] < enemyCoord[START]['x'] and botCoord[START]['y'] < \
                enemyCoord[START]['y']:
            BOTmove = {'x': botCoord[START]['x'] + n, 'y': botCoord[START]['y']}

        elif direction == RIGHT and botCoord[START]['x'] > enemyCoord[START]['x'] and botCoord[START]['y'] > \
                enemyCoord[START]['y']:
            BOTmove = {'x': botCoord[START]['x'], 'y': botCoord[START]['y'] - n}
        elif direction == RIGHT and botCoord[START]['x'] > enemyCoord[START]['x'] and botCoord[START]['y'] < \
                enemyCoord[START]['y']:
            BOTmove = {'x': botCoord[START]['x'], 'y': botCoord[START]['y'] + n}
        elif direction == RIGHT and botCoord[START]['x'] < enemyCoord[START]['x'] and botCoord[START]['y'] > \
                enemyCoord[START]['y']:
            BOTmove = {'x': botCoord[START]['x'], 'y': botCoord[START]['y'] - n}
        elif direction == RIGHT and botCoord[START]['x'] < enemyCoord[START]['x'] and botCoord[START]['y'] < \
                enemyCoord[START]['y']:
            BOTmove = {'x': botCoord[START]['x'] + n, 'y': botCoord[START]['y']}
        else:
            BOTmove = {'x': botCoord[START]['x'], 'y': botCoord[START]['y']}

        # 2nd AI green
        if direction == UP and botCoord2[START]['x'] > enemyCoord[START]['x'] and botCoord2[START]['y'] > \
                enemyCoord[START]['y']:
            BOTmove1 = {'x': botCoord2[START]['x'] - n, 'y': botCoord2[START]['y']}
        elif direction == UP and botCoord2[START]['x'] > enemyCoord[START]['x'] and botCoord2[START]['y'] < \
                enemyCoord[START]['y']:
            BOTmove1 = {'x': botCoord2[START]['x'] - n, 'y': botCoord2[START]['y']}
        elif direction == UP and botCoord2[START]['x'] < enemyCoord[START]['x'] and botCoord2[START]['y'] > \
                enemyCoord[START]['y']:
            BOTmove1 = {'x': botCoord2[START]['x'], 'y': botCoord2[START]['y'] - n}
        elif direction == UP and botCoord2[START]['x'] < enemyCoord[START]['x'] and botCoord2[START]['y'] < \
                enemyCoord[START]['y']:
            BOTmove1 = {'x': botCoord2[START]['x'], 'y': botCoord2[START]['y'] + n}

        elif direction == DOWN and botCoord2[START]['x'] > enemyCoord[START]['x'] and botCoord2[START]['y'] > \
                enemyCoord[START]['y']:
            BOTmove1 = {'x': botCoord2[START]['x'], 'y': botCoord2[START]['y'] - n}
        elif direction == DOWN and botCoord2[START]['x'] > enemyCoord[START]['x'] and botCoord2[START]['y'] < \
                enemyCoord[START]['y']:
            BOTmove1 = {'x': botCoord2[START]['x'], 'y': botCoord2[START]['y'] + n}
        elif direction == DOWN and botCoord2[START]['x'] < enemyCoord[START]['x'] and botCoord2[START]['y'] > \
                enemyCoord[START]['y']:
            BOTmove1 = {'x': botCoord2[START]['x'], 'y': botCoord2[START]['y'] - n}
        elif direction == DOWN and botCoord2[START]['x'] < enemyCoord[START]['x'] and botCoord2[START]['y'] < \
                enemyCoord[START]['y']:
            BOTmove1 = {'x': botCoord2[START]['x'] + n, 'y': botCoord2[START]['y']}

        elif direction == LEFT and botCoord2[START]['x'] > enemyCoord[START]['x'] and botCoord2[START]['y'] > \
                enemyCoord[START]['y']:
            BOTmove1 = {'x': botCoord2[START]['x'], 'y': botCoord2[START]['y'] - n}
        elif direction == LEFT and botCoord2[START]['x'] > enemyCoord[START]['x'] and botCoord2[START]['y'] < \
                enemyCoord[START]['y']:
            BOTmove1 = {'x': botCoord2[START]['x'] - n, 'y': botCoord2[START]['y']}
        elif direction == LEFT and botCoord2[START]['x'] < enemyCoord[START]['x'] and botCoord2[START]['y'] > \
                enemyCoord[START]['y']:
            BOTmove1 = {'x': botCoord2[START]['x'] + n, 'y': botCoord2[START]['y']}
        elif direction == LEFT and botCoord2[START]['x'] < enemyCoord[START]['x'] and botCoord2[START]['y'] < \
                enemyCoord[START]['y']:
            BOTmove1 = {'x': botCoord2[START]['x'], 'y': botCoord2[START]['y'] + n}

        elif direction == RIGHT and botCoord2[START]['x'] > enemyCoord[START]['x'] and botCoord2[START]['y'] > \
                enemyCoord[START]['y']:
            BOTmove1 = {'x': botCoord2[START]['x'], 'y': botCoord2[START]['y'] - n}
        elif direction == RIGHT and botCoord2[START]['x'] > enemyCoord[START]['x'] and botCoord2[START]['y'] < \
                enemyCoord[START]['y']:
            BOTmove1 = {'x': botCoord2[START]['x'] - n, 'y': botCoord2[START]['y']}
        elif direction == RIGHT and botCoord2[START]['x'] < enemyCoord[START]['x'] and botCoord2[START]['y'] > \
                enemyCoord[START]['y']:
            BOTmove1 = {'x': botCoord2[START]['x'] + n, 'y': botCoord2[START]['y']}
        elif direction == RIGHT and botCoord2[START]['x'] < enemyCoord[START]['x'] and botCoord2[START]['y'] < \
                enemyCoord[START]['y']:
            BOTmove1 = {'x': botCoord2[START]['x'] + n, 'y': botCoord2[START]['y']}
        else:
            BOTmove1 = {'x': botCoord2[START]['x'], 'y': botCoord2[START]['y']}

        # 3rd AI blue
        if direction == UP and botCoord3[START]['x'] > enemyCoord[START]['x'] and botCoord3[START]['y'] > \
                enemyCoord[START]['y']:
            BOTmove2 = {'x': botCoord3[START]['x'] - n, 'y': botCoord3[START]['y']}
        elif direction == UP and botCoord3[START]['x'] > enemyCoord[START]['x'] and botCoord3[START]['y'] < \
                enemyCoord[START]['y']:
            BOTmove2 = {'x': botCoord3[START]['x'], 'y': botCoord3[START]['y'] + n}
        elif direction == UP and botCoord3[START]['x'] < enemyCoord[START]['x'] and botCoord3[START]['y'] > \
                enemyCoord[START]['y']:
            BOTmove2 = {'x': botCoord3[START]['x'], 'y': botCoord3[START]['y'] - n}
        elif direction == UP and botCoord3[START]['x'] < enemyCoord[START]['x'] and botCoord3[START]['y'] < \
                enemyCoord[START]['y']:
            BOTmove2 = {'x': botCoord3[START]['x'], 'y': botCoord3[START]['y'] + n}

        elif direction == DOWN and botCoord3[START]['x'] > enemyCoord[START]['x'] and botCoord3[START]['y'] > \
                enemyCoord[START]['y']:
            BOTmove2 = {'x': botCoord3[START]['x'], 'y': botCoord3[START]['y'] - n}
        elif direction == DOWN and botCoord3[START]['x'] > enemyCoord[START]['x'] and botCoord3[START]['y'] < \
                enemyCoord[START]['y']:
            BOTmove2 = {'x': botCoord3[START]['x'], 'y': botCoord3[START]['y'] + n}
        elif direction == DOWN and botCoord3[START]['x'] < enemyCoord[START]['x'] and botCoord3[START]['y'] > \
                enemyCoord[START]['y']:
            BOTmove2 = {'x': botCoord3[START]['x'] + n, 'y': botCoord3[START]['y']}
        elif direction == DOWN and botCoord3[START]['x'] < enemyCoord[START]['x'] and botCoord3[START]['y'] < \
                enemyCoord[START]['y']:
            BOTmove2 = {'x': botCoord3[START]['x'] + n, 'y': botCoord3[START]['y']}

        elif direction == LEFT and botCoord3[START]['x'] > enemyCoord[START]['x'] and botCoord3[START]['y'] > \
                enemyCoord[START]['y']:
            BOTmove2 = {'x': botCoord3[START]['x'] - n, 'y': botCoord3[START]['y']}
        elif direction == LEFT and botCoord3[START]['x'] > enemyCoord[START]['x'] and botCoord3[START]['y'] < \
                enemyCoord[START]['y']:
            BOTmove2 = {'x': botCoord3[START]['x'] - n, 'y': botCoord3[START]['y']}
        elif direction == LEFT and botCoord3[START]['x'] < enemyCoord[START]['x'] and botCoord3[START]['y'] > \
                enemyCoord[START]['y']:
            BOTmove2 = {'x': botCoord3[START]['x'] + n, 'y': botCoord3[START]['y']}
        elif direction == LEFT and botCoord3[START]['x'] < enemyCoord[START]['x'] and botCoord3[START]['y'] < \
                enemyCoord[START]['y']:
            BOTmove2 = {'x': botCoord3[START]['x'], 'y': botCoord3[START]['y'] + n}

        elif direction == RIGHT and botCoord3[START]['x'] > enemyCoord[START]['x'] and botCoord3[START]['y'] > \
                enemyCoord[START]['y']:
            BOTmove2 = {'x': botCoord3[START]['x'], 'y': botCoord3[START]['y'] - n}
        elif direction == RIGHT and botCoord3[START]['x'] > enemyCoord[START]['x'] and botCoord3[START]['y'] < \
                enemyCoord[START]['y']:
            BOTmove2 = {'x': botCoord3[START]['x'] - n, 'y': botCoord3[START]['y']}
        elif direction == RIGHT and botCoord3[START]['x'] < enemyCoord[START]['x'] and botCoord3[START]['y'] > \
                enemyCoord[START]['y']:
            BOTmove2 = {'x': botCoord3[START]['x'], 'y': botCoord3[START]['y'] - n}
        elif direction == RIGHT and botCoord3[START]['x'] < enemyCoord[START]['x'] and botCoord3[START]['y'] < \
                enemyCoord[START]['y']:
            BOTmove2 = {'x': botCoord3[START]['x'] + n, 'y': botCoord3[START]['y']}
        else:
            BOTmove2 = {'x': botCoord3[START]['x'], 'y': botCoord3[START]['y']}

        del botCoord[-1]
        del botCoord2[-1]
        del botCoord3[-1]
        del enemyCoord[-1]

        botCoord2.insert(0, BOTmove1)
        botCoord3.insert(0, BOTmove2)
        botCoord.insert(0, BOTmove)
        enemyCoord.insert(0, newPLACE)
        drawbotScore(BOTscore)
        drawbotScore2(BOTscore2)
        drawbotScore3(BOTscore3)
        drawEnemy(enemyCoord)
        drawBOT(botCoord)
        drawBOT2(botCoord2)
        drawBOT3(botCoord3)
        gameOptions()
        key()
        drawexit()
        pygame.display.update()
        FPSCLOCK.tick(FPS)


def gameplay_HUMANvsHUMAN():
    n = 1
    PLYRscore = 0
    PLYRscore2 = 0
    BOTscore = 0
    move = STOP
    move2 = STOP
    # startx = random.randint(0,WINDOWWIDTH)
    # starty = random.randint(0,WINDOWHEIGHT)
    midx = WINDOWWIDTH / 2
    midy = WINDOWHEIGHT / 2
    enemyCoord = getRandomLocation()  # [{'x':startx, 'y':starty}]
    playerACoord = [{'x': midx, 'y': midy}]
    playerBCoord = [{'x': midx, 'y': midy}]
    if NUMBER == 1:
        direction = UP
    elif NUMBER == 2:
        direction = DOWN
    elif NUMBER == 3:
        direction = LEFT
    elif NUMBER == 4:
        direction = RIGHT

    while True:
        DISPLAYSURF.fill(WHITE)
        textSurf = FONT.render('MODE : Human VS Human', True, BLACK)
        textRect = textSurf.get_rect()
        textRect.topleft = (20, 10)
        DISPLAYSURF.blit(textSurf, textRect)
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            elif event.type == KEYDOWN:
                if event.key == K_w:
                    move = UP
                elif event.key == K_s:
                    move = DOWN
                elif event.key == K_a:
                    move = LEFT
                elif event.key == K_d:
                    move = RIGHT
                elif event.key == K_UP:
                    move2 = UP
                elif event.key == K_DOWN:
                    move2 = DOWN
                elif event.key == K_LEFT:
                    move2 = LEFT
                elif event.key == K_RIGHT:
                    move2 = RIGHT
                elif event.key == K_LCTRL:
                    move = STOP
                elif event.key == K_RCTRL:
                    move2 = STOP
            elif event.type == KEYUP:
                pass  # move = STOP
            elif event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                if pygame.Rect(10, WINDOWHEIGHT - Y_MENU - 10, X_MENU, Y_MENU).collidepoint(mousex, mousey):
                    return
                elif pygame.Rect(WINDOWWIDTH - X_EXIT - 10, WINDOWHEIGHT - Y_EXIT - 10, X_EXIT, Y_EXIT).collidepoint(
                        mousex, mousey):
                    terminate()

        if -25 < playerACoord[A]['x'] - enemyCoord[START]['x'] < 25 and -25 < playerACoord[A]['y'] - enemyCoord[START][
            'y'] < 25:
            enemyCoord = getRandomLocation()
            # pygame.time.delay(500)
            PLYRscore += 1
        elif -25 < playerBCoord[B]['x'] - enemyCoord[START]['x'] < 25 and -25 < playerBCoord[B]['y'] - \
                enemyCoord[START]['y'] < 25:
            enemyCoord = getRandomLocation()
            # pygame.time.delay(500)
            PLYRscore2 += 1

        if move == UP:
            newMOVE = {'x': playerACoord[A]['x'], 'y': playerACoord[A]['y'] - n}
        elif move == DOWN:
            newMOVE = {'x': playerACoord[A]['x'], 'y': playerACoord[A]['y'] + n}
        elif move == LEFT:
            newMOVE = {'x': playerACoord[A]['x'] - n, 'y': playerACoord[A]['y']}
        elif move == RIGHT:
            newMOVE = {'x': playerACoord[A]['x'] + n, 'y': playerACoord[A]['y']}
        elif move == STOP:
            newMOVE = {'x': playerACoord[A]['x'], 'y': playerACoord[A]['y']}

        if playerACoord[A]['x'] < 25 or playerACoord[A]['x'] > WINDOWWIDTH - 25 or playerACoord[A]['y'] < 25 or \
                playerACoord[A]['y'] > WINDOWHEIGHT - 25:
            move = STOP

        if move2 == UP:
            newMOVE2 = {'x': playerBCoord[B]['x'], 'y': playerBCoord[B]['y'] - n}
        elif move2 == DOWN:
            newMOVE2 = {'x': playerBCoord[B]['x'], 'y': playerBCoord[B]['y'] + n}
        elif move2 == LEFT:
            newMOVE2 = {'x': playerBCoord[B]['x'] - n, 'y': playerBCoord[B]['y']}
        elif move2 == RIGHT:
            newMOVE2 = {'x': playerBCoord[B]['x'] + n, 'y': playerBCoord[B]['y']}
        elif move2 == STOP:
            newMOVE2 = {'x': playerBCoord[B]['x'], 'y': playerBCoord[B]['y']}

        if playerBCoord[B]['x'] < 25 or playerBCoord[B]['x'] > WINDOWWIDTH - 25 or playerBCoord[B]['y'] < 25 or \
                playerBCoord[B]['y'] > WINDOWHEIGHT - 25:
            move2 = STOP

        if direction == UP:
            newPLACE = {'x': enemyCoord[START]['x'] - n, 'y': enemyCoord[START]['y'] - n}
        elif direction == DOWN:
            newPLACE = {'x': enemyCoord[START]['x'] + n, 'y': enemyCoord[START]['y'] + n}
        elif direction == LEFT:
            newPLACE = {'x': enemyCoord[START]['x'] - n, 'y': enemyCoord[START]['y'] + n}
        elif direction == RIGHT:
            newPLACE = {'x': enemyCoord[START]['x'] + n, 'y': enemyCoord[START]['y'] - n}

        if ((enemyCoord[START]['x'] < 0) and (direction == UP)):
            direction = RIGHT
        elif ((enemyCoord[START]['x'] < 0) and (direction == LEFT)):
            direction = DOWN
        elif ((enemyCoord[START]['x'] > WINDOWWIDTH) and (direction == RIGHT)):
            direction = UP
        elif ((enemyCoord[START]['x'] > WINDOWWIDTH) and (direction == DOWN)):
            direction = LEFT
        elif ((enemyCoord[START]['y'] < 0) and (direction == RIGHT)):
            direction = DOWN
        elif ((enemyCoord[START]['y'] < 0) and (direction == UP)):
            direction = LEFT
        elif ((enemyCoord[START]['y'] > WINDOWHEIGHT) and (direction == DOWN)):
            direction = RIGHT
        elif ((enemyCoord[START]['y'] > WINDOWHEIGHT) and (direction == LEFT)):
            direction = UP

        del enemyCoord[-1]
        del playerACoord[-1]
        del playerBCoord[-1]

        enemyCoord.insert(0, newPLACE)
        playerACoord.insert(0, newMOVE)
        playerBCoord.insert(0, newMOVE2)
        drawplayerAScore(PLYRscore)
        drawplayerBScore(PLYRscore2)
        drawEnemy(enemyCoord)
        drawPlayerA(playerACoord)
        drawPlayerB(playerBCoord)
        drawMENU()
        drawexit()
        pygame.display.update()
        FPSCLOCK.tick(FPS)


def gameplay_AIvsAIvsAI():
    n = 1
    BOTscore = 0
    BOTscore2 = 0
    BOTscore3 = 0
    enemyCoord = getRandomLocation()
    botCoord = getRandomLocation()
    botCoord2 = getRandomLocation()
    botCoord3 = getRandomLocation()
    if NUMBER == 1:
        direction = UP
    elif NUMBER == 2:
        direction = DOWN
    elif NUMBER == 3:
        direction = LEFT
    elif NUMBER == 4:
        direction = RIGHT

    while True:
        DISPLAYSURF.fill(WHITE)
        textSurf = FONT.render('MODE : AI vs AI vs AI (the Movie)', True, BLACK)
        textRect = textSurf.get_rect()
        textRect.topleft = (20, 10)
        DISPLAYSURF.blit(textSurf, textRect)
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            elif event.type == KEYDOWN:
                pass
            elif event.type == KEYUP:
                pass
            elif event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                if pygame.Rect(10, WINDOWHEIGHT - Y_MENU - 10, X_MENU, Y_MENU).collidepoint(mousex, mousey):
                    return
                elif pygame.Rect(WINDOWWIDTH - X_EXIT - 10, WINDOWHEIGHT - Y_EXIT - 10, X_EXIT, Y_EXIT).collidepoint(
                        mousex, mousey):
                    terminate()

        if -25 < botCoord[START]['x'] - enemyCoord[START]['x'] < 25 and -25 < botCoord[START]['y'] - enemyCoord[START][
            'y'] < 25:
            BOTscore += 1
            enemyCoord = getRandomLocation()
        if -25 < botCoord2[START]['x'] - enemyCoord[START]['x'] < 25 and -25 < botCoord2[START]['y'] - \
                enemyCoord[START]['y'] < 25:
            BOTscore2 += 1
            enemyCoord = getRandomLocation()
        if -25 < botCoord3[START]['x'] - enemyCoord[START]['x'] < 25 and -25 < botCoord3[START]['y'] - \
                enemyCoord[START]['y'] < 25:
            BOTscore3 += 1
            enemyCoord = getRandomLocation()

        if direction == UP:
            newPLACE = {'x': enemyCoord[START]['x'] - n, 'y': enemyCoord[START]['y'] - n}
        elif direction == DOWN:
            newPLACE = {'x': enemyCoord[START]['x'] + n, 'y': enemyCoord[START]['y'] + n}
        elif direction == LEFT:
            newPLACE = {'x': enemyCoord[START]['x'] - n, 'y': enemyCoord[START]['y'] + n}
        elif direction == RIGHT:
            newPLACE = {'x': enemyCoord[START]['x'] + n, 'y': enemyCoord[START]['y'] - n}

        if ((enemyCoord[START]['x'] < 0) and (direction == UP)):
            direction = RIGHT
        elif ((enemyCoord[START]['x'] < 0) and (direction == LEFT)):
            direction = DOWN
        elif ((enemyCoord[START]['x'] > WINDOWWIDTH) and (direction == RIGHT)):
            direction = UP
        elif ((enemyCoord[START]['x'] > WINDOWWIDTH) and (direction == DOWN)):
            direction = LEFT
        elif ((enemyCoord[START]['y'] < 0) and (direction == RIGHT)):
            direction = DOWN
        elif ((enemyCoord[START]['y'] < 0) and (direction == UP)):
            direction = LEFT
        elif ((enemyCoord[START]['y'] > WINDOWHEIGHT) and (direction == DOWN)):
            direction = RIGHT
        elif ((enemyCoord[START]['y'] > WINDOWHEIGHT) and (direction == LEFT)):
            direction = UP
        # AI program red
        if direction == UP and botCoord[START]['x'] > enemyCoord[START]['x'] and botCoord[START]['y'] > \
                enemyCoord[START]['y']:
            BOTmove = {'x': botCoord[START]['x'] - n, 'y': botCoord[START]['y']}
        elif direction == UP and botCoord[START]['x'] > enemyCoord[START]['x'] and botCoord[START]['y'] < \
                enemyCoord[START]['y']:
            BOTmove = {'x': botCoord[START]['x'], 'y': botCoord[START]['y'] + n}
        elif direction == UP and botCoord[START]['x'] < enemyCoord[START]['x'] and botCoord[START]['y'] > \
                enemyCoord[START]['y']:
            BOTmove = {'x': botCoord[START]['x'], 'y': botCoord[START]['y'] - n}
        elif direction == UP and botCoord[START]['x'] < enemyCoord[START]['x'] and botCoord[START]['y'] < \
                enemyCoord[START]['y']:
            BOTmove = {'x': botCoord[START]['x'] + n, 'y': botCoord[START]['y']}

        elif direction == DOWN and botCoord[START]['x'] > enemyCoord[START]['x'] and botCoord[START]['y'] > \
                enemyCoord[START]['y']:
            BOTmove = {'x': botCoord[START]['x'] - n, 'y': botCoord[START]['y']}
        elif direction == DOWN and botCoord[START]['x'] > enemyCoord[START]['x'] and botCoord[START]['y'] < \
                enemyCoord[START]['y']:
            BOTmove = {'x': botCoord[START]['x'], 'y': botCoord[START]['y'] + n}
        elif direction == DOWN and botCoord[START]['x'] < enemyCoord[START]['x'] and botCoord[START]['y'] > \
                enemyCoord[START]['y']:
            BOTmove = {'x': botCoord[START]['x'] + n, 'y': botCoord[START]['y']}
        elif direction == DOWN and botCoord[START]['x'] < enemyCoord[START]['x'] and botCoord[START]['y'] < \
                enemyCoord[START]['y']:
            BOTmove = {'x': botCoord[START]['x'] + n, 'y': botCoord[START]['y']}

        elif direction == LEFT and botCoord[START]['x'] > enemyCoord[START]['x'] and botCoord[START]['y'] > \
                enemyCoord[START]['y']:
            BOTmove = {'x': botCoord[START]['x'] - n, 'y': botCoord[START]['y']}
        elif direction == LEFT and botCoord[START]['x'] > enemyCoord[START]['x'] and botCoord[START]['y'] < \
                enemyCoord[START]['y']:
            BOTmove = {'x': botCoord[START]['x'], 'y': botCoord[START]['y'] + n}
        elif direction == LEFT and botCoord[START]['x'] < enemyCoord[START]['x'] and botCoord[START]['y'] > \
                enemyCoord[START]['y']:
            BOTmove = {'x': botCoord[START]['x'] + n, 'y': botCoord[START]['y']}
        elif direction == LEFT and botCoord[START]['x'] < enemyCoord[START]['x'] and botCoord[START]['y'] < \
                enemyCoord[START]['y']:
            BOTmove = {'x': botCoord[START]['x'] + n, 'y': botCoord[START]['y']}

        elif direction == RIGHT and botCoord[START]['x'] > enemyCoord[START]['x'] and botCoord[START]['y'] > \
                enemyCoord[START]['y']:
            BOTmove = {'x': botCoord[START]['x'], 'y': botCoord[START]['y'] - n}
        elif direction == RIGHT and botCoord[START]['x'] > enemyCoord[START]['x'] and botCoord[START]['y'] < \
                enemyCoord[START]['y']:
            BOTmove = {'x': botCoord[START]['x'], 'y': botCoord[START]['y'] + n}
        elif direction == RIGHT and botCoord[START]['x'] < enemyCoord[START]['x'] and botCoord[START]['y'] > \
                enemyCoord[START]['y']:
            BOTmove = {'x': botCoord[START]['x'], 'y': botCoord[START]['y'] - n}
        elif direction == RIGHT and botCoord[START]['x'] < enemyCoord[START]['x'] and botCoord[START]['y'] < \
                enemyCoord[START]['y']:
            BOTmove = {'x': botCoord[START]['x'] + n, 'y': botCoord[START]['y']}
        else:
            BOTmove = {'x': botCoord[START]['x'], 'y': botCoord[START]['y']}

        # 2nd AI green
        if direction == UP and botCoord2[START]['x'] > enemyCoord[START]['x'] and botCoord2[START]['y'] > \
                enemyCoord[START]['y']:
            BOTmove1 = {'x': botCoord2[START]['x'] - n, 'y': botCoord2[START]['y']}
        elif direction == UP and botCoord2[START]['x'] > enemyCoord[START]['x'] and botCoord2[START]['y'] < \
                enemyCoord[START]['y']:
            BOTmove1 = {'x': botCoord2[START]['x'] - n, 'y': botCoord2[START]['y']}
        elif direction == UP and botCoord2[START]['x'] < enemyCoord[START]['x'] and botCoord2[START]['y'] > \
                enemyCoord[START]['y']:
            BOTmove1 = {'x': botCoord2[START]['x'], 'y': botCoord2[START]['y'] - n}
        elif direction == UP and botCoord2[START]['x'] < enemyCoord[START]['x'] and botCoord2[START]['y'] < \
                enemyCoord[START]['y']:
            BOTmove1 = {'x': botCoord2[START]['x'], 'y': botCoord2[START]['y'] + n}

        elif direction == DOWN and botCoord2[START]['x'] > enemyCoord[START]['x'] and botCoord2[START]['y'] > \
                enemyCoord[START]['y']:
            BOTmove1 = {'x': botCoord2[START]['x'], 'y': botCoord2[START]['y'] - n}
        elif direction == DOWN and botCoord2[START]['x'] > enemyCoord[START]['x'] and botCoord2[START]['y'] < \
                enemyCoord[START]['y']:
            BOTmove1 = {'x': botCoord2[START]['x'], 'y': botCoord2[START]['y'] + n}
        elif direction == DOWN and botCoord2[START]['x'] < enemyCoord[START]['x'] and botCoord2[START]['y'] > \
                enemyCoord[START]['y']:
            BOTmove1 = {'x': botCoord2[START]['x'], 'y': botCoord2[START]['y'] - n}
        elif direction == DOWN and botCoord2[START]['x'] < enemyCoord[START]['x'] and botCoord2[START]['y'] < \
                enemyCoord[START]['y']:
            BOTmove1 = {'x': botCoord2[START]['x'] + n, 'y': botCoord2[START]['y']}

        elif direction == LEFT and botCoord2[START]['x'] > enemyCoord[START]['x'] and botCoord2[START]['y'] > \
                enemyCoord[START]['y']:
            BOTmove1 = {'x': botCoord2[START]['x'], 'y': botCoord2[START]['y'] - n}
        elif direction == LEFT and botCoord2[START]['x'] > enemyCoord[START]['x'] and botCoord2[START]['y'] < \
                enemyCoord[START]['y']:
            BOTmove1 = {'x': botCoord2[START]['x'] - n, 'y': botCoord2[START]['y']}
        elif direction == LEFT and botCoord2[START]['x'] < enemyCoord[START]['x'] and botCoord2[START]['y'] > \
                enemyCoord[START]['y']:
            BOTmove1 = {'x': botCoord2[START]['x'] + n, 'y': botCoord2[START]['y']}
        elif direction == LEFT and botCoord2[START]['x'] < enemyCoord[START]['x'] and botCoord2[START]['y'] < \
                enemyCoord[START]['y']:
            BOTmove1 = {'x': botCoord2[START]['x'], 'y': botCoord2[START]['y'] + n}

        elif direction == RIGHT and botCoord2[START]['x'] > enemyCoord[START]['x'] and botCoord2[START]['y'] > \
                enemyCoord[START]['y']:
            BOTmove1 = {'x': botCoord2[START]['x'], 'y': botCoord2[START]['y'] - n}
        elif direction == RIGHT and botCoord2[START]['x'] > enemyCoord[START]['x'] and botCoord2[START]['y'] < \
                enemyCoord[START]['y']:
            BOTmove1 = {'x': botCoord2[START]['x'] - n, 'y': botCoord2[START]['y']}
        elif direction == RIGHT and botCoord2[START]['x'] < enemyCoord[START]['x'] and botCoord2[START]['y'] > \
                enemyCoord[START]['y']:
            BOTmove1 = {'x': botCoord2[START]['x'] + n, 'y': botCoord2[START]['y']}
        elif direction == RIGHT and botCoord2[START]['x'] < enemyCoord[START]['x'] and botCoord2[START]['y'] < \
                enemyCoord[START]['y']:
            BOTmove1 = {'x': botCoord2[START]['x'] + n, 'y': botCoord2[START]['y']}
        else:
            BOTmove1 = {'x': botCoord2[START]['x'], 'y': botCoord2[START]['y']}

        # 3rd AI blue
        if direction == UP and botCoord3[START]['x'] > enemyCoord[START]['x'] and botCoord3[START]['y'] > \
                enemyCoord[START]['y']:
            BOTmove2 = {'x': botCoord3[START]['x'] - n, 'y': botCoord3[START]['y']}
        elif direction == UP and botCoord3[START]['x'] > enemyCoord[START]['x'] and botCoord3[START]['y'] < \
                enemyCoord[START]['y']:
            BOTmove2 = {'x': botCoord3[START]['x'], 'y': botCoord3[START]['y'] + n}
        elif direction == UP and botCoord3[START]['x'] < enemyCoord[START]['x'] and botCoord3[START]['y'] > \
                enemyCoord[START]['y']:
            BOTmove2 = {'x': botCoord3[START]['x'], 'y': botCoord3[START]['y'] - n}
        elif direction == UP and botCoord3[START]['x'] < enemyCoord[START]['x'] and botCoord3[START]['y'] < \
                enemyCoord[START]['y']:
            BOTmove2 = {'x': botCoord3[START]['x'], 'y': botCoord3[START]['y'] + n}

        elif direction == DOWN and botCoord3[START]['x'] > enemyCoord[START]['x'] and botCoord3[START]['y'] > \
                enemyCoord[START]['y']:
            BOTmove2 = {'x': botCoord3[START]['x'], 'y': botCoord3[START]['y'] - n}
        elif direction == DOWN and botCoord3[START]['x'] > enemyCoord[START]['x'] and botCoord3[START]['y'] < \
                enemyCoord[START]['y']:
            BOTmove2 = {'x': botCoord3[START]['x'], 'y': botCoord3[START]['y'] + n}
        elif direction == DOWN and botCoord3[START]['x'] < enemyCoord[START]['x'] and botCoord3[START]['y'] > \
                enemyCoord[START]['y']:
            BOTmove2 = {'x': botCoord3[START]['x'] + n, 'y': botCoord3[START]['y']}
        elif direction == DOWN and botCoord3[START]['x'] < enemyCoord[START]['x'] and botCoord3[START]['y'] < \
                enemyCoord[START]['y']:
            BOTmove2 = {'x': botCoord3[START]['x'] + n, 'y': botCoord3[START]['y']}

        elif direction == LEFT and botCoord3[START]['x'] > enemyCoord[START]['x'] and botCoord3[START]['y'] > \
                enemyCoord[START]['y']:
            BOTmove2 = {'x': botCoord3[START]['x'] - n, 'y': botCoord3[START]['y']}
        elif direction == LEFT and botCoord3[START]['x'] > enemyCoord[START]['x'] and botCoord3[START]['y'] < \
                enemyCoord[START]['y']:
            BOTmove2 = {'x': botCoord3[START]['x'] - n, 'y': botCoord3[START]['y']}
        elif direction == LEFT and botCoord3[START]['x'] < enemyCoord[START]['x'] and botCoord3[START]['y'] > \
                enemyCoord[START]['y']:
            BOTmove2 = {'x': botCoord3[START]['x'] + n, 'y': botCoord3[START]['y']}
        elif direction == LEFT and botCoord3[START]['x'] < enemyCoord[START]['x'] and botCoord3[START]['y'] < \
                enemyCoord[START]['y']:
            BOTmove2 = {'x': botCoord3[START]['x'], 'y': botCoord3[START]['y'] + n}

        elif direction == RIGHT and botCoord3[START]['x'] > enemyCoord[START]['x'] and botCoord3[START]['y'] > \
                enemyCoord[START]['y']:
            BOTmove2 = {'x': botCoord3[START]['x'], 'y': botCoord3[START]['y'] - n}
        elif direction == RIGHT and botCoord3[START]['x'] > enemyCoord[START]['x'] and botCoord3[START]['y'] < \
                enemyCoord[START]['y']:
            BOTmove2 = {'x': botCoord3[START]['x'] - n, 'y': botCoord3[START]['y']}
        elif direction == RIGHT and botCoord3[START]['x'] < enemyCoord[START]['x'] and botCoord3[START]['y'] > \
                enemyCoord[START]['y']:
            BOTmove2 = {'x': botCoord3[START]['x'], 'y': botCoord3[START]['y'] - n}
        elif direction == RIGHT and botCoord3[START]['x'] < enemyCoord[START]['x'] and botCoord3[START]['y'] < \
                enemyCoord[START]['y']:
            BOTmove2 = {'x': botCoord3[START]['x'] + n, 'y': botCoord3[START]['y']}
        else:
            BOTmove2 = {'x': botCoord3[START]['x'], 'y': botCoord3[START]['y']}

        del botCoord[-1]
        del botCoord2[-1]
        del botCoord3[-1]
        del enemyCoord[-1]

        botCoord2.insert(0, BOTmove1)
        botCoord3.insert(0, BOTmove2)
        botCoord.insert(0, BOTmove)
        enemyCoord.insert(0, newPLACE)
        drawbotScore(BOTscore)
        drawbotScore2(BOTscore2)
        drawbotScore3(BOTscore3)
        drawEnemy(enemyCoord)
        drawBOT(botCoord)
        drawBOT2(botCoord2)
        drawBOT3(botCoord3)
        drawMENU()
        drawexit()
        pygame.display.update()
        FPSCLOCK.tick(FPS)


def gameOptions():
    global X_OPT1, Y_OPT1, X_OPT2, Y_OPT2, X_OPT3, Y_OPT3, X_OPT4, Y_OPT4, X_OPT5, Y_OPT5
    menuSurf1 = FONT.render('Select Battle!', True, BLACK)
    menuRect1 = menuSurf1.get_rect()
    menuRect1.topleft = (WINDOWWIDTH * 5 / 8 - (menuSurf1.get_width() / 4), WINDOWHEIGHT * 5 / 8)
    DISPLAYSURF.blit(menuSurf1, menuRect1)
    menuSurf2 = FONT.render('\a Human SOLO(L)', True, BLACK)
    menuRect2 = menuSurf2.get_rect()
    menuRect2.topleft = (WINDOWWIDTH * 5 / 8, WINDOWHEIGHT * 5 / 8 + menuSurf2.get_height() + 10)
    DISPLAYSURF.blit(menuSurf2, menuRect2)
    menuSurf3 = FONT.render('\a HUMAN vs AI', True, BLACK)
    menuRect3 = menuSurf3.get_rect()
    menuRect3.topleft = (WINDOWWIDTH * 5 / 8, WINDOWHEIGHT * 5 / 8 + 2 * (menuSurf3.get_height() + 10))
    DISPLAYSURF.blit(menuSurf3, menuRect3)
    menuSurf4 = FONT.render('\a HUMAN vs HUMAN', True, BLACK)
    menuRect4 = menuSurf4.get_rect()
    menuRect4.topleft = (WINDOWWIDTH * 5 / 8, WINDOWHEIGHT * 5 / 8 + 3 * (menuSurf4.get_height() + 10))
    DISPLAYSURF.blit(menuSurf4, menuRect4)
    menuSurf5 = FONT.render('\a AI vs AI vs AI (the Movie)', True, BLACK)
    menuRect5 = menuSurf5.get_rect()
    menuRect5.topleft = (WINDOWWIDTH * 5 / 8, WINDOWHEIGHT * 5 / 8 + 4 * (menuSurf5.get_height() + 10))
    DISPLAYSURF.blit(menuSurf5, menuRect5)
    X_OPT1 = menuSurf1.get_width()
    Y_OPT1 = menuSurf1.get_height()
    X_OPT2 = menuSurf2.get_width()
    Y_OPT2 = menuSurf2.get_height()
    X_OPT3 = menuSurf3.get_width()
    Y_OPT3 = menuSurf3.get_height()
    X_OPT4 = menuSurf4.get_width()
    Y_OPT4 = menuSurf4.get_height()
    X_OPT5 = menuSurf5.get_width()
    Y_OPT5 = menuSurf5.get_height()


def key():
    for event in pygame.event.get():
        if event.type == QUIT:
            terminate()
        elif event.type == KEYDOWN:
            pass
        elif event.type == KEYUP:
            pass
        elif event.type == MOUSEBUTTONUP:
            mousex, mousey = event.pos
            if pygame.Rect(WINDOWWIDTH - X_EXIT - 10, WINDOWHEIGHT - Y_EXIT - 10, X_EXIT, Y_EXIT).collidepoint(mousex,
                                                                                                               mousey):
                terminate()
            elif pygame.Rect(WINDOWWIDTH * 5 / 8, WINDOWHEIGHT * 5 / 8 + Y_OPT2 + 10, X_OPT2, Y_OPT2).collidepoint(
                    mousex, mousey):
                gameplay_HUMANsolo()
            elif pygame.Rect(WINDOWWIDTH * 5 / 8, WINDOWHEIGHT * 5 / 8 + 2 * (Y_OPT3 + 10), X_OPT3,
                             Y_OPT3).collidepoint(mousex, mousey):
                gameplay_HUMANvsAI()
            elif pygame.Rect(WINDOWWIDTH * 5 / 8, WINDOWHEIGHT * 5 / 8 + 3 * (Y_OPT4 + 10), X_OPT4,
                             Y_OPT4).collidepoint(mousex, mousey):
                gameplay_HUMANvsHUMAN()
            elif pygame.Rect(WINDOWWIDTH * 5 / 8, WINDOWHEIGHT * 5 / 8 + 4 * (Y_OPT5 + 10), X_OPT5,
                             Y_OPT5).collidepoint(mousex, mousey):
                gameplay_AIvsAIvsAI()


def drawMENU():
    global X_MENU, Y_MENU
    menuSurf = FONT.render('MAIN MENU', True, BLACK)
    X_MENU = menuSurf.get_width()
    Y_MENU = menuSurf.get_height()
    menuRect = menuSurf.get_rect()
    menuRect.topleft = (10, WINDOWHEIGHT - menuSurf.get_height() - 10)
    DISPLAYSURF.blit(menuSurf, menuRect)


def drawexit():
    global X_EXIT, Y_EXIT
    menuSurf = FONT.render('EXIT', True, BLACK)
    X_EXIT = menuSurf.get_width()
    Y_EXIT = menuSurf.get_height()
    menuRect = menuSurf.get_rect()
    menuRect.topleft = (WINDOWWIDTH - menuSurf.get_width() - 10, WINDOWHEIGHT - menuSurf.get_height() - 10)
    DISPLAYSURF.blit(menuSurf, menuRect)


def drawEnemy(EnemyCoord):
    for coord in EnemyCoord:
        x = int(coord['x'])
        y = int(coord['y'])
        ENEMY = pygame.draw.circle(DISPLAYSURF, BLACK, (x, y), 20, 0)


def drawPlayerA(PlayerCoord):
    for coord in PlayerCoord:
        x = int(coord['x'])
        y = int(coord['y'])
        PLAYER = pygame.draw.circle(DISPLAYSURF, RED, (x, y), 30, 5)


def drawPlayerB(PlayerCoord):
    for coord in PlayerCoord:
        x = int(coord['x'])
        y = int(coord['y'])
        PLAYER = pygame.draw.circle(DISPLAYSURF, (0, 0, 255), (x, y), 30, 5)


def drawBOT(PlayerCoord):
    for coord in PlayerCoord:
        x = int(coord['x'])
        y = int(coord['y'])
        PLAYER = pygame.draw.circle(DISPLAYSURF, (255, 0, 0), (x, y), 30, 5)


def drawBOT2(PlayerCoord):
    for coord in PlayerCoord:
        x = int(coord['x'])
        y = int(coord['y'])
        PLAYER = pygame.draw.circle(DISPLAYSURF, (0, 255, 0), (x, y), 30, 5)


def drawBOT3(PlayerCoord):
    for coord in PlayerCoord:
        x = int(coord['x'])
        y = int(coord['y'])
        PLAYER = pygame.draw.circle(DISPLAYSURF, BLUE, (x, y), 30, 5)


def drawplayerAScore(score):
    scoreSurf = FONT.render('RED Player = %s point' % (score), True, BLACK)
    scoreRect = scoreSurf.get_rect()
    scoreRect.topleft = (WINDOWWIDTH - scoreSurf.get_width() - 20, 10)
    DISPLAYSURF.blit(scoreSurf, scoreRect)


def drawplayerBScore(score):
    scoreSurf = FONT.render('BLUE Player = %s point' % (score), True, BLACK)
    scoreRect = scoreSurf.get_rect()
    scoreRect.topleft = (WINDOWWIDTH - scoreSurf.get_width() - 20, 20 + scoreSurf.get_height())
    DISPLAYSURF.blit(scoreSurf, scoreRect)


def drawbotScore(score):
    scoreSurf = FONT.render('REDBot = %s point' % (score), True, BLACK)
    scoreRect = scoreSurf.get_rect()
    scoreRect.topleft = (WINDOWWIDTH - scoreSurf.get_width() - 20, 10)
    DISPLAYSURF.blit(scoreSurf, scoreRect)


def drawbotScore2(score):
    scoreSurf = FONT.render('GREENBot = %s point' % (score), True, BLACK)
    scoreRect = scoreSurf.get_rect()
    scoreRect.topleft = (WINDOWWIDTH - scoreSurf.get_width() - 20, 20 + scoreSurf.get_height())
    DISPLAYSURF.blit(scoreSurf, scoreRect)


def drawbotScore3(score):
    scoreSurf = FONT.render('BLUEBot = %s point' % (score), True, BLACK)
    scoreRect = scoreSurf.get_rect()
    scoreRect.topleft = (WINDOWWIDTH - scoreSurf.get_width() - 20, 30 + 2 * (scoreSurf.get_height()))
    DISPLAYSURF.blit(scoreSurf, scoreRect)


def terminate():
    pygame.quit()
    sys.exit()


def getRandomLocation():
    return [{'x': random.randint(0, WINDOWWIDTH), 'y': random.randint(0, WINDOWHEIGHT)}]


if __name__ == '__main__':
    main()
