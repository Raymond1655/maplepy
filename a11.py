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



class a11a(QThread):
    a11a1=pyqtSignal(str)

    def __init__(self,t,y,u,parent=None):
        super(a11a,self).__init__(parent)
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
                    part=pyautogui.locateOnScreen('img/a11/3.png',confidence=0.8)
                if self.t==1:
                    part=pyautogui.locateOnScreen('img/a11/1.png',confidence=0.8)
                if part is not None:
                    start1[0]=part[0]
                    start1[1]=part[1]
                    break
                
            if self.t==0:        
                clr1=pyautogui.locateOnScreen('img/a11/2l.png',region=(start1[0]-5,start1[1]+58,33,20),confidence=0.95)
                clr2=pyautogui.locateOnScreen('img/a11/2r.png',region=(start1[0]+145,start1[1]+58,33,20),confidence=0.95)

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
                pydirectinput.press('shift')
                time.sleep(0.1)
                break

            rnd1=random.randint(1,10)
            self.time1=datetime.now().strftime("%H:%M:%S")
            #測謊
            clr3=pyautogui.locateOnScreen('img/a11/a3.png',region=(1,1,1919,1079),confidence=0.95)
            if clr3 is not None:
                pygame.mixer.music.load("alarm1.mp3")
                pygame.mixer.music.play()
                
                while True:
                    clr3=pyautogui.locateOnScreen('img/a11/a3.png',region=(1,1,1919,1079),confidence=0.95)
                    if clr3 is None:
                        pygame.mixer.music.stop()
                        break
            
            
            
            if rnd1==1:
                clr3=pyautogui.locateOnScreen('img/a11/4.png',region=(start1[0]+904,start1[1]+577,573,220),confidence=0.999)
                if clr3 is not None:
                    self.a11a1.emit(f"{self.time1}    釋放技能(風魔手裏劍)")
                    time.sleep(0.2)
                    pydirectinput.press('alt')
                    #time.sleep(0.01)
                    pydirectinput.press('alt')
                    #time.sleep(0.01)
                    pydirectinput.press('q')
                    time.sleep(0.1)
            if rnd1==2:   
                clr3=pyautogui.locateOnScreen('img/a11/5.png',region=(start1[0]+904,start1[1]+577,573,220),confidence=0.999)
                if clr3 is not None:
                    self.a11a1.emit(f"{self.time1}    釋放技能(出血毒素)")
                    time.sleep(0.5)
                    pydirectinput.press('w')
                    time.sleep(0.5)
            if rnd1==3:    
                clr3=pyautogui.locateOnScreen('img/a11/6.png',region=(start1[0]+904,start1[1]+577,573,220),confidence=0.999)
                if clr3 is not None:
                    self.a11a1.emit(f"{self.time1}    釋放技能(傳說冒險)")
                    time.sleep(0.5)
                    pydirectinput.press('e')
                    time.sleep(0.5)
            if rnd1==4:    
                clr3=pyautogui.locateOnScreen('img/a11/7.png',region=(start1[0]+904,start1[1]+577,573,220),confidence=0.999)
                if clr3 is not None:
                    self.a11a1.emit(f"{self.time1}    釋放技能(愛爾達斯的降臨)")
                    time.sleep(0.1)
                    pydirectinput.keyDown('down')
                    time.sleep(0.1)
                    pydirectinput.press('3')
                    time.sleep(0.1)
                    pydirectinput.keyUp('down')
                    time.sleep(0.1)
            if rnd1==5:    
                clr3=pyautogui.locateOnScreen('img/a11/8.png',region=(start1[0]+904,start1[1]+577,573,220),confidence=0.999)
                if clr3 is not None:
                    self.a11a1.emit(f"{self.time1}    釋放技能(散式投擲)")
                    time.sleep(0.1)
                    pydirectinput.press('4')
                    time.sleep(0.5)
            if rnd1==6:    
                clr3=pyautogui.locateOnScreen('img/a11/9.png',region=(start1[0]+904,start1[1]+577,573,220),confidence=0.999)
                if clr3 is not None:
                    self.a11a1.emit(f"{self.time1}    釋放技能(絕殺領域)")
                    time.sleep(0.5)
                    pydirectinput.press('a')
                    time.sleep(0.5)
            if rnd1==7:
                clr3=pyautogui.locateOnScreen('img/a11/10.png',region=(start1[0]+904,start1[1]+577,573,220),confidence=0.999)
                if clr3 is not None:
                    self.a11a1.emit(f"{self.time1}    釋放技能(四星鏢雨)")
                    time.sleep(0.2)
                    pydirectinput.press('alt')
                    #time.sleep(0.01)
                    pydirectinput.press('alt')
                    #time.sleep(0.01)
                    pydirectinput.press('s')
                    time.sleep(0.1)
            if rnd1==8:    
                clr3=pyautogui.locateOnScreen('img/a11/11.png',region=(start1[0]+904,start1[1]+577,573,220),confidence=0.999)
                if clr3 is not None:
                    self.a11a1.emit(f"{self.time1}    釋放技能(達克魯的秘傳)")
                    time.sleep(0.1)
                    pydirectinput.press('d')
                    time.sleep(0.1)
            if rnd1==9:    
                clr3=pyautogui.locateOnScreen('img/a11/12.png',region=(start1[0]+904,start1[1]+577,573,220),confidence=0.999)
                if clr3 is not None:
                    self.a11a1.emit(f"{self.time1}    釋放技能(飛閃起爆符)")
                    time.sleep(0.1)
                    pydirectinput.press('f')
                    time.sleep(0.1)
            if rnd1==10:
                clr3=pyautogui.locateOnScreen('img/a11/13.png',region=(start1[0]+904,start1[1]+577,573,220),confidence=0.999)
                if clr3 is not None:
                    self.a11a1.emit(f"{self.time1}    釋放技能(穢土轉升)")
                    time.sleep(0.2)
                    pydirectinput.press('alt')
                    #time.sleep(0.01)
                    pydirectinput.press('alt')
                    #time.sleep(0.01)
                    pydirectinput.press('c')
                    time.sleep(0.1)
            
            
            
            
            
            
            
            
            
            
            
            """if rnd1==7:
                cc1=cc1+1
                if cc1>10:
                    self.a11a1.emit(f"{self.time1}    釋放技能(輔助一)")
                    time.sleep(0.2)
                    pydirectinput.press('q')
                    time.sleep(2)
                    cc1=0
            if rnd1==8:
                cc2=cc2+1
                if cc1>20:
                    self.a11a1.emit(f"{self.time1}    釋放技能(輔助二)")
                    time.sleep(0.2)
                    pydirectinput.press('w')
                    time.sleep(2)
                    cc2=0"""