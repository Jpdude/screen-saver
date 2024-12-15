from tkinter import *
from PIL import Image , ImageTk
import os
import time
from datetime import datetime
from screeninfo import get_monitors
import pyautogui
print(datetime.now().minute)
Directory = os.getcwd()
print('Directoy:',Directory)
pic_list = []
for path , dirs , files in os.walk(Directory):
    pic_no = 0
    for x in files:
        if x.endswith(".jpg") == True or x.endswith(".png") == True or x.endswith(".jpeg") == True or x.endswith(".JPG") == True:
            pic_no += 1
            pic_list.append(str(x))
def full(self):
    if win.attributes('-fullscreen'):
        win.attributes('-fullscreen',False)
        t.attributes('-fullscreen',False)
    else:
        win.attributes('-fullscreen',True)
        t.attributes('-fullscreen',True)
        win.geometry("300x322-1959+0")
        
win = Tk(screenName = ":0.2")


##print(win.winfo_screen())
##win.title("{POOP")
##win.geometry("300x322-1959+0")
##screen_width = win.winfo_screenwidth()
##screen_heigth = win.winfo_screenheight()
##frame1 = Frame(win, bg = "#000000")
##img = Image.open("mini.jpg")
##img = img.resize((1920,1080))
##print(img.size,)
###img = img.resize((1920,1080))
##img2 = ImageTk.PhotoImage(img)
##t = Toplevel(win)
##t.title("poop")
##can_1 = Canvas(frame1, width = screen_width , height = screen_heigth,bg = "#000000")
##can_1.create_image((0,0) , image = img2,anchor = "nw")
##can_1.pack(fill = "both",expand = True, ipadx = 0 , ipady = 0)
##
##img = Image.open("poo2.jpg")
##img = img.resize((1920,1080))
##img1 = ImageTk.PhotoImage(img)
##can_2 = Canvas(t, width = screen_width , height = screen_heigth,bg = "#000000")
##can_2.create_image((0,0) , image = img1,anchor = "nw")
##can_2.pack(fill = "both",expand = True, ipadx = 0 , ipady = 0)
##frame1.pack(fill = "both",expand = True)
##win.bind("f",full)



class Display:
    def __init__(self,master,display,pic = 0,typeof = "PIC"):
        self.master = master
        self.pic = pic
        self.display = display
        self.typeof = typeof.upper()
        self.time = 0
        self.picn = 0
        self.change_time = 2



    def create(self):
        self.t = Toplevel(self.master,bg = "black")
        self.t.title("PooPz")
        self.t.bind("f",self.full)
        if self.typeof == "PIC":
            self.t["bg"] = "black"
            self.can_1 = Canvas(self.t, width = self.display.width , height = self.display.height,bg = "#000000")
            self.image_id = self.can_1.create_image((0,0) , image = self.gen_image(self.pic),anchor = "nw")
            self.can_1.pack(fill = "both",expand = True, ipadx = 0 , ipady = 0)
            if self.pic == 0:
                self.roulette()
        else:
            self.t.rowconfigure(index = 0,weight = 1,uniform="u")
            self.t.rowconfigure(index = 1,weight = 2,uniform="u")
            self.t.rowconfigure(index = 2,weight = 1,uniform="u")

            self.t.columnconfigure(index = 0,weight = 2,uniform="u")
            self.t.columnconfigure(index = 1,weight = 15,uniform="u")
            self.t.columnconfigure(index = 2,weight = 1,uniform="u")
            self.t.columnconfigure(index = 3,weight = 2,uniform="u")
            d = datetime.now().strftime("%I:%M:%S %p")
            print(d)

            self.d = Label(self.t, text=f'{datetime.now().strftime("%a")}', font=('Consolas', 30, "bold",), fg="white",bg = "black") 
            self.d.grid(row = 0 , column = 0,sticky = "nw")
            
            self.h = Label(self.t, text=f'{datetime.now().strftime("%I:%M:%S")}', font=('Consolas', 150, "bold",), fg="white",bg = "black") 
            self.h.grid(row = 1 , column = 1,sticky = "e")
            
            self.a = Label(self.t, text=f'{datetime.now().strftime("%p")}', font=('Consolas', 20, "bold",), fg="white",bg = "black") 
            self.a.grid(row = 1 , column = 2 , sticky = "ww")


            self.roulette()
        
    def gen_image(self,n,strech = True):
        if self.pic == 0:
            img = Image.open(pic_list[n])
        else:
            img = Image.open(n)
        
        if strech:
            img = img.resize((self.display.width,self.display.height))
            
        self.img1 = ImageTk.PhotoImage(img) # made it an instance variable(self.) cuz if i dont tkinter stupidly disposes of the variable  
        return self.img1

    def roulette(self):
        if self.typeof == "PIC":
            if int(self.time_func()) == self.change_time:
                print("HIA")
                self.picn+=1
                self.can_1.delete(self.image_id)
                try:
                    self.image_id = self.can_1.create_image((0,0) , image = self.gen_image(self.picn),anchor = "nw")
                except IndexError:
                    self.picn = 0
                    self.image_id = self.can_1.create_image((0,0) , image = self.gen_image(self.picn),anchor = "nw")
                self.time = 0
                
            ...
        else:
            self.h["text"] = f'{datetime.now().strftime("%I:%M:%S")}'
        self.t.after(100,self.roulette)

    def time_func(self):
        if self.time == 0:
            self.time = time.time()
        return time.time() - self.time
    
    def full(self,key):
        if self.t.attributes('-fullscreen'):
            self.t.attributes('-fullscreen',False)  
        else:
            self.t.attributes('-fullscreen',True)

        print(self.display.x)
        if self.display.x > 0 or self.display.y > 0:
            pyautogui.hotkey('shift','win', 'left', interval=0.1)
        elif self.display.x < 0 or self.display.y < 0:
            pyautogui.hotkey('shift', 'win', 'right', interval=0.1)
        else:
            pass


            
        
y = get_monitors()
print(y)
x = Display(win,y[2])
x.create()

z = Display(win,y[1],typeof = "P")
z.create()
win.mainloop()       
        
def resiszer(img):
    ...
    
