import pygame
from pygame.locals import *
import random
#Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 155, 0)
RED = (155, 0, 0)
PURPLE = (100, 0, 100)
RED2 = (200, 50, 50)
PINK = (250, 150, 150)
BUTTONBLUE = (0, 58, 254)

pygame.init()

screen = pygame.display.set_mode([1920, 1050])
pygame.display.set_caption('Country Simulator')

button_positionsx = [635, 955, 1275, 1595, 635, 955, 1275, 1595]
button_positionsy = [50, 50, 50, 50, 600, 600, 600, 600]
button_positionsw = [290, 290, 290, 290, 290, 290, 290, 290]
button_positionsh = [400, 400, 400, 400, 400, 400, 400, 400]
button_colors = [BUTTONBLUE, GREEN, RED, PURPLE, PURPLE, RED, GREEN, BUTTONBLUE]
button_colsOG = [BUTTONBLUE, GREEN, RED, PURPLE, PURPLE, RED, GREEN, BUTTONBLUE]
button_text = ['Save', 'Save', 'Save', 'Save', 'Save', 'Save', 'Save', 'Save']

###############
'Functions'
###############


def enter_number(variable):
    global numkeydone
    global numberused
    numberused = ""
    numberkeycolors = [WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE]
    number_positionsx = [100, 100, 100, 300, 300, 300, 300, 500, 500, 500, 500]
    number_positionsy = [100, 300, 500, 100, 300, 500, 700, 100, 300, 500, 700]
    number_positionsw = [175, 175, 175, 175, 175, 175, 175, 175, 175, 175, 175]
    number_positionsh = [175, 175, 175, 175, 175, 175, 175, 175, 175, 175, 175]
    numkeydone = False
    pygame.draw.rect(screen, (100,100,100), (0,0,800,800))
    #load number grid
    while not numkeydone:
        pygame.event.get()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               done = True
               numkeydone = True
        get_pos = pygame.mouse.get_pos()
        for i in range(len(number_positionsx)):
            numberkeycolors[i] = WHITE
            mousesx, mousesy = get_pos
            if (mousesx > (number_positionsx[i]) and  (mousesy > number_positionsy[i]) and (mousesx < (number_positionsx[i] + number_positionsw[i])) and (mousesy < number_positionsy[i] + number_positionsh[i])):
                numberkeycolors[i] = BLACK
        pygame.display.update()
        for i in range(len(number_positionsx)):
            if (numberkeycolors[i] == BLACK) and (pygame.mouse.get_pressed() == (True, False, False)):
                runnums(i)
        #Display the Buttons
        for i in range(len(number_positionsx)):
            pygame.draw.rect(screen, numberkeycolors[i], (number_positionsx[i], number_positionsy[i], number_positionsw[i], number_positionsh[i]))
        dispnum()
        pygame.display.update()
    return numberused


def runfxn(c):
    if c == 0:
        ''
    if c == 1:
        ''
    if c == 2:
        ''
    if c == 3:
        ''
    if c == 4:
        ''
    if c == 5:
        ''
    if c == 6:
        ''
    if c == 7:
        ''
    if c == 8:
        ''
    if c == 9:
        ''
    if c == 10:
        ''
    if c == 11:
        ''
    pygame.time.wait(2000)
        
        
def dispfxn(fxnnum):
    if fxnnum == 0:
        ''
        #Display fxn in info tab

titlefont = pygame.font.SysFont('Helvetica', 100)
subtitlefont = pygame.font.SysFont('Times New Roman', 70)
#textsurface = myfont.render('Some Text', False, (0, 0, 0)) #Text Here
#screen.blit(textsurface,(0,0))

sbx = []
sby = []
sbw = []
sbh = []
counter = 10
while counter >= 1:
    sbx.append(50)
    sby.append(100 * counter - 25)
    sbw.append(500)
    sbh.append(50)
    counter -= 1



done = False
while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               done = True

        #Cursor Sensing
        pygame.event.get()
        get_pos = pygame.mouse.get_pos()
        for i in range(len(button_positionsx)):
            mousex, mousey = get_pos
            if (mousex > (button_positionsx[i]) and  (mousey > button_positionsy[i]) and (mousex < (button_positionsx[i] + button_positionsw[i])) and (mousey < button_positionsy[i] + button_positionsh[i])):
                button_colors[i] = (30,30,30)
            else:
                button_colors[i] = button_colsOG[i]

        for i in range(len(sbx)):
            if (mousex > (sbx[i]) and  (mousey > sby[i]) and (mousex < (sbx[i] + sbw[i])) and (mousey < sby[i] + sbh[i])):
                sbc[i] = (100,100,100) #Work on button colors on left buttons

        pygame.display.update()
        
        for i in range(len(button_positionsx)):
            if (button_colors[i] == PINK) and (pygame.mouse.get_pressed() == (True, False, False)):
                runfxn(i)
            elif (button_colors[i] == PINK) and (pygame.mouse.get_pressed() == (False, False, False)):
                dispfxn(i)
 
        pygame.draw.rect(screen, (0, 0, 0), (0, 0, 1920, 1050))
        #Sidebar
        pygame.draw.rect(screen, (50, 50, 50), (0, 0, 600, 1050))
        pygame.draw.rect(screen, (255, 255, 255), (600, 0, 10, 1050))
        counter = 10
        while counter >= 1:
            pygame.draw.rect(screen, (255, 255, 255), (50, 100 * counter - 50, 500, 10))
            counter -= 1

        counter = 10
        while counter >= 1:
            pygame.draw.rect(screen, (200, 200, 200), (50, 100 * counter - 25, 500, 50))
            counter -= 1

        pygame.draw.rect(screen, (255, 255, 255), (600, 0, 10, 1050))
        
        #Display the Buttons
        for i in range(len(button_positionsx)):
            pygame.draw.rect(screen, (50,50,50), (button_positionsx[i] - 5, button_positionsy[i] - 5, button_positionsw[i] + 10, button_positionsh[i] + 10))

        for i in range(len(button_positionsx)):
            pygame.draw.rect(screen, button_colors[i], (button_positionsx[i], button_positionsy[i], button_positionsw[i], button_positionsh[i]))
            textsurface = subtitlefont.render(button_text[i], False, (255, 255, 255)) #Text Here
            screen.blit(textsurface,(button_positionsx[i] + 12,button_positionsy[i] + 30))
            pygame.draw.rect(screen, (255,255,255), (button_positionsx[i] + 50, button_positionsy[i] + (button_positionsh[i] / 2 ) * 1.5, button_positionsw[i] - 100, 5))

        
 
pygame.quit()
