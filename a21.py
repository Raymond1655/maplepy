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

class a21a(QThread):
    a21a1=pyqtSignal(str)

    def __init__(self,t,y,u,parent=None):
        super(a21a,self).__init__(parent)
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
                    part=pyautogui.locateOnScreen('img/a21/4.png',confidence=0.8)

                if part is not None:
                    start1[0]=part[0]
                    start1[1]=part[1]
                    break
                
            if self.t==0:        
                clr1=pyautogui.locateOnScreen('img/a21/3L.png',region=(start1[0]-19,start1[1]+26,36,55),confidence=0.9)
                clr2=pyautogui.locateOnScreen('img/a21/3R.png',region=(start1[0]+99,start1[1]+66,38,15),confidence=0.9)

            if clr1 is not None:
                #print("1",clr1)
                time.sleep(0.5)
                pydirectinput.press('`')
                time.sleep(0.5)
                pydirectinput.press('`')
                time.sleep(0.2)
                pydirectinput.press('right')
                time.sleep(0.1)


            if clr2 is not None:
                #print("2",clr2)
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

            rnd1=random.randint(1,14)
            self.time1=datetime.now().strftime("%H:%M:%S")
            
            
            # #出現測謊OK
            # clr3=pyautogui.locateOnScreen('img/lie1.png',region=(1,1,1919,1079),confidence=0.95)
            # if clr3 is not None:
            #     pygame.mixer.music.load("lie.mp3")
            #     pygame.mixer.music.play()
            # #點擊
            # clr3=pyautogui.locateOnScreen('img/lie2.png',region=(1,1,1919,1079),confidence=0.95)
            # if clr3 is not None:
            #     pydirectinput.moveTo(clr3[0]+10, clr3[1]+10)
            #     pydirectinput.click()
            
            # #出現黑王
            # clr3=pyautogui.locateOnScreen('img/RRR.png',region=(1,1,1919,1079),confidence=0.95)
            # if clr3 is not None:
            #     pygame.mixer.music.load("blackboss.mp3")
            #     pygame.mixer.music.play()


            # #出現蘑菇測謊
            # clr3=pyautogui.locateOnScreen('img/a21/a3.png',region=(1,1,1919,1079),confidence=0.95)
            # if clr3 is not None:
            #     pygame.mixer.music.load("lie.mp3")
            #     pygame.mixer.music.play()
                
            #     while True:
            #         clr3=pyautogui.locateOnScreen('img/a21/a3.png',region=(1,1,1919,1079),confidence=0.95)
            #         if clr3 is None:
            #             pygame.mixer.music.stop()
            #             break
                    
            # #有輪
            # clr3=pyautogui.locateOnScreen('img/a21/a4.png',region=(start1[0]-5,start1[1]+20,178,58),confidence=0.95)
            # if clr3 is not None:
            #     pygame.mixer.music.load("lun1.mp3")
            #     pygame.mixer.music.play()


            
            if rnd1==1:   
                clr3=pyautogui.locateOnScreen('img/a21/11.png',region=(start1[0]+904,start1[1]+577,573,220),confidence=0.999)
                if clr3 is not None:
                    self.a21a1.emit(f"{self.time1}    釋放技能(魔力爆裂)")
                    time.sleep(0.5)
                    pydirectinput.press('c')
                    time.sleep(0.3)  
            
            if rnd1==2:   
                clr3=pyautogui.locateOnScreen('img/a21/12.png',region=(start1[0]+904,start1[1]+577,573,220),confidence=0.999)
                if clr3 is not None:
                    self.a21a1.emit(f"{self.time1}    釋放技能(綻放)")
                    time.sleep(0.5)
                    pydirectinput.press('x')
                    time.sleep(0.3) 
            
            if rnd1==3:   
                clr3=pyautogui.locateOnScreen('img/a21/13.png',region=(start1[0]+904,start1[1]+577,573,220),confidence=0.999)
                if clr3 is not None:
                    self.a21a1.emit(f"{self.time1}    釋放技能(靈魂契約)")
                    time.sleep(0.5)
                    pydirectinput.press('z')
                    time.sleep(0.3) 
            
            if rnd1==4:   
                clr3=pyautogui.locateOnScreen('img/a21/14.png',region=(start1[0]+904,start1[1]+577,573,220),confidence=0.999)
                if clr3 is not None:
                    self.a21a1.emit(f"{self.time1}    釋放技能(回歸)")
                    time.sleep(0.5)
                    pydirectinput.press('s')
                    time.sleep(0.3)
                    
            if rnd1==5:   
                clr3=pyautogui.locateOnScreen('img/a21/15.png',region=(start1[0]+904,start1[1]+577,573,220),confidence=0.999)
                if clr3 is not None:
                    self.a21a1.emit(f"{self.time1}    釋放技能(劍域)")
                    time.sleep(0.5)
                    pydirectinput.press('a')
                    time.sleep(0.3)
                    
            if rnd1==6:   
                clr3=pyautogui.locateOnScreen('img/a21/16.png',region=(start1[0]+904,start1[1]+577,573,220),confidence=0.999)
                if clr3 is not None:
                    self.a21a1.emit(f"{self.time1}    釋放技能(復原)")
                    time.sleep(0.5)
                    pydirectinput.press('6')
                    time.sleep(0.3)
                    
            if rnd1==7:   
                clr3=pyautogui.locateOnScreen('img/a21/17.png',region=(start1[0]+904,start1[1]+577,573,220),confidence=0.999)
                if clr3 is not None:
                    self.a21a1.emit(f"{self.time1}    釋放技能(乙太風暴)")
                    time.sleep(0.5)
                    pydirectinput.press('5')
                    time.sleep(0.3)
                    
            if rnd1==8:   
                clr3=pyautogui.locateOnScreen('img/a21/18.png',region=(start1[0]+904,start1[1]+577,573,220),confidence=0.999)
                if clr3 is not None:
                    self.a21a1.emit(f"{self.time1}    釋放技能(無限)")
                    time.sleep(0.5)
                    pydirectinput.press('4')
                    time.sleep(0.3)
                    
            if rnd1==9:   
                clr3=pyautogui.locateOnScreen('img/a21/19.png',region=(start1[0]+904,start1[1]+577,573,220),confidence=0.999)
                if clr3 is not None:
                    self.a21a1.emit(f"{self.time1}    釋放技能(毀滅)")
                    time.sleep(0.5)
                    pydirectinput.press('3')
                    time.sleep(0.3)
                    
            if rnd1==10:   
                clr3=pyautogui.locateOnScreen('img/a21/20.png',region=(start1[0]+904,start1[1]+577,573,220),confidence=0.999)
                if clr3 is not None:
                    self.a21a1.emit(f"{self.time1}    釋放技能(蜘蛛之鏡)")
                    time.sleep(0.5)
                    pydirectinput.press('r')
                    time.sleep(0.3)
                    
            if rnd1==11:   
                clr3=pyautogui.locateOnScreen('img/a21/21.png',region=(start1[0]+904,start1[1]+577,573,220),confidence=0.999)
                if clr3 is not None:
                    self.a21a1.emit(f"{self.time1}    釋放技能(神之種族)")
                    time.sleep(0.5)
                    pydirectinput.press('e')
                    time.sleep(0.3)
                    
            if rnd1==12:   
                clr3=pyautogui.locateOnScreen('img/a21/22.png',region=(start1[0]+904,start1[1]+577,573,220),confidence=0.999)
                if clr3 is not None:
                    self.a21a1.emit(f"{self.time1}    釋放技能(愛爾達斯的降臨)")
                    time.sleep(0.5)
                    pydirectinput.press('w')
                    time.sleep(0.3) 
                    
            if rnd1==13:   
                clr3=pyautogui.locateOnScreen('img/a21/23.png',region=(start1[0]+904,start1[1]+577,573,220),confidence=0.999)
                if clr3 is not None:
                    self.a21a1.emit(f"{self.time1}    釋放技能(幻靈武具)")
                    time.sleep(0.5)
                    pydirectinput.press('q')
                    time.sleep(0.3)               

            if rnd1==14:   
                self.a21a1.emit(f"{self.time1}    釋放技能(追蹤)")
                time.sleep(0.5)
                pydirectinput.press('ctrl')
            
            
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