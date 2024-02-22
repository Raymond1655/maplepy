from  PyQt5.QtCore import QObject, QThread,pyqtSignal
import time
from datetime import datetime
import pyautogui
import win32con
import win32gui
import random
import pydirectinput
import win32api
import win32com.client
time.sleep(1)
shell = win32com.client.Dispatch("WScript.Shell")
shell.SendKeys('{LEFT}')
#win32api.MessageBox(win32con.NULL, 'Python 您好！', '您好', win32con.MB_OK)
time.sleep(1)
pydirectinput.keyDown('w')
time.sleep(1)
pydirectinput.keyUp('w')

"""while True:
   start1=[0,0]
   while True:
         part=pyautogui.locateOnScreen('img/a18/1.png',confidence=0.8)
         if part is not None:
            start1[0]=part[0]
            start1[1]=part[1]
            break

   clr1=pyautogui.locateOnScreen('img/a18/2.png',region=(start1[0]-3,start1[1]+55,30,25),confidence=0.95)
   clr2=pyautogui.locateOnScreen('img/a18/2.png',region=(start1[0]+147,start1[1]+55,+30,25),confidence=0.95)
   if clr1 is not None:
         pydirectinput.press('right')
         time.sleep(0.1)


   if clr2 is not None:
         pydirectinput.press('left')
         time.sleep(0.1)



   while True:
         time.sleep(0.05)
         pydirectinput.press('alt')
         time.sleep(0.01)
         pydirectinput.press('alt')
         time.sleep(0.01)
         pydirectinput.press('ctrl')
         time.sleep(0.1)
         break

   rnd1=random.randint(1,10)
   print(rnd1)
   
   if rnd1==1:
         print(222)
         clr3=pyautogui.locateOnScreen('img/a18/3.png',region=(start1[0]+904,start1[1]+577,573,220),confidence=0.999)
         if clr3 is not None:
            time.sleep(0.5)
            pydirectinput.press('2')
            time.sleep(0.2)
            print(3333)
         else:
            print(111)
   if rnd1==9:   
         clr3=pyautogui.locateOnScreen('img/a18/4.png',region=(start1[0]+904,start1[1]+577,573,220),confidence=0.999)
         if clr3 is not None:
            time.sleep(0.1)
            pydirectinput.press('v')
            time.sleep(0.1)
   if rnd1==3:    
         clr3=pyautogui.locateOnScreen('img/a18/5.png',region=(start1[0]+904,start1[1]+577,573,220),confidence=0.999)
         if clr3 is not None:
            time.sleep(0.1)
            pydirectinput.keyDown('down')
            time.sleep(0.1)
            pydirectinput.press('s')
            time.sleep(0.1)
            pydirectinput.keyUp('down')
            time.sleep(0.1)
   if rnd1==4:    
         clr3=pyautogui.locateOnScreen('img/a18/6.png',region=(start1[0]+904,start1[1]+577,573,220),confidence=0.999)
         if clr3 is not None:
            time.sleep(0.1)
            pydirectinput.press('x')
            time.sleep(0.1)
            pydirectinput.press('5')
            time.sleep(0.1)
   if rnd1==5:    
         clr3=pyautogui.locateOnScreen('img/a18/7.png',region=(start1[0]+904,start1[1]+577,573,220),confidence=0.999)
         if clr3 is not None:
            time.sleep(0.05)
            pydirectinput.press('alt')
            time.sleep(0.01)
            pydirectinput.press('alt')
            time.sleep(0.01)
            pydirectinput.press('shift')
            time.sleep(0.1)
   if rnd1==6:    
         clr3=pyautogui.locateOnScreen('img/a18/8.png',region=(start1[0]+904,start1[1]+577,573,220),confidence=0.999)
         if clr3 is not None:
            time.sleep(0.05)
            pydirectinput.press('alt')
            time.sleep(0.01)
            pydirectinput.press('alt')
            time.sleep(0.01)
            pydirectinput.press('c')
            time.sleep(0.1)"""