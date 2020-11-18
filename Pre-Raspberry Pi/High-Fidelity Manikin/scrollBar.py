import pygame, math
from pygame.locals import *

class ScrollBar:
    #position -- the position of the scroll bar
    #scrollrange -- the range of the scroll bar
    #color -- the color of the scroller
    #barcolor -- the color of the scroll bar
    #pane -- a linked ScrollPane object
    def __init__(self, parent, position, scrollrange,
                 color = (100,100,100), barcolor = (0,0,0), pane = None):
        self.parent = parent
        self.x, self.y, self.width, self.height = position
        self.initx = self.x
        self.inity = self.y
        self.scrollrange = scrollrange

        self.pane = pane
        self.color = color
        self.barcolor = barcolor
        
        self.update()

    def get_range(self):
        return self.scrollrange
    
    def set_pos(self, position):
        self.x, self.y, self.width, self.height = position

    def get_tuple(self):
        new_tuple = (self.x, self.y, self.width, self.height)
        return new_tuple

    #checks if the mouse is in range to click the scroll bar
    def in_range(self, mouse):
        mousex, mousey = mouse
        if self.initx < mousex and mousex < self.x+self.width and self.inity < mousey and mousey < self.inity+self.scrollrange:
            return True
        return False

    #returns the relative height
    def rel_height(self):
        return int(self.y - self.inity) / self.scrollrange

    def update(self):
        new_tuple = self.get_tuple()
        pygame.draw.rect(self.parent, self.barcolor, (self.initx,    self.inity, self.width,self.scrollrange + self.height))
        pygame.draw.rect(self.parent, self.color, new_tuple)

        try:
            self.pane.set_scroll(int(self.rel_height() * self.pane.get_tuple()[3]))
            self.pane.update()
        except:
            pass



class ScrollPane:
    #position -- the position of the pane
    #text -- an array of text to display
    #spacing -- the space between the text
    #font -- the font of the text
    #color -- the color of the pane
    def __init__(self, parent, position, text, spacing = 30,
                 font = "comicsansms", color = (255,255,255)):
       self.parent = parent
       self.x, self.y, self.width, self.height = position
       self.text = text
       self.position = position
       self.spacing = spacing
       self.color = color        
            
       self.font = pygame.font.SysFont(font, 28)
       self.scroll = 0

       self.update()

    #sets the scroll value
    def set_scroll(self, n):
        self.scroll = n

    def get_tuple(self):
        new_tuple = (self.x, self.y, self.width, self.height)
        return new_tuple

    #checks if mouse is in range of the pane
    def in_range(self, mouse):
        mousex, mousey = mouse
        if self.x < mousex and mousex < self.x+self.width and self.y < mousey and mousey < self.y+self.height:
            return True
        return False     

    #gets the selected text
    def get_select(self, mouse):
        if (self.in_range(mouse)):
            mousey = mouse[1]
            for i in range(len(self.text)):
                text_y = self.y + self.spacing * i - self.scroll
                if(mousey > text_y and mousey < text_y + self.spacing):
                    return self.text[i]             
            

    #updates the display
    def update(self):
        new_tuple = self.get_tuple()
        pygame.draw.rect(self.parent, self.color, new_tuple)
        for i in range(len(self.text)):
            text = self.font.render(self.text[i], True, (0,0,0))
            text_y = self.y + self.spacing * i - self.scroll
            if (text_y <= self.y + self.height - self.spacing and text_y >= self.y):
                self.parent.blit(text, (self.x, text_y))





        
if __name__ == "__main__":

#Demo Code

#Demos both linked and unlinked scroll bars
#Functionally both demos are the same, but the linked one is easier to use
    linked = True

    if not linked:
        pygame.init()       
        surface = pygame.display.set_mode((500,500))

        pane = ScrollPane(surface, (50,50,200,400), ["text", "bard", "jeff", "deep", "well", "week", "like", "bomb", "user",
        "tire", "suck", "gold", "sock", "lyre", "dump",
                                "dire", "east", "high"])


        #Create ScrollBar without linked pane
        scrawl = ScrollBar(surface, (300,50,50,50), 350)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                  pygame.quit()
                  quit()

                if event.type == pygame.MOUSEMOTION:
                    #sets the position of the scroll bar if clicked
                    if scrawl.in_range(pygame.mouse.get_pos()) == True:
                        if pygame.mouse.get_pressed() == (1,0,0):
                            pos = scrawl.get_tuple()
                            scrawl.set_pos((pos[0], pygame.mouse.get_pos()[1], pos[2], pos[3]))

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pane.in_range(pygame.mouse.get_pos()) == True:
                        t = pane.get_select(pygame.mouse.get_pos())
                        print(t)
                    
                    c = 0
                    c

            #updates the pane and the scroll bar when the pane is unlinked
            pane.set_scroll(int(scrawl.rel_height() * pane.get_tuple()[3]))
            pane.update()      
            scrawl.update()
            pygame.display.update()

    elif linked:
        pygame.init()       
        surface = pygame.display.set_mode((500,500))

        pane = ScrollPane(surface, (50,50,200,400), ["text", "bard", "jeff", "deep", "well", "week", "like", "bomb", "user",
        "tire", "suck", "gold", "sock", "lyre", "dump",
        "dire", "east", "high"])


        #Create ScrollBar with linked pane
        scrawl = ScrollBar(surface, (300,50,50,50), 350, pane = pane)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                  pygame.quit()
                  quit()

                if event.type == pygame.MOUSEMOTION:
                    #sets the position of the scroll bar if clicked
                    if scrawl.in_range(pygame.mouse.get_pos()) == True:
                        if pygame.mouse.get_pressed() == (1,0,0):
                            pos = scrawl.get_tuple()
                            scrawl.set_pos((pos[0], pygame.mouse.get_pos()[1], pos[2], pos[3]))

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pane.in_range(pygame.mouse.get_pos()) == True:
                        t = pane.get_select(pygame.mouse.get_pos())
                        print(t)
                    
                    c = 0
                    c

            #updates just the scroll bar if linked    
            scrawl.update()
            pygame.display.update()

    else:
        print("what the heck")
        

