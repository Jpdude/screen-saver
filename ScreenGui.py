from tkinter import *
from tkinter import filedialog as fd
from screeninfo import get_monitors
win = Tk()
win.title("Window Manager")
from PIL import Image , ImageTk
img = Image.open("C:\\Users\\user\\AppData\\Roaming\\Microsoft\\Windows\\Themes\\TranscodedWallpaper")
img = img.resize((480,270))
img1 = ImageTk.PhotoImage(img)

topmost_f = ScrollableFrame(win)
# for x in y.windows():
#   f.columnfigure(index = x , weight = 1 )

# Where I configured the grid layout of the topmost frame
topmost_f.columnconfigure(index = 0 , weight = 1 , uniform ="u")
topmost_f.columnconfigure(index = 1 , weight = 1 , uniform ="u")
topmost_f.columnconfigure(index = 2 , weight = 1 , uniform ="u")

topmost_f.rowconfigure(index = 0 , weight = 1 , uniform ="u")
topmost_f.rowconfigure(index = 1 , weight = 10 , uniform ="u")
topmost_f.rowconfigure(index = 2 , weight = 1 , uniform ="u")



#topmost_f.config( yscrollcommand=vbar.set)
topmost_f.pack(side = LEFT , fill = "both" , expand = True)
#=====================ENDS=================================


heading_label = Label(topmost_f , text = "Detected Windows", font = ("comic sans",20,"bold")).grid( row = 0 , column = 0 , sticky = "nw")


class Screen:
    def __init__(self,master,screen,last = ""):
        self.master = master
        self.screen = screen
        self.last = last

    def revealrl(self):
        print("jodfnojhnd")
        if self.roulette_ckbtn_var.get() == 1:
            for child in self.static_frameholder.winfo_children():
                child.configure(state = "disabled")
                print(child)
            self.roulette_optLblFrm.pack(pady = 20)
        else:
            for child in self.static_frameholder.winfo_children():
                child.configure(state = "normal")
            self.roulette_optLblFrm.pack_forget()
            
    def poop(self,x,y,z):
        
            self.toolFrameTime.pack_forget()
            self.toolFramePic.pack_forget()
            
            if self.typa.get() == "Time":
                self.toolFrameTime.pack(anchor = "nw", pady = 10 , padx = 10)
            elif self.typa.get() == "Pictures":
                self.toolFramePic.pack(anchor = "nw", pady = 10 , padx = 10)
    #Note to self rmr to make these functions dynamic in the future ( opendir and openfile) like a variable is passed to them and they just pass on the path to the variable
    def opendir(self):
        
        fname = fd.askdirectory()
        self.current_dir.set(fname)
        
    def openfile(self):

        ft = (("Images","*.jpg"),("Images","*.png"),("Images","*.jpeg"),("Images","*.JPG") )
        
        fname = fd.askopenfilename(
            title = "open a file",
            filetypes = ft,
            )
        self.current_static_pic.set(fname)
    def build(self,row,column):
        print(row,column)
        self.f = Frame(self.master, highlightbackground = "black", highlightthickness = 1 )
        if self.last == "":
            self.f.grid(row = row, column = column ,sticky = "n" ,padx = 15 ,pady = 15  )
        else:
            self.f.grid(row = row, column = column ,sticky = "n" ,padx = 15 ,pady = 15,rowspan = 100  )
            
        
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
        types.pack(padx=(0,20))

        corner_time = Entry(types, bg = "#ffffff" , width = 7 , textvariable = self.current_time , relief = "flat" )  
        corner_time.pack(anchor = "ne" , padx = (0,5), pady = (0,5))
        
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
        templating.pack(pady = (0,15))

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

        #-------------------------------------PICTURES-----------------------------------------------
        #-------------------------------------PICTURES-----------------------------------------------
        #-------------------------------------PICTURES-----------------------------------------------

        #--------------All Vars and options for option menus-------
        self.current_static_pic = StringVar()
        self.current_interval = IntVar()
        self.current_dir = StringVar()

        optPic = ["Please Choose Template","Time" ,"Pictures","Music"]
        self.typatempPic = StringVar()
        self.typatempPic.set(optPic[0])
        #--------------------END----------------------------
        #for the Picture choice 
        self.toolFramePic = Frame(toolframe,bg = "white")

        self.roulette_ckbtn_var = IntVar()
        self.roulette_ckbtn_var.set(0)
        

        roulette_ckbtn = Checkbutton(self.toolFramePic , text = "Roulette" , onvalue = 1 , offvalue = 0 ,bg = "white",variable = self.roulette_ckbtn_var,command = self.revealrl)
        roulette_ckbtn.pack()
        

        self.static_frameholder = Frame(self.toolFramePic, bg = "#ffffff")
        self.static_frameholder.pack()

        static_lbl = Label(self.static_frameholder , text  = "Static: " , bg = "#ffffff").pack(side = LEFT)
        static_ent = Entry(self.static_frameholder , textvariable = self.current_static_pic, bg = "#ffffff")
        static_ent.pack(side = LEFT)
        static_fileOpenBtn = Button(self.static_frameholder , text = "Open File" , command = self.openfile, bg = "#ffffff").pack(side = LEFT)


        self.roulette_optLblFrm = LabelFrame(self.toolFramePic, bg = "#ffffff")
        
        
        rlbls = ['Interval' , "Directory" , "Templates"]
        x = 0
        for lbls in rlbls:
            lbls_frm = Label(self.roulette_optLblFrm,text = lbls, bg = "#ffffff").grid(row = x , column = 0)
            x+=1

        interval_ent = Entry(self.roulette_optLblFrm , textvariable = self.current_interval, bg = "#ffffff").grid(row = 0 , column = 1)
        directory_ent = Entry(self.roulette_optLblFrm , textvariable = self.current_dir, bg = "#ffffff").grid(row = 1 , column = 1)
        static_fileOpenBtn = Button(self.roulette_optLblFrm , text = "Open File" , command = self.opendir, bg = "#ffffff").grid(row = 1 , column = 2)

        drop_tempPic = OptionMenu(self.roulette_optLblFrm , self.typatempPic , *optPic )
        drop_tempPic.configure(state="disabled")
        drop_tempPic.grid(row = 2 , column = 1)

        
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
s3 = Screen(topmost_f, "heyoo",last = "adg")
s.build(1,0)
s1.build(1,1)
s2.build(1,2)
s3.build(2,0)
win.mainloop()        
