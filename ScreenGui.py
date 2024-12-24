from tkinter import *
win = Tk()
win.title("Window Manager")

##win.rowconfigure(index = 0 , weight = 1 , uniform ="u")
##win.rowconfigure(index = 1 , weight = 2 , uniform ="u")
#=====================ENDS=================================

heading_label = Label(win , text = "Detected Windows", font = ("comic sans",20,"bold")).pack(side = TOP , expand = True)
topmost_frame = Frame(win, highlightbackground = "black", highlightthickness = 1 , bg = "red" )
topmost_frame.pack( side = BOTTOM , expand = True , fill = BOTH)
#heading_label = Label(topmost_frame , text = "Detected Windows", font = ("comic sans",20,"bold")).pack()
print(topmost_frame.pack_info())
class Screen:
    def __init__(self,master,screen):
        self.master = master
        self.screen = screen

    def build(self,row,column):
        print(row,column)
        self.f = Frame(self.master, highlightbackground = "black", highlightthickness = 1 )
        self.f.rowconfigure(index = 0 , weight = 0 , uniform = "p")
        self.f.rowconfigure(index = 1 , weight = 1, uniform = "p")
        self.f.grid(row = row, column = column ,sticky = "nsew" ,padx = 20  )
        
        
        viewframe = Frame(self.f , bg = "red" , highlightbackground = "yellow", highlightthickness = 1)
        viewframe.grid(row = 0 , column = 0 ,sticky = "nsew")

        view_canvas = Canvas(viewframe ,  width = 500 , height = 300 ,bg = "#000000")
        view_canvas.pack(fill = "both" , expand = True)
        
        

        toolframe = Frame(self.f,bg = "yellow", highlightbackground = "pink", highlightthickness = 5 )
        toolframe.grid(row = 1 , column = 0)

        
##s = Screen(topmost_f,"hey")
##s1 = Screen(topmost_f, "heyoo")
##s2 = Screen(topmost_f, "heyoo")
##s.build(1,0)
##s1.build(1,1)
##s2.build(1,2)
win.mainloop()        
