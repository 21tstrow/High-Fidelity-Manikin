from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from PIL import ImageTk, Image

class EmptyPopup(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

class AddPopup(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        self.geometry("575x350")
        self.frame()
        
    def frame(self):
        #intializes the frame
        self.canvas = Canvas(self)
        self.canvas.pack(expand = 1, fill = "both")

        self.images = []
        self.createimage((20,20),
                image="/Users/arthurgarvin/Downloads/chicken-man-seed.jpg")

        #adds rectangles
        self.canvas.create_rectangle(210, 20, 250, 60, fill = "")
        self.canvas.create_rectangle(260, 20, 300, 60, fill = "")
        self.canvas.create_rectangle(210, 70, 250, 110, fill = "")
        self.canvas.create_rectangle(260, 70, 300, 110, fill = "")
        self.canvas.create_rectangle(210, 120, 250, 160, fill = "")
        self.canvas.create_rectangle(260, 120, 300, 160, fill = "")

        #adds buttons and entries
        self.label = Label(self, text = "Name:")
        self.label.place(x = 310, y = 20)
        self.name_entry = Entry(self)
        self.name_entry.place(x = 360, y = 20)
        self.button = Button(self, text = "Upload Image", command = self.upload)
        self.button.place(x = 60, y = 210)
        self.button2 = Button(self, text = "Add Scenario")
        self.button2.place(x = 460, y = 310)

    def upload(self):
        filename = filedialog.askopenfilename()
        self.createimage((20,20), image = filename, index = 0)

    def createimage(self, *args, **kwargs):
        t = (0,0)
        for argv in args:
            if isinstance(argv, tuple):
                t = argv
        i = ""
        if "image" in kwargs:
            i = kwargs["image"]
        #add images
        try:
            tki = ImageTk.PhotoImage(Image.open(i))
            self.canvas.create_image(t, image = tki, anchor = NW)
        except FileNotFoundError:
            pass
        if "index" in kwargs:
            n = kwargs["index"]
            self.images[n] = tki
        else:
            self.images.append(tki)
        

if __name__ == "__main__":
    root = AddPopup()
    root.title("untitled")
    root.mainloop()
