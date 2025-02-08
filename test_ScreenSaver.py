import unittest
print(type(unittest),unittest.__path__)
from ScreenSaver import *
from tkinter import *
import _tkinter
from screeninfo import get_monitors
from datetime import datetime
import time
class TestScreenSaver(unittest.TestCase):
    
    def setUp(cls):
        cls.pump_events()
        pass

    @classmethod
    def setUpClass(cls):
        super(TestScreenSaver, cls).setUpClass()
        cls.win = Tk() 
        cls.dis1 = Display(master = cls.win, display = get_monitors()[0] , pic = "C:\\Users\\user\\AppData\\Roaming\\Microsoft\\Windows\\Themes\\TranscodedWallpaper")
        cls.dis2 =  Display(master = cls.win, display = get_monitors()[0],typeof="DF")
        cls.dis3 =  Display(master = cls.win, display = get_monitors()[0],typeof="TT", time = 3)
        cls.dis4 =  Display(master = cls.win, display = get_monitors()[0],typeof="CD", time = 3)
        cls.dis5 =  Display(master = cls.win, display = get_monitors()[0],typeof="WT")
        cls.dis6 =  Display(master = cls.win, display = get_monitors()[0],typeof="PIC",inter = 3 , dire = "C:\\Users\\user\\Desktop\\Screen Saver")
        cls.dis1.create()
        cls.dis2.create()
        cls.dis3.create()
        cls.dis4.create()
        cls.dis5.create()
        cls.dis6.create()
   
    
    def pump_events(self):
        while self.win.dooneevent(_tkinter.ALL_EVENTS|_tkinter.DONT_WAIT):
            pass

    def test_diplay_can_be_created(self):
        self.assertTrue(self.dis1.t.winfo_exists())
        self.assertTrue(self.dis2.t.winfo_exists())
        self.assertTrue(self.dis3.t.winfo_exists())
        self.assertTrue(self.dis4.t.winfo_exists())
        self.assertTrue(self.dis5.t.winfo_exists())
        
    
    def test_task_screen(self):
        self.dis1.full("j")
        self.assertTrue(self.dis1.t.attributes("-fullscreen"))

    def test_time_function(self):
        self.assertEqual(self.dis2.getTime(),datetime.now().strftime("%I:%M:%S"))
        self.assertEqual(self.dis2.a["text"],datetime.now().strftime("%p"))
        self.assertEqual(self.dis2.d["text"],datetime.now().strftime("%a"))
        
    def test_timer_function(self):
        a = int(self.dis3.tie.times)
        b = int(self.dis4.tie.times)
        
        print(a,b)
        self.assertTrue(a == 3 or a == 6 or a ==5 or a ==4)#Depends on when the tests finishes unfortunately
        self.assertTrue(b == self.dis4.tie.countdown)
        self.assertTrue(self.dis4.d["text"] == "TIMES UP!")
        self.assertFalse(self.dis4.tie.active)

        
    def test_roulette_function(self):
        self.assertTrue(self.dis6.pic_list)
        pass


if __name__ == "__main__":
    unittest.main()
