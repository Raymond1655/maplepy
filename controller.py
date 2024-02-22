from PyQt5 import QtWidgets, QtGui, QtCore
from UI import Ui_MainWindow
import time
from datetime import datetime
from a11 import a11a
from a18 import a18a
from a24 import a24a
from a51 import a51a
from a21 import a21a
from a31 import a31a
from PyQt5.QtCore import pyqtSignal
from multiprocessing import Process
import atexit
import torch
from PyQt5.QtWidgets import QApplication
import sys
import time
import torch
import win32api
import win32con
import pyautogui
import pygame
import pydirectinput

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        # in python3, super(Class, self).xxx = super().xxx
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.tab2now=self.ui.tabWidget_2.currentIndex()
        self.setup_control()
        print("1111")
        
        

    def setup_control(self):
        # TODO
        self.ui.pushButton.clicked.connect(self.startClicked)
        self.ui.pushButton_2.clicked.connect(self.stopClicked)
        self.ui.tabWidget_2.currentChanged.connect(self.tab2)
        self.ui.comboBox.currentIndexChanged.connect(self.cbx1)
        self.ui.comboBox_2.currentIndexChanged.connect(self.cbx2)
        self.ui.comboBox_3.currentIndexChanged.connect(self.cbx3)
        self.ui.comboBox_4.currentIndexChanged.connect(self.cbx4)
        self.ui.comboBox_5.currentIndexChanged.connect(self.cbx5)
        self.ui.comboBox_6.currentIndexChanged.connect(self.cbx6)
        self.ui.comboBox_7.currentIndexChanged.connect(self.cbx7)
        self.time1=datetime.now().strftime("%H:%M:%S")
        print("1111222")
    
    def message2(self,str1):
        self.ui.textBrowser.append(f"{str1}")
        
        
    #按開始
    def startClicked(self):
        self.time1=datetime.now().strftime("%H:%M:%S")
        #self.ui.pushButton.setEnabled(False)
        #self.ui.pushButton_2.setEnabled(True)
        self.ui.textBrowser.append(f"{self.time1}    You clicked starttttt")
        print(self.tab2now)
        print(self.cbxnow)
        if (self.tab2now==0)and(self.cbxnow==1):
            self.a11a=a11a(t=self.ui.comboBox_8.currentIndex(),y=1,u=1)
            self.a11a.a11a1.connect(self.message2)
            self.a11a.start()#開始程序
        if (self.tab2now==0)and(self.cbxnow==8):
            self.a18a=a18a(t=self.ui.comboBox_8.currentIndex(),y=1,u=1)
            self.a18a.a18a1.connect(self.message2)
            self.a18a.start()#開始程序
            
        if (self.tab2now==1)and(self.cbxnow==4):
            self.a24a=a24a(t=self.ui.comboBox_8.currentIndex(),y=1,u=1)
            self.a24a.a24a1.connect(self.message2)
            self.a24a.start()#開始程序
            
        if (self.tab2now==4)and(self.cbxnow==1):
            self.a51a=a51a(t=self.ui.comboBox_8.currentIndex(),y=1,u=1)
            self.a51a.a51a1.connect(self.message2)
            self.a51a.start()#開始程序
            
        if (self.tab2now==1)and(self.cbxnow==1):
            self.a21a=a21a(t=self.ui.comboBox_8.currentIndex(),y=1,u=1)
            self.a21a.a21a1.connect(self.message2)
            self.a21a.start()#開始程序
        
        if (self.tab2now==2)and(self.cbxnow==1):
            self.a31a=a31a(t=self.ui.comboBox_8.currentIndex(),y=1,u=1)
            self.a31a.a31a1.connect(self.message2)
            self.a31a.start()#開始程序

    #按停止
    def stopClicked(self):
        self.time1=datetime.now().strftime("%H:%M:%S")
        #self.ui.pushButton_2.setEnabled(False)
        #self.ui.pushButton.setEnabled(True)
        self.ui.textBrowser.append(f"{self.time1}    You clicked stoppppp")
        if (self.tab2now==0)and(self.cbxnow==1):
            self.a11a.terminate()#終止程序
        if (self.tab2now==0)and(self.cbxnow==8):
            self.a18a.terminate()#終止程序
        if (self.tab2now==1)and(self.cbxnow==4):
            self.a24a.terminate()#終止程序
        if (self.tab2now==4)and(self.cbxnow==1):
            self.a51a.terminate()#終止程序
        if (self.tab2now==1)and(self.cbxnow==1):
            self.a21a.terminate()#終止程序
        if (self.tab2now==2)and(self.cbxnow==1):
            self.a31a.terminate()#終止程序
 
    #選職業群
    def tab2(self):
        
        self.tab2now=self.ui.tabWidget_2.currentIndex()
        if self.ui.tabWidget_2.currentIndex()==0:
            self.ui.textBrowser.append(f"{self.time1}    職業群   冒險家")
        elif self.ui.tabWidget_2.currentIndex()==1:
            self.ui.textBrowser.append(f"{self.time1}    職業群   雷普族")
        elif self.ui.tabWidget_2.currentIndex()==2:
            self.ui.textBrowser.append(f"{self.time1}    職業群   皇家")
        elif self.ui.tabWidget_2.currentIndex()==3:
            self.ui.textBrowser.append(f"{self.time1}    職業群   末日")
        elif self.ui.tabWidget_2.currentIndex()==4:
            self.ui.textBrowser.append(f"{self.time1}    職業群   英雄")
        elif self.ui.tabWidget_2.currentIndex()==5:
            self.ui.textBrowser.append(f"{self.time1}    職業群   新星")
        elif self.ui.tabWidget_2.currentIndex()==6:
            self.ui.textBrowser.append(f"{self.time1}    職業群   其他")
    #選職業       
    def cbx1(self):
        self.cbxnow=self.ui.comboBox.currentIndex()
        if self.ui.comboBox.currentIndex()==1:
            self.ui.textBrowser.append(f"{self.time1}    選擇職業   夜使者")
            self.ui.comboBox_8.clear()
            self.ui.comboBox_8.addItem("阿爾卡娜-土之森")
        elif self.ui.comboBox.currentIndex()==2:
            self.ui.textBrowser.append(f"{self.time1}    選擇職業   影舞者")
        elif self.ui.comboBox.currentIndex()==3:
            self.ui.textBrowser.append(f"{self.time1}    選擇職業   暗影神偷")
        elif self.ui.comboBox.currentIndex()==4:
            self.ui.textBrowser.append(f"{self.time1}    選擇職業   主教")
        elif self.ui.comboBox.currentIndex()==5:
            self.ui.textBrowser.append(f"{self.time1}    選擇職業   冰雷魔導")
        elif self.ui.comboBox.currentIndex()==6:
            self.ui.textBrowser.append(f"{self.time1}    選擇職業   火毒魔導")
        elif self.ui.comboBox.currentIndex()==7:
            self.ui.textBrowser.append(f"{self.time1}    選擇職業   神射手")
        elif self.ui.comboBox.currentIndex()==8:
            self.ui.textBrowser.append(f"{self.time1}    選擇職業   開拓者")
            self.ui.comboBox_8.clear()
            self.ui.comboBox_8.addItem("阿爾卡娜-土之森")
            self.ui.comboBox_8.addItem("艾斯佩拉-鏡光大海2")
        elif self.ui.comboBox.currentIndex()==9:
            self.ui.textBrowser.append(f"{self.time1}    選擇職業   箭神")
            self.ui.comboBox_8.clear()
            self.ui.comboBox_8.addItem("1111")
        elif self.ui.comboBox.currentIndex()==10:
            self.ui.textBrowser.append(f"{self.time1}    選擇職業   龍騎士")
        elif self.ui.comboBox.currentIndex()==11:
            self.ui.textBrowser.append(f"{self.time1}    選擇職業   黑騎士")
        elif self.ui.comboBox.currentIndex()==12:
            self.ui.textBrowser.append(f"{self.time1}    選擇職業   聖騎士")
        elif self.ui.comboBox.currentIndex()==13:
            self.ui.textBrowser.append(f"{self.time1}    選擇職業   槍神")
        elif self.ui.comboBox.currentIndex()==14:
            self.ui.textBrowser.append(f"{self.time1}    選擇職業   拳霸")
        elif self.ui.comboBox.currentIndex()==15:
            self.ui.textBrowser.append(f"{self.time1}    選擇職業  重砲指揮")
    
    def cbx2(self):
        self.cbxnow=self.ui.comboBox_2.currentIndex()
        if self.ui.comboBox_2.currentIndex()==1:
            self.ui.textBrowser.append(f"{self.time1}    選擇職業   阿戴爾")
            self.ui.comboBox_8.clear()
            self.ui.comboBox_8.addItem("海邊岩石地帶2")
        elif self.ui.comboBox_2.currentIndex()==2:
            self.ui.textBrowser.append(f"{self.time1}    選擇職業   亞克")
        elif self.ui.comboBox_2.currentIndex()==3:
            self.ui.textBrowser.append(f"{self.time1}    選擇職業   伊利恩")
        elif self.ui.comboBox_2.currentIndex()==4:
            self.ui.textBrowser.append(f"{self.time1}    選擇職業   卡莉")
            self.ui.comboBox_8.clear()
            self.ui.comboBox_8.addItem("阿爾卡娜-土之森")
    
    def cbx3(self):
        self.cbxnow=self.ui.comboBox_3.currentIndex()
        if self.ui.comboBox_3.currentIndex()==1:
            self.ui.textBrowser.append(f"{self.time1}    選擇職業   聖魂劍士")
            self.ui.comboBox_8.clear()
            self.ui.comboBox_8.addItem("世界的眼淚下方2")
            self.ui.comboBox_8.addItem("海邊岩石地帶2")
        elif self.ui.comboBox_3.currentIndex()==2:
            self.ui.textBrowser.append(f"{self.time1}    選擇職業   破風使者")
        elif self.ui.comboBox_3.currentIndex()==3:
            self.ui.textBrowser.append(f"{self.time1}    選擇職業   暗夜使者")
        elif self.ui.comboBox_3.currentIndex()==4:
            self.ui.textBrowser.append(f"{self.time1}    選擇職業   閃雷悍將")
        elif self.ui.comboBox_3.currentIndex()==5:
            self.ui.textBrowser.append(f"{self.time1}    選擇職業   烈焰巫師")
        elif self.ui.comboBox_3.currentIndex()==6:
            self.ui.textBrowser.append(f"{self.time1}    選擇職業   米哈逸")
    
    def cbx4(self):
        self.cbxnow=self.ui.comboBox_4.currentIndex()
        if self.ui.comboBox_4.currentIndex()==1:
            self.ui.textBrowser.append(f"{self.time1}    選擇職業   惡魔復仇")
        elif self.ui.comboBox_4.currentIndex()==2:
            self.ui.textBrowser.append(f"{self.time1}    選擇職業   惡魔殺手")
        elif self.ui.comboBox_4.currentIndex()==3:
            self.ui.textBrowser.append(f"{self.time1}    選擇職業   傑諾")
        elif self.ui.comboBox_4.currentIndex()==4:
            self.ui.textBrowser.append(f"{self.time1}    選擇職業   爆拳槍神")
        elif self.ui.comboBox_4.currentIndex()==5:
            self.ui.textBrowser.append(f"{self.time1}    選擇職業   煉獄巫師")
        elif self.ui.comboBox_4.currentIndex()==6:
            self.ui.textBrowser.append(f"{self.time1}    選擇職業   狂豹獵人")
        elif self.ui.comboBox_4.currentIndex()==7:
            self.ui.textBrowser.append(f"{self.time1}    選擇職業   機甲戰神")
    
    def cbx5(self):
        self.cbxnow=self.ui.comboBox_5.currentIndex()
        if self.ui.comboBox_5.currentIndex()==1:
            self.ui.textBrowser.append(f"{self.time1}    選擇職業   夜光")
            self.ui.comboBox_8.clear()
            self.ui.comboBox_8.addItem("阿爾卡娜-土之森")
            self.ui.comboBox_8.addItem("日光之森")
            self.ui.comboBox_8.addItem("虛空海浪3")
        elif self.ui.comboBox_5.currentIndex()==2:
            self.ui.textBrowser.append(f"{self.time1}    選擇職業   龍魔導士")
        elif self.ui.comboBox_5.currentIndex()==3:
            self.ui.textBrowser.append(f"{self.time1}    選擇職業   狂狼勇士")
        elif self.ui.comboBox_5.currentIndex()==4:
            self.ui.textBrowser.append(f"{self.time1}    選擇職業   精靈遊俠")
        elif self.ui.comboBox_5.currentIndex()==5:
            self.ui.textBrowser.append(f"{self.time1}    選擇職業   幻影俠盜")
        elif self.ui.comboBox_5.currentIndex()==6:
            self.ui.textBrowser.append(f"{self.time1}    選擇職業   隱月")
            
    def cbx6(self):
        self.cbxnow=self.ui.comboBox_6.currentIndex()
        if self.ui.comboBox_6.currentIndex()==1:
            self.ui.textBrowser.append(f"{self.time1}    選擇職業   天使破壞者")
        elif self.ui.comboBox_6.currentIndex()==2:
            self.ui.textBrowser.append(f"{self.time1}    選擇職業   凱薩")
        elif self.ui.comboBox_6.currentIndex()==3:
            self.ui.textBrowser.append(f"{self.time1}    選擇職業   卡蒂娜")
        elif self.ui.comboBox_6.currentIndex()==4:
            self.ui.textBrowser.append(f"{self.time1}    選擇職業   卡殷")
    
    def cbx7(self):
        self.cbxnow=self.ui.comboBox_7.currentIndex()
        if self.ui.comboBox_7.currentIndex()==1:
            self.ui.textBrowser.append(f"{self.time1}    選擇職業   陰陽師")
        elif self.ui.comboBox_7.currentIndex()==2:
            self.ui.textBrowser.append(f"{self.time1}    選擇職業   劍豪")
        elif self.ui.comboBox_7.currentIndex()==3:
            self.ui.textBrowser.append(f"{self.time1}    選擇職業   菈菈")
        elif self.ui.comboBox_7.currentIndex()==4:
            self.ui.textBrowser.append(f"{self.time1}    選擇職業   虎影")
        elif self.ui.comboBox_7.currentIndex()==5:
            self.ui.textBrowser.append(f"{self.time1}    選擇職業   幻獸師")
        elif self.ui.comboBox_7.currentIndex()==6:
            self.ui.textBrowser.append(f"{self.time1}    選擇職業   凱內西斯")
        elif self.ui.comboBox_7.currentIndex()==7:
            self.ui.textBrowser.append(f"{self.time1}    選擇職業   神之子")


def function1():

    while True:
        time.sleep(5)
        
        #出現測謊OK
        clr3=pyautogui.locateOnScreen('img/lie1.png',region=(1,1,1919,1079),confidence=0.95)
        if clr3 is not None:
            pygame.mixer.music.load("lie.mp3")
            pygame.mixer.music.play()
        #點擊
        clr3=pyautogui.locateOnScreen('img/lie2.png',region=(1,1,1919,1079),confidence=0.95)
        if clr3 is not None:
            pydirectinput.moveTo(clr3[0]+10, clr3[1]+10)
            pydirectinput.click()
        
        #出現黑王
        clr3=pyautogui.locateOnScreen('img/RRR.png',region=(1,1,1919,1079),confidence=0.95)
        if clr3 is not None:
            pygame.mixer.music.load("blackboss.mp3")
            pygame.mixer.music.play()

        #出現蘑菇測謊
        clr3=pyautogui.locateOnScreen('img/a3.png',region=(1,1,1919,1079),confidence=0.95)
        if clr3 is not None:
            pygame.mixer.music.load("lie.mp3")
            pygame.mixer.music.play()
                
        #有輪
        part=pyautogui.locateOnScreen('img/map260.png',confidence=0.8)
        if part is not None:
            clr3=pyautogui.locateOnScreen('img/a4.png',region=(part[0]-19,part[1]+20,156,65),confidence=0.95)
            if clr3 is not None:
                pygame.mixer.music.load("lun1.mp3")
                pygame.mixer.music.play()
    

def cleanup():
    process1.terminate()

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    process1 = Process(target=function1)
    process1.start()
    
    atexit.register(cleanup)
    sys.exit(app.exec_())



























"""def setup_control(self):
        # TODO
        self.roll1=0
        self.ui.radioButton.toggled.connect(self.roll11)
        self.ui.radioButton_2.toggled.connect(self.roll12)
        self.ui.pushButton_2.setEnabled(False)
        
        self.ui.spinBox_2.setValue(50)
        self.ui.spinBox_3.setValue(10)
        self.spin2=self.ui.spinBox_2.value()
        self.spin3=self.ui.spinBox_3.value()
        self.ui.spinBox_2.valueChanged.connect(self.spinChanged2)
        self.ui.spinBox_3.valueChanged.connect(self.spinChanged3)
        
        
        
        
        self.ui.pushButton.clicked.connect(self.startClicked)
        self.ui.pushButton_2.clicked.connect(self.stopClicked)

    #按開始
    def startClicked(self):
        self.ui.pushButton.setEnabled(False)
        self.ui.pushButton_2.setEnabled(True)
        print("You clicked starttttt")
        self.combobox1=self.ui.comboBox.currentIndex()
        #打弊
        if self.combobox1==0:
            self.money1=money1(t=self.roll1,y=50,u=20)
            self.money1.start()#開始程序
        #原地    
        if self.combobox1==1:
            self.point1=point1(t=self.spin2,y=self.spin3,u=20)
            self.point1.start()#開始程序



    #按停止
    def stopClicked(self):
        self.ui.pushButton_2.setEnabled(False)
        self.ui.pushButton.setEnabled(True)
        print(f"You clicked stoppppp")
        if self.combobox1==0:
            self.money1.terminate()#終止程序
        if self.combobox1==1:
            self.point1.terminate()#終止程序


    #打幣選加倍
    def roll11(self):
        self.roll1=10
    def roll12(self):
        self.roll1=20
        
        
    #循環次數
    def spinChanged2(self):
        self.spin2=self.ui.spinBox_2.value()
    def spinChanged3(self):
        self.spin3=self.ui.spinBox_3.value()"""
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#------------------AI
# # data setting
# GAME_WIDTH = 1920
# GAME_HEIGHT = 1080

# IMG_PATH = 'screenshot.bmp'

# HUBCONF_FOLDER_PATH = r'.'
# MODEL_PATH = 'best.pt'
# CONFIDENCE_THRESHOLD = 0.4

# MOVE_DELAY1 = 0.049
# MOVE_DELAY2 = 0.033
# ONE_SHOT_DELAY = 0.001


# def screenshot(screen, img_path):
#     img = screen.grabWindow(0).toImage()
#     img.save(img_path)


# def inference_by_image(model, img_path):
#     results = model(img_path)
#     results_pandas = results.pandas()

#     # box coordinates
#     x_mins = results_pandas.xyxy[0]['xmin']
#     x_maxs = results_pandas.xyxy[0]['xmax']
#     y_mins = results_pandas.xyxy[0]['ymin']
#     y_maxs = results_pandas.xyxy[0]['ymax']

#     confidences = results_pandas.xyxy[0]['confidence']

#     return x_mins, x_maxs, y_mins, y_maxs, confidences


# def get_points_by_threshold(zip_object, threshold):
#     points = []
#     for x_min, x_max, y_min, y_max, conf in zip_object:
#         if conf > threshold:
#             points.append([int(x_min), int(x_max), int(y_min), int(y_max)])
#             print([int(x_min), int(x_max), int(y_min), int(y_max)])
#     return points






# def function1():

#     time.sleep(1)
#     print("Function 1 executed")
#     # init model
#     device = torch.device('cuda')
#     model = torch.hub.load(HUBCONF_FOLDER_PATH, 'custom', MODEL_PATH,
#                             source='local', force_reload=False)
#     model = model.to(device)

#     # init PyQt
#     app = QApplication(sys.argv)
#     screen = QApplication.primaryScreen()

#     # inference and move to shot
#     while True:
#         screenshot(screen, IMG_PATH)
#         x_mins, x_maxs, y_mins, y_maxs, confidences = inference_by_image(model, IMG_PATH)
#         points = get_points_by_threshold(zip(x_mins, x_maxs, y_mins, y_maxs, confidences),
#                                         CONFIDENCE_THRESHOLD)

# def cleanup():
#     process1.terminate()

#----------------------
# if __name__ == '__main__':
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     process1 = Process(target=function1)
#     process1.start()
    
#     atexit.register(cleanup)
#     sys.exit(app.exec_())