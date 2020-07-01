from pynput.mouse import Button, Controller
from pynput import *
from time import sleep
import ctypes 
import imageio
import matplotlib.pyplot as plt
import numpy as np
import pygetwindow as gw
from PIL import Image, ImageGrab, ImageFile


gw.getAllTitles()
print(gw.getAllWindows())
print(gw.getWindowsWithTitle('Studio'))


def minimize_others():
    mouse = Controller()
    otherWindows = gw.getAllWindows()

    for i in range(len(otherWindows)):
        otherWindows[i].minimize()

    ready_scape(mouse)
   

def ready_scape(mouse):

    scapeWindow = gw.getWindowsWithTitle('runescape')[0]
    scapeWindow.maximize()

    user32 = ctypes.windll.user32
    screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

    humanX = int(screensize[0]/2)
    humanY = int(screensize[1]/1.5)

    print(humanX,humanY)
    scapeWindow.maximize()
    scapeWindow.resizeTo(humanX, humanY)

    mouse.position = (int(humanX * .4), int(humanY * .78))
    
    

def sign_in():
    mouse = 'null'
    from pynput.keyboard import Key, Controller
    keyboard = Controller()
    sleep(1)
    # user
    keyboard.type('')
    sleep(1)
    keyboard.press(Key.tab)
    # pass
    keyboard.type('')
    sleep(1)
    keyboard.press(Key.enter)
    keyboard = 'null'


def act_natural(mouse):
    initial = mouse.position  
    mouse.press(Button.middle)
    mouse.move(10,10)
    mouse.move(20,20)
    
    mouse.release(Button.middle)


def scan_surroundings():
    enlarged = gw.getWindowsWithTitle('runescape')[0]
    enlarged.resize(1920,1080)

    sleep(4)
    
    current_surroundings = ImageGrab.grab()
    current_surroundings.save('recentcave.png')

    im = imageio.imread('recentcave.png')
    
    
    green = [0,255,0]
    x,y = np.where(np.all(im==green,axis=2))
    import pynput.mouse
    mouse = pynput.mouse.Controller()
    mouse.position = (x[0],y[0])
    print(x,y)


    
    

def controller_powerstruggle():
    import pynput.mouse
    botay = pynput.mouse.Controller()
    sleep(10)
    botay.click(Button.left, 1)
    act_natural(botay)


    



minimize_others()  
sign_in()
controller_powerstruggle()
scan_surroundings()












    
  





