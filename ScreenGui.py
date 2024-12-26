from tkinter import *
win = Tk()
win.title("Window Manager")

#Making the top most frame in red
topmost_f = Canvas(win, highlightbackground = "red", highlightthickness = 1 ,scrollregion=(0,0,500,500))
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

    def build(self,row,column):
        print(row,column)
        self.f = Frame(self.master, highlightbackground = "black", highlightthickness = 1 )
        self.f.grid(row = row, column = column ,sticky = "nsew" ,padx = 15  )
        
        
        viewframe = Frame(self.f , bg = "red" , highlightbackground = "yellow", highlightthickness = 1)
        viewframe.pack(expand = True , fill = BOTH , side = TOP)

        
        
        

        toolframe = Frame(self.f,bg = "yellow", highlightbackground = "pink", highlightthickness = 5 )
        toolframe.pack(expand = True , fill = BOTH , side = BOTTOM)

        
s = Screen(topmost_f,"hey")
s1 = Screen(topmost_f, "heyoo")
s2 = Screen(topmost_f, "heyoo")
s3 = Screen(topmost_f, "heyoo")
s.build(1,0)
s1.build(1,1)
s2.build(1,2)
s3.build(2,0)
win.mainloop()        
