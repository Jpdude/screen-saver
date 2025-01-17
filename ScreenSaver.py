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
import argparse


Directory = os.getcwd()
            

class Timer():
    def __init__(self,display,win,countdown = None):
        self.buffer = 0 #Buffer Incase paused
        self.countdown = countdown # Countdown meaning the the time to countdown
        self.active = False #Needed for pausing and unpausing
        self.display = display #The display instance to be edited
        self.win = win #Window needed for event , But self.diplay.t could be used havent tested it yet

    #Initiates Timer 
    def initiate(self):
        self.buffer = 0
        self.initial = time.time()
        self.active = True
        

    def stop(self):
        self.unpause()
        self.active = False
        
        
    #Destroys timer event
    def destroy(self):
        self.active = False
        self.win.after_cancel(self.callback)
        
    #self.times is the current time
    def start(self):
        stop = time.time()
        self.times = stop - (self.initial+self.buffer)#Adjusting time incase Paused
            
        if self.countdown:
            red = True if (0.5*self.countdown) <= self.times else False #Checking if the countdown has gone down by half to display Error message
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
            if self.countdown == int(self.times):
                self.display.h['text'] = "00:00.00"
                self.display.d["text"] = "TIMES UP!"
                self.win.bell()
                self.active = False
                self.win.bell()
                self.win.bell()
                self.win.bell()
                
                
            t1 = int(self.countdown/60) 
            r1 = int(self.countdown%60)
            tp = int(int(t1) - int(t))
            t = int(int(t1) - int(t)-1) if self.countdown%60 == 0 else tp
            if t == -1:
                t = "00"
            if self.countdown%60 == 0:
                r = 59 - (r - r1)
            else:
                r = r1 - r
            
        if r == 0 or r in range(0,10) :# Making sure it displays as double digits i.e 01 instead of 1
            r = '0' + str(r)
        if t in range(0,10):
            t = '0' + str(t)
        
        try:
            if self.countdown != int(self.times):
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

    def __init__(self,master,display,pic = None,typeof = "PIC",dire = 0, inter = 20,time = 5):
        self.master = master
        if not self.master:
            self.master = Display.win 
        self.pic = pic
        self.display = display
        self.typeof = typeof.upper()
        self.timess = 0
        self.picn = 0
        self.change_time = inter
        self.dire = dire
        self.time = time
        print("ksfgs")
        


    def create(self):
        print("Created")
        self.t = Toplevel(self.master,bg = "black")
        self.t.geometry(f"{self.display.width}x{self.display.height}+{self.display.x}+{self.display.y}")
        self.t.title("Screen"+self.display.name[-1])
        self.t.bind("f",self.full)
        
        if self.typeof == "PIC":
            self.t["bg"] = "black"
            if self.dire != 0:
                self.get_pic_list()
            self.can_1 = Canvas(self.t, width = self.display.width , height = self.display.height,bg = "#000000")
            self.image_id = self.can_1.create_image((0,0) , image = self.gen_image(self.pic if self.pic else 0),anchor = "nw")
            self.can_1.pack(fill = "both",expand = True, ipadx = 0 , ipady = 0)
            if self.pic == None:#if not given a static picture it runs the roulette
                self.roulette()

        elif self.typeof == "WT":#Wt means World time
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
                name = x[0]
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

            if self.typeof == "TT":# TT means Timer
                self.a["text"] = "s"
                self.tie = Timer(self,self.master)
                self.tie.initiate()
                self.tie.start()
            elif self.typeof == "CD":# CD means CountDown
                self.a["text"] = "s"
                self.tie = Timer(self,self.master,countdown = self.time)
                self.tie.initiate()
                self.tie.start()
                

            else:# if no option is given it displays the normal time
                self.roulette()
    #gets all the pictures in the given dir 
    def get_pic_list(self):
        self.pic_list = []
        try:
            for path , dirs , files in os.walk(self.dire):
                pic_no = 0
                for x in files:
                    if x.endswith(".jpg") == True or x.endswith(".png") == True or x.endswith(".jpeg") == True or x.endswith(".JPG") == True:
                        pic_no += 1
                        self.pic_list.append(str(x))
        except Exception as e:
            return f"Error while loading Directory {e}"
        
    def destroy(self):
        self.t.withdraw()
        self.t.after_cancel(self.callback)# Weirdly if this line is commented out the program runs faster
        
    def getTime(self):
        try:
            return self.h["text"]
        except:
            return None
    
    
    def gen_image(self,n=0,strech = True):
        if self.pic == None:
            img = Image.open(self.dire +'/'+self.pic_list[n])
        else:
            try:
                img = Image.open(n)
            except Exception as e:
                return f"Error loading Path{e}"
        
        if strech:
            img = img.resize((self.display.width,self.display.height))
            
        self.img1 = ImageTk.PhotoImage(img) # made it an instance variable(self.) cuz if i dont tkinter stupidly disposes of the variable  
        return self.img1

    def roulette(self,gg =""):
        
        if self.typeof == "PIC":
            
            if int(self.time_func()) == self.change_time:
                self.picn+=1
                self.can_1.delete(self.image_id)
                try:
                    self.image_id = self.can_1.create_image((0,0) , image = self.gen_image(self.picn),anchor = "nw")
                except IndexError:
                    self.picn = 0
                    self.image_id = self.can_1.create_image((0,0) , image = self.gen_image(self.picn),anchor = "nw")
                self.timess = 0
                self.t.update_idletasks()
                
            ...
        else:
            if self.typeof == "WT":
                for x in self.tz_list:
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
        self.callback = self.t.after(100,self.roulette)

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

     
    

def main():
    win = Tk()
    # Display(win , display=get_monitors()[0],typeof = "DF").create()
    print("fsg")
   
    print("adhb")
    parser = argparse.ArgumentParser(prog="ScreenSaver",description="ScreenSaver")
    parser.add_argument("-d","--display", required=True, action='append',help="Monitor to display on i.e 1 , 2 ,3 or '0 for all' ")
    parser.add_argument("-pd","--picture",required=False, help="Path to picture to display")
    parser.add_argument("-m","--mode", required=True ,choices = ["p", "tt", "cd", "wt", "df"], help = "Type of mode to display p tt cd wt or df" )
    parser.add_argument("-dd","--directory",required= False, help="dirctory for roulette")
    parser.add_argument("-i","--interval",required= False, help="Interval for roulette")
    parser.add_argument("-t","--time",required= False, help="time for timer")
    parser.add_argument("-y",action='store_true', help="amount of search results to returns")
    args = parser.parse_args()
    monitors = get_monitors()
    display_list = args.display
    
    if monitors:
        for m in enumerate(monitors):
            if "0" not in display_list:
                print(m[0],display_list)
                if str(m[0]) in display_list:
                    print("dbasghi")
                    d = Display(master = win , display = m[1] , typeof = args.mode.upper() , pic = args.picture , dire = args.directory , inter = args.interval , time = args.time )
                    d.create() 
                    
            else:
                print("asdibhg")
                d = Display(master = win , display = m[1] , typeof = args.mode.upper() , pic = args.picture , dire = args.directory , inter = args.interval , time = args.time )
                d.create() 
            d.full("j")
            
    
    win.mainloop()
    
    
    
    
    
if __name__ == "__main__":
    main()
 

    
  
    
   



