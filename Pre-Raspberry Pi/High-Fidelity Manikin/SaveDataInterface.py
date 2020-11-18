import pygame,math
from datetime import date
from pygame.locals import *

###########
'Variables'
textBoxTexts = {
  "Text Box Top" : "",
  "Text Box Middle" : "",
  "Text Box Bottom" : "",
  }
dataSaveInfo = []
commentText = ""
nameText = ""
###########
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

#The Following resizes the assets based on the screen size
def wRatio(x):
  w = pygame.display.get_surface().get_size()[0]
  x *= (w / 1920)
  return int(x)

def hRatio(x):
  w = pygame.display.get_surface().get_size()[1]
  x *= (w / 1050)
  return int(x)

###########

def save():#This is the main function of this file
    #The following reads from a glossary of created data saves
    f = open("dataSaveGlossary.txt","a+")
    f.close()
    f= open("dataSaveGlossary.txt","r+")
    lines = f.readlines()
    f.close()
    #f= open("dataSaveGlossary.txt","r")
    dataSaveInfo = []
    parseDataSaves(lines)
    #The following initializes some of the assets needed to construct the window
    global screen,writing_font
    'Window'
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode((1280, 720), pygame.RESIZABLE)
    pygame.display.set_caption('SMART DUMMY')
    pygame.draw.rect(screen, MEDIUM_GREY, (wRatio(0),hRatio(0),wRatio(1920),hRatio(1050)))

    writing_font = pygame.font.SysFont('Times New Roman', wRatio(35))


    #These build the square images on the screen
    #renderRect(3,710,300,500,450,30,MEDIUM_GREY)
    renderRect(1,510,200,900,600,0,0,WHITE)
    renderRect(1,810,275,300,100,0,0,MEDIUM_GREY)
    renderRect(2,605,500,300,200,400,0,MEDIUM_GREY)
    drawSectionText(screen, "Yes ", WHITE, (wRatio(725),hRatio(575),wRatio(200),hRatio(1000)),writing_font)
    drawSectionText(screen, "No ", WHITE, (wRatio(1135),hRatio(575),wRatio(200),hRatio(1000)),writing_font)
    drawSectionText(screen, "Is this a new save?  ", WHITE, (wRatio(830),hRatio(300),wRatio(200),hRatio(1000)),writing_font)

    pygame.display.update()
    choice = False
    chosen = False
    while not chosen:
      for event in pygame.event.get():
        if event.type == pygame.QUIT: #Checks if the USER presses close on the window
          pygame.quit()
          quit()
        """
        elif event.type == VIDEORESIZE:
          SCREEN_SIZE = event.size
          screen = pygame.display.set_mode(SCREEN_SIZE, RESIZABLE, 32)
          writing_font = pygame.font.SysFont('Comic Sans MS', wRatio(20))
          onOffFont = pygame.font.SysFont('Comic Sans MS', wRatio(19))
          save()
          chosen = True
        """
      #Checks if one of the choice buttons (new or old data save) has been pressed
      get_pos = pygame.mouse.get_pos()
      mousex, mousey = get_pos
      if mousex > wRatio(605) and mousey > hRatio(500) and mousex < wRatio(605) + wRatio(300) and mousey < hRatio(500) + hRatio(200) and pygame.mouse.get_pressed() == (True, False, False):
        chosen = True
        choice = True
      elif mousex > wRatio(1005) and mousey > hRatio(500) and mousex < wRatio(1005) + wRatio(300) and mousey < hRatio(500) + hRatio(200) and pygame.mouse.get_pressed() == (True, False, False):
        chosen = True
        choice = False


    if choice:
        return newDataSave()
    else:
        return oldDataSave()




def oldDataSave():
    global screen,writing_font,dataSaveInfo
    #Creates the images on the screen
    renderRect(1,0,0,1920,1080,0,0,MEDIUM_GREY)
    renderRect(3,100,100,600,200,0,350,WHITE)
    renderRect(1,1000,100,900,900,0,0,WHITE)
    drawSectionText(screen, "Name   ", WHITE, (wRatio(100),hRatio(50),wRatio(600),hRatio(1)),writing_font)
    drawSectionText(screen, "Date Created (mm/dd/yyyy)       ", WHITE, (wRatio(100),hRatio(400),wRatio(600),hRatio(1)),writing_font)
    drawSectionText(screen, "Comments     ", WHITE, (wRatio(100),hRatio(750),wRatio(600),hRatio(1)),writing_font)
    pygame.display.update()
    #Begins the text Cursor on the top box
    runTextBox("Text Box Top", "")
    while True:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          quit()
      get_pos = pygame.mouse.get_pos()
      mousex, mousey = get_pos
      if pygame.mouse.get_pressed() == (True, False, False):
          #Checks which data save was chosen and returns the name, date, and comment values
          if mousex > wRatio(1000)and mousey > hRatio(100) and mousex < wRatio(1000) + wRatio(900) and mousey < hRatio(100) + hRatio(900):
            chosenSave = int((mousey - hRatio(100)) / hRatio(90))
            name, dateCreated, dateLastAccessed, comments = dataSaveInfo[chosenSave]
            return (name, dateCreated, dateLastAccessed, comments)
          for i in range(3):
            #Check if textBoxes were chosen again
            if mousex > wRatio(100) and mousey > hRatio(100 + 350 * i) and mousex < wRatio(100) + wRatio(600) and mousey < hRatio(100 + 350 * i) + hRatio(200):
              if mousey > hRatio(800):
                runTextBox("Text Box Bottom", textBoxTexts["Text Box Bottom"])
                break
              elif mousey > hRatio(450):
                runTextBox("Text Box Middle", textBoxTexts["Text Box Middle"])
                break
              else:
                runTextBox("Text Box Top", textBoxTexts["Text Box Top"])
                break
    

def newDataSave():
    global screen,writing_font,dataSaveInfo,nameText,commentText
    #Creates the images on the screen
    renderRect(1,0,0,1920,1080,0,0,MEDIUM_GREY)
    renderRect(1,360,100,1200,150,0,525,WHITE)
    renderRect(1,360,400,1200,600,0,0,WHITE)
    renderRect(1, 1610,800,275,200,0,0,BLACK,WHITE)
    drawSectionText(screen, "Please enter a name for the file (Avoid using the ` character):       ", WHITE, (wRatio(360),hRatio(50),wRatio(1200),hRatio(1)),writing_font)
    drawSectionText(screen, "Enter comments to help distinguish this save from others:         ", WHITE, (wRatio(360),hRatio(350),wRatio(1200),hRatio(1)),writing_font)
    drawSectionText(screen, 'DONE    ', WHITE, (wRatio(1700), hRatio(875),wRatio(275),hRatio(200)),writing_font)
    pygame.display.update()
    try:
      name, comments = collectTextInformationNewDataSave()#Attempts to collect info about the data save
    except:
      name,comments = nameText, commentText #Backup method if both text boxes are empty
    cDate = date.today().strftime('%m/%d/%Y')#Gets the current date
    return (removeBar(name), cDate, cDate, removeBar(comments))#The removeBar gets rid of the index bar from the string
    










def renderRect(it,x,y,w,h,xs,ys,c, *args):
    '''
    it - iteration
    x - starting x value
    y - starting y value
    w - the width of the rectangles
    h - the height of the rectangles
    xs - the x-value to be added to the rectangle each iteration
    ys - the y-value to be added to the rectangle each iteration
    c - the color of the rectangle
    *args - allows for an alternate line color to be specified
    '''
    if len(args) == 1:
      c2 = args
    else:
      c2 = BLACK
    for i in range(it):
        pygame.draw.rect(screen, c, (wRatio(x + xs * i),hRatio(y + ys * i),wRatio(w),hRatio(h)))
        pygame.draw.line(screen, c2, [wRatio(x + xs * i),hRatio(y+i*ys)],[wRatio(x+w + xs * i),hRatio(y+ys*i)],3)
        pygame.draw.line(screen, c2, [wRatio(x + xs * i),hRatio(y+h+i*ys)],[wRatio(x+w + xs * i),hRatio(y+h+ys*i)],3)
        pygame.draw.line(screen, c2, [wRatio(x + xs * i),hRatio(y+ys*i)],[wRatio(x + xs * i),hRatio(y+h+ys*i)],3)
        pygame.draw.line(screen, c2, [wRatio(x+w + xs * i),hRatio(y+ys*i)],[wRatio(x+w + xs * i),hRatio(y+h+ys*i)],3)

def drawTextComic20NoUpdate(surface, text_list, color, rect, font):
  
  x,y,w,h = rect

  char_per_line = math.floor(w/wRatio(15)) #Gets the number of characters per line
  
  new_y = y

  for word in text_list:
    word = str(word)
    if len(word) <= char_per_line or word[:4] == "Date": #Blits any text shorter than the max character per line limit
      surface.blit(font.render(word, True, color), (x,new_y))
      new_y += hRatio(60)
    else:
      #Blits text line by line
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
        
def drawSectionText(surface, text, color, rect, font): #Draws text with a line below it
  x,y,w,h = rect
  surface.blit(font.render(text, True, color), (x,y))
  pygame.draw.rect(surface, color, (x, y + hRatio(40), wRatio(len(text) * 12), 2))


def parseDataSaves(lines):#Gets the save info from the data save glossary
  global dataSaveInfo
  for line in lines:
    if line != "" and line != "\n":
      name,dateAccessed,dateCreated,comments = ("","","","")
      index = 0
      char = line[index]
      while char != "`":
        name += char
        index +=1
        char = line[index]
      index +=1
      char = line[index]
      while char != "`":
        dateAccessed += char
        index +=1
        char = line[index]
      index +=1
      char = line[index]
      while char != "`":
        dateCreated += char
        index +=1
        char = line[index]
      index +=1
      char = line[index]
      while index < len(line) - 1:
        comments += char
        index +=1
        char = line[index]
      dataSaveInfo.append([name, dateAccessed, dateCreated, comments])



##////////////////////////////////////////////////////////
newDataTexts = []

def collectTextInformationNewDataSave(): #This function gathers information from the user to use as name and comments for the data Save
  global nameText, commentText
  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
          pygame.quit()
          quit()
      get_pos = pygame.mouse.get_pos()
      mousex, mousey = get_pos
      if pygame.mouse.get_pressed() == (True, False, False):
          #Chooses which box to manipulate
          for i in range(2):
            if mousex > wRatio(360) and mousey > hRatio(100 + 300 * i) and mousex < wRatio(1200) + wRatio(360) and mousey < hRatio(100 + 300 * i) + hRatio(150 + 450 * i):
              if mousey > hRatio(400):
                return commentsActive()#Allows input into the comments box
                break
              else:
                return nameActive()#Allows input into the name box
                break
          #Returns the name and comments values to create the file
          if mousex > wRatio(1610) and mousey > hRatio(800) and mousex < wRatio(1885) and mousey < hRatio(1000):
            return (nameText, commentText)


def commentsActive(): #Allows for input into the comments box
  global nameText, commentText, writing_font, screen, constantBar, currentIndex
  thisTextBox = True
  textBoxText = commentText
  x,y,w,h = (wRatio(360),hRatio(400),wRatio(1200),wRatio(600))#Dimensions of the comments box adjusted for the screen size
  x2,y2,w2,h2 = (360,400,1200,600)#Dimensions of the comments box NOT adjusted for the screen size
  renderTextBox('null', nameText, x,hRatio(100),w,hRatio(150))
  while thisTextBox:
   for event in pygame.event.get():
    if event.type == pygame.QUIT:#Checks if the user closes the window
          pygame.quit()
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_TAB:
              textBoxText = removeBar(textBoxText)#Gets the Index bar out of the text
              pygame.draw.rect(screen, WHITE, (x + 3,y+3,w-6,h-6))    
              commentText = textBoxText
              constantBar = 0
              thisTextBox = False#Ends this iteration of the loop
              nameActive()#Switches over to the name section
        elif event.key == pygame.K_BACKSPACE:
            barIndex = getIndexBar(textBoxText)#Gets the index of the index bar
            textBoxText = textBoxText[:barIndex - 1] + textBoxText[barIndex:] #Removes the character before the index bar
            commentText = textBoxText
            used = True#Lets the program know to update the text on the screen
        else:
            textBoxText = runTextIndexing(textBoxText, event.key, event)#Adds a character into the text
            commentText = textBoxText
            pygame.display.update()
            used = True
        if used:#Updates the screen with the new text
          used = False
          renderRect(1,x2,y2,w2,h2,0,0,WHITE)
          renderTextBox('null', textBoxText, x,y,w,h)
    if pygame.mouse.get_pressed() == (True, False, False): #Checks for user input on the boxes
          mousex, mousey = pygame.mouse.get_pos()
          for i in range(2):
            if mousex > wRatio(360) and mousey > hRatio(100 + 300 * i) and mousex < wRatio(1200) + wRatio(360) and mousey < hRatio(100 + 300 * i) + hRatio(150 + 450 * i):
              if mousey > hRatio(400):#Comments Box
                thisTextBox = False
                renderRect(1,x2,y2,w2,h2,0,0,WHITE)
                renderTextBox('null', removeBar(textBoxText), x,y,w,h)
                commentsActive()#Switches to a new iteration
              else:#Name Box
                thisTextBox = False
                renderRect(1,x2,y2,w2,h2,0,0,WHITE)
                renderTextBox('null', removeBar(textBoxText), x,y,w,h)
                nameActive()#Begins an iteration of the Name box
          if mousex > wRatio(1610) and mousey > hRatio(800) and mousex < wRatio(1885) and mousey < hRatio(1000): #Returns values of name and comments boxes
            return (nameText, commentText)

def nameActive():#Allows for input into the Name box
  global commentText, nameText, writing_font, screen, constantBar, currentIndex
  thisTextBox = True
  textBoxText = nameText
  x,y,w,h = (wRatio(360),hRatio(100),wRatio(1200),wRatio(150))#Dimensions of the comments box adjusted for the screen size
  x2,y2,w2,h2 = (360,100,1200,150)#Dimensions of the comments box NOT adjusted for the screen size
  renderTextBox('null', commentText, x,hRatio(400),w,hRatio(600))
  while thisTextBox:#This code is nearly exactly the same as the version in the commentsActive() function
   for event in pygame.event.get():
    if event.type == pygame.QUIT:
          pygame.quit()
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_TAB:
              textBoxText = removeBar(textBoxText)
              pygame.draw.rect(screen, WHITE, (x + 3,y+3,w-6,h-6))    
              nameText = textBoxText
              constantBar = 0
              thisTextBox = False
              commentsActive()
        elif event.key == pygame.K_BACKSPACE:
            barIndex = getIndexBar(textBoxText)
            textBoxText = textBoxText[:barIndex - 1] + textBoxText[barIndex:]
            nameText = textBoxText
            used = True
        else:
            textBoxText = runTextIndexing(textBoxText, event.key, event)
            nameText = textBoxText
            pygame.display.update()
            used = True
        if used:
          used = False
          renderRect(1,x2,y2,w2,h2,0,0,WHITE)
          renderTextBox('null', textBoxText, x,y,w,h)
    if pygame.mouse.get_pressed() == (True, False, False):
          mousex, mousey = pygame.mouse.get_pos()
          for i in range(2):
            if mousex > wRatio(360) and mousey > hRatio(100 + 300 * i) and mousex < wRatio(1200) + wRatio(360) and mousey < hRatio(100 + 300 * i) + hRatio(150 + 450 * i):
              if mousey > hRatio(400):
                thisTextBox = False
                commentsActive()
                break
              else:
                thisTextBox = False
                nameActive()
                break
          if mousex > wRatio(1610) and mousey > hRatio(800) and mousex < wRatio(1885) and mousey < hRatio(1000):
            return (nameText, commentText)



#All of the following code was copied over from the MAIN and slightly adjusted to apply to this program. For more in-depth comments, please see this code in the MAIN.

def renderTextBox(textBox, String,x,y,w,h):
  drawTextDetPage(screen, [String], BLACK, (x + 3,y,w-13,h), writing_font)

def renderTextBoxes():
  global textBoxTexts, screen
  drawTextDetPage(screen,[textBoxTexts["Text Box Top"]], BLACK, (wRatio(175),hRatio(200),wRatio(400),hRatio(60)), writing_font)
  drawTextDetPage(screen,[textBoxTexts["Text Box Middle"]], BLACK, (wRatio(175),hRatio(500),wRatio(400),hRatio(60)), writing_font)
  drawTextDetPage(screen,[textBoxTexts["Text Box Bottom"]], BLACK, (wRatio(175),hRatio(650),wRatio(400),hRatio(250)), writing_font)

def removeBar(text):
  tempPhrase = ""
  for i in text:
    if i != "|":
      tempPhrase += i
  return tempPhrase

def getIndexBar(string):
  char = string[0]
  i = 0
  while char != "|":
    i+=1
    try:
      char = string[i]
    except IndexError:
      return len(string)
    char = string[i]
  return i
currentIndex = 0
def runTextBox(currentTextBox, textBoxText):
  global textBoxActive, textBoxTexts, scene_name, writing_font, onOffFont, screen, constantBar, currentIndex
  textBoxActive = True
  x,y,w,h =  returnXYWHBoxValue(currentTextBox)
  while textBoxActive:
    for event in pygame.event.get():

      if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_TAB:
              textBoxText = removeBar(textBoxText)
              x,y,w,h = returnXYWHBoxValue(currentTextBox)
              pygame.draw.rect(screen, WHITE, (x + 3,y+3,w-6,h-6))    
              renderTextBox(currentTextBox, textBoxText,x,y,w,h)
              textBoxTexts[currentTextBox] = textBoxText
              compTextBoxes()
              constantBar = 0
              
              if currentTextBox == "Text Box Top":
                x,y,w,h = (wRatio(100),hRatio(100),wRatio(600),hRatio(200))
                runTextBox("Text Box Middle", textBoxTexts["Text Box Middle"])
                textBoxActive = False
                break


              if currentTextBox == "Text Box Middle":
                x,y,w,h = (wRatio(100),hRatio(450),wRatio(600),hRatio(200))
                runTextBox("Text Box Bottom", textBoxTexts["Text Box Bottom"])
                textBoxActive = False
                break


              if currentTextBox == "Text Box Bottom":
                x,y,w,h = (wRatio(100),hRatio(800),wRatio(600),hRatio(200))
                runTextBox("Text Box Top", textBoxTexts["Text Box Top"])
                textBoxActive = False
                break
              pygame.display.update()
          elif event.key == pygame.K_BACKSPACE:
            barIndex = getIndexBar(textBoxText)
            textBoxText = textBoxText[:barIndex - 1] + textBoxText[barIndex:]
            textBoxTexts[currentTextBox] = textBoxText
          else:
              textBoxText = runTextIndexing(textBoxText, event.key, event)
              textBoxTexts[currentTextBox] = textBoxText


          x,y,w,h =  returnXYWHBoxValue(currentTextBox)  
          pygame.draw.rect(screen, WHITE, (x + 3,y+3,w-6,h-6))    
          renderTextBox(currentTextBox, textBoxText,x,y,w,h)
          textBoxText = removeBar(textBoxText)
          textBoxTexts[currentTextBox] = textBoxText
          compTextBoxes()
          pygame.display.update()
      #The following is commented out because it seems to still have a few issues actually rendering based on window size
      '''
      elif event.type == VIDEORESIZE:
        SCREEN_SIZE = event.size
        screen = pygame.display.set_mode(SCREEN_SIZE, RESIZABLE, 32)
        writing_font = pygame.font.SysFont('Comic Sans MS', wRatio(20))
        onOffFont = pygame.font.SysFont('Comic Sans MS', wRatio(19))
        if scene_name == "Status Page":
          load_scene("Status Page")
        elif scene_name == "Data Page":
          load_scene("Data Page")
        if currentTextBox == "Text Box Top":
          x,y,w,h = (wRatio(175),hRatio(200),wRatio(400),hRatio(60))
        if currentTextBox == "Text Box Middle":
          x,y,w,h = (wRatio(175),hRatio(350),wRatio(400),hRatio(60))
        if currentTextBox == "Text Box Bottom":
          x,y,w,h = (wRatio(175),hRatio(650),wRatio(400),hRatio(250))
        renderTextBoxes()
        compTextBoxes()
      '''
      if event.type == pygame.QUIT:
        pygame.quit()
        quit()
      mousex, mousey = pygame.mouse.get_pos()
      if (not(mousex > x and mousey > y and mousex < x + w and mousey < y + h)) and pygame.mouse.get_pressed() == (True, False, False):
        textBoxActive = False
  textBoxText = removeBar(textBoxText)
  pygame.draw.rect(screen, WHITE, (x + 3,y+3,w-6,h-6))    
  renderTextBox(currentTextBox, textBoxText,x,y,w,h)
  textBoxTexts[currentTextBox] = textBoxText
  compTextBoxes()



def compTextBoxes():
  global textBoxTexts, dataSaveInfo, matchesAccessor
  name, dateCreated, comments = (textBoxTexts["Text Box Top"],textBoxTexts["Text Box Middle"],textBoxTexts["Text Box Bottom"])
  matches = []
  
  name = removeExtraSpaces(name)
  dateCreated = removeExtraSpaces(dateCreated)
  comments = removeExtraSpaces(comments)
  for dataEntry in dataSaveInfo:
    match = True
    if not(areCommentsRelevant(dataEntry[0], name)):
      match = False
    elif not(areCommentsRelevant(dataEntry[1], dateCreated)):
      match = False
    elif not(areCommentsRelevant(dataEntry[2], comments)):
      match = False
    if match == True:
      matches.append(dataEntry)
  matchesAccessor = matches
  renderMatches(matches)

def returnXYWHBoxValue(currentTextBox):
  if currentTextBox == "Text Box Top":
    return (wRatio(100),hRatio(100),wRatio(600),hRatio(200))
  if currentTextBox == "Text Box Middle":
    return (wRatio(100),hRatio(450),wRatio(600),hRatio(200))
  else:
    return (wRatio(100),hRatio(800),wRatio(600),hRatio(200))
    



def removeExtraSpaces(nStr):
  c = 0
  for char in nStr:
    if char == " ":
      c+=1
    else:
      break
  return nStr[c:]

def areCommentsRelevant(ogCom, newCom):
  if newCom == "":
    return True
  ogCom, newCom = (ogCom.lower(), newCom.lower())
  relevant = False
  c = 0
  for char in ogCom:
    if char == newCom[0]:
      tempc = c
      for i in range(1, len(newCom)):
        tempc +=1
        try:
          ogCom[tempc]
        except IndexError:
          relevant = False
          break
        if ogCom[tempc] != newCom[i]:
          relevant = False
          break
        relevant = True
    c+=1
    if relevant:
      break
  return relevant


def drawTextDetPage(surface, text_list, color, rect, font):
  
  x,y,w,h = rect

  char_per_line = math.floor(w/wRatio(15))
  
  new_y = y

  for word in text_list:
    if len(word) <= char_per_line:
      surface.blit(font.render(word, True, color), (x,new_y))
      new_y += hRatio(60)
    else:
      while (len(word) > 0):
        if len(word) > char_per_line and word[:char_per_line - 1][-1] != " " and word[char_per_line] != " ":
          extraChar = "-"
        else:
          extraChar = ""
        text = font.render((word[:char_per_line - 1] + extraChar), True, color)
        surface.blit(text, (x,new_y))
        word = word[char_per_line - 1:]
        new_y += hRatio(40)
      
  pygame.display.update()

constantBar = 0

def runTextIndexing(phrase, eventKey, event):
  global currentIndex, currentTime, constantBar
  tempPhrase = ""
  for i in phrase:
    if i != "|":
      tempPhrase += i
  if eventKey == 276:
        constantBar -= 1
  if eventKey == 275:
        constantBar += 1
  if constantBar < (-1 * len(phrase)):
        constantBar = (-1 * len(phrase))
  if constantBar > 0:
        constantBar = -1
  currentIndex = len(phrase) + constantBar
  tempPhrase = tempPhrase[:currentIndex] + event.unicode + "|" + tempPhrase[currentIndex:]
  return tempPhrase




def renderMatches(matches):
  renderRect(1,1000,100,900,900,0,0, WHITE)
  if len(matches) > 10:
    numBlit = 10
  else:
    numBlit = len(matches)
  x,y,w,h = wRatio(1000),hRatio(100),wRatio(900),hRatio(90)
  newx, newy = x,y
  renderRect(numBlit, 1000,190,900,1,0,90,BLACK)
  pygame.display.update()
  name,dateAccessed,dateCreated,comments = ([],[],[],[])
  for i in range(len(matches)):
    name.append(matches[i][0])
    dateCreated.append(matches[i][2])
    comments.append(matches[i][3])
  
  for i in range(numBlit):
    drawTextComic20NoUpdate(screen, ["Name: " + name[i]], BLACK, (newx + wRatio(5), newy, wRatio(300)- wRatio(5), hRatio(30)), writing_font)
    drawTextComic20NoUpdate(screen, ["Date Created: " + dateCreated[i]], BLACK, (newx + wRatio(5), newy + hRatio(40), wRatio(300)- wRatio(5), hRatio(20)), writing_font)
    drawTextComic20NoUpdate(screen, [comments[0]], BLACK, (newx + wRatio(8) + wRatio(390), newy, wRatio(505) - wRatio(8), hRatio(70)), writing_font)
    newy += hRatio(91)
    pygame.draw.line(screen, BLACK, [newx + wRatio(378),y],[newx + wRatio(378), y+615],1)
  pygame.display.update()
