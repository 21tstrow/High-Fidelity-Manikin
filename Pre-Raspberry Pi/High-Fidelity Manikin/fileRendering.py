import pygame, math
"""
Files need to be arranged in the following format:

exFile.txt
----------:
bool cardiacArrest
bool Cyanosis(fingernails)
bool Cyanosis(mouth)
int heartrate
string currentTime
list currentSoundsBeingPlayed
list activeConditions
list activeMedicines
list activeScenarios
list eventLog

--
Example File:

true
false
true
67
"00:05:45"
["Bronchitus", "Third Heart Gallop"]
["Hemophiliac"]
["Asprin"]
[]
["00:5:35 ~ Cariac Arrest Activated", ...]

"""
import pygame
from pygame.locals import *

###########
'Variables'
cardiacArrest = ''
cyanosisFingers = ''
cyanosisMouth = ''
heartRate = ''
currentTime = ''
currentSoundsBeingPlayed = ''
activeConditions = ''
activeMedicines = ''
activeScenarios = ''
eventLog = ''
dataInfo = [cardiacArrest, cyanosisFingers, cyanosisMouth, heartRate, currentTime, currentSoundsBeingPlayed, activeConditions, activeMedicines, activeScenarios, eventLog]
##########
'Colors'
BLACK = [0,0,0]
WHITE = [242,234,237]
WHITE2 = [255,220,115]
MEDIUM_GREY = [42,52,87]
#MEDIUM_GREY = [128,128,128]
AQUA = [164,164,191]
NAVY_BLUE	= [0,0,128]
GREEN	= [0,255,0]
ORANGE = [255,165,0]
YELLOW = [255,255,0]
###########

def wRatio(x):
  w = pygame.display.get_surface().get_size()[0]
  x *= (w / 1920)
  return int(x)

def hRatio(x):
  w = pygame.display.get_surface().get_size()[1]
  x *= (w / 1050)
  return int(x)

###########

def renderAndChoose(dataSave):
    global dataInfo
    chosen = False
    'Window'
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode((1280, 720), pygame.RESIZABLE)
    pygame.display.set_caption('SMART DUMMY')
    #Data
    '''
    fileName = ""
    for i in dataSave:
        fileName += i
    f=open(fileName, "r+")
    lines = f.readlines()
    f.close
    dataInfoIndex = -1
    for line in lines:
        dataInfoIndex += 1
        dataInfo[dataInfoIndex] = ""
        index = 0
        char = line[index]
        while char != "\n":
            dataInfo[dataInfoIndex] += char
            index += 1
            char = line[index]
    '''
    #Shapes    
    pygame.draw.rect(screen, WHITE, (wRatio(0),hRatio(0),wRatio(1920),hRatio(1050)))
    for i in range(4):
      pygame.draw.rect(screen, MEDIUM_GREY, (wRatio(50),hRatio(30 + 100 * i),wRatio(600),hRatio(90)))
      pygame.draw.line(screen, BLACK, [wRatio(50),hRatio(30 + 100 * i)],[wRatio(650),hRatio(30 + 100 * i)],3)
      pygame.draw.line(screen, BLACK, [wRatio(50),hRatio(120 + 100 * i)],[wRatio(650),hRatio(120 + 100 * i)],3)
      pygame.draw.line(screen, BLACK, [wRatio(50),hRatio(30 + 100 * i)],[wRatio(50),hRatio(120 + 100 * i)],3)
      pygame.draw.line(screen, BLACK, [wRatio(650),hRatio(30 + 100 * i)],[wRatio(650),hRatio(120 + 100 * i)],3)
    for i in range(4):
      pygame.draw.rect(screen, MEDIUM_GREY, (wRatio(700),hRatio(30 + 100 * i),wRatio(600),hRatio(90)))
      pygame.draw.line(screen, BLACK, [wRatio(700),hRatio(30 + 100 * i)],[wRatio(1300),hRatio(30 + 100 * i)],3)
      pygame.draw.line(screen, BLACK, [wRatio(700),hRatio(120 + 100 * i)],[wRatio(1300),hRatio(120 + 100 * i)],3)
      pygame.draw.line(screen, BLACK, [wRatio(700),hRatio(30 + 100 * i)],[wRatio(700),hRatio(120 + 100 * i)],3)
      pygame.draw.line(screen, BLACK, [wRatio(1300),hRatio(30 + 100 * i)],[wRatio(1300),hRatio(120 + 100 * i)],3)
    for i in range(2):
      pygame.draw.rect(screen, MEDIUM_GREY, (wRatio(50 + 650 * i),hRatio(430),wRatio(600),hRatio(600)))
      pygame.draw.line(screen, BLACK, [wRatio(50 + 650 * i),hRatio(430)],[wRatio(50 + 650 * i),hRatio(1030)],3)
      pygame.draw.line(screen, BLACK, [wRatio(650 + 650 * i),hRatio(430)],[wRatio(650 + 650 * i),hRatio(1030)],3)
      pygame.draw.line(screen, BLACK, [wRatio(50 + 650 * i),hRatio(430)],[wRatio(650 + 650 * i),hRatio(430)],3)
      pygame.draw.line(screen, BLACK, [wRatio(50 + 650 * i),hRatio(1030)],[wRatio(650 + 650 * i),hRatio(1030)],3)
    for i in range(4):
      pygame.draw.rect(screen, MEDIUM_GREY, (wRatio(1350),hRatio(30 + 200 * i),wRatio(500),hRatio(190)))
      pygame.draw.line(screen, BLACK, [wRatio(1350),hRatio(30+200*i)],[wRatio(1850),hRatio(30+200*i)],3)
      pygame.draw.line(screen, BLACK, [wRatio(1350),hRatio(220+200*i)],[wRatio(1850),hRatio(220+200*i)],3)
      pygame.draw.line(screen, BLACK, [wRatio(1350),hRatio(30+200*i)],[wRatio(1350),hRatio(220+200*i)],3)
      pygame.draw.line(screen, BLACK, [wRatio(1850),hRatio(30+200*i)],[wRatio(1850),hRatio(220+200*i)],3)
    pygame.draw.rect(screen, MEDIUM_GREY, (wRatio(1350),hRatio(830),wRatio(500),hRatio(200)))
    pygame.draw.line(screen, BLACK, [wRatio(1350),hRatio(830)],[wRatio(1850),hRatio(830)],3)
    pygame.draw.line(screen, BLACK, [wRatio(1350),hRatio(1030)],[wRatio(1850),hRatio(1030)],3)
    pygame.draw.line(screen, BLACK, [wRatio(1350),hRatio(830)],[wRatio(1350),hRatio(1030)],3)
    pygame.draw.line(screen, BLACK, [wRatio(1850),hRatio(830)],[wRatio(1850),hRatio(1030)],3)
    for i in range(2):
      pygame.draw.rect(screen, WHITE, (wRatio(1375 + i * 250),hRatio(900),wRatio(200),hRatio(100)))
      pygame.draw.line(screen, BLACK, [wRatio(1375 + i * 250),hRatio(900)],[wRatio(1575 + i * 250),hRatio(900)],3)
      pygame.draw.line(screen, BLACK, [wRatio(1375 + i * 250),hRatio(1000)],[wRatio(1575 + i * 250),hRatio(1000)],3)
      pygame.draw.line(screen, BLACK, [wRatio(1375 + i * 250),hRatio(900)],[wRatio(1375 + i * 250),hRatio(1000)],3)
      pygame.draw.line(screen, BLACK, [wRatio(1575 + i * 250),hRatio(900)],[wRatio(1575 + i * 250),hRatio(1000)],3)
    #TEXT
    writing_font = pygame.font.SysFont('Times New Roman', wRatio(35))
    #Button Texts
    drawSectionText(screen, "Is This The Desired Save?", WHITE, (wRatio(1405),hRatio(835),wRatio(590),hRatio(90)), writing_font)
    drawTextComic20NoUpdate(screen, ["Yes"], BLACK, (wRatio(1445),hRatio(930),wRatio(590),hRatio(90)), writing_font)
    drawTextComic20NoUpdate(screen, ["No"], BLACK, (wRatio(1705),hRatio(930),wRatio(590),hRatio(90)), writing_font)
    #Titleing Text
    drawTextComic20NoUpdate(screen, ["Name: "], WHITE, (wRatio(55),hRatio(35),wRatio(590),hRatio(80)), writing_font)
    drawTextComic20NoUpdate(screen, ["Date Last Accessed: "], WHITE, (wRatio(55),hRatio(135),wRatio(590),hRatio(80)), writing_font)
    drawTextComic20NoUpdate(screen, ["Date Created: "], WHITE, (wRatio(55),hRatio(235),wRatio(590),hRatio(80)), writing_font)
    drawTextComic20NoUpdate(screen, ["Length of Session: "], WHITE, (wRatio(55),hRatio(335),wRatio(590),hRatio(80)), writing_font)
    drawTextComic20NoUpdate(screen, ["Heart Rate: "], WHITE, (wRatio(705),hRatio(35),wRatio(590),hRatio(80)), writing_font)
    drawTextComic20NoUpdate(screen, ["Cardiac Arrest: "], WHITE, (wRatio(705),hRatio(135),wRatio(590),hRatio(80)), writing_font)
    drawTextComic20NoUpdate(screen, ["Cyanosis (Fingernails): "], WHITE, (wRatio(705),hRatio(235),wRatio(590),hRatio(80)), writing_font)
    drawTextComic20NoUpdate(screen, ["Cyanosis (Mouth): "], WHITE, (wRatio(705),hRatio(335),wRatio(590),hRatio(80)), writing_font)
    drawSectionText(screen, "Comments  ", WHITE, (wRatio(55),hRatio(435),wRatio(590),hRatio(80)),writing_font)
    drawSectionText(screen, "Event Log (Most Recent Events)", WHITE, (wRatio(705),hRatio(435),wRatio(590),hRatio(80)),writing_font)
    drawSectionText(screen, "Active Sounds", WHITE, (wRatio(1355),hRatio(35),wRatio(590),hRatio(80)), writing_font)
    drawSectionText(screen, "Active Conditions", WHITE, (wRatio(1355),hRatio(235),wRatio(590),hRatio(80)), writing_font)
    drawSectionText(screen, "Active Medications", WHITE, (wRatio(1355),hRatio(435),wRatio(590),hRatio(80)), writing_font)
    drawSectionText(screen, "Other Applied Scenarios", WHITE, (wRatio(1355),hRatio(635),wRatio(590),hRatio(80)), writing_font)
    #Answer Text
    drawTextComic20NoUpdate(screen, [dataSave[0]], WHITE2, (wRatio(150),hRatio(35),wRatio(590),hRatio(80)), writing_font)
    drawTextComic20NoUpdate(screen, [dataSave[1]], WHITE2, (wRatio(345),hRatio(135),wRatio(590),hRatio(80)), writing_font)
    drawTextComic20NoUpdate(screen, [dataSave[2]], WHITE2, (wRatio(257),hRatio(235),wRatio(590),hRatio(80)), writing_font)
    drawTextComic20NoUpdate(screen, [dataSave[3]], WHITE2, (wRatio(55),hRatio(485),wRatio(590),hRatio(420)), writing_font)
    (cardiacArrest, cyanosisFingers, cyanosisMouth, heartRate, currentTime, currentSoundsBeingPlayed, activeConditions, activeMedicines, activeScenarios, eventLog) = getInfo(dataSave)
    varList = [cardiacArrest, cyanosisFingers, cyanosisMouth, heartRate, currentTime, currentSoundsBeingPlayed, activeConditions, activeMedicines, activeScenarios, eventLog]
    for i in range(len(varList)):
      if i <= 2:
        if i == 0:
          x = 925
        elif i == 1:
          x = 1035
        else:
          x = 970
        if varList[i]:
          drawTextComic20NoUpdate(screen, ["On"], WHITE2, (wRatio(x),hRatio(135 + 100 * i),wRatio(590),hRatio(80)), writing_font)
        else:
          drawTextComic20NoUpdate(screen, ["Off"], WHITE2, (wRatio(x),hRatio(135 + 100 * i),wRatio(590),hRatio(80)), writing_font)
      elif i == 3:
        drawTextComic20NoUpdate(screen, [varList[i]], WHITE2, (wRatio(880),hRatio(35),wRatio(590),hRatio(80)), writing_font)
      elif i == 4:
        drawTextComic20NoUpdate(screen, [varList[i]], WHITE2, (wRatio(325),hRatio(335),wRatio(590),hRatio(80)), writing_font)
      elif i >= 5 and i <=8:
        print(varList[i])
        printString = ""
        for item in varList[i]:
          printString += item + ", "
        printString = printString[:len(printString) - 2]
        drawTextComic20NoUpdate(screen, [printString], WHITE2, (wRatio(1355),hRatio(75 + 200 * (i - 5)),wRatio(490),hRatio(180)), writing_font)
      else:
        drawTextComic20NoUpdate(screen, varList[i], WHITE2, (wRatio(705),hRatio(485),wRatio(590),hRatio(420)), writing_font)


    #Update
    pygame.display.update()
    #Loop
    while not chosen:
      for event in pygame.event.get():
        event2 = event
        if event.type == pygame.QUIT:
          pygame.quit()
          quit()
        elif event.type == VIDEORESIZE:
          SCREEN_SIZE = event.size
          screen = pygame.display.set_mode(SCREEN_SIZE, RESIZABLE, 32)
          writing_font = pygame.font.SysFont('Comic Sans MS', wRatio(20))
          onOffFont = pygame.font.SysFont('Comic Sans MS', wRatio(19))
          return renderAndChoose(dataSave)
      get_pos = pygame.mouse.get_pos()
      mousex, mousey = get_pos
      if mousex > wRatio(1375) and mousey > hRatio(900) and mousex < wRatio(1375) + wRatio(200) and mousey < hRatio(900) + hRatio(100) and pygame.mouse.get_pressed() == (True, False, False):
        return True
      elif mousex > wRatio(1625) and mousey > hRatio(900) and mousex < wRatio(1625) + wRatio(200) and mousey < hRatio(900) + hRatio(100) and pygame.mouse.get_pressed() == (True, False, False):
        return False
      
    ##Find some way to diplay the data of the save to the user and then confirm that this is indeed the data they want to load
    



def getInfo(dataSave):
    fileName = ''
    fileNameTemp = ''
    for i in dataSave:
        fileName += i + '`'
    fileName = fileName[:-1]
    for i in fileName:
      if i != '/':
        fileNameTemp += i
    fileName = fileNameTemp + '.txt'
    f=open(fileName, "r+")
    lines = f.readlines()
    f.close
    dataInfoIndex = -1
    for line in lines:
        dataInfoIndex += 1
        dataInfo[dataInfoIndex] = ""
        index = 0
        char = line[index]
        while char != "\n":
            try:
              dataInfo[dataInfoIndex] += char
              index += 1
              char = line[index]
            except IndexError:
              break
    #The following converts from string into more applicable data types
    cardiacArrest, cyanosisFingers, cyanosisMouth, heartRate, currentTime, currentSoundsBeingPlayed, activeConditions, activeMedicines, activeScenarios, eventLog = tuple(dataInfo)
    #To Bool
    if cardiacArrest == "true":
        cardiacArrest = True
    else:
        cardiacArrest = False
    if cyanosisFingers == "true":
        cyanosisFingers = True
    else:
        cyanosisFingers = False
    if cyanosisMouth == "true":
        cyanosisMouth = True
    else:
        cyanosisMouth = False
    #To Int
    heartRate = int(heartRate)
    #To Usable String
    currentTime = currentTime[1:len(currentTime)-1]
    #To List
    currentSoundsBeingPlayedL, activeConditionsL, activeMedicinesL, activeScenariosL, eventLogL = ([],[],[],[],[])
    testCase = 0
    currentString = ""
    for char in currentSoundsBeingPlayed:
        if char == "\"":
            testCase += 1
            if testCase %2 == 0:
                currentSoundsBeingPlayedL.append(currentString)
                currentString = ""
            continue
        if testCase %2 == 1:
            currentString += char

    testCase = 0
    currentString = ""
    for char in activeConditions:
        if char == "\"":
            testCase += 1
            if testCase %2 == 0:
                activeConditionsL.append(currentString)
                currentString = ""
            continue
        if testCase %2 == 1:
            currentString += char

    testCase = 0
    currentString = ""
    for char in activeMedicines:
        if char == "\"":
            testCase += 1
            if testCase %2 == 0:
                activeMedicinesL.append(currentString)
                currentString = ""
            continue
        if testCase %2 == 1:
            currentString += char

    testCase = 0
    currentString = ""
    for char in activeScenarios:
        if char == "\"":
            testCase += 1
            if testCase %2 == 0:
                activeScenariosL.append(currentString)
                currentString = ""
            continue
        if testCase %2 == 1:
            currentString += char

    testCase = 0
    currentString = ""
    for char in eventLog:
        if char == "\"":
            testCase += 1
            if testCase %2 == 0:
                eventLogL.append(currentString)
                currentString = ""
            continue
        if testCase %2 == 1:
            currentString += char

    #return
    return (cardiacArrest, cyanosisFingers, cyanosisMouth, heartRate, currentTime, currentSoundsBeingPlayedL, activeConditionsL, activeMedicinesL, activeScenariosL, eventLogL)
        
#getInfo("//e042000h1/2021/21tstrow/My Documents/Python Programs/FileRendering Test File.txt")

def drawTextComic20NoUpdate(surface, text_list, color, rect, font):
  
  x,y,w,h = rect

  char_per_line = math.floor(w/wRatio(15))
  
  new_y = y

  for word in text_list:
    word = str(word)
    if len(word) <= char_per_line or word[:4] == "Date":
      surface.blit(font.render(word, True, color), (x,new_y))
      new_y += hRatio(60)
    else:
      if not(word[char_per_line - 2] == "," or word[char_per_line - 2] == " "):
        text = font.render((word[:char_per_line - 1] + "-"), True, color)
      else:
        text = font.render((word[:char_per_line - 1]), True, color)
      surface.blit(text, (x,new_y))
      word = word[char_per_line - 1:]
      new_y += hRatio(40)
      word = word[:char_per_line]
      surface.blit(font.render(word, True, color), (x,new_y))
      new_y += hRatio(60)
        
def drawSectionText(surface, text, color, rect, font):
  x,y,w,h = rect
  surface.blit(font.render(text, True, color), (x,y))
  pygame.draw.rect(surface, color, (x, y + hRatio(40), wRatio(len(text) * 15), 2))

  
