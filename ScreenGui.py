from tkinter import *
win = Tk()
win.title("Window Manager")

f = Frame(win, highlightbackground = "red", highlightthickness = 1 )
# for x in y.windows():
#   f.columnfigure(index = x , weight = 1 )
f.columnconfigure(index = 0 , weight = 1 , uniform ="u")
f.columnconfigure(index = 1 , weight = 1 , uniform ="u")
f.columnconfigure(index = 2 , weight = 1 , uniform ="u")

f.rowconfigure(index = 0 , weight = 0 , uniform ="u")
f.rowconfigure(index = 1 , weight = 2 , uniform ="u")
f.rowconfigure(index = 2 , weight = 0 , uniform ="u")
f.grid(row = 0 , column = 0)

heading_label = Label(f , text = "Detected Windows", font = ("comic sans",20,"bold")).grid( row = 0 , column = 0 )

class Screen:
    def __init__(self,master,screen):
        self.master = master
        self.screen = screen

    def build(self,row,column):
        print(row,column)
        self.f = Frame(self.master, highlightbackground = "black", highlightthickness = 1 )
        self.f.rowconfigure(index = 0 , weight = 1 , uniform = "p")
        self.f.rowconfigure(index = 1 , weight = 2 , uniform = "p")
        self.f.grid(row = row, column = column  )
        
        
        viewframe = Frame(self.f , bg = "red" , highlightbackground = "yellow", highlightthickness = 1)
        viewframe.grid(row = 0 , column = 0 )
        self.viewCanvas = Frame(viewframe,bg = "black" , highlightbackground = "black", highlightthickness = 1 )
        self.viewCanvas.pack()
        screen = Label(self.viewCanvas, text = "2").pack()
        
        

        toolframe = Frame(self.f,bg = "yellow", highlightbackground = "pink", highlightthickness = 1 )
        toolframe.grid(row = 1 , column = 0)

        
s = Screen(f,"hey")
s.build(1,0)
win.mainloop()        
