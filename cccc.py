from PyQt5 import QtWidgets, QtGui, QtCore
from  PyQt5.QtCore import QObject, QThread,pyqtSignal
import time
from datetime import datetime
import pyautogui
#import win32gui
import random
import pydirectinput

#找圖
while True:
    start1=[0,0]
    part=None
    while True:
        part=pyautogui.locateOnScreen('img/cccc/a5.png',confidence=0.8)
        if part is not None:
            start1[0]=part[0]
            start1[1]=part[1]
            break
        
    #a1
    #clr1=pyautogui.locateOnScreen('img/cccc/2l.png',region=(start1[0]-8,start1[1]+72,35,30),confidence=0.98)
    #clr2=pyautogui.locateOnScreen('img/cccc/2r.png',region=(start1[0]+174,start1[1]+72,38,30),confidence=0.95)

    #a2
    #clr1=pyautogui.locateOnScreen('img/cccc/2l.png',region=(start1[0]-7,start1[1]+35,42,25),confidence=0.98)
    #clr2=pyautogui.locateOnScreen('img/cccc/2r.png',region=(start1[0]+81,start1[1]+35,38,25),confidence=0.95)
    
    #a4
    #clr1=pyautogui.locateOnScreen('img/cccc/3l.png',region=(start1[0]-11,start1[1]+92,60,32),confidence=0.998)
    #clr2=pyautogui.locateOnScreen('img/cccc/3r.png',region=(start1[0]+156,start1[1]+92,30,32),confidence=0.998)
    
    #a5
    clr1=pyautogui.locateOnScreen('img/cccc/3l.png',region=(start1[0]-11,start1[1]+72,26,17),confidence=0.998)
    clr2=pyautogui.locateOnScreen('img/cccc/3r.png',region=(start1[0]+116,start1[1]+72,45,17),confidence=0.998)
    

    
    
    if clr1 is not None:
        
        pydirectinput.press('right')
        time.sleep(0.1)


    if clr2 is not None:
        pydirectinput.keyDown("up")
        pydirectinput.press('alt')
        pydirectinput.keyUp('up')
        time.sleep(2)
        pydirectinput.keyDown("down")
        pydirectinput.press('alt')
        pydirectinput.keyUp('down')
        time.sleep(1)
        
        pydirectinput.press('left')
        time.sleep(0.1)



    while True:
        time.sleep(0.05)
        pydirectinput.press('alt')
        time.sleep(0.15)
        pydirectinput.press('alt')
        #time.sleep(0.01)
        pydirectinput.press('ctrl')
        time.sleep(0.5)
        pydirectinput.press('ctrl')
        time.sleep(0.5)
        pydirectinput.press('ctrl')
        time.sleep(0.5)
        break

    rnd1=random.randint(1,10)
    if rnd1==1:
        clr3=pyautogui.locateOnScreen('img/cccc/1.png',region=(start1[0]+904,start1[1]+577,573,220),confidence=0.999)
        if clr3 is not None:
            time.sleep(0.5)
            pydirectinput.press('q')
            time.sleep(0.2)
    if rnd1==2:
        clr3=pyautogui.locateOnScreen('img/cccc/2.png',region=(start1[0]+904,start1[1]+577,573,220),confidence=0.999)
        if clr3 is not None:
            time.sleep(0.5)
            pydirectinput.press('w')
            time.sleep(0.2)
    '''if rnd1==3:
        clr3=pyautogui.locateOnScreen('img/cccc/3.png',region=(start1[0]+904,start1[1]+577,573,220),confidence=0.999)
        if clr3 is not None:
            time.sleep(0.5)
            pydirectinput.press('a')
            time.sleep(0.2)'''
    if rnd1==4:
        clr3=pyautogui.locateOnScreen('img/cccc/4.png',region=(start1[0]+904,start1[1]+577,573,220),confidence=0.999)
        if clr3 is not None:
            time.sleep(0.5)
            pydirectinput.press('d')
            time.sleep(0.2)
    if rnd1==5:
        clr3=pyautogui.locateOnScreen('img/cccc/5.png',region=(start1[0]+904,start1[1]+577,573,220),confidence=0.999)
        if clr3 is not None:
            time.sleep(0.5)
            pydirectinput.press('shift')
            time.sleep(0.2)
            