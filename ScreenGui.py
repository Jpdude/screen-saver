from tkinter import *
win = Tk()
win.title("Window Manager")
from PIL import Image , ImageTk
img = Image.open("C:\\Users\\user\\AppData\\Roaming\\Microsoft\\Windows\\Themes\\TranscodedWallpaper")
img = img.resize((480,270))
img1 = ImageTk.PhotoImage(img)

topmost_f = Canvas(win, highlightbackground = "red", highlightthickness = 1 ,scrollregion=(0,0,500,500) , bg = "white")
# for x in y.windows():
#   f.columnfigure(index = x , weight = 1 )

# Where I configured the grid layout of the topmost frame
topmost_f.columnconfigure(index = 0 , weight = 1 , uniform ="u")
topmost_f.columnconfigure(index = 1 , weight = 1 , uniform ="u")
topmost_f.columnconfigure(index = 2 , weight = 1 , uniform ="u")

topmost_f.rowconfigure(index = 0 , weight = 1 , uniform ="u")
topmost_f.rowconfigure(index = 1 , weight = 10 , uniform ="u")
topmost_f.rowconfigure(index = 2 , weight = 1 , uniform ="u")

vbar=Scrollbar(win,orient=VERTICAL)
vbar.pack(side=RIGHT,fill=Y)
vbar.config(command=topmost_f.yview)

topmost_f.config( yscrollcommand=vbar.set)
topmost_f.pack(side = LEFT , fill = "both" , expand = True)
#=====================ENDS=================================


heading_label = Label(topmost_f , text = "Detected Windows", font = ("comic sans",20,"bold")).grid( row = 0 , column = 0 , sticky = "nw")

class Screen:
    def __init__(self,master,screen):
        self.master = master
        self.screen = screen
    def poop(self,x,y,z):
            print("poop:",self.typa.get(),y,z,self.master.grid_slaves())
            if self.typa.get() == "Time":
                #self.toolFrameTime.pack()
                ...
    def build(self,row,column):
        print(row,column)
        self.f = Frame(self.master, highlightbackground = "black", highlightthickness = 1 )
        self.f.grid(row = row, column = column ,sticky = "ns" ,padx = 15 ,pady = 15 )
        
        
        viewframe = Canvas(self.f, width = 480 , height = 270 , bg = "black")
        self.image_id = viewframe.create_image((0,0) , image = img1,anchor = "nw")
        viewframe.create_text(550, 250, text="1", fill="WHITE", font=('Helvetica 15 bold'))
        viewframe.pack( fill = X , side = TOP  )
        print("JJ:",viewframe.cget("width"),viewframe.keys(),self.f.bbox())
        

        
        opt = ["Time" ,"Pictures","Music"]
        self.typa = StringVar()
        self.typa.set(opt[0])
        
        
        
        toolframe = Frame(self.f,bg = "yellow", highlightbackground = "pink", highlightthickness = 5 )
        toolframe.pack(expand = True , fill = BOTH , side = BOTTOM)

        drop = OptionMenu(toolframe , self.typa , *opt)
        drop.pack(anchor = "nw")

        self.typa.trace("w",self.poop)
        
        #for the time choice 
        #self.toolFrameTime = Frame(toolframe,bg = "white", highlightbackground = "pink", highlightthickness = 5 )
        
        time_config = Label(self.f, text = "1" , font=('Helvetica 5 bold'))
        time_config.pack(pady = (5))

##        self.toolFrameTime = Frame(toolframe,bg = "white", highlightbackground = "pink", highlightthickness = 5 )
##        
##        time_config = Label(self.toolFrameTime, text = "Time Configuration" , font=('Helvetica 5 bold'))
##        time_config.pack()
        

##        #for the pictures choice
##        toolframe = Frame(self.f,bg = "yellow", highlightbackground = "pink", highlightthickness = 5 )
##        toolframe.pack(expand = True , fill = BOTH , side = BOTTOM)

        
s = Screen(topmost_f,"hey")
s1 = Screen(topmost_f, "heyoo")
s2 = Screen(topmost_f, "heyoo")
s3 = Screen(topmost_f, "heyoo")
s.build(1,0)
s1.build(1,1)
s2.build(1,2)
s3.build(2,0)
win.mainloop()        
