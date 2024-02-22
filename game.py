import os
import time
from PIL import ImageGrab
import win32gui

def capture_window(window_title):
    hwnd = win32gui.FindWindow(None, window_title)
    if hwnd:
        left, top, right, bottom = win32gui.GetWindowRect(hwnd)
        window_image = ImageGrab.grab((left, top, right, bottom))
        return window_image
    else:
        print("找不到窗口：", window_title)
        return None

def save_image(image, folder):
    if not os.path.exists(folder):
        os.makedirs(folder)
    timestamp = int(time.time())
    filename = os.path.join(folder, f"screenshot_{timestamp}{a}.png")
    image.save(filename)
    print(f"截图已保存为：{filename}")

if __name__ == "__main__":
    window_title = "MapleStory"  # 替换成你想要截图的窗口标题
    folder_name = "a"
    a=0
    
    while True:
        window_image = capture_window(window_title)
        if window_image:
            save_image(window_image, folder_name)
        
        time.sleep(0.5)
        a=a+1
        if a>60:
            break
        
        #labelImg