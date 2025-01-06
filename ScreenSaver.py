from tkinter import *
from PIL import Image , ImageTk
import os
import time
from datetime import datetime
from screeninfo import get_monitors
import pyautogui
import pymonctl as pmc
import win32gui
from zoneinfo import ZoneInfo
print(ZoneInfo("America/New_York"))
#print("rt",pmc.getAllMonitors()[2].setBrightness(30))
print(datetime.now().minute)
Directory = os.getcwd()
print('Directoy:',Directory)

            
def full(self):
    if win.attributes('-fullscreen'):
        win.attributes('-fullscreen',False)
        t.attributes('-fullscreen',False)
    else:
        win.attributes('-fullscreen',True)
        t.attributes('-fullscreen',True)
        win.geometry("300x322-1959+0")
        
#win = Tk(screenName = ":0.2")

##print(win.winfo_screen())
#win.title("{POOP")
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

class Timer():
    def __init__(self,display,win,countdown = None):
        self.buffer = 0
        #self.time = int(display.time)
        self.time = countdown
        self.active = False
        self.times = "000"
        self.display = display
        self.countdown = countdown
        self.win = win
        #self.win.bell() very useful for debugging
        print("wrwrghe",countdown,self.time)


    def initiate(self):
        self.buffer = 0
        self.initial = time.time()
        self.active = True
        

    def stop(self):
        self.unpause()
        self.active = False
        print("Time Elapsed",self.times)
        
        
    def destroy(self):
        self.active = False
        self.win.after_cancel(self.callback)
        

    def start(self):
        #self.countdown = countdown #prob
        stop = time.time()
        times = stop - (self.initial+self.buffer)
            
        self.times = times
        if self.countdown:
            red = True if (0.5*self.time) <= self.times else False
            if red:
                self.display.h['foreground'] = "red"
                self.display.d['foreground'] = "red"
                self.display.d['text'] = "YOU'RE RUNNING OUT OF TIME!"
            else:
                self.display.h['foreground'] = "white"

        t = int(self.times/60)
        t = str(t)
        r = int(self.times%60)
        if self.countdown:
            if self.time == int(self.times):
                self.display.h['text'] = "00:00.00"
                self.display.d["text"] = "TIMES UP!"
                self.active = False
                self.win.bell()
                
                
            t1 = int(self.time/60)
            r1 = int(self.time%60)
            t = str(int(t1) - int(t))
            r = r1 - r
        if r == 0 or r in range(0,10) :
            r = '0' + str(r)
        #print(str(self.times%1)[2:4])
        #print(self.times - (int(r)*60))
        try:
            if self.time != int(self.times):
                self.display.h['text'] = f"{t}:{r}.{str(self.times%1)[2:4]}" # I know im meant to do %60 at the self.times ill do it l8r
                if self.active:
                    self.callback = self.win.after(100,self.start)
        except ValueError:
            self.display.h['text'] = "ERROR!"
            pass

    def pause(self):
        self.pause_start = time.time()
        self.destroy()
        self.win.bind('u',lambda x:self.unpause())
        self.win.unbind('p')

    def unpause(self):
        self.active = True
        pause_stop = time.time()
        try:
            self.buffer += ( pause_stop - self.pause_start)#prob self.Pause_start
        except AttributeError:
            pass

        try:
            self.win.after(100,self.start)
        except:
            pass
        self.win.bind('p',lambda x:self.pause())
        self.win.unbind('u')
        pass

class Display:
    def __init__(self,master,display,pic = 0,typeof = "PIC",dire = 0, inter = 20,dupObj="",time = 5):
        self.master = master
        self.pic = pic
        self.display = display
        self.typeof = typeof.upper()
        self.timess = 0
        self.picn = 0
        self.change_time = inter
        self.dire = dire
        self.dupObj = dupObj
        self.time = time
        


    def create(self):
        self.t = Toplevel(self.master,bg = "black")
        self.t.geometry(f"{self.display.width}x{self.display.height}+{self.display.x}+{self.display.y}")
        self.t.title("Screen"+self.display.name[-1])
        self.t.bind("f",self.full)
        
        if self.typeof == "PIC":
            self.t["bg"] = "black"
            if self.dire != 0:
                self.get_pic_list()
            self.can_1 = Canvas(self.t, width = self.display.width , height = self.display.height,bg = "#000000")
            self.image_id = self.can_1.create_image((0,0) , image = self.gen_image(self.pic),anchor = "nw")
            self.can_1.pack(fill = "both",expand = True, ipadx = 0 , ipady = 0)
            if self.pic == 0:
                self.roulette()
        elif self.typeof == "POOP":
            self.tz_list =[]
            self.t.rowconfigure(index = 0,weight = 1,uniform="u")
            self.t.rowconfigure(index = 1,weight = 2,uniform="u")
            self.t.rowconfigure(index = 2,weight = 1,uniform="u")

            self.t.columnconfigure(index = 0,weight = 1,uniform="u")
            self.t.columnconfigure(index = 1,weight = 2,uniform="u")
            self.t.columnconfigure(index = 2,weight = 1,uniform="u")
            
            self.maps = [["Texas",ZoneInfo("CST6CDT")],["Nigeria",ZoneInfo("Africa/lagos")],["India",ZoneInfo("Asia/Kolkata")],
                         ["Australia",ZoneInfo("Australia/Sydney")],
                         ["Kamloops",ZoneInfo("Canada/Pacific")],["London",ZoneInfo("GMT")],
                         ["Pennsylvania ",ZoneInfo("EST")],
                         ["Mozambique",ZoneInfo("Africa/Harare")],["Manitoba",ZoneInfo("Africa/lagos")]]
            y = 0
            z = -1
            for x in self.maps:
                theme1 = "#808080" if datetime.now(x[1]).strftime("%p") == "AM" else "#000000"
                theme2 = "#D3D3D3" if datetime.now(x[1]).strftime("%p") == "AM" else "#ffffff"
                self.tz = Frame(self.t,bg = theme1,highlightbackground = "#ffffff",highlightthickness = 1)
                self.tz.rowconfigure(index = 0,weight = 1,uniform="u")
                self.tz.rowconfigure(index = 1,weight = 2,uniform="u")
                self.tz.rowconfigure(index = 2,weight = 1,uniform="u")

                self.tz.columnconfigure(index = 0,weight = 2,uniform="u")
                self.tz.columnconfigure(index = 1,weight = 15,uniform="u")
                self.tz.columnconfigure(index = 2,weight = 1,uniform="u")
                self.tz.columnconfigure(index = 3,weight = 2,uniform="u")
                
                d = datetime.now(x[1]).strftime("%I:%M:%S %p")
                print(x)
                name = x[0]
                print("nadm",name)
                d = Label(self.tz, text=f'{name}:{datetime.now(x[1]).strftime("%a")}', font=('Consolas', 20, "bold",), fg=theme2,bg = theme1) 
                d.grid(row = 0 , column = 0,sticky = "nw",columnspan = 100)
                
                h = Label(self.tz, text=f'{datetime.now(x[1]).strftime("%I:%M:%S")}', font=('Consolas', 30, "bold",), fg=theme2,bg = theme1) 
                h.grid(row = 1 , column = 1,sticky = "e")
                
                a = Label(self.tz, text=f'{datetime.now(x[1]).strftime("%p")}', font=('Consolas', 15, "bold",), fg=theme2,bg = theme1) 
                a.grid(row = 1 , column = 2 , sticky = "w")
                #Evnentually youd have to add self.d and a to the roulttee

                if y % 3 == 0:
                    z+= 1
                if z == 1 and y%3 == 1:
                    h["font"] = ('Consolas', 80, "bold",)
                print(z,y%3)    
                self.tz.grid(row = z , column  = y%3 , sticky = "nsew")
                y+=1
                self.tz_list.append([h,x[1],d,a,self.tz])
                
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

            self.d = Label(self.t, text=f'{datetime.now().strftime("%a")}', font=('Consolas', 30, "bold",), fg="white",bg = "black") 
            self.d.grid(row = 0 , column = 0,sticky = "nw",columnspan = 100)
            
            self.h = Label(self.t, text=f'{datetime.now().strftime("%I:%M:%S")}', font=('Consolas', 150, "bold",), fg="white",bg = "black") 
            self.h.grid(row = 1 , column = 1,sticky = "e")
            
            self.a = Label(self.t, text=f'{datetime.now().strftime("%p")}', font=('Consolas', 20, "bold",), fg="white",bg = "black") 
            self.a.grid(row = 1 , column = 2 , sticky = "ww")
            #Evnentually youd have to add self.d and a to the roulttee

            if self.typeof == "TT":
                self.a["text"] = "s"
                self.tie = Timer(self,self.master)
                self.tie.initiate()
                self.tie.start()
            elif self.typeof == "CD":
                self.a["text"] = "s"
                self.tie = Timer(self,self.master,countdown = self.time)
                self.tie.initiate()
                self.tie.start()
                

            else:
                self.roulette()

    def get_pic_list(self):
        self.pic_list = []
        for path , dirs , files in os.walk(self.dire):
            pic_no = 0
            for x in files:
                if x.endswith(".jpg") == True or x.endswith(".png") == True or x.endswith(".jpeg") == True or x.endswith(".JPG") == True:
                    pic_no += 1
                    self.pic_list.append(str(x))
        
    def destroy(self):
        self.t.withdraw()
        
    def getTime(self):
        try:
            return self.h["text"]
        except:
            return None
    
    def gen_image(self,n,strech = True):
        if self.pic == 0:
            img = Image.open(self.dire +'/'+self.pic_list[n])
        else:
            img = Image.open(n)
        
        if strech:
            img = img.resize((self.display.width,self.display.height))
            
        self.img1 = ImageTk.PhotoImage(img) # made it an instance variable(self.) cuz if i dont tkinter stupidly disposes of the variable  
        return self.img1

    def roulette(self,gg =""):
        
        if self.typeof == "PIC":
            #print("sg",int(self.time_func()),self.change_time)
            if int(self.time_func()) == self.change_time:
                self.picn+=1
                self.can_1.delete(self.image_id)
                try:
                    self.image_id = self.can_1.create_image((0,0) , image = self.gen_image(self.picn),anchor = "nw")
                except IndexError:
                    self.picn = 0
                    self.image_id = self.can_1.create_image((0,0) , image = self.gen_image(self.picn),anchor = "nw")
                self.timess = 0
                
            ...
        else:
            if self.typeof == "POOP":
                for x in self.tz_list:
                    #text = datetime.now().replace(tzinfo = x[1])
                    text = datetime.now().now(x[1])
                    theme1 = "#808080" if datetime.now(x[1]).strftime("%p") == "AM" else "#000000"
                    theme2 = "#D3D3D3" if datetime.now(x[1]).strftime("%p") == "AM" else "#ffffff"
                    x[0]["bg"] =theme1
                    x[2]["bg"] =theme1
                    x[3]["bg"] =theme1

                    x[0]["fg"] =theme2
                    x[2]["fg"] =theme2
                    x[3]["fg"] =theme2
                    
                    x[4]["bg"] = theme1
                    x[0]["text"] = f'{text.strftime("%I:%M:%S")}'
            else:
                self.h["text"] = f'{datetime.now().strftime("%I:%M:%S")}'
        self.t.after(100,self.roulette)

    def time_func(self):
        if self.timess == 0:
            self.timess = time.time()
        return time.time() - self.timess

    def enumHandler(self,hwnd, lParam):
        if win32gui.IsWindowVisible(hwnd):
            if f'Screen{self.display.name[-1]}' in win32gui.GetWindowText(hwnd):
                win32gui.MoveWindow(hwnd, self.display.x, 0, self.display.width, self.display.height, True)

    def full(self,key):
        if self.t.attributes('-fullscreen'):
            self.t.attributes('-fullscreen',False)  
        else:
            self.t.attributes('-fullscreen',True)

        win32gui.EnumWindows(self.enumHandler, None)
    
##        print(self.display.x)
##        if self.display.x > 0 or self.display.y > 0:
##            pyautogui.hotkey('shift','win', 'left', interval=0.1)
##        elif self.display.x < 0 or self.display.y < 0:
##            pyautogui.hotkey('shift', 'win', 'right', interval=0.1)
##        else:
##            pass


            
        
#y = get_monitors()
#print(y)
##x = Display(win,y[2],typeof = "POOP")
##x.create()
##
##z = Display(win,y[1],typeof = "P")
##z.create()
#win.mainloop()       

#Windows wallpaper
#img = Image.open("C:\\Users\\user\\AppData\\Roaming\\Microsoft\\Windows\\Themes\\TranscodedWallpaper")
def resiszer(img):
    ...
    
