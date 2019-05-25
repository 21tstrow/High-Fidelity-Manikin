import pygame
from pygame.locals import *
import random
import tkinter as tk

#Aspect Ratio
root = tk.Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
wRatio = float(screen_width / 1920)
hRatio = float(screen_height / 1050)

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

screen = pygame.display.set_mode([screen_width, screen_height])
pygame.display.set_caption('SMART DUMMY')

button_positionsx = [635, 955, 1275, 1595, 635, 955, 1275, 1595]
button_positionsy = [50, 50, 50, 50, 600, 600, 600, 600]
button_positionsw = [290, 290, 290, 290, 290, 290, 290, 290]
button_positionsh = [400, 400, 400, 400, 400, 400, 400, 400]
button_colors = [BUTTONBLUE, GREEN, RED, PURPLE, PURPLE, RED, GREEN, BUTTONBLUE]
button_colsOG = [BUTTONBLUE, GREEN, RED, PURPLE, PURPLE, RED, GREEN, BUTTONBLUE]
button_text = ['Save 1', 'Save 2', 'Save 3', 'Save 4', 'Save 5', 'Save 6', 'Save 7', 'Save 8']

for i in range(len(button_positionsx)):
    button_positionsx[i] = int(button_positionsx[i] * wRatio)
for i in range(len(button_positionsy)):
    button_positionsy[i] = int(button_positionsy[i] * hRatio)
for i in range(len(button_positionsw)):
    button_positionsw[i] = int(button_positionsw[i] * wRatio)
for i in range(len(button_positionsh)):
    button_positionsh[i] = int(button_positionsh[i] * hRatio)
    
###############
'Functions'
###############

def ask(screen, question):
    "ask(screen, question) -> answer"
    pygame.font.init()
    current_string = ''
    display_box(screen, question + ": " + current_string)
    inkey = 128
    while True:
      pygame.event.get()
      if event.key != K_LEFT:
        print(pygame.key.name(event.key))


def display_box(screen, qa):
    pygame.draw.rect(screen, (100,100,100), (0,0,int(800 * wRatio),int(800 * hRatio)))
    textsurface = smallbuttonfont.render(qa, False, (0, 0, 0))
    screen.blit(textsurface,(0,0))
    pygame.display.update()


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

    for i in range(len(button_positionsx)):
        number_positionsx[i] = int(number_positionsx[i] * wRatio)
    for i in range(len(button_positionsy)):
        number_positionsy[i] = int(number_positionsy[i] * hRatio)
    for i in range(len(button_positionsw)):
        number_positionsw[i] = int(number_positionsw[i] * wRatio)
    for i in range(len(button_positionsh)):
        number_positionsh[i] = int(number_positionsh[i] * hRatio)
    
    pygame.draw.rect(screen, (100,100,100), (0,0,int(800 * wRatio),int(800 * hRatio)))
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


def runfxn(c,title):
    if title == 'save button':
        if c == 0:
            ''
        if c == 1:
            ask(screen, "Does this work? (y/n)")
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
    else:
        if title == 'sidebar':
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



    pygame.time.wait(2000)
        
        
def dispfxn(fxnnum):
    if fxnnum == 0:
        ''
        #Display fxn in info tab

titlefont = pygame.font.SysFont('Helvetica', int(100 * hRatio))
subtitlefont = pygame.font.SysFont('Times New Roman', int(70 * hRatio))
#textsurface = myfont.render('Some Text', False, (0, 0, 0)) #Text Here
#screen.blit(textsurface,(0,0))

sbx = []
sby = []
sbw = []
sbh = []
sbc = []
sbt = ["Settings", "Diagnostics", "", "", "", "", "", "Save Data", "Scenario Design", "Scenarios"]
counter = 10
while counter >= 1:
    sbx.append(int(50 * wRatio))
    sby.append(int((100 * counter - 60) * hRatio))
    sbw.append(int(500 * wRatio))
    sbh.append(int(50 * hRatio))
    sbc.append(WHITE)
    counter -= 1

smallbuttonfont = pygame.font.SysFont('Times New Roman', int(50 * hRatio))

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
                sbc[i] = (200,200,200)
            else:
                sbc[i] = (255,255,255)

        pygame.display.update()
        
        for button in range(len(button_positionsx)):
            if (button_colors[button] == (30,30,30)) and (pygame.mouse.get_pressed() == (True, False, False)):
                runfxn(button, 'save button')
                print("n")

        for sidebar in range(len(sbx)):
            if (sbc[sidebar] == (200,200,200)) and (pygame.mouse.get_pressed() == (True, False, False)):
                runfxn(sidebar,'sidebar')
                print("y")
 
        pygame.draw.rect(screen, (0, 0, 0), (0, 0, screen_width, screen_height))

        #Sidebar
        pygame.draw.rect(screen, (50, 50, 50), (0, 0, int(600 * wRatio), screen_height))
        pygame.draw.rect(screen, (255, 255, 255), (int(600 * wRatio), 0, int(10 * wRatio), screen_height))
        for i in range(len(sbx)):
            pygame.draw.rect(screen, sbc[i], (sbx[i], sby[i], sbw[i], sbh[i]))
            pygame.draw.rect(screen, (255,255,255), (int(50 * wRatio), sby[i] + int(60 * hRatio), int(500 * wRatio), int(10 * hRatio)))
            textsurface = smallbuttonfont.render(sbt[i], False, (0, 0, 0))
            screen.blit(textsurface,(sbx[i], sby[i] - int(5 * hRatio)))


        pygame.draw.rect(screen, (255, 255, 255), (int(600 * wRatio), 0, int(10 * wRatio), screen_height))
        
        #Display the Buttons
        for i in range(len(button_positionsx)):
            pygame.draw.rect(screen, (50,50,50), (button_positionsx[i] - int(5 * wRatio), button_positionsy[i] - int(5 * hRatio), button_positionsw[i] + int(10 * wRatio), button_positionsh[i] + int(10 * hRatio)))

        for i in range(len(button_positionsx)):
            pygame.draw.rect(screen, button_colors[i], (button_positionsx[i], button_positionsy[i], button_positionsw[i], button_positionsh[i]))
            textsurface = subtitlefont.render(button_text[i], False, (255, 255, 255)) #Text Here
            screen.blit(textsurface,(button_positionsx[i] + int(12 * wRatio),button_positionsy[i] + int(30 * hRatio)))
            pygame.draw.rect(screen, (255,255,255), (button_positionsx[i] + int(50 * wRatio), button_positionsy[i] + (button_positionsh[i] / 2 ) * 1.5, button_positionsw[i] - int(100 * wRatio), int(5 * hRatio)))

        
 
pygame.quit()
