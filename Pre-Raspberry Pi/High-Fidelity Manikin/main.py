#Start Arduino Scripts
#Add Dropdown list of sounds to status page
import pygame, random, time, math, pathlib, platform, sys, os, SaveDataInterface, fileRendering, GPIO, os
from pygame.locals import *
#The below initializes some of the assests for the window and font
pygame.font.init()
screen = pygame.display.set_mode((1280, 720), pygame.RESIZABLE)
pygame.display.set_caption('SMART DUMMY')

#The below two funcitons adjust the size of screen objects based on the size of the screen
def wRatio(x):
  w = pygame.display.get_surface().get_size()[0]
  x *= (w / 1920)
  return int(x)

def hRatio(x):
  w = pygame.display.get_surface().get_size()[1]
  x *= (w / 1050)
  return int(x)

#handles an error in event logging
global box_4_text
box_4_text = []

##########
'Colors'
##########
BLACK = [0,0,0]
WHITE	= [255,255,255]
WHITE = [242,234,237]
MEDIUM_GREY = [42,52,87]
#MEDIUM_GREY = [128,128,128]
AQUA = [164,164,191]
NAVY_BLUE	= [0,0,128]
GREEN	= [0,255,0]
ORANGE = [255,165,0]
YELLOW = [255,255,0]
RED = [255,0,0]

heart_rate = 80


class ECG:
    #position is a rectangle tuple
    def __init__(self, parent, heartrate, position, *args, **kwargs):
        self.parent = parent
        self.x, self.y, self.max_x, self.max_y = position;
        #sylist: sinus rhythm, sinus bradycardia, sinus tachycardia, vfib
        self.sylist = [self.y, self.y, self.y, self.y + 20]
        self.sx = self.x
        self.cardiacarrest = False
        self.img = None
        self.rect = None
        self.set_rate(heartrate)
        self.xratio = 1
        self.yratio = 1



    def set_rate(self, heartrate):
        self.heartrate = heartrate
        if(self.cardiacarrest == True):
          #self.img = pygame.image.load("\\\e042000h1\\2020\\20acgarvi\\My Documents\\smamtDummy\\VFib.png")
          self.img = pygame.image.load(os.path.join(pathlib.Path(__file__).parent.absolute(),"VFib.png"))
          self.y = self.sylist[3]
        elif(heartrate <= 60):
          #self.img = pygame.image.load("\\\e042000h1\\2020\\20acgarvi\\My Documents\\smamtDummy\\Sinus Bradycardia.png")
          self.img = pygame.image.load(os.path.join(pathlib.Path(__file__).parent.absolute(),"Sinus Bradycardia.png"))
          self.y = self.sylist[1]
        elif(heartrate > 60 and heartrate < 100):
          #self.img = pygame.image.load("\\\e042000h1\\2020\\20acgarvi\\My Documents\\smamtDummy\\Sinus Rhythm.png")
          self.img = pygame.image.load(os.path.join(pathlib.Path(__file__).parent.absolute(),"Sinus Rhythm.png"))
          self.y = self.sylist[0]
        elif(heartrate >= 100):
          #self.img = pygame.image.load("\\\e042000h1\\2020\\20acgarvi\\My Documents\\smamtDummy\\Sinus Tachycardia.png")
          self.img = pygame.image.load(os.path.join(pathlib.Path(__file__).parent.absolute(),"Sinus Tachycardia.png"))
          self.y = self.sylist[2]
        self.rect = self.img.get_rect()

    #b is a boolean
    def arrest(self, b):
      self.cardiacarrest = b
      self.set_rate(self.heartrate)

    def tick(self):
        displayconst = pygame.display.get_surface().get_size()
        #1280 x 720
        self.xratio = (displayconst[0] / 1280)
        self.yratio = (displayconst[1] / 720)

        img_width = self.rect.width
        if(self.cardiacarrest == True):
          self.x += (self.heartrate/(60/0.1))*self.xratio
        if(self.heartrate <= 60):
          self.x += (self.heartrate/(30/0.22))*self.xratio
        if(self.heartrate > 60 and self.heartrate < 100):
          self.x += (self.heartrate/(60/0.3))*self.xratio
        if(self.heartrate >= 100):
          self.x += (self.heartrate/(120/0.3))*self.xratio

        #print(self.heartrate/(60/0.3))
        if (self.x+5 > img_width):
            self.sx += self.x
            self.x=0
        if (self.x+self.sx > self.max_x):
            self.sx=0-self.x

    def blit(self):
        ##Resp. Rate Box vvvv
        pygame.draw.rect(screen, BLACK, (wRatio(20),hRatio(340),wRatio(300),hRatio(200)))
        pygame.draw.line(screen, BLACK, [wRatio(20), hRatio(340)], [wRatio(20), hRatio(540)],3)
        pygame.draw.line(screen, BLACK, [wRatio(320), hRatio(340)], [wRatio(320), hRatio(540)],3)
        pygame.draw.line(screen, BLACK, [wRatio(20), hRatio(340)], [wRatio(320), hRatio(340)],3)
        pygame.draw.line(screen, BLACK, [wRatio(20), hRatio(540)], [wRatio(320), hRatio(540)],3)
        img_height = self.rect.height
        self.parent.blit(self.img, (round((self.x*self.xratio)+(self.sx*self.xratio)), round(self.y*self.yratio)),
                                    (round(self.x),0,round(10*self.xratio),round(img_height*self.yratio)))


ecg = ECG(screen, heart_rate, (wRatio(20),hRatio(340),wRatio(300),hRatio(200)))

#############
'File finder'
#############
def mainpath():
    if platform.system() == "Windows":
        f = "C:\\Users"
    elif platform.system() == "Darwin":
        f = "/Users"
    elif platform.system() == "Linux":
        f = None
    else:
        print("System not found!")
    return pathlib.Path(f).glob('**/*')


def search(path, file):
    for x in path:
        if (x.name == file):
            return x

def findImage(file):
    m = mainpath()
    fname = search(m, file)
    print(fname)
    print("Done")




#########
'Buttons'
#########
buttons = {

}

#♪
"""
Scenes:
~Status Page
~Saved Data
"""
#The below is a list of buttons on each scene
#It is important that whenever a new button is created it is added below because the below
#list is used to render the buttons on the screen
scene_status_page_buttons = ['switchToData', 'right arrow 1', 'left arrow 1', 'right arrow 2', 'left arrow 2', 'right arrow 3', 'left arrow 3', 'right arrow 4', 'left arrow 4', 'play button', 'pause button', 'box1_1', 'box1_2', 'box1_3', 'box1_4', 'finger_led_on', 'finger_led_off','mouth_led_on','mouth_led_off','heart_up', 'heart_down', 'card_arrest_on','card_arrest_off', 'fingernail_options', 'finger_left', 'finger_right']
scene_data_page_buttons = ['Text Box Top','Text Box Middle Top','Text Box Middle Bottom','Text Box Bottom', 'switchToStatus']


def load_buttons(scene_name):
  #The following if statements help render buttons based on what screen is active
  if scene_name == "Status Page":
    for button in scene_status_page_buttons:
      x, y, w, h, color1, color2 = buttons[button]
      load_button(x, y, h, w, color1, color2)
  elif scene_name == "Data Page":
    for button in scene_data_page_buttons:
      x, y, w, h, color1, color2 = buttons[button]
      load_button(x, y, h, w, color1, color2)


def load_button(x, y, h, w, color1, color2):
  #The folowing renders the button image onto the screen
  new_tuple = (int(x),int(y),int(h),int(w))
  pygame.draw.rect(screen, color1, new_tuple)

#The following returns a list of the button x, y, h, and w values
def get_button_stats(button_name):
  x, y, h, w, color1, color2 = buttons[button_name]
  return [x, y, h, w]


###################
'Button creation'
###################
#The following is a duplicate list and should be merged with the above version
scene_status_page_buttons = ['save data', 'Sound Selection 1','Sound Selection 2', 'Sound Selection 3', 'Sound Selection 4', 'Sound Selection 5', 'Sound Selection 6','Sound Selection 7', 'Sound Selection 8','Sound Selection 9', 'switchToData','right arrow 1', 'left arrow 1', 'right arrow 2', 'left arrow 2', 'right arrow 3', 'left arrow 3', 'right arrow 4', 'left arrow 4', 'play button', 'pause button', 'box1_1', 'box1_2', 'box1_3', 'box1_4', 'finger_led_on','mouth_led_on','mouth_led_off','heart_up', 'heart_down', 'card_arrest_on','card_arrest_off', 'fingernail_options', 'finger_left', 'finger_right' ]
#Condensed function to add a new button to the scene
def add_button(button_name, x, y, w, h, color1, color2):
  buttons.update( {button_name : [x, y, h, w, color1, color2],} )

def buttonAddUpdate(scenePage):
  if scenePage == "Status Page":
    #Top right arrows vvv
    add_button('right arrow 1', str(wRatio(1850)), str(hRatio(130)), str(wRatio(30)), str(hRatio(30)), MEDIUM_GREY, MEDIUM_GREY)
    add_button('left arrow 1', str(wRatio(1810)), str(hRatio(130)), str(wRatio(30)), str(hRatio(30)), MEDIUM_GREY, MEDIUM_GREY)
    #Middle right arrows vvv
    add_button('right arrow 2', str(wRatio(1850)), str(hRatio(450)), str(wRatio(30)), str(hRatio(30)), MEDIUM_GREY, MEDIUM_GREY)
    add_button('left arrow 2', str(wRatio(1810)), str(hRatio(450)), str(wRatio(30)), str(hRatio(30)), MEDIUM_GREY, MEDIUM_GREY)
    #Bottom right arrows vvv
    add_button('right arrow 3', str(wRatio(1850)), str(hRatio(770)), str(wRatio(30)), str(hRatio(30)), MEDIUM_GREY, MEDIUM_GREY)
    add_button('left arrow 3', str(wRatio(1810)), str(hRatio(770)), str(wRatio(30)), str(hRatio(30)), MEDIUM_GREY, MEDIUM_GREY)
    #Bottom Left arrows vvv
    add_button('right arrow 4', str(wRatio(270)), str(hRatio(570)), str(wRatio(30)), str(hRatio(30)), MEDIUM_GREY, MEDIUM_GREY)
    add_button('left arrow 4', str(wRatio(230)), str(hRatio(570)), str(wRatio(30)), str(hRatio(30)), MEDIUM_GREY, MEDIUM_GREY)
    #Controls the clock vvv
    add_button('play button', str(wRatio(140)), str(hRatio(30)), str(wRatio(40)), str(hRatio(40)), MEDIUM_GREY, MEDIUM_GREY)
    add_button('pause button', str(wRatio(80)), str(hRatio(30)), str(wRatio(40)), str(hRatio(40)), MEDIUM_GREY, MEDIUM_GREY)
    #The buttons on the bottom of the screen that control the LEDs
    add_button('finger_led_on', str(wRatio(720)), str(hRatio(850)), str(wRatio(100)), str(hRatio(43)), MEDIUM_GREY, MEDIUM_GREY)
    add_button('mouth_led_on', str(wRatio(770)) , str(hRatio(915)) , str(wRatio(50)) ,str(hRatio(43)), MEDIUM_GREY, MEDIUM_GREY)
    add_button('mouth_led_off', str(wRatio(720)) , str(hRatio(915)) , str(wRatio(50)) ,str(hRatio(43)), MEDIUM_GREY, MEDIUM_GREY)
    #The buttons that control the heartrate
    add_button('heart_up', str(wRatio(850)) , str(hRatio(170)) , str(wRatio(30)) ,str(hRatio(20)), MEDIUM_GREY, MEDIUM_GREY)
    add_button('heart_down', str(wRatio(850)) , str(hRatio(190)) , str(wRatio(30)) ,str(hRatio(20)), MEDIUM_GREY, MEDIUM_GREY)
    #The switch that controls cardiac arrest
    add_button('card_arrest_on', str(wRatio(780)) , str(hRatio(230)) , str(wRatio(50)) ,str(hRatio(45)), MEDIUM_GREY, MEDIUM_GREY)
    add_button('card_arrest_off', str(wRatio(825)) , str(hRatio(230)) , str(wRatio(50)) ,str(hRatio(45)), MEDIUM_GREY, MEDIUM_GREY)
    #The buttons on the bottom of the screen that control the LEDs more in-depth
    add_button('fingernail_options', str(wRatio(890)) , str(hRatio(795)) , str(wRatio(110)) ,str(hRatio(40)), MEDIUM_GREY, MEDIUM_GREY)
    add_button('finger_left', str(wRatio(1160)), str(hRatio(850)), str(wRatio(100)), str(hRatio(43)), MEDIUM_GREY, MEDIUM_GREY)
    add_button('finger_right', str(wRatio(1160)) , str(hRatio(915)) , str(wRatio(100)) ,str(hRatio(43)), MEDIUM_GREY, MEDIUM_GREY)


    ###Top right box buttons
    add_button('box1_1', str(wRatio(1505)), str(hRatio(175)), str(wRatio(390)), str(hRatio(60)), WHITE, WHITE)
    add_button('box1_2', str(wRatio(1505)), str(hRatio(235)), str(wRatio(390)), str(hRatio(60)), WHITE, WHITE)
    add_button('box1_3', str(wRatio(1505)), str(hRatio(295)), str(wRatio(390)), str(hRatio(60)), WHITE, WHITE)
    add_button('box1_4', str(wRatio(1505)), str(hRatio(355)), str(wRatio(390)), str(hRatio(60)), WHITE, WHITE)

    ###Middle right box buttons
    add_button('box2_1', str(wRatio(1505)), str(hRatio(495)), str(wRatio(390)), str(hRatio(60)), WHITE, WHITE)
    add_button('box2_2', str(wRatio(1505)), str(hRatio(555)), str(wRatio(390)), str(hRatio(60)), WHITE, WHITE)
    add_button('box2_3', str(wRatio(1505)), str(hRatio(615)), str(wRatio(390)), str(hRatio(60)), WHITE, WHITE)
    add_button('box2_4', str(wRatio(1505)), str(hRatio(675)), str(wRatio(390)), str(hRatio(60)), WHITE, WHITE)

    ###Bottom right box buttons
    add_button('box3_1', str(wRatio(1505)), str(hRatio(815)), str(wRatio(390)), str(hRatio(60)), WHITE, WHITE)
    add_button('box3_2', str(wRatio(1505)), str(hRatio(875)), str(wRatio(390)), str(hRatio(60)), WHITE, WHITE)
    add_button('box3_3', str(wRatio(1505)), str(hRatio(935)), str(wRatio(390)), str(hRatio(60)), WHITE, WHITE)


    ###Bottom left box buttons
    add_button('box4_1', str(wRatio(25)), str(hRatio(615)), str(wRatio(290)), str(hRatio(60)), WHITE, WHITE)
    add_button('box4_2', str(wRatio(25)), str(hRatio(675)), str(wRatio(290)), str(hRatio(60)), WHITE, WHITE)
    add_button('box4_3', str(wRatio(25)), str(hRatio(735)), str(wRatio(290)), str(hRatio(60)), WHITE, WHITE)
    add_button('box4_4', str(wRatio(25)), str(hRatio(795)), str(wRatio(290)), str(hRatio(60)), WHITE, WHITE)
    add_button('box4_5', str(wRatio(25)), str(hRatio(855)), str(wRatio(290)), str(hRatio(60)), WHITE, WHITE)
    add_button('box4_6', str(wRatio(25)), str(hRatio(915)), str(wRatio(290)), str(hRatio(60)), WHITE, WHITE)

    ###Switch Scenes (In the top right)
    add_button('switchToData', str(wRatio(1700)), str(hRatio(20)), str(wRatio(200)), str(hRatio(60)), WHITE, WHITE)

    #Save Data Button
    add_button('save data', str(wRatio(1500)), str(hRatio(20)), str(wRatio(150)), str(hRatio(60)), WHITE, WHITE)

    ###Sound Selection Buttons
    add_button('Sound Selection 1', str(wRatio(433)), str(hRatio(283)), str(wRatio(441)), str(hRatio(60)), WHITE, WHITE)
    add_button('Sound Selection 2', str(wRatio(433)), str(hRatio(343)), str(wRatio(441)), str(hRatio(60)), WHITE, WHITE)
    add_button('Sound Selection 3', str(wRatio(433)), str(hRatio(403)), str(wRatio(441)), str(hRatio(60)), WHITE, WHITE)
    add_button('Sound Selection 4', str(wRatio(433)), str(hRatio(463)), str(wRatio(441)), str(hRatio(60)), WHITE, WHITE)
    add_button('Sound Selection 5', str(wRatio(433)), str(hRatio(523)), str(wRatio(441)), str(hRatio(60)), WHITE, WHITE)
    add_button('Sound Selection 6', str(wRatio(433)), str(hRatio(583)), str(wRatio(441)), str(hRatio(60)), WHITE, WHITE)
    add_button('Sound Selection 7', str(wRatio(433)), str(hRatio(643)), str(wRatio(441)), str(hRatio(60)), WHITE, WHITE)
    add_button('Sound Selection 8', str(wRatio(433)), str(hRatio(703)), str(wRatio(441)), str(hRatio(45)), WHITE, WHITE)
    add_button('Sound Selection 9', str(wRatio(433)), str(hRatio(748)), str(wRatio(441)), str(hRatio(45)), WHITE, WHITE)

  if scenePage == "Data Page":
    ###Text Boxes
    #Name
    add_button("Text Box Top", str(wRatio(175)), str(hRatio(200)), str(wRatio(400)), str(hRatio(60)), WHITE, BLACK)
    #Dates
    add_button("Text Box Middle Top", str(wRatio(175)), str(hRatio(350)), str(wRatio(400)), str(hRatio(60)), WHITE, BLACK)
    add_button("Text Box Middle Bottom", str(wRatio(175)), str(hRatio(500)), str(wRatio(400)), str(hRatio(60)), WHITE, BLACK)
    #Comments
    add_button("Text Box Bottom", str(wRatio(175)), str(hRatio(650)), str(wRatio(400)), str(hRatio(250)), WHITE, BLACK)
    ###Switch Scenes (In the top right)
    add_button('switchToStatus', str(wRatio(1700)), str(hRatio(20)), str(wRatio(200)), str(hRatio(60)), MEDIUM_GREY, WHITE)
    #Creates buttons to read from the right-side selection box
    for i in range(0,10):
      add_button("Data Option " + str(i + 1), str(wRatio(775)), str(hRatio(200 + 70 * i)), str(wRatio(845)), str(hRatio(70)), WHITE, BLACK)
      scene_data_page_buttons.append("Data Option " + str(i + 1))







###################
'Scene Backgrounds'
###################
def load_scene(scene_name):
  global soundBoxPage, heart_rate, card_on, mouth_on
  if scene_name == "Status Page":
    #Preps all of the buttons for the scene
    buttonAddUpdate("Status Page")
    load_buttons("Status Page")
    #Renders the background shapes
    pygame.draw.rect(screen, WHITE, (wRatio(0),hRatio(0),wRatio(1920),hRatio(1050)))
    pygame.draw.rect(screen, MEDIUM_GREY, (wRatio(0),hRatio(0),wRatio(1920),hRatio(100)))
    pygame.draw.rect(screen, MEDIUM_GREY, (wRatio(20),hRatio(560),wRatio(300),hRatio(50)))
    pygame.draw.rect(screen, WHITE, (wRatio(20),hRatio(610),wRatio(300),hRatio(400)))
    pygame.draw.rect(screen, MEDIUM_GREY, (wRatio(420),hRatio(120),wRatio(980),hRatio(890)))
    pygame.draw.line(screen, BLACK, [wRatio(0),hRatio(0)],[wRatio(1920),hRatio(0)], 3)
    pygame.draw.line(screen, BLACK, [wRatio(0),hRatio(0)],[wRatio(0),hRatio(100)],3)
    pygame.draw.line(screen, BLACK, [wRatio(0),hRatio(100)],[wRatio(1920),hRatio(100)],3)
    pygame.draw.line(screen, BLACK, [wRatio(1920),hRatio(0)],[wRatio(1920),hRatio(100)],3)
    pygame.draw.line(screen, BLACK, [wRatio(18), hRatio(560)], [wRatio(18), hRatio(1010)], 3)
    pygame.draw.line(screen, BLACK,[wRatio(321),hRatio(560)], [wRatio(321),hRatio(1010)], 3)
    pygame.draw.aaline(screen, BLACK, [wRatio(18),hRatio(560)],[wRatio(321), hRatio(560)], False)
    pygame.draw.aaline(screen, BLACK, [wRatio(18),hRatio(1010)],[wRatio(321), hRatio(1010)], False)
    pygame.draw.aaline(screen, BLACK, [wRatio(18),hRatio(610)],[wRatio(321), hRatio(610)], False)

    #Middle Box Border Lines vvvv
    pygame.draw.line(screen, BLACK, [wRatio(420),hRatio(120)], [wRatio(420 + 980),hRatio(120)],3)
    pygame.draw.line(screen, BLACK, [wRatio(420),hRatio(120)], [wRatio(420),hRatio(120 + 890)],3)
    pygame.draw.line(screen, BLACK, [wRatio(420),hRatio(120 + 890)], [wRatio(420 + 980),hRatio(120 + 890)],3)
    pygame.draw.line(screen, BLACK, [wRatio(420 + 980),hRatio(120)], [wRatio(420 + 980),hRatio(120 + 890)],3)
    ##Heart Rate Box vvvv
    pygame.draw.rect(screen, BLACK, (wRatio(20),hRatio(120),wRatio(300),hRatio(200)))
    pygame.draw.line(screen, BLACK, [wRatio(20),hRatio(120)], [wRatio(20), hRatio(320)], 3)
    pygame.draw.line(screen, BLACK, [wRatio(320),hRatio(120)], [wRatio(320), hRatio(320)], 3)
    pygame.draw.line(screen, BLACK, [wRatio(20),hRatio(120)], [wRatio(320), hRatio(120)], 3)
    pygame.draw.line(screen, BLACK, [wRatio(20),hRatio(320)], [wRatio(320), hRatio(320)], 3)
    ##Resp. Rate Box vvvv
    pygame.draw.rect(screen, BLACK, (wRatio(20),hRatio(340),wRatio(300),hRatio(200)))
    pygame.draw.line(screen, BLACK, [wRatio(20), hRatio(340)], [wRatio(20), hRatio(540)],3)
    pygame.draw.line(screen, BLACK, [wRatio(320), hRatio(340)], [wRatio(320), hRatio(540)],3)
    pygame.draw.line(screen, BLACK, [wRatio(20), hRatio(340)], [wRatio(320), hRatio(340)],3)
    pygame.draw.line(screen, BLACK, [wRatio(20), hRatio(540)], [wRatio(320), hRatio(540)],3)

    ###Sound Box
    updateSoundBoxPage()

    ##Top right box vvvv
    pygame.draw.rect(screen, MEDIUM_GREY, (wRatio(1500),hRatio(120),wRatio(400),hRatio(50)))
    pygame.draw.rect(screen, WHITE, (wRatio(1500),hRatio(170),wRatio(400),hRatio(250)))
    pygame.draw.line(screen, BLACK, [wRatio(1500), hRatio(120)], [wRatio(1500), hRatio(420)], 3)
    pygame.draw.line(screen, BLACK,[wRatio(1900),hRatio(120)], [wRatio(1900),hRatio(420)], 3)
    pygame.draw.aaline(screen, BLACK, [wRatio(1500),hRatio(120)],[wRatio(1900), hRatio(120)], False)
    pygame.draw.aaline(screen, BLACK, [wRatio(1500),hRatio(170)],[wRatio(1900), hRatio(170)], False)
    pygame.draw.aaline(screen, BLACK, [wRatio(1500),hRatio(420)],[wRatio(1900), hRatio(420)], False)
    ##Middle right box vvvv
    pygame.draw.rect(screen, MEDIUM_GREY, (wRatio(1500),hRatio(440),wRatio(400),hRatio(50)))
    pygame.draw.rect(screen, WHITE, (wRatio(1500),hRatio(490),wRatio(400),hRatio(250)))
    pygame.draw.line(screen, BLACK, [wRatio(1500), hRatio(440)], [wRatio(1500), hRatio(740)], 3)
    pygame.draw.line(screen, BLACK,[wRatio(1900),hRatio(440)], [wRatio(1900),hRatio(740)], 3)
    pygame.draw.aaline(screen, BLACK, [wRatio(1500),hRatio(440)],[wRatio(1900), hRatio(440)], False)
    pygame.draw.aaline(screen, BLACK, [wRatio(1500),hRatio(490)],[wRatio(1900), hRatio(490)], False)
    pygame.draw.aaline(screen, BLACK, [wRatio(1500),hRatio(740)],[wRatio(1900), hRatio(740)], False)



    ##Bottom Right Box vvvv
    pygame.draw.rect(screen, MEDIUM_GREY, (wRatio(1500),hRatio(760),wRatio(400),hRatio(50)))
    pygame.draw.rect(screen, WHITE, (wRatio(1500),hRatio(810),wRatio(400),hRatio(200)))
    pygame.draw.line(screen, BLACK, [wRatio(1500), hRatio(760)], [wRatio(1500), hRatio(1010)], 3)
    pygame.draw.line(screen, BLACK,[wRatio(1900),hRatio(760)], [wRatio(1900),hRatio(1010)], 3)
    pygame.draw.aaline(screen, BLACK, [wRatio(1500),hRatio(760)],[wRatio(1900), hRatio(760)], False)
    pygame.draw.aaline(screen, BLACK, [wRatio(1500),hRatio(810)],[wRatio(1900),hRatio(810)], False)
    pygame.draw.aaline(screen, BLACK, [wRatio(1500),hRatio(1010)],[wRatio(1900), hRatio(1010)], False)

    ###Section Titles
    drawSectionText(screen, "Events", WHITE, (wRatio(25),hRatio(566),wRatio(393),hRatio(57)), writing_font)
    drawSectionText(screen, "Conditions", WHITE, (wRatio(1505),hRatio(126),wRatio(393),hRatio(57)), writing_font)
    drawSectionText(screen, "Medicines", WHITE, (wRatio(1505),hRatio(446),wRatio(393),hRatio(57)), writing_font)
    drawSectionText(screen, "Scenarios", WHITE, (wRatio(1505),hRatio(766),wRatio(393),hRatio(57)), writing_font)
    #Draws all of the triangle images for the arrows on the top of the boxes
    pygame.draw.polygon(screen, WHITE, [[wRatio(1850), hRatio(130)], [wRatio(1850), hRatio(160)], [wRatio(1880), hRatio(145)]], 4)
    pygame.draw.polygon(screen, WHITE, [[wRatio(1840), hRatio(130)], [wRatio(1840), hRatio(160)], [wRatio(1810), hRatio(145)]], 4)
    pygame.draw.polygon(screen, WHITE, [[wRatio(1850), hRatio(450)], [wRatio(1850), hRatio(480)], [wRatio(1880), hRatio(465)]], 4)
    pygame.draw.polygon(screen, WHITE, [[wRatio(1840), hRatio(450)], [wRatio(1840), hRatio(480)], [wRatio(1810), hRatio(465)]], 4)
    pygame.draw.polygon(screen, WHITE, [[wRatio(1850), hRatio(770)], [wRatio(1850), hRatio(800)], [wRatio(1880), hRatio(785)]], 4)
    pygame.draw.polygon(screen, WHITE, [[wRatio(1840), hRatio(770)], [wRatio(1840), hRatio(800)], [wRatio(1810), hRatio(785)]], 4)
    pygame.draw.polygon(screen, WHITE, [[wRatio(270), hRatio(570)], [wRatio(270), hRatio(600)], [wRatio(300), hRatio(585)]], 4)
    pygame.draw.polygon(screen, WHITE, [[wRatio(260), hRatio(570)], [wRatio(260), hRatio(600)], [wRatio(230), hRatio(585)]], 4)

    ### Draws the button images that control the clock
    pygame.draw.circle(screen, AQUA, [wRatio(100), hRatio(50)], wRatio(20))
    pygame.draw.circle(screen, AQUA, [wRatio(160), hRatio(50)], wRatio(20))
    pygame.draw.polygon(screen, BLACK, [[wRatio(150), hRatio(37)], [wRatio(150), hRatio(57)], [wRatio(178), hRatio(47)]], 3)
    pygame.draw.line(screen, BLACK, [wRatio(95), hRatio(35)], [wRatio(95), hRatio(60)], 5)
    pygame.draw.line(screen, BLACK,[wRatio(105),hRatio(35)], [wRatio(105),hRatio(60)], 5)
    ###

#### LED Controls
    drawSectionText(screen, "LED CONTROL ", WHITE, (wRatio(430),hRatio(795),wRatio(110),hRatio(40)), writing_font)
    drawSectionText(screen, "OPTIONS ", WHITE, (wRatio(890),hRatio(795),wRatio(110),hRatio(40)), writing_font)
    pygame.draw.line(screen, WHITE, [wRatio(430),hRatio(845)], [wRatio(430), hRatio(895)], 3)
    pygame.draw.line(screen, WHITE,[wRatio(830),hRatio(845)], [wRatio(830),hRatio(895)], 3)
    pygame.draw.aaline(screen, WHITE, [wRatio(430),hRatio(845)],[wRatio(830), hRatio(845)], False)
    pygame.draw.aaline(screen, WHITE, [wRatio(430),hRatio(895)],[wRatio(830), hRatio(895)], False)

    pygame.draw.line(screen, WHITE, [wRatio(430),hRatio(910)], [wRatio(430), hRatio(960)], 3)
    pygame.draw.line(screen, WHITE,[wRatio(830),hRatio(910)], [wRatio(830),hRatio(960)], 3)
    pygame.draw.aaline(screen, WHITE, [wRatio(430),hRatio(910)],[wRatio(830), hRatio(910)], False)
    pygame.draw.aaline(screen, WHITE, [wRatio(430),hRatio(960)],[wRatio(830), hRatio(960)], False)
      ##### Turn on left tear switch ( left )
    #pygame.draw.rect(screen, WHITE, (wRatio(720),hRatio(850),wRatio(50),hRatio(43)))
    pygame.draw.line(screen, BLACK, [wRatio(720),hRatio(850)], [wRatio(720), hRatio(890)], 3)
    pygame.draw.line(screen, BLACK,[wRatio(770),hRatio(850)], [wRatio(770),hRatio(890)], 3)
    pygame.draw.aaline(screen, BLACK, [wRatio(720),hRatio(850)],[wRatio(770), hRatio(850)], False)
    pygame.draw.aaline(screen, BLACK, [wRatio(720),hRatio(890)],[wRatio(770), hRatio(890)], False)
      ##### Turn off right tear switch ( left )
    #pygame.draw.rect(screen, MEDIUM_GREY, (wRatio(770),hRatio(850),wRatio(50),hRatio(40)))
    pygame.draw.line(screen, BLACK, [wRatio(770),hRatio(850)], [wRatio(770), hRatio(890)], 3)
    pygame.draw.line(screen, BLACK,[wRatio(820),hRatio(850)], [wRatio(820),hRatio(890)], 3)
    pygame.draw.aaline(screen, BLACK, [wRatio(770),hRatio(850)],[wRatio(820), hRatio(850)], False)
    pygame.draw.aaline(screen, BLACK, [wRatio(770),hRatio(890)],[wRatio(820), hRatio(890)], False)
        ##### Turn off left tear switch ( right )
    #pygame.draw.rect(screen, WHITE, (wRatio(720),hRatio(915),wRatio(50),hRatio(40)))
    pygame.draw.line(screen, BLACK, [wRatio(720),hRatio(915)], [wRatio(720), hRatio(955)], 3)
    pygame.draw.line(screen, BLACK,[wRatio(770),hRatio(915)], [wRatio(770),hRatio(955)], 3)
    pygame.draw.aaline(screen, BLACK, [wRatio(720),hRatio(915)],[wRatio(770), hRatio(915)], False)
    pygame.draw.aaline(screen, BLACK, [wRatio(720),hRatio(955)],[wRatio(770), hRatio(955)], False)
      ##### Turn on right tear switch ( right )
    #pygame.draw.rect(screen, MEDIUM_GREY, (wRatio(770),hRatio(915),wRatio(50),hRatio(43)))
    pygame.draw.line(screen, BLACK, [wRatio(770),hRatio(915)], [wRatio(770), hRatio(955)], 3)
    pygame.draw.line(screen, BLACK,[wRatio(820),hRatio(915)], [wRatio(820),hRatio(955)], 3)
    pygame.draw.aaline(screen, BLACK, [wRatio(770),hRatio(915)],[wRatio(820), hRatio(915)], False)
    pygame.draw.aaline(screen, BLACK, [wRatio(770),hRatio(955)],[wRatio(820), hRatio(955)], False)

    #### Heart control
    drawSectionText(screen, " HEART ", WHITE, (wRatio(430),hRatio(128),wRatio(110),hRatio(40)), writing_font)
    pygame.draw.line(screen, WHITE, [wRatio(430),hRatio(168)], [wRatio(430), hRatio(213)], 1)
    pygame.draw.line(screen, WHITE,[wRatio(875),hRatio(168)], [wRatio(875),hRatio(213)], 1)
    pygame.draw.aaline(screen, WHITE, [wRatio(430),hRatio(168)],[wRatio(875), hRatio(168)], False)
    pygame.draw.aaline(screen, WHITE, [wRatio(430),hRatio(213)],[wRatio(875), hRatio(213)], False)
    pygame.draw.polygon(screen, WHITE, [[wRatio(850), hRatio(187)], [ wRatio(860), hRatio(170)], [wRatio(870), hRatio(187)]], 2)
    pygame.draw.polygon(screen, WHITE, [[wRatio(850), hRatio(193)], [ wRatio(860), hRatio(210)], [wRatio(870), hRatio(193)]], 2)

    pygame.draw.line(screen, WHITE, [wRatio(430),hRatio(223)], [wRatio(430), hRatio(268)], 1)
    pygame.draw.line(screen, WHITE,[wRatio(875),hRatio(223)], [wRatio(875),hRatio(268)], 1)
    pygame.draw.aaline(screen, WHITE, [wRatio(430),hRatio(223)],[wRatio(875), hRatio(223)], False)
    pygame.draw.aaline(screen, WHITE, [wRatio(430),hRatio(268)],[wRatio(875), hRatio(268)], False)
    #pygame.draw.rect(screen, WHITE, (wRatio(775),hRatio(223),wRatio(101),hRatio(47)))
    #pygame.draw.rect(screen, MEDIUM_GREY, (wRatio(778),hRatio(225),wRatio(50),hRatio(43)))
    '''
    pygame.draw.rect(screen, WHITE, (wRatio(775),hRatio(223),wRatio(101),hRatio(47)))

    pygame.draw.polygon(screen, WHITE, [[wRatio(850), hRatio(241)], [ wRatio(860), hRatio(225)], [wRatio(870), hRatio(241)]], 2)
    pygame.draw.polygon(screen, WHITE, [[wRatio(850), hRatio(247)], [ wRatio(860), hRatio(265)], [wRatio(870), hRatio(247)]], 2)
    '''

       #### Initial Description
    drawTextComic20(screen, left, WHITE, ((wRatio(440),hRatio(855),wRatio(220),hRatio(40))), writing_font)
    drawTextComic20(screen, right, WHITE, ((wRatio(440),hRatio(920),wRatio(220),hRatio(40))), writing_font)
    drawTextComic20(screen, ['Heart Rate'], WHITE, ((wRatio(440),hRatio(175), wRatio(120), hRatio(40))), writing_font)
    drawTextComic20(screen, ['bpm'], WHITE, ((wRatio(795),hRatio(185), wRatio(40), hRatio(30))), writing_font)
    drawTextComic20(screen, ['Activate Cardiac Arrest'], WHITE, ((wRatio(440),hRatio(230), wRatio(230), hRatio(40))), writing_font)
    drawTextComic20(screen, ['OFF'], MEDIUM_GREY, ((wRatio(833),hRatio(231), wRatio(30), hRatio(20))), writing_font)
    drawTextComic20(screen, ['OFF'], MEDIUM_GREY, ((wRatio(725),hRatio(855),wRatio(45),hRatio(30))), writing_font)
    drawTextComic20(screen, ['OFF'], MEDIUM_GREY, ((wRatio(725),hRatio(920),wRatio(45),hRatio(30))), writing_font)
    drawTextComic20(screen, [str(heart_rate)], WHITE,(wRatio(760),hRatio(175),wRatio(45), hRatio(55)) , writing_font)

    #### Image
    pygame.draw.rect(screen,WHITE,(wRatio(890),hRatio(128),wRatio(505),hRatio(663)))
    pygame.draw.line(screen, BLACK, [wRatio(890),hRatio(128)],[wRatio(1395),hRatio(128)],3)
    pygame.draw.line(screen, BLACK, [wRatio(890),hRatio(791)],[wRatio(1395),hRatio(791)],3)
    pygame.draw.line(screen, BLACK, [wRatio(890),hRatio(128)],[wRatio(890),hRatio(791)],3)
    pygame.draw.line(screen, BLACK, [wRatio(1395),hRatio(128)],[wRatio(1395),hRatio(791)],3)





    ##### Switch Scenes
    pygame.draw.rect(screen, WHITE, ((wRatio(1700)), (hRatio(20)), (wRatio(200)), (hRatio(60))))
    pygame.draw.line(screen, BLACK, [wRatio(1700), hRatio(20)],[wRatio(1900), hRatio(20)],3)
    pygame.draw.line(screen, BLACK, [wRatio(1700), hRatio(20)],[wRatio(1700), hRatio(80)],3)
    pygame.draw.line(screen, BLACK, [wRatio(1700), hRatio(80)],[wRatio(1900), hRatio(80)],3)
    pygame.draw.line(screen, BLACK, [wRatio(1900), hRatio(20)],[wRatio(1900), hRatio(80)],3)
    drawTextComic20(screen, ["Go to Data Page"],BLACK, (wRatio(1725), hRatio(35), wRatio(150), hRatio(80)),writing_font)

    ##### Save Data
    pygame.draw.rect(screen, WHITE, ((wRatio(1500)), (hRatio(20)), (wRatio(150)), (hRatio(60))))
    pygame.draw.line(screen, BLACK, [wRatio(1500), hRatio(20)],[wRatio(1650), hRatio(20)],3)
    pygame.draw.line(screen, BLACK, [wRatio(1500), hRatio(20)],[wRatio(1500), hRatio(80)],3)
    pygame.draw.line(screen, BLACK, [wRatio(1500), hRatio(80)],[wRatio(1650), hRatio(80)],3)
    pygame.draw.line(screen, BLACK, [wRatio(1650), hRatio(20)],[wRatio(1650), hRatio(80)],3)
    drawTextComic20(screen, ["Save Data"],BLACK, (wRatio(1525), hRatio(35), wRatio(150), hRatio(80)),writing_font)

    image = pygame.image.load(os.path.join(pathlib.Path(__file__).parent.absolute(),"Man.png"))
    rect = image.get_rect()
    scalar = pygame.transform.scale(image, (int((rect.width/1280)*pygame.display.get_surface().get_size()[0]),
                                   int((rect.height/720)*pygame.display.get_surface().get_size()[1])))


    screen.blit(scalar, (wRatio(960),hRatio(150)))

    if card_on:
      cd_arrest_on()
    else:
      cd_arrest_off()
    if mouth_on:
      led_mouth()
    else:
      led_mouth_off()
    on_off_left_tear()

    pygame.display.update()

  elif scene_name == "Data Page":
    buttonAddUpdate("Data Page")
    load_buttons("Data Page")
    pygame.draw.rect(screen, WHITE, (wRatio(0),hRatio(0),wRatio(1920),hRatio(1050)))
    pygame.draw.rect(screen, MEDIUM_GREY, (wRatio(100),hRatio(100),wRatio(1720),hRatio(850)))
    pygame.draw.line(screen, BLACK, [wRatio(100), hRatio(100)],[wRatio(1820), hRatio(100)],3)
    pygame.draw.line(screen, BLACK, [wRatio(100), hRatio(100)],[wRatio(100), hRatio(950)],3)
    pygame.draw.line(screen, BLACK, [wRatio(100), hRatio(950)],[wRatio(1820), hRatio(950)],3)
    pygame.draw.line(screen, BLACK, [wRatio(1820), hRatio(100)],[wRatio(1820), hRatio(950)],3)
    #Name vvvv
    pygame.draw.rect(screen, WHITE, (wRatio(175),hRatio(200),wRatio(400),hRatio(60)))
    pygame.draw.line(screen, BLACK, [wRatio(175), hRatio(200)],[wRatio(575), hRatio(200)],3)
    pygame.draw.line(screen, BLACK, [wRatio(175), hRatio(200)],[wRatio(175), hRatio(260)],3)
    pygame.draw.line(screen, BLACK, [wRatio(175), hRatio(260)],[wRatio(575), hRatio(260)],3)
    pygame.draw.line(screen, BLACK, [wRatio(575), hRatio(200)],[wRatio(575), hRatio(260)],3)
    drawSectionText(screen, "Name ", WHITE, (wRatio(175),hRatio(170),wRatio(400),hRatio(60)), writing_font)
    #Date of last accessed vvvv
    pygame.draw.rect(screen, WHITE, (wRatio(175),hRatio(350),wRatio(400),hRatio(60)))
    pygame.draw.line(screen, BLACK, [wRatio(175), hRatio(350)],[wRatio(575), hRatio(350)],3)
    pygame.draw.line(screen, BLACK, [wRatio(175), hRatio(350)],[wRatio(175), hRatio(410)],3)
    pygame.draw.line(screen, BLACK, [wRatio(175), hRatio(410)],[wRatio(575), hRatio(410)],3)
    pygame.draw.line(screen, BLACK, [wRatio(575), hRatio(350)],[wRatio(575), hRatio(410)],3)
    drawSectionText(screen, "Date Last Accessed", WHITE, (wRatio(175),hRatio(320),wRatio(400),hRatio(60)), writing_font)
    #Date of creation vvvv
    pygame.draw.rect(screen, WHITE, (wRatio(175),hRatio(500),wRatio(400),hRatio(60)))
    pygame.draw.line(screen, BLACK, [wRatio(175), hRatio(500)],[wRatio(575), hRatio(500)],3)
    pygame.draw.line(screen, BLACK, [wRatio(175), hRatio(500)],[wRatio(175), hRatio(560)],3)
    pygame.draw.line(screen, BLACK, [wRatio(175), hRatio(560)],[wRatio(575), hRatio(560)],3)
    pygame.draw.line(screen, BLACK, [wRatio(575), hRatio(500)],[wRatio(575), hRatio(560)],3)
    drawSectionText(screen, "Date Created", WHITE, (wRatio(175),hRatio(470),wRatio(400),hRatio(60)), writing_font)
    #Comments on save
    pygame.draw.rect(screen, WHITE, (wRatio(175),hRatio(650),wRatio(400),hRatio(250)))
    pygame.draw.line(screen, BLACK, [wRatio(175), hRatio(650)],[wRatio(575), hRatio(650)],3)
    pygame.draw.line(screen, BLACK, [wRatio(175), hRatio(650)],[wRatio(175), hRatio(900)],3)
    pygame.draw.line(screen, BLACK, [wRatio(175), hRatio(900)],[wRatio(575), hRatio(900)],3)
    pygame.draw.line(screen, BLACK, [wRatio(575), hRatio(650)],[wRatio(575), hRatio(900)],3)
    drawSectionText(screen, "Comments ", WHITE, (wRatio(175),hRatio(620),wRatio(400),hRatio(250)), writing_font)

    #Data Selector
    pygame.draw.rect(screen, WHITE, (wRatio(775),hRatio(200),wRatio(845),hRatio(700)))
    pygame.draw.line(screen, BLACK, [wRatio(775), hRatio(200)],[wRatio(845+ 775), hRatio(200)],3)
    pygame.draw.line(screen, BLACK, [wRatio(775), hRatio(200)],[wRatio(775), hRatio(900)],3)
    pygame.draw.line(screen, BLACK, [wRatio(775), hRatio(900)],[wRatio(845+ 775), hRatio(900)],3)
    pygame.draw.line(screen, BLACK, [wRatio(845 + 775), hRatio(200)],[wRatio(845+ 775), hRatio(900)],3)
    drawSectionText(screen, "Data Saves", WHITE, (wRatio(775),hRatio(170),wRatio(845),hRatio(700)), writing_font)

    ##### Switch Scenes
    pygame.draw.rect(screen, MEDIUM_GREY, ((wRatio(1700)), (hRatio(20)), (wRatio(200)), (hRatio(60))))
    pygame.draw.line(screen, BLACK, [wRatio(1700), hRatio(20)],[wRatio(1900), hRatio(20)],3)
    pygame.draw.line(screen, BLACK, [wRatio(1700), hRatio(20)],[wRatio(1700), hRatio(80)],3)
    pygame.draw.line(screen, BLACK, [wRatio(1700), hRatio(80)],[wRatio(1900), hRatio(80)],3)
    pygame.draw.line(screen, BLACK, [wRatio(1900), hRatio(20)],[wRatio(1900), hRatio(80)],3)
    drawTextComic20(screen, ["Go to Status Page"],WHITE, (wRatio(1720), hRatio(35), wRatio(175), hRatio(80)),writing_font)

    pygame.display.update()


def render_left_tear_lines():
  pygame.draw.line(screen, BLACK, [wRatio(720),hRatio(850)], [wRatio(720), hRatio(890)], 3)
  pygame.draw.line(screen, BLACK,[wRatio(770),hRatio(850)], [wRatio(770),hRatio(890)], 3)
  pygame.draw.aaline(screen, BLACK, [wRatio(720),hRatio(850)],[wRatio(770), hRatio(850)], False)
  pygame.draw.aaline(screen, BLACK, [wRatio(720),hRatio(890)],[wRatio(770), hRatio(890)], False)
  pygame.draw.line(screen, BLACK, [wRatio(770),hRatio(850)], [wRatio(770), hRatio(890)], 3)
  pygame.draw.line(screen, BLACK,[wRatio(820),hRatio(850)], [wRatio(820),hRatio(890)], 3)
  pygame.draw.aaline(screen, BLACK, [wRatio(770),hRatio(850)],[wRatio(820), hRatio(850)], False)
  pygame.draw.aaline(screen, BLACK, [wRatio(770),hRatio(890)],[wRatio(820), hRatio(890)], False)

def display_nail_option():
  pygame.draw.line(screen, WHITE, [wRatio(890),hRatio(845)], [wRatio(890), hRatio(895)], 3)
  pygame.draw.line(screen, WHITE,[wRatio(1290),hRatio(845)], [wRatio(1290),hRatio(895)], 3)
  pygame.draw.aaline(screen, WHITE, [wRatio(890),hRatio(845)],[wRatio(1290), hRatio(845)], False)
  pygame.draw.aaline(screen, WHITE, [wRatio(890),hRatio(895)],[wRatio(1290), hRatio(895)], False)
  pygame.draw.line(screen, WHITE, [wRatio(890),hRatio(910)], [wRatio(890), hRatio(960)], 3)
  pygame.draw.line(screen, WHITE,[wRatio(1290),hRatio(910)], [wRatio(1290),hRatio(960)], 3)
  pygame.draw.aaline(screen, WHITE, [wRatio(890),hRatio(910)],[wRatio(1290), hRatio(910)], False)
  pygame.draw.aaline(screen, WHITE, [wRatio(890),hRatio(960)],[wRatio(1290), hRatio(960)], False)

def updateSoundBoxPage():
    global soundBoxPage, lungSounds, heartSounds, abdominalSounds, vocalPhrases
    pygame.draw.rect(screen, WHITE, (wRatio(430), hRatio(280), wRatio(447), hRatio(510)))
    pygame.draw.line(screen, BLACK, [wRatio(430),hRatio(280)],[wRatio(877),hRatio(280)],3)
    pygame.draw.line(screen, BLACK, [wRatio(430),hRatio(790)],[wRatio(877),hRatio(790)],3)
    pygame.draw.line(screen, BLACK, [wRatio(430),hRatio(280)],[wRatio(430),hRatio(790)],3)
    pygame.draw.line(screen, BLACK, [wRatio(877),hRatio(280)],[wRatio(877),hRatio(790)],3)
    if soundBoxPage == "main":
      #pygame.draw.line(screen, BLACK, [wRatio(430),hRatio(340)],[wRatio(877),hRatio(340)],3)
      #pygame.draw.line(screen, BLACK, [wRatio(430),hRatio(400)],[wRatio(877),hRatio(400)],3)
      #pygame.draw.line(screen, BLACK, [wRatio(430),hRatio(460)],[wRatio(877),hRatio(460)],3)
      #pygame.draw.line(screen, BLACK, [wRatio(430),hRatio(520)],[wRatio(877),hRatio(520)],3)
      drawTextComic20(screen, ['Lung Sounds'], BLACK, (wRatio(435),hRatio(280), wRatio(447), hRatio(60)),writing_font)
      drawTextComic20(screen, ['Heart Sounds'], BLACK, (wRatio(435),hRatio(340), wRatio(447), hRatio(60)),writing_font)
      drawTextComic20(screen, ['Abdominal Sounds'], BLACK, (wRatio(435),hRatio(400), wRatio(447), hRatio(60)),writing_font)
      drawTextComic20(screen, ['Vocal Phrases'], BLACK, (wRatio(435),hRatio(460), wRatio(447), hRatio(60)),writing_font)
    if soundBoxPage == "Lung Sounds":
      displaySounds(lungSounds)
      #pygame.draw.line(screen, BLACK, [wRatio(430),hRatio(340)],[wRatio(877),hRatio(340)],3)
      #pygame.draw.line(screen, BLACK, [wRatio(430),hRatio(400)],[wRatio(877),hRatio(400)],3)
      #pygame.draw.line(screen, BLACK, [wRatio(430),hRatio(460)],[wRatio(877),hRatio(460)],3)
      #pygame.draw.line(screen, BLACK, [wRatio(430),hRatio(520)],[wRatio(877),hRatio(520)],3)
      #pygame.draw.line(screen, BLACK, [wRatio(430),hRatio(580)],[wRatio(877),hRatio(580)],3)
      #pygame.draw.line(screen, BLACK, [wRatio(430),hRatio(640)],[wRatio(877),hRatio(640)],3)
      #pygame.draw.line(screen, BLACK, [wRatio(430),hRatio(700)],[wRatio(877),hRatio(700)],3)
    if soundBoxPage == "Heart Sounds":
      displaySounds(heartSounds)
    if soundBoxPage == "Abdominal Sounds":
      displaySounds(abdominalSounds)
    if soundBoxPage == "Vocal Phrases":
      displaySounds(vocalPhrases)
    pygame.display.update()

def displaySounds(sounds):
  x,y,w,h = (435,280,447,60)
  if len(sounds) > 8:
    numSound = 8
  else:
    numSound = len(sounds)
  for i in range(numSound):
    drawTextComic20(screen, [sounds[i][0]], BLACK, (wRatio(x),hRatio(y), wRatio(w), hRatio(h)),writing_font)
    y += 60
  pygame.draw.line(screen, BLACK, [wRatio(430), hRatio(745)], [wRatio(877), hRatio(745)],3)
  drawTextComic20(screen, ["BACK"], BLACK, (wRatio(620),hRatio(750),wRatio(200),hRatio(45)), writing_font)

##########
'Functions'
##########
def playsound(song):
    pygame.mixer.music.load('/home/pi/Documents/Smart-Dummy-REAL/' + song)
    pygame.mixer.music.play(-1)




def run_button(button):
  global testcaseClockStart, forceNextLog, scene_name, textBoxTexts, box_1_page, box_2_page, box_3_page, box_4_page, heart_rate, tearLeftIndex, currentTextBox, textBoxActive, soundBoxPage, left_right, left_count, right_count, card_on
  try: forceNextLog
  except NameError: forceNextLog = False
  if button == "play button":
    testcaseClockStart = True
    if currentTime == "":
      forceNextLog = True
    event_log("stopwatch started")
  if button == "pause button":
    testcaseClockStart = False
    event_log("stopwatch paused")
  if button == "right arrow 1":
    box_1_page += 1
  if button == "left arrow 1":
    box_1_page -= 1
  if button == "right arrow 2":
    box_2_page += 1
  if button == "left arrow 2":
    box_2_page -= 1
  if button == "right arrow 3":
    box_3_page += 1
  if button == "left arrow 3":
    box_3_page -= 1
  if button == "right arrow 4":
    box_4_page += 1
  if button == "left arrow 4":
    box_4_page -= 1
  if button[:3] == "box":
    runItem(getItemName(button[:4], int(button[len(button) - 1]) -1))
  if button == "finger_led_on":
    tearLeftIndex += 1
    on_off_left_tear()
    if (on_off_display == True):
      event_log("fingernail LED off")
      GPIO.righthand_led_on(False)
    else:
      event_log("fingernail LED on")
      GPIO.righthand_led_on(True)
  if button == "mouth_led_on":
    mouth_on = True
    led_mouth()
    GPIO.mouth_led_on(True)
    event_log("mouth LED on")
  if button == "mouth_led_off":
    mouth_on = False
    led_mouth_off()
    GPIO.mouth_led_on(False)
    event_log("mouth LED off")
  if button == "Text Box Top":
    textBoxActive = True
    currentTextBox = "Text Box Top"
  if button == "Text Box Middle Top":
    textBoxActive = True
    currentTextBox = "Text Box Middle Top"
  if button == "Text Box Middle Bottom":
    textBoxActive = True
    currentTextBox = "Text Box Middle Bottom"
  if button == "Text Box Bottom":
    textBoxActive = True
    currentTextBox = "Text Box Bottom"
  if button == "switchToData":
    scene_name = "Data Page"
    load_scene("Data Page")
    buttonAddUpdate("Data Page")
  if button == "switchToStatus":
    scene_name = "Status Page"
    load_scene("Status Page")
    buttonAddUpdate("Status Page")
    textBoxTexts = {
      "Text Box Top" : "",
      "Text Box Middle Top" : "",
      "Text Box Middle Bottom" : "",
      "Text Box Bottom" : "",
    }
  if button == "heart_up":
    rate_up = True
    heart_rate += 1
    pygame.draw.rect(screen, MEDIUM_GREY, (wRatio(743),hRatio(175),wRatio(48), hRatio(25)))
    heart_rate_up()
    event_log("heart rate increased")
  if button == "heart_down":
    if (heart_rate > 0):
      rate_up = False
      heart_rate -= 1
      pygame.draw.rect(screen, MEDIUM_GREY, (wRatio(743),hRatio(175),wRatio(48), hRatio(25)))
      heart_rate_down()
      event_log("heart rate decreased")
  if button == "card_arrest_on":
    card_on = True
    cd_arrest_on()
    event_log("activated cardiac arrest")
  if button == "card_arrest_off":
    card_on = False
    cd_arrest_off()
    event_log("deactivated cardiac arrest")
  if button == "fingernail_options":
    f_nail_options()
    left_right += 1
  if button == 'finger_left':
    left_count += 1
    left_on()
    if (left_count % 2 == 0):
      ###### lefthand_led_on(False)
      event_log("right finger LED off")
    else:
      ###### lefthand_led_on(True)
      event_log("right finger LED on")
  if button == 'finger_right':
    right_count += 1
    right_on()
    if (right_count % 2 == 0):
      GPIO.righthand_led_on(False)
      event_log("right finger LED off")
    else:
      GPIO.righthand_led_on(True)
      event_log("right finger LED on")
  if soundBoxPage == "main":
    if button == "Sound Selection 1":
      soundBoxPage = "Lung Sounds"
      updateSoundBoxPage()
    if button == "Sound Selection 2":
      soundBoxPage = "Heart Sounds"
      updateSoundBoxPage()
    if button == "Sound Selection 3":
      soundBoxPage = "Abdominal Sounds"
      updateSoundBoxPage()
    if button == "Sound Selection 4":
      soundBoxPage = "Vocal Phrases"
      updateSoundBoxPage()
  elif button == "Sound Selection 9":
    soundBoxPage = "main"
    updateSoundBoxPage()
  elif soundBoxPage == "Lung Sounds" and button[:15] == "Sound Selection":
    if button[-1:] == "1":
        playsound("ASTHMAWHEEZE.wav")
    elif button[-1:] == "2":
        playsound("BRONCHIALSOUND.wav")
    elif button[-1:] == "3":
        playsound("DEATHRATTLE.wav")
    elif button[-1:] == "4":
        playsound("MEDIUMRALESCRACKLES.wav")
    elif button[-1:] == "5":
        playsound("PLEURALFRICTIONRUB.wav")
    elif button[-1:] == "6":
        playsound("SONOROUSRHONCHUS.wav")
    elif button[-1:] == "7":
        playsound("STRIDOR.wav")
    elif button[-1:] == "8":
        playsound("TRACHEALSOUND.wav")
    #pythonToArduino.feed("speaker", lungSounds[int(button[-1:]) - 1][1])
  elif soundBoxPage == "Heart Sounds" and button[:15] == "Sound Selection":
    if button[-1:] == "1":
        'playsound(".wav")'
    elif button[-1:] == "2":
        playsound("AORTACOARCTATION.wav")
    elif button[-1:] == "3":
        playsound("EBSTEINSANOMALY.wav")
    elif button[-1:] == "4":
        playsound("GALLOPTHIRDHEARTSOUND.wav")
    elif button[-1:] == "5":
        playsound("GALLOPFOURTHHEARTSOUND.wav")
    elif button[-1:] == "6":
        playsound("GALLOP3&4HEARTSOUND.wav")
    elif button[-1:] == "7":
        playsound("HEARTMURMUR.wav")
    elif button[-1:] == "8":
        playsound("MITRALVALVEPROLAPSE.wav")
    #pythonToArduino.feed("speaker", heartSounds[int(button[-1:]) - 1][1])
  elif soundBoxPage == "Abdominal Sounds" and button[:15] == "Sound Selection":
    ''
    #pythonToArduino.feed("speaker", abdominalSounds[int(button[-1:]) - 1][1])
  elif soundBoxPage == "Vocal Phrases" and button[:15] == "Sound Selection":
    ''
    #pythonToArduino.feed("speaker", vocalPhrases[int(button[-1:]) - 1][1])
  if button[:11] == "Data Option":
    prepareDataSave(matchesAccessor[int(button[len(button) - 1]) - 1])
  #pythonToArduino.useButton(button)
  if button == "save data":
    saveCurrentFile()
  #print(button)
  if button != "play button":
    forceNextLog = False
  pygame.time.wait(150)



def getItemName(boxName, ItemNum):
  global box_1_text, box_2_text, box_3_text, box_4_text, box_1_page, box_2_page, box_3_page, box_4_page, list_items

  if boxName == "box1":#Top Right
    box_1_render(box_1_text)
    try:
      return list_items[box_1_page][ItemNum]
    except IndexError:
      return "null"
  if boxName == "box2":#Middle Right
    box_2_render(box_2_text)
    try:
      return list_items[box_2_page][ItemNum]
    except IndexError:
      return "null"

  if boxName == "box3":#Bottom Right
    box_3_render(box_3_text)
    try:
      return list_items[box_3_page][ItemNum]
    except IndexError:
      return "null"

  if boxName == "box4":#Bottom Left
    box_4_render(box_4_text)
    try:
      return list_items[box_4_page][ItemNum]
    except IndexError:
      return "null"


def runItem(itemName):
  print(itemName)
  event_log(itemName)


##############
'Text Control'
##############
writing_font = pygame.font.SysFont('Times New Roman', wRatio(24))
onOffFont = pygame.font.SysFont('Times New Roman', wRatio(23))

#Draws text with a line underneath
def drawSectionText(surface, text, color, rect, font):
  x,y,w,h = rect
  surface.blit(font.render(text, True, color), (x,y))
  pygame.draw.rect(screen, color, (x, y + hRatio(26), wRatio(len(text) * 10), 2))

#Draws plain text that wraps inside a certain rectangle of space
def drawTextComic20(surface, text_list, color, rect, font):

  x,y,w,h = rect

  char_per_line = math.floor(w/wRatio(10))

  new_y = y

  for word in text_list:
    if len(word) <= char_per_line or word[:4] == "Date":
      surface.blit(font.render(word, True, color), (x,new_y))
      new_y += hRatio(60)
    else:
      text = font.render((word[:char_per_line - 1] + "-"), True, color)
      surface.blit(text, (x,new_y))
      word = word[char_per_line - 1:]
      new_y += hRatio(20)
      word = word[:char_per_line]
      surface.blit(font.render(word, True, color), (x,new_y))
      new_y += hRatio(40)
#Draws text without updating the screen
def drawTextComic20NoUpdate(surface, text_list, color, rect, font):

  x,y,w,h = rect

  char_per_line = math.floor(w/wRatio(10))

  new_y = y

  for word in text_list:
    if len(word) <= char_per_line or word[:4] == "Date":
      surface.blit(font.render(word, True, color), (x,new_y))
      new_y += hRatio(60)
    else:
      text = font.render((word[:char_per_line - 1] + "-"), True, color)
      surface.blit(text, (x,new_y))
      word = word[char_per_line - 1:]
      new_y += hRatio(20)
      word = word[:char_per_line]
      surface.blit(font.render(word, True, color), (x,new_y))
      new_y += hRatio(40)

#Draws a different size of text
def drawTextDetPage(surface, text_list, color, rect, font):

  x,y,w,h = rect

  char_per_line = math.floor(w/wRatio(10))

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
        new_y += hRatio(20)

  pygame.display.update()

constantBar = 0
#Checks where the indexing bar is
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





############
'Text Boxes'
############


def renderTextBox(textBox, String,x,y,w,h):
  drawTextDetPage(screen, [String], BLACK, (x + 3,y,w-13,h), writing_font)

def renderTextBoxes():
  global textBoxTexts, screen
  drawTextDetPage(screen,[textBoxTexts["Text Box Top"]], BLACK, (wRatio(175),hRatio(200),wRatio(400),hRatio(60)), writing_font)
  drawTextDetPage(screen,[textBoxTexts["Text Box Middle Top"]], BLACK, (wRatio(175),hRatio(350),wRatio(400),hRatio(60)), writing_font)
  drawTextDetPage(screen,[textBoxTexts["Text Box Middle Bottom"]], BLACK, (wRatio(175),hRatio(500),wRatio(400),hRatio(60)), writing_font)
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
                x,y,w,h = (wRatio(175),hRatio(200),wRatio(400),hRatio(60))
                runTextBox("Text Box Middle Top", textBoxTexts["Text Box Middle Top"])
                textBoxActive = False

              if currentTextBox == "Text Box Middle Top":
                x,y,w,h = (wRatio(175),hRatio(350),wRatio(400),hRatio(60))
                runTextBox("Text Box Middle Bottom", textBoxTexts["Text Box Middle Bottom"])
                textBoxActive = False

              if currentTextBox == "Text Box Middle Bottom":
                x,y,w,h = (wRatio(175),hRatio(500),wRatio(400),hRatio(60))
                runTextBox("Text Box Bottom", textBoxTexts["Text Box Bottom"])
                textBoxActive = False

              if currentTextBox == "Text Box Bottom":
                x,y,w,h = (wRatio(175),hRatio(650),wRatio(400),hRatio(250))
                runTextBox("Text Box Top", textBoxTexts["Text Box Top"])
                textBoxActive = False
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
          pygame.display.update()
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
        if currentTextBox == "Text Box Middle Top":
          x,y,w,h = (wRatio(175),hRatio(350),wRatio(400),hRatio(60))
        if currentTextBox == "Text Box Middle Bottom":
          x,y,w,h = (wRatio(175),hRatio(500),wRatio(400),hRatio(60))
        if currentTextBox == "Text Box Bottom":
          x,y,w,h = (wRatio(175),hRatio(650),wRatio(400),hRatio(250))
        renderTextBoxes()
        compTextBoxes()
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
  name, dateAccessed, dateCreated, comments = (textBoxTexts["Text Box Top"],textBoxTexts["Text Box Middle Top"],textBoxTexts["Text Box Middle Bottom"],textBoxTexts["Text Box Bottom"])
  matches = []

  name = removeExtraSpaces(name)
  dateAccessed = removeExtraSpaces(dateAccessed)
  dateCreated = removeExtraSpaces(dateCreated)
  comments = removeExtraSpaces(comments)
  for dataEntry in dataSaveInfo:
    match = True
    if not(areCommentsRelevant(dataEntry[0], name)):
      match = False
    elif not(areCommentsRelevant(dataEntry[1], dateAccessed)):
      match = False
    elif not(areCommentsRelevant(dataEntry[2], dateCreated)):
      match = False
    elif not(areCommentsRelevant(dataEntry[3], comments)):
      match = False
    if match == True:
      matches.append(dataEntry)
  matchesAccessor = matches
  renderMatches(matches)

def returnXYWHBoxValue(currentTextBox):
  if currentTextBox == "Text Box Top":
    return (wRatio(175),hRatio(200),wRatio(400),hRatio(60))
  if currentTextBox == "Text Box Middle Top":
    return (wRatio(175),hRatio(350),wRatio(400),hRatio(60))
  if currentTextBox == "Text Box Middle Bottom":
    return (wRatio(175),hRatio(500),wRatio(400),hRatio(60))
  if currentTextBox == "Text Box Bottom":
    return (wRatio(175),hRatio(650),wRatio(400),hRatio(250))



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



def renderMatches(matches):
  global matchPage
  name, dateAccessed, dateCreated, comments = ([],[],[],[])
  pygame.draw.rect(screen, WHITE, (wRatio(775),hRatio(200),wRatio(845),hRatio(700)))
  for matchSet in matches:
    names, datesAccessed, datesCreated, commentss = matchSet
    name.append(names)
    dateAccessed.append(datesAccessed)
    dateCreated.append(datesCreated)
    comments.append(commentss)
  matchLen = len(matches)
  pygame.draw.rect(screen, WHITE, (wRatio(775),hRatio(200),wRatio(845),hRatio(700)))
  x,y,w,h = wRatio(775),hRatio(200),wRatio(845),hRatio(700)
  newx, newy = x,y
  rangeNum = 10
  if len(matches) < 10:
    rangeNum = len(matches)
  pygame.draw.rect(screen, BLACK, (wRatio(775),hRatio(200),wRatio(845),hRatio(70 * rangeNum + 5)))
  for i in range(0,rangeNum):
    pygame.draw.rect(screen, WHITE, (newx + 3,newy + 3,wRatio(836),hRatio(66)))
    drawTextComic20NoUpdate(screen, ["Name: " + name[i]], BLACK, (newx + wRatio(5), newy, wRatio(300)- wRatio(5), hRatio(30)), writing_font)
    drawTextComic20NoUpdate(screen, ["Date Last Accessed: " + dateAccessed[i]], BLACK, (newx + wRatio(5), newy + hRatio(20), wRatio(300)- wRatio(5), hRatio(20)), writing_font)
    drawTextComic20NoUpdate(screen, ["Date Created: " + dateCreated[i]], BLACK, (newx + wRatio(5), newy + hRatio(40), wRatio(300)- wRatio(5), hRatio(20)), writing_font)
    drawTextComic20NoUpdate(screen, [comments[0]], BLACK, (newx + wRatio(8) + wRatio(350), newy, wRatio(545) - wRatio(8), hRatio(70)), writing_font)
    newy += hRatio(70)
  pygame.draw.line(screen,BLACK,[x + wRatio(350), y],[x + wRatio(350), y + hRatio(70 * rangeNum)],3)
  pygame.display.update()

#################
'File Management'
#################
dataSaveInfo = []
f = open("dataSaveGlossary.txt","a+")
f.close()
def refreshFiles():
  f= open("dataSaveGlossary.txt","r+")
  lines = f.readlines()
  f.close()
#f= open("dataSaveGlossary.txt","r")
  dataSaveInfo = []
  parseDataSaves(lines)
def parseDataSaves(lines):
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
refreshFiles()
#Data save format = NAME`DATEACCESSED`DATECREATED`COMMENTS\n
def prepareDataSave(dataSave):
  global button, scene_name, card_on, finger_led_on, mouth_on, heart_rate, currentTime, box_1_text, box_2_text, box_3_text, box_4_text, box_1_page
  button = ""
  print(dataSave)
  loadFile = fileRendering.renderAndChoose(dataSave)
  pygame.font.init()
  screen = pygame.display.set_mode((1280, 720), pygame.RESIZABLE)
  pygame.display.set_caption('SMART DUMMY')
  pygame.init()

  button = ""
  if loadFile:
    dataStrip = fileRendering.getInfo(dataSave)
    print(dataStrip)
    (card_on, finger_led_on, mouth_on, heart_rate, currentTime, SOUNDS, box_1_text, box_2_text, box_3_text, box_4_text) = dataStrip
    print(box_1_text, box_2_text, box_3_text, box_4_text)
    #Cardiac Arrest
    if card_on:
      run_button("card_arrest_on")
    else:
      run_button("card_arrest_off")
    #Finger Cyan.
    #Mouth Cyan.
    if mouth_on:
      run_button("mouth_led_on")
    else:
      run_button("mouth_led_off")
    #Time Management
    #box_1_text = ['apnea', 'desaturation']
    #box_2_text = ['Ativan', 'Adderall', 'Acetaminophen', 'Atropine', 'Epinephrine 1:10,000']
    #box_3_text = ["Jameson Watson", "Sarah Banet", "Steve Willson"]
    #box_4_text = []
    #Box Rendering
    print(box_1_text, box_2_text, box_3_text, box_4_text)
    box_1_page=0
    box_1_render(box_1_text)
    box_2_render(box_2_text)
    box_3_render(box_3_text)
    box_4_render(box_4_text)
    load_scene("Status Page")
    scene_name = "Status Page"
    printS()

def printS():
  global card_on, finger_led_on, mouth_on, heart_rate, currentTime, SOUNDS, box_1_text, box_2_text, box_3_text, box_4_text
  print(card_on, finger_led_on, mouth_on, heart_rate, currentTime, SOUNDS, box_1_text, box_2_text, box_3_text, box_4_text)

def saveCurrentFile():
  global button, scene_name, card_on, finger_led_on, mouth_on, heart_rate, currentTime, box_1_text, box_2_text, box_3_text, box_4_text
  button = ""
  """
  Psuedo: Is this a new file? (y/n)
  if no:
    What is name, dateLastAccessed, DateCreated, Comments?
    Use renderMatches to help piecemeal info
  if yes:
    getDate
    Create file as Name`Date`Date`Comments
  Write to file
  """
  (name,dateCreated,dateLastAccessed,comments) = SaveDataInterface.save()
  f = open("dataSaveGlossary.txt","w+")
  f.write("%s`%s`%s`%s\n" % (name,dateCreated,dateLastAccessed,comments))
  f.close()
  new = ''
  for i in dateCreated:
    if i != '/':
      new += i
  dateCreated = new
  new = ''
  for i in dateLastAccessed:
    if i != '/':
      new += i
  dateLastAccessed = new
  f=open("%s`%s`%s`%s.txt" % (name,dateCreated,dateLastAccessed,comments),"w+")
  f.write("%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n" % (card_on, finger_led_on, mouth_on, heart_rate, currentTime, box_1_text, box_2_text, box_3_text, box_4_text))
  f.close()
  refreshFiles()
  load_scene("Status Page")
  scene_name = "Status Page"
##############
'Display Text'
##############

def run_scenario():
  display_medicine = []
  display_condition = []
  display_intervention = []
  medication_names = [ 'Ativan', 'Adderall', 'Acetaminophen' ]
  for x in range(10):
    i = random.randint(0, len(medication_names)-1)
    display_medicine.append(medication_names[i])
    print(*display_medicine, sep = "\n")


def box_1_render(text):
  global list_items, box_1_page
  pygame.draw.rect(screen, WHITE, (wRatio(1505),hRatio(176),wRatio(393),hRatio(243)))
  items_per_page_box1 = math.floor(hRatio(250)/hRatio(60))
  c = len(text) - 1
  temp_list_items = []
  list_items = []
  c2 = items_per_page_box1
  while c >= 0:
    temp_list_items.append(text[c])
    c-=1
    c2-=1
    if c2 == 0:
      c2 = items_per_page_box1
      list_items.append(temp_list_items)
      temp_list_items = []
  if box_1_page < 0:
    box_1_page = len(list_items)
  if box_1_page > len(list_items):
    box_1_page = 0
  list_items.append(temp_list_items)
  drawTextComic20(screen, list_items[box_1_page], BLACK, (wRatio(1505),hRatio(176),wRatio(393),hRatio(243)), writing_font)

def box_2_render(text):
  global list_items, box_2_page
  pygame.draw.rect(screen, WHITE, (wRatio(1505),hRatio(496),wRatio(393),hRatio(243)))
  items_per_page_box2 = math.floor(hRatio(250)/hRatio(60))
  c = len(text) - 1
  temp_list_items = []
  list_items = []
  c2 = items_per_page_box2
  while c >= 0:
    temp_list_items.append(text[c])
    c-=1
    c2-=1
    if c2 == 0:
      c2 = items_per_page_box2
      list_items.append(temp_list_items)
      temp_list_items = []
  if box_2_page < 0:
    box_2_page = len(list_items)
  if box_2_page > len(list_items):
    box_2_page = 0

  list_items.append(temp_list_items)
  drawTextComic20(screen, list_items[box_2_page], BLACK, (wRatio(1505),hRatio(496),wRatio(393),hRatio(243)), writing_font)


def box_3_render(text):
  global list_items, box_3_page
  pygame.draw.rect(screen, WHITE, (wRatio(1505),hRatio(816),wRatio(393),hRatio(193)))
  items_per_page_box3 = math.floor(hRatio(200)/hRatio(60))
  c = len(text) - 1
  temp_list_items = []
  list_items = []
  c2 = items_per_page_box3
  while c >= 0:
    temp_list_items.append(text[c])
    c-=1
    c2-=1
    if c2 == 0:
      c2 = items_per_page_box3
      list_items.append(temp_list_items)
      temp_list_items = []


  if box_3_page < 0:
    box_3_page = len(list_items)
  if box_3_page > len(list_items):
    box_3_page = 0
  list_items.append(temp_list_items)
  drawTextComic20(screen, list_items[box_3_page], BLACK, (wRatio(1505),hRatio(816),wRatio(393),hRatio(193)), writing_font)

def box_4_render(text):
  global list_items, box_4_page
  pygame.draw.rect(screen, WHITE, (wRatio(25),hRatio(616),wRatio(293),hRatio(393)))
  items_per_page_box4 = math.floor(hRatio(400)/hRatio(60))
  c = len(text) - 1
  temp_list_items = []
  list_items = []
  c2 = items_per_page_box4
  while c >= 0:
    temp_list_items.append(text[c])
    c-=1
    c2-=1
    if c2 == 0:
      c2 = items_per_page_box4
      list_items.append(temp_list_items)
      temp_list_items = []


  if box_4_page < 0:
    box_4_page = len(list_items)
  if box_4_page > len(list_items):
    box_4_page = 0
  list_items.append(temp_list_items)
  drawTextComic20(screen, list_items[box_4_page], BLACK, (wRatio(25),hRatio(616),wRatio(393),hRatio(393)), writing_font)

def event_log(event):
  if len(box_4_text) == 0:
      box_4_text.append(str(event))
  if currentTime == "" and box_4_text[len(box_4_text) - 1] != str(event):
      box_4_text.append(str(event))
  elif currentTime != "" and box_4_text[len(box_4_text) - 2] != str(event) and not forceNextLog:
      box_4_text.append(str(event))
      box_4_text.append(currentTime)
  elif forceNextLog and box_4_text[len(box_4_text) - 1] != str(event):
      box_4_text.append(str(event))
      box_4_text.append(currentTime)

##############
' Modify Mannequin '
##############
def cd_arrest_on():
    pygame.draw.rect(screen, MEDIUM_GREY, (wRatio(823),hRatio(225),wRatio(50),hRatio(43)))
    pygame.draw.rect(screen, WHITE, (wRatio(778),hRatio(225),wRatio(50),hRatio(43)))
    drawTextComic20(screen, ["ON"], MEDIUM_GREY, (wRatio(785),hRatio(230),wRatio(25), hRatio(30)), writing_font)
    ecg.arrest(True)
def cd_arrest_off():
  pygame.draw.rect(screen, WHITE, (wRatio(823),hRatio(225),wRatio(50),hRatio(43)))
  pygame.draw.rect(screen, MEDIUM_GREY, (wRatio(778),hRatio(225),wRatio(50),hRatio(43)))
  drawTextComic20(screen, ['OFF'], MEDIUM_GREY, ((wRatio(833),hRatio(231), wRatio(30), hRatio(20))), writing_font)
  ecg.arrest(False)

def heart_rate_up():
  global heart_rate
  if (heart_rate > 0):
    global rate_up
    rate_up = True
    if (rate_up == True):
      pass
      #print (heart_rate)
    ecg.set_rate(heart_rate)
  drawTextComic20(screen, [str(heart_rate)], WHITE, (wRatio(760),hRatio(175),wRatio(45), hRatio(55)), writing_font)

def heart_rate_down():
  global heart_rate
  if (heart_rate > 0):
    global rate_up
    rate_up = False
    if (rate_up == False):
      pass
      #print (heart_rate)
    ecg.set_rate(heart_rate)
  drawTextComic20(screen, [str(heart_rate)], WHITE, (wRatio(760),hRatio(175),wRatio(45), hRatio(55)), writing_font)





##############
' LED '
##############
### Function that stores the text 'Cyanosis( fingernail )' and 'Cyanosis( mouth )' to variables "left" and "right". The variables are called in line 355 and 356 under the initial description section
def LED():
  global left
  global right
  global text_tear
  left = []
  right = []
  text_tear = []
  text_display = ['Cyanosis( fingernail )' , 'Cyanosis( mouth )' ]
  for i in range(2):
    if (i == 0):
      left.append(text_display[i])
    elif (i == 1):
      right.append(text_display[i])

LED()

### Function that outputs "on" and "off" corresponding to the button that the user clicked, indicating the current status of the "Cyanosis( fingernail )" ( wheter it is on or off )
def on_off_left_tear():
  global tearLeftIndex
  global on_off_display
  if tearLeftIndex % 2 == 0:
    on_off_display = True ### when the button is off
    pygame.draw.rect(screen, WHITE, (wRatio(720),hRatio(850),wRatio(50),hRatio(43)))
    pygame.draw.rect(screen, MEDIUM_GREY, (wRatio(770),hRatio(850),wRatio(50),hRatio(40)))
    render_left_tear_lines()
    drawTextComic20(screen, ["OFF"], BLACK, (wRatio(725),hRatio(855),wRatio(45),hRatio(30)), onOffFont)
  else:
    on_off_display = False ### when the button is on
    pygame.draw.rect(screen, MEDIUM_GREY, (wRatio(720),hRatio(850),wRatio(50),hRatio(43)))
    pygame.draw.rect(screen, WHITE, (wRatio(770),hRatio(850),wRatio(50),hRatio(40)))
    render_left_tear_lines()
    drawTextComic20(screen, ["ON"], BLACK, (wRatio(775),hRatio(855),wRatio(45),hRatio(30)), onOffFont)

### Function that outputs "on" and "off" corresponding to the button that the user clicked, indicating the current status of the "Cyanosis( mouth )" ( wheter it is on or off )
def led_mouth():
  global mouth_on
  mouth_on = True
  if (mouth_on == True):
    pygame.draw.rect(screen, WHITE, (wRatio(772),hRatio(917),wRatio(48),hRatio(41)))
    pygame.draw.rect(screen, MEDIUM_GREY, (wRatio(722),hRatio(917),wRatio(48),hRatio(38)))
    render_left_tear_lines()
    drawTextComic20(screen, ["ON"], BLACK, (wRatio(775),hRatio(920),wRatio(45),hRatio(30)), onOffFont)
def led_mouth_off():
  global mouth_on
  mouth_on = False
  if (mouth_on == False):
    pygame.draw.rect(screen, MEDIUM_GREY, (wRatio(772),hRatio(917),wRatio(48),hRatio(41)))
    pygame.draw.rect(screen, WHITE, (wRatio(722),hRatio(917),wRatio(48),hRatio(38)))
    render_left_tear_lines()
    drawTextComic20(screen, ['OFF'], BLACK, (wRatio(725),hRatio(920),wRatio(45),hRatio(30)), onOffFont)

### Function that displays a hidden text once the user clicks "OPTIONS"
### Hidden texts are the extra functions, left and right fingernail, that provides more options for the users to control
def f_nail_options():
  global left_right
  if ((left_right % 2) == 1): ### Indicates that the text "OPTIONS" is clicked to be turned on
    display_nail_option() ### Creates the white text box in the background: White squares that the texts are inside of
    print ( "options_shown" )
    drawTextComic20(screen, ['Fingernail: LEFT '], WHITE, ((wRatio(898),hRatio(855),wRatio(220),hRatio(40))), writing_font)
    drawTextComic20(screen, ['Fingernail: RIGHT '] , WHITE, ((wRatio(898),hRatio(920),wRatio(220),hRatio(40))), writing_font)
    pygame.draw.rect(screen, WHITE, (wRatio(1170),hRatio(850),wRatio(50),hRatio(43)))
    pygame.draw.rect(screen, MEDIUM_GREY, (wRatio(1220),hRatio(850),wRatio(50),hRatio(40)))
    render_left_tear_lines()
    drawTextComic20(screen, ["OFF"], BLACK, (wRatio(1175),hRatio(855),wRatio(45),hRatio(30)), onOffFont)
    pygame.draw.rect(screen, WHITE, (wRatio(1170),hRatio(917),wRatio(50),hRatio(43)))
    pygame.draw.rect(screen, MEDIUM_GREY, (wRatio(1220),hRatio(917),wRatio(50),hRatio(40)))
    render_left_tear_lines()
    drawTextComic20(screen, ["OFF"], BLACK, (wRatio(1175),hRatio(920),wRatio(45),hRatio(30)), onOffFont)
  elif ((left_right % 2) == 0): ### Indicates that the text "OPTIONS" is clicked once again to be turned off
    pygame.draw.rect(screen, MEDIUM_GREY, (wRatio(850),hRatio(830),wRatio(480),hRatio(180)))

### Function that outputs "on" and "off" corresponding to the button that the user clicked, indicating the current status of the "Left Fingernail" ( wheter it is on or off )
def left_on():
  global left_count
  if left_count % 2 == 0:
    ### button that inidcate "on" and "off"
    pygame.draw.rect(screen, WHITE, (wRatio(1170),hRatio(850),wRatio(50),hRatio(43)))
    pygame.draw.rect(screen, MEDIUM_GREY, (wRatio(1220),hRatio(850),wRatio(50),hRatio(40)))
    render_left_tear_lines()
    drawTextComic20(screen, ["OFF"], BLACK, (wRatio(1175),hRatio(855),wRatio(45),hRatio(30)), onOffFont)
  else:
    pygame.draw.rect(screen, MEDIUM_GREY, (wRatio(1170),hRatio(850),wRatio(50),hRatio(43)))
    pygame.draw.rect(screen, WHITE, (wRatio(1220),hRatio(850),wRatio(50),hRatio(40)))
    render_left_tear_lines()
    drawTextComic20(screen, ["ON"], BLACK, (wRatio(1225),hRatio(855),wRatio(45),hRatio(30)), onOffFont)

### Function that outputs "on" and "off" corresponding to the button that the user clicked, indicating the current status of the "Right Fingernail" ( wheter it is on or off )
def right_on():
  global right_count
  if right_count % 2 == 0:
    ### button that inidcate "on" and "off"
    pygame.draw.rect(screen, WHITE, (wRatio(1170),hRatio(917),wRatio(50),hRatio(43)))
    pygame.draw.rect(screen, MEDIUM_GREY, (wRatio(1220),hRatio(917),wRatio(50),hRatio(40)))
    render_left_tear_lines()
    drawTextComic20(screen, ["OFF"], BLACK, (wRatio(1175),hRatio(920),wRatio(45),hRatio(30)), onOffFont)
  else:
    pygame.draw.rect(screen, MEDIUM_GREY, (wRatio(1170),hRatio(917),wRatio(50),hRatio(43)))
    pygame.draw.rect(screen, WHITE, (wRatio(1220),hRatio(917),wRatio(50),hRatio(40)))
    render_left_tear_lines()
    drawTextComic20(screen, ["ON"], BLACK, (wRatio(1225),hRatio(920),wRatio(45),hRatio(30)), onOffFont)


##################
'Clock Management'
##################

currentTime = ""


def render_clock(millis):
  global currentTime, clockFont
  seconds=(millis/1000)%60
  seconds = int(seconds)
  minutes=(millis/(1000*60))%60
  minutes = int(minutes)
  hours=(millis/(1000*60*60))%24
  hours = int(hours)
  if (seconds < 10):
    s = ("0"+str(seconds))
  else:
    s = str(seconds)
  if (minutes < 10):
    m = ("0"+str(minutes))
  else:
    m = str(minutes)
  if hours < 10:
    h = "0"+str(hours)
  else:
    h = str(hours)

  if ("%s:%s:%s" % (h, m, s)) != currentTime:
    currentTime = "%s:%s:%s" % (h, m, s)
    pygame.draw.rect(screen, BLACK, (wRatio(850),hRatio(50),wRatio(110),hRatio(30)))
    clock_font = pygame.font.SysFont('Comic Sans MS', wRatio(20))
    drawTextComic20(screen, [currentTime], WHITE, (wRatio(865), hRatio(50), wRatio(100), hRatio(30)), clock_font)



###################
'Control Structure'
###################

pygame.init()

soundBoxPage = "main"
lungSounds = [["Asthmatic Wheezing","ASTHMA WHEEZE.wav"], ["Bronchial Sound","BRONCHIAL SOUND.wav"], ["Death Rattle","DEATH RATTLE.wav"], ["Rales and Crackles","MEDIUM RALES CRACKLES.wav"], ["Pleural Friction Rubbing","PLEURAL FRICTION RUB.wav"], ["Sonorous Rhonchus","SONOROUS RHONCHUS.wav"], ["Stridor","STRIDOR.wav"], ["Tracheal Sound","TRACHEAL SOUND.wav"], ["Vesicular Breathing Sounds","VESICULAR BREATH SOUNDS.wav"], ["Name 10","filePath10"]]
heartSounds = [["Use Above Preset",""],["Coarctation of the Aorta", "AORTA COARCTATION.wav"],["Ebsteins Anomaly","EBSTEINS ANOMALY.wav"],["Third Heart Sound - Gallop","GALLOP THIRD HEART SOUND.wav"],["Fourth Heart Sound - Gallop","GALLOP FOURTH HEART SOUND.wav"],["Third and Fourth Heart Sound - Gallop","GALLOP 3&4 HEART SOUND.wav"], ["Heart Murmur","HEART MURMUR.wav"], ["Prolapse of the Mitral Valve","MITRAL VALVE PROLAPSE.wav"]]
abdominalSounds = []
vocalPhrases = []

card_on = False
finger_led_on = False
mouth_on = False


tearLeftIndex = 0
left_count = 0
right_count = 0

scene_name = "Status Page"

load_scene("Status Page")
pygame.display.update()
##DELETEvvv
SOUNDS = 'null'

testcaseClockStart = False
clock = pygame.time.Clock()
clockTime = 0

heart_rate = heart_rate
box_1_page = 0
box_2_page = 0
box_3_page = 0
box_4_page = 0
left_right = 0

pygame.display.update()

box_1_text = ['apnea', 'desaturation']
box_2_text = ['Ativan', 'Adderall', 'Acetaminophen', 'Atropine', 'Epinephrine 1:10,000']
box_3_text = ["Jameson Watson", "Sarah Banet", "Steve Willson"]
box_4_text = []


buttonAddUpdate("Scene Page")
buttonAddUpdate("Data Page")


textBoxActive = False
currentTextBox = "null"
textBoxTexts = {
  "Text Box Top" : "",
  "Text Box Middle Top" : "",
  "Text Box Middle Bottom" : "",
  "Text Box Bottom" : "",
  }

image = pygame.image.load(os.path.join(pathlib.Path(__file__).parent.absolute(),"Man.png"))
rect = image.get_rect()
scalar = pygame.transform.scale(image, (int((rect.width/1280)*pygame.display.get_surface().get_size()[0]),
  int((rect.height/720)*pygame.display.get_surface().get_size()[1])))

screen.blit(scalar, (wRatio(960),hRatio(150)))

while True:
  ecg.tick()
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
      if scene_name == "Status Page":
        load_scene("Status Page")
        image = pygame.image.load(os.path.join(pathlib.Path(__file__).parent.absolute(),"Man.png"))
        rect = image.get_rect()
        scalar = pygame.transform.scale(image, (int((rect.width/1280)*pygame.display.get_surface().get_size()[0]),
                                   int((rect.height/720)*pygame.display.get_surface().get_size()[1])))


        screen.blit(scalar, (wRatio(960),hRatio(150)))
      elif scene_name == "Data Page":
        load_scene("Data Page")
  buttonRun = False
  pygame.event.get()
  get_pos = pygame.mouse.get_pos()
  mousex, mousey = get_pos
  if scene_name == "Status Page":
    for i in scene_status_page_buttons:
     x, y, h, w, color1, color2 = buttons[i]
     x = int(x)
     y = int(y)
     h = int(h)
     w = int(w)
     if mousex > x and mousey > y and mousex < x + w and mousey < y + h and pygame.mouse.get_pressed() == (True, False, False):
       run_button(i)
       buttonRun = True
       break
    if scene_name != "Data Page":
      box_1_render(box_1_text)
      box_2_render(box_2_text)
      box_3_render(box_3_text)
      box_4_render(box_4_text)
      ecg.blit()
    pygame.display.update()
  if scene_name == "Data Page":
   if not(buttonRun):
    for i in scene_data_page_buttons:
     x, y, h, w, color1, color2 = buttons[i]
     x = int(x)
     y = int(y)
     h = int(h)
     w = int(w)
     if mousex > x and mousey > y and mousex < x + w and mousey < y + h and pygame.mouse.get_pressed() == (True, False, False):
       run_button(i)
       buttonRun = True
       break
    if textBoxActive:
      runTextBox(currentTextBox, textBoxTexts[currentTextBox])
    pygame.display.update()
   else:
     buttonRun = False
  clock.tick()
  if testcaseClockStart:
    clockTime += clock.get_time()
    render_clock(clockTime)


#Condense Code
###All buttons have functions, but there is currently no set parameters for running any of the medicines (rn it just prints their names)
#Change Arrows to a Scroll Bar?