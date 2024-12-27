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
            self.toolFrameTime.pack_forget()
            print("poop:",self.typa.get(),y,z,self.master.grid_slaves())
            if self.typa.get() == "Time":
                self.toolFrameTime.pack(anchor = "nw", pady = 10 , padx = 10)
                ...
    def build(self,row,column):
        print(row,column)
        self.f = Frame(self.master, highlightbackground = "black", highlightthickness = 1 )
        self.f.grid(row = row, column = column ,sticky = "ns" ,padx = 15 ,pady = 15 )
        
        
        viewframe = Canvas(self.f, width = 480 , height = 270 , bg = "black")
        self.image_id = viewframe.create_image((0,0) , image = img1,anchor = "nw")
        #viewframe.create_text(550, 250, text="1", fill="WHITE", font=('Helvetica 15 bold'))
        viewframe.pack( fill = X , side = TOP  )
        print("JJ:",viewframe.cget("width"),viewframe.keys(),self.f.bbox())
        win_no = Label(self.f, text = "1" , font=('Helvetica 10 bold'))
        win_no.pack(pady = (5))
        #-------------------------------------TIME-----------------------------------------------
        #-------------------------------------TIME-----------------------------------------------
        #-------------------------------------TIME-----------------------------------------------

        #--------------All Vars and options for option menus-------
        self.current_time = StringVar()
        self.current_time.set("5:30.23")

        opt = ["Please Choose Type","Time" ,"Pictures","Music"]
        self.typa = StringVar()
        self.typa.set(opt[0])

        opt_time_zone = ["System Time","GMT +2" ]
        self.typa_time = StringVar()
        self.typa_time.set(opt_time_zone[0])

        opt_templates = ["Default","Jp Custom 1" ]
        self.temp = StringVar()
        self.temp.set(opt_templates[0])
        #--------------------END----------------------------
        
        toolframe = Frame(self.f,bg = "#ffffff", highlightbackground = "pink", highlightthickness = 5 )
        toolframe.pack(expand = True , fill = BOTH , side = BOTTOM)

        drop = OptionMenu(toolframe , self.typa , *opt)
        drop.pack(anchor = "nw")

        self.typa.trace("w",self.poop)
        
        #for the time choice 
        self.toolFrameTime = Frame(toolframe,bg = "white")
        
        

        #-------------------------------------------------------------------------------------
        time_config = LabelFrame(self.toolFrameTime, text = "Time Configuration", bg = "#ffffff" )
        time_config.pack(pady = (5))

        drop_time_zone = OptionMenu(time_config , self.typa_time , *opt_time_zone)
        drop_time_zone.pack()
        
        current_time = Label(time_config, text="Current Time: 5:00", bg = "#ffffff")  
        current_time.pack()  
        #-------------------------------------------------------------------------------------

        #-------------------------------------------------------------------------------------
        types = LabelFrame(self.toolFrameTime, text = "Types", bg = "#ffffff" )
        types.pack(pady = (5))

        corner_time = Entry(types, bg = "#ffffff" , width = 7 , textvariable = self.current_time , relief = "flat" )  
        corner_time.pack(anchor = "ne" , padx = (0,10), pady = (0,10))
        
        ar1 = Frame(types, bg = "#ffffff")
        ar1.pack()
        drop_time_zone = Label(ar1 , text="Stopwatch:", bg = "#ffffff").pack(side = LEFT)

        stopwatch_btn = Button(ar1, text = "Start")
        stopwatch_btn.pack(side = LEFT)
        
        ar2 = Frame(types, bg = "#ffffff")
        ar2.pack()
        drop_time_zone = Label(ar2 , text="Timer:", bg = "#ffffff").pack(side = LEFT)

        timer_btn = Button(ar2, text = "Start")
        timer_btn.pack(side = LEFT)
        #-------------------------------------------------------------------------------------



        #-------------------------------------------------------------------------------------
        templating = LabelFrame(self.toolFrameTime, text = "Templating", bg = "#ffffff" )
        templating.pack(pady = (5))

        drop_template = OptionMenu(templating , self.temp , *opt_templates)
        drop_template.pack()
        
        current_time = Button(templating, text="+ Add Template", bg = "#ffffff")  
        current_time.pack()
        
        current_time = Button(templating, text="- Remove Template", bg = "#ffffff")  
        current_time.pack()
        
        current_time = Button(templating, text=" Edit Template", bg = "#ffffff")  
        current_time.pack()
        #-------------------------------------------------------------------------------------


        #-------------------------------------TIME-----------------------------------------------
        #-------------------------------------TIME-----------------------------------------------
        #-------------------------------------TIME-----------------------------------------------
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
