from PyQt5 import QtWidgets, QtGui, QtCore
from  PyQt5.QtCore import QObject, QThread,pyqtSignal
import time
from datetime import datetime
import pyautogui
#import win32gui
import random
import pydirectinput
import pygame
pygame.mixer.init()

class a24a(QThread):
    a24a1=pyqtSignal(str)

    def __init__(self,t,y,u,parent=None):
        super(a24a,self).__init__(parent)
        self.t=t
        self.y=y
        self.u=u
    
    def run(self):
        cc1=5
        cc2=10
        """window=win32gui.FindWindow(None,"MapleStory")
        win32gui.SetForegroundWindow(window)
        time.sleep(1)"""

        #找圖
        while True:
            start1=[0,0]
            part=None
            while True:
                if self.t==0:
                    part=pyautogui.locateOnScreen('img/a24/3.png',confidence=0.8)
                if self.t==1:
                    part=pyautogui.locateOnScreen('img/a24/1.png',confidence=0.8)
                if part is not None:
                    start1[0]=part[0]
                    start1[1]=part[1]
                    break
                
            if self.t==0:        
                clr1=pyautogui.locateOnScreen('img/a24/2l.png',region=(start1[0]-5,start1[1]+58,33,20),confidence=0.95)
                clr2=pyautogui.locateOnScreen('img/a24/2r.png',region=(start1[0]+145,start1[1]+58,33,20),confidence=0.95)

            if clr1 is not None:
                #time.sleep(0.1)
                pydirectinput.press('right')
                time.sleep(0.1)


            if clr2 is not None:
                #time.sleep(0.1)
                pydirectinput.press('left')
                time.sleep(0.1)



            while True:
                #time.sleep(0.05)
                pydirectinput.press('alt')
                time.sleep(0.1)
                pydirectinput.press('alt')
                #time.sleep(0.1)
                pydirectinput.press('ctrl')
                time.sleep(0.1)
                break

            rnd1=random.randint(1,12)
            self.time1=datetime.now().strftime("%H:%M:%S")
            #測謊
            clr3=pyautogui.locateOnScreen('img/a24/a3.png',region=(1,1,1919,1079),confidence=0.95)
            if clr3 is not None:
                pygame.mixer.music.load("alarm1.mp3")
                pygame.mixer.music.play()
                
                while True:
                    clr3=pyautogui.locateOnScreen('img/a24/a3.png',region=(1,1,1919,1079),confidence=0.95)
                    if clr3 is None:
                        pygame.mixer.music.stop()
                        break
                    
            #有輪
            clr3=pyautogui.locateOnScreen('img/a24/a4.png',region=(start1[0]-5,start1[1]+20,178,58),confidence=0.95)
            if clr3 is not None:
                pygame.mixer.music.load("lun1.mp3")
                pygame.mixer.music.play()
                
                while True:
                    clr3=pyautogui.locateOnScreen('img/a24/a4.png',region=(start1[0]-5,start1[1]+20,178,58),confidence=0.95)
                    if clr3 is None:
                        pygame.mixer.music.stop()
                        break
            
            
            if rnd1==1:
                clr3=pyautogui.locateOnScreen('img/a24/4.png',region=(start1[0]+904,start1[1]+577,573,220),confidence=0.999)
                if clr3 is not None:
                    self.a24a1.emit(f"{self.time1}    釋放技能(環刃橫掃))")
                    time.sleep(0.2)
                    pydirectinput.press('alt')
                    #time.sleep(0.01)
                    pydirectinput.press('alt')
                    #time.sleep(0.01)
                    pydirectinput.press('c')
                    time.sleep(1)
            if rnd1==2:
                clr3=pyautogui.locateOnScreen('img/a24/5.png',region=(start1[0]+904,start1[1]+577,573,220),confidence=0.999)
                if clr3 is not None:
                    self.a24a1.emit(f"{self.time1}    釋放技能(環刃分裂))")
                    time.sleep(0.2)
                    pydirectinput.press('alt')
                    #time.sleep(0.01)
                    pydirectinput.press('alt')
                    #time.sleep(0.01)
                    pydirectinput.press('x')
                    time.sleep(1)
            if rnd1==3:
                clr3=pyautogui.locateOnScreen('img/a24/6.png',region=(start1[0]+904,start1[1]+577,573,220),confidence=0.999)
                if clr3 is not None:
                    self.a24a1.emit(f"{self.time1}    釋放技能(環刃之怒))")
                    time.sleep(0.2)
                    pydirectinput.press('alt')
                    #time.sleep(0.01)
                    pydirectinput.press('alt')
                    #time.sleep(0.01)
                    pydirectinput.press('shift')
                    time.sleep(2)        
            if rnd1==4:    
                clr3=pyautogui.locateOnScreen('img/a24/7.png',region=(start1[0]+904,start1[1]+577,573,220),confidence=0.999)
                if clr3 is not None:
                    self.a24a1.emit(f"{self.time1}    釋放技能(愛爾達斯的降臨)")
                    time.sleep(0.1)
                    pydirectinput.keyDown('down')
                    time.sleep(0.1)
                    pydirectinput.press('s')
                    time.sleep(0.1)
                    pydirectinput.keyUp('down')
                    time.sleep(0.1)
            if rnd1==5:
                clr3=pyautogui.locateOnScreen('img/a24/8.png',region=(start1[0]+904,start1[1]+577,573,220),confidence=0.999)
                if clr3 is not None:
                    self.a24a1.emit(f"{self.time1}    釋放技能(虛空突襲))")
                    time.sleep(0.2)
                    pydirectinput.press('alt')
                    #time.sleep(0.01)
                    pydirectinput.press('alt')
                    #time.sleep(0.01)
                    pydirectinput.press('d')
                    time.sleep(0.5)          
            if rnd1==6:
                clr3=pyautogui.locateOnScreen('img/a24/9.png',region=(start1[0]+904,start1[1]+577,573,220),confidence=0.999)
                if clr3 is not None:
                    self.a24a1.emit(f"{self.time1}    釋放技能(瘋狂))")
                    time.sleep(0.2)
                    pydirectinput.press('alt')
                    #time.sleep(0.01)
                    pydirectinput.press('alt')
                    #time.sleep(0.01)
                    pydirectinput.press('d')
                    time.sleep(0.5)         
            if rnd1==7:   
                clr3=pyautogui.locateOnScreen('img/a24/10.png',region=(start1[0]+904,start1[1]+577,573,220),confidence=0.999)
                if clr3 is not None:
                    self.a24a1.emit(f"{self.time1}    釋放技能(虛空破滅)")
                    time.sleep(0.5)
                    pydirectinput.press('5')
                    time.sleep(5)
            if rnd1==8:   
                clr3=pyautogui.locateOnScreen('img/a24/11.png',region=(start1[0]+904,start1[1]+577,573,220),confidence=0.999)
                if clr3 is not None:
                    self.a24a1.emit(f"{self.time1}    釋放技能(最後通牒)")
                    time.sleep(0.5)
                    pydirectinput.press('4')
                    time.sleep(1)                
            if rnd1==9:   
                clr3=pyautogui.locateOnScreen('img/a24/12.png',region=(start1[0]+904,start1[1]+577,573,220),confidence=0.999)
                if clr3 is not None:
                    self.a24a1.emit(f"{self.time1}    釋放技能(混亂)")
                    time.sleep(0.5)
                    pydirectinput.press('3')
                    time.sleep(1)         
            if rnd1==10:   
                clr3=pyautogui.locateOnScreen('img/a24/13.png',region=(start1[0]+904,start1[1]+577,573,220),confidence=0.999)
                if clr3 is not None:
                    self.a24a1.emit(f"{self.time1}    釋放技能(混亂)")
                    time.sleep(1)
                    pydirectinput.press('e')
                    time.sleep(1) 
            if rnd1==11:   
                clr3=pyautogui.locateOnScreen('img/a24/14.png',region=(start1[0]+904,start1[1]+577,573,220),confidence=0.999)
                if clr3 is not None:
                    self.a24a1.emit(f"{self.time1}    釋放技能(忘卻)")
                    time.sleep(1)
                    pydirectinput.press('w')
                    time.sleep(1)      
            if rnd1==12:
                cc1=cc1+1
                if cc1>5:
                    self.a24a1.emit(f"{self.time1}    釋放技能(輔助一)")
                    time.sleep(0.2)
                    pydirectinput.press('q')
                    time.sleep(2)
                    cc1=0

            
            
            """if rnd1==7:
                cc1=cc1+1
                if cc1>5:
                    self.a11a1.emit(f"{self.time1}    釋放技能(輔助一)")
                    time.sleep(0.2)
                    pydirectinput.press('q')
                    time.sleep(2)
                    cc1=0
            if rnd1==8:
                cc2=cc2+1
                if cc1>10:
                    self.a11a1.emit(f"{self.time1}    釋放技能(輔助二)")
                    time.sleep(0.2)
                    pydirectinput.press('w')
                    time.sleep(2)
                    cc2=0"""