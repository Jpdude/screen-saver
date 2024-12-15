from tkinter import *
win = Tk()
win.title("Window Manager")

#Making the top most frame in red
topmost_f = Frame(win, highlightbackground = "red", highlightthickness = 1 ,bg = "white")
# for x in y.windows():
#   f.columnfigure(index = x , weight = 1 )

# Where I configured the grid layout of the topmost frame
topmost_f.columnconfigure(index = 0 , weight = 1 , uniform ="u")
topmost_f.columnconfigure(index = 1 , weight = 1 , uniform ="u")
topmost_f.columnconfigure(index = 2 , weight = 1 , uniform ="u")

topmost_f.rowconfigure(index = 0 , weight = 1 , uniform ="u")
topmost_f.rowconfigure(index = 1 , weight = 15 , uniform ="u")
topmost_f.rowconfigure(index = 2 , weight = 1 , uniform ="u")
topmost_f.grid(row = 0 , column = 0)
#=====================ENDS=================================


heading_label = Label(topmost_f , text = "Detected Windows", font = ("comic sans",20,"bold")).grid( row = 0 , column = 0 )

class Screen:
    def __init__(self,master,screen):
        self.master = master
        self.screen = screen

    def build(self,row,column):
        print(row,column)
        self.f = Frame(self.master, highlightbackground = "black", highlightthickness = 1 )
        self.f.rowconfigure(index = 0 , weight = 0 , uniform = "p")
        self.f.rowconfigure(index = 1 , weight = 1, uniform = "p")
        self.f.grid(row = row, column = column ,sticky = "nsew"  )
        
        
        viewframe = Frame(self.f , bg = "red" , highlightbackground = "yellow", highlightthickness = 1)
        viewframe.grid(row = 0 , column = 0 ,sticky = "nsew")

        view_canvas = Canvas(viewframe ,  width = 350 , height = 350 ,bg = "#000000")
        view_canvas.pack(fill = "both" , expand = True)
        
        

        toolframe = Frame(self.f,bg = "yellow", highlightbackground = "pink", highlightthickness = 5 )
        toolframe.grid(row = 1 , column = 0)

        
s = Screen(topmost_f,"hey")
s.build(1,0)
win.mainloop()        
