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
import sys
import time
import torch
import win32api
import win32con
from PyQt5.QtWidgets import QApplication


# data setting
GAME_WIDTH = 1920
GAME_HEIGHT = 1080

IMG_PATH = 'screenshot.bmp'

HUBCONF_FOLDER_PATH = r'.'
MODEL_PATH = 'best.pt'
CONFIDENCE_THRESHOLD = 0.4

MOVE_DELAY1 = 0.049
MOVE_DELAY2 = 0.033
ONE_SHOT_DELAY = 0.001





class a51a(QThread):
    a51a1=pyqtSignal(str)

    def __init__(self,t,y,u,parent=None):
        super(a51a,self).__init__(parent)
        self.t=t
        self.y=y
        self.u=u
    
    
    def run(self):
        cc1=10
        cc2=10
        ww=1
        """window=win32gui.FindWindow(None,"MapleStory")
        win32gui.SetForegroundWindow(window)
        time.sleep(1)"""

        #找圖
        while True:
            start1=[0,0]
            part=None
            while True:
                if (self.t==0)or(self.t==1):
                    part=pyautogui.locateOnScreen('img/a51/9.png',confidence=0.8)
                    
                if self.t==2:
                    part=pyautogui.locateOnScreen('img/a51/10.png',confidence=0.8)
                    

                if part is not None:
                    start1[0]=part[0]
                    start1[1]=part[1]
                    break
                
            if self.t==0:        
                clr1=pyautogui.locateOnScreen('img/a51/3L.png',region=(start1[0]-5,start1[1]+58,35,20),confidence=0.95)
                clr2=pyautogui.locateOnScreen('img/a51/3R.png',region=(start1[0]+150,start1[1]+58,28,20),confidence=0.95)
            
            if self.t==1:        
                clr1=pyautogui.locateOnScreen('img/a51/3L.png',region=(start1[0]-6,start1[1]+83,28,17),confidence=0.95)
                clr2=pyautogui.locateOnScreen('img/a51/3R.png',region=(start1[0]+133,start1[1]+83,43,17),confidence=0.95)
            
            if self.t==2:        
                clr1=pyautogui.locateOnScreen('img/a51/3L.png',region=(start1[0]-7,start1[1]+76,45,30),confidence=0.95)
                clr2=pyautogui.locateOnScreen('img/a51/3R.png',region=(start1[0]+130,start1[1]+76,37,30),confidence=0.95)
                clr3=pyautogui.locateOnScreen('img/a51/3R.png',region=(start1[0]+74,start1[1]+88,30,18),confidence=0.95)
            
            
            if (self.t==2) and (clr3 is not None):
                pydirectinput.keyDown('up')
                time.sleep(0.1)
                pydirectinput.press('x')
                pydirectinput.keyUp('up')
                pydirectinput.press('ctrl')
            
            
            
            if clr1 is not None:
                ww=1

            if clr2 is not None:
                ww=2
                

            if ww==1:
                pydirectinput.keyDown('right')
                time.sleep(0.1)
                pydirectinput.press('x')
                #time.sleep(0.3)
                #pydirectinput.press('x')
                pydirectinput.keyUp('right')
                pydirectinput.press('ctrl')
                time.sleep(0.5)
                pydirectinput.press('ctrl')

            if ww==2:
                pydirectinput.keyDown('left')
                time.sleep(0.1)
                pydirectinput.press('x')
                #time.sleep(0.3)
                #pydirectinput.press('x')
                pydirectinput.keyUp('left')
                pydirectinput.press('ctrl')





            rnd1=random.randint(1,10)
            self.time1=datetime.now().strftime("%H:%M:%S")
            #測謊
            
            
            
            
            # # init model
            # device = torch.device('cuda')
            # model = torch.hub.load(HUBCONF_FOLDER_PATH, 'custom', MODEL_PATH,
            #                         source='local', force_reload=False)
            # model = model.to(device)

            # # init PyQt
            # app = QApplication(sys.argv)
            # screen = QApplication.primaryScreen()

            # # inference and move to shot
            # img = screen.grabWindow(0).toImage()
            # img.save(IMG_PATH)
            
            
            
            # ########
            # results = model(IMG_PATH)
            # results_pandas = results.pandas()

            # # box coordinates
            # x_mins = results_pandas.xyxy[0]['xmin']
            # x_maxs = results_pandas.xyxy[0]['xmax']
            # y_mins = results_pandas.xyxy[0]['ymin']
            # y_maxs = results_pandas.xyxy[0]['ymax']

            # confidences = results_pandas.xyxy[0]['confidence']




            # ##########
            # points = []
            # for x_min, x_max, y_min, y_max, conf in zip(x_mins, x_maxs, y_mins, y_maxs, confidences):
            #     if conf > CONFIDENCE_THRESHOLD:
            #         points.append([int(x_min), int(x_max), int(y_min), int(y_max)])
            #         print([int(x_min), int(x_max), int(y_min), int(y_max)])


            
            
            #出現
            clr3=pyautogui.locateOnScreen('img/lie1.png',region=(1,1,1919,1079),confidence=0.95)
            if clr3 is not None:
                pygame.mixer.music.load("lie.mp3")
                pygame.mixer.music.play()
            #點擊
            clr3=pyautogui.locateOnScreen('img/lie2.png',region=(1,1,1919,1079),confidence=0.95)
            if clr3 is not None:
                pydirectinput.moveTo(clr3[0]+10, clr3[1]+10)
                pydirectinput.click()
                
            
            clr3=pyautogui.locateOnScreen('img/a51/a3.png',region=(1,1,1919,1079),confidence=0.95)
            if clr3 is not None:
                pygame.mixer.music.load("lie.mp3")
                pygame.mixer.music.play()
                
                while True:
                    clr3=pyautogui.locateOnScreen('img/a51/a3.png',region=(1,1,1919,1079),confidence=0.95)
                    if clr3 is None:
                        pygame.mixer.music.stop()
                        break
            
            if rnd1==1:
                clr3=pyautogui.locateOnScreen('img/a51/18.png',region=(start1[0]+904,start1[1]+577,573,220),confidence=0.999)
                if clr3 is not None:
                    self.a51a1.emit(f"{self.time1}    釋放技能(英雄誓言)")
                    time.sleep(0.5)
                    pydirectinput.press('q')
                    time.sleep(0.2)
            
            if rnd1==2:
                clr3=pyautogui.locateOnScreen('img/a51/17.png',region=(start1[0]+904,start1[1]+577,573,220),confidence=0.999)
                if clr3 is not None:
                    self.a51a1.emit(f"{self.time1}    釋放技能(光與暗的洗禮)")
                    time.sleep(0.5)
                    pydirectinput.press('3')
                    time.sleep(0.2)
                    
            if rnd1==3:
                clr3=pyautogui.locateOnScreen('img/a51/16.png',region=(start1[0]+904,start1[1]+577,573,220),confidence=0.999)
                if clr3 is not None:
                    self.a51a1.emit(f"{self.time1}    釋放技能(混沌共鳴)")
                    time.sleep(0.5)
                    pydirectinput.press('4')
                    time.sleep(0.2)
            
            if rnd1==4:
                clr3=pyautogui.locateOnScreen('img/a51/15.png',region=(start1[0]+904,start1[1]+577,573,220),confidence=0.999)
                if clr3 is not None:
                    self.a51a1.emit(f"{self.time1}    釋放技能(解放寶珠)")
                    time.sleep(0.5)
                    pydirectinput.press('5')
                    time.sleep(0.2)
            
            if rnd1==5:
                clr3=pyautogui.locateOnScreen('img/a51/14.png',region=(start1[0]+904,start1[1]+577,573,220),confidence=0.999)
                if clr3 is not None:
                    self.a51a1.emit(f"{self.time1}    釋放技能(晨星殞落)")
                    time.sleep(0.5)
                    pydirectinput.press('a')
                    time.sleep(0.2)
                    
            if rnd1==6:
                clr3=pyautogui.locateOnScreen('img/a51/13.png',region=(start1[0]+904,start1[1]+577,573,220),confidence=0.999)
                if clr3 is not None:
                    self.a51a1.emit(f"{self.time1}    釋放技能(末日審判)")
                    time.sleep(0.5)
                    pydirectinput.press('s')
                    time.sleep(0.2)
                    
            if rnd1==7:
                clr3=pyautogui.locateOnScreen('img/a51/12.png',region=(start1[0]+904,start1[1]+577,573,220),confidence=0.999)
                if clr3 is not None:
                    self.a51a1.emit(f"{self.time1}    釋放技能(死神鐮刀)")
                    time.sleep(0.5)
                    pydirectinput.press('c')
                    time.sleep(0.2)
                    
            if rnd1==8:
                clr3=pyautogui.locateOnScreen('img/a51/11.png',region=(start1[0]+904,start1[1]+577,573,220),confidence=0.999)
                if clr3 is not None:
                    self.a51a1.emit(f"{self.time1}    釋放技能(絕對擊殺)")
                    time.sleep(0.5)
                    pydirectinput.press('v')
                    time.sleep(0.2)
                    

            if rnd1==9:
                cc1=cc1+1
                if cc1>10:
                    self.a51a1.emit(f"{self.time1}    釋放技能(輔助一)")
                    time.sleep(0.2)
                    pydirectinput.press('e')
                    time.sleep(3)
                    cc1=0
