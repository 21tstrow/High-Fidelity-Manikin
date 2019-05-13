import pygame
from pygame.locals import *
import random
#Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)
RED2 = (200, 50, 50)
PINK = (250, 150, 150)

#images
global susuc
global subfail

'''
Subsidize Farming -> decrease government wealth, increase food
Take land -> decrease military might, increase resource diversity proportional to previous military might, increase pop happiness, decrease foreign relations, increase government wealth.
Import -> decrease government wealth, increase resource diversity or food
Export -> decrease food or resource diversity, increase government wealth
Take over country -> if military might is greater than neighbouring country, gain 25% to every category but lose % military might proportional to neighbouring country's military might vs. own and 25% foreign relations; else, lose 50% military might and resource diversity
Increase innovation -> decrease government wealth and food, increase resource diversity and population happiness
Accept immigrants -> decrease food and government wealth, increase pop. and foreign_relations
Gift -> decrease government wealth, increase foriegn relations
Deport citizens -> decrease pop. and population happiness, increase food resource and government wealth
Draft citizens -> decrease pop. and pop happiness, increase military might
Hold festival -> decrease government wealth, increase population happiness
Increase taxes -> decrease pop happiness, increase government wealth proportional to pop.
'''
population_happiness = 30
military_might = 80

food_resource = 25
foreign_relations = 30
total_population = 35
government_wealth = 50
resource_diversity = 40

variables = [population_happiness, military_might, food_resource, foreign_relations, total_population, government_wealth, resource_diversity]

def display_values():
    for var in variables:
        if var == population_happiness:
            print_squares(500, 75, population_happiness)
        if var == military_might:
            print_squares(500, 125, military_might)
        if var == food_resource:
            print_squares(500, 180, food_resource)
        if var == foreign_relations:
            print_squares(500, 235, foreign_relations)
        if var == total_population:
            print_squares(500, 290, total_population)
        if var == government_wealth:
            print_squares(500, 340, government_wealth)
        if var == resource_diversity:
            print_squares(500, 395, resource_diversity)

        
def print_squares(x, y, value):
    tempval = value

    xval = x
    yval = y
    for i in range(10):
        if value > 0:
            pygame.draw.rect(screen, RED2, (xval, yval, 10, 10))
        if value <= 0:
            pygame.draw.rect(screen, WHITE, (xval, yval, 10, 10))
        value -= 10
        xval += 20
    

pygame.init()

screen = pygame.display.set_mode([800,800])
pygame.display.set_caption('Country Simulator')

button_positionsx = [10, 145, 280, 415, 550, 685, 10, 145, 280, 415, 550, 685]
button_positionsw = [250, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90]
button_positionsy = [10, 535, 535, 535, 535, 535, 655, 655, 655, 655, 655, 655]
button_positionsh = [150, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70]
button_colors = [GREEN, RED2, RED2, RED2, RED2, RED2, RED2, RED2, RED2, RED2, RED2, RED2]
button_colsOG = [GREEN, RED2, RED2, RED2, RED2, RED2, RED2, RED2, RED2, RED2, RED2, RED2]

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
        print("yaya")
        #Display fxn in info tab

myfont = pygame.font.SysFont('Comic Sans MS', 30)
#textsurface = myfont.render('Some Text', False, (0, 0, 0)) #Text Here
#screen.blit(textsurface,(0,0))



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
                button_colors[i] = PINK
                print("yay")
                print(get_pos)
            else:
                button_colors[i] = button_colsOG[i]

        pygame.display.update()
        
        for i in range(len(button_positionsx)):
            if (button_colors[i] == PINK) and (pygame.mouse.get_pressed() == (True, False, False)):
                runfxn(i)
            elif (button_colors[i] == PINK) and (pygame.mouse.get_pressed() == (False, False, False)):
                dispfxn(i)
 

        #Display the Buttons
        for i in range(len(button_positionsx)):
            pygame.draw.rect(screen, button_colors[i], (button_positionsx[i], button_positionsy[i], button_positionsw[i], button_positionsh[i]))
 
        display_values()
 
pygame.quit()

#Moving Logic
#if event.type == pygame.KEYDOWN:
    #if event.key == pygame.K_LEFT:
        #player.changespeed(-5, 0)
                

