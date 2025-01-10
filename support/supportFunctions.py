import pyautogui
import time
import random

def leftClick(x, y):
    pyautogui.leftClick(x + random.randint(1, 20), y + random.randint(1, 15))
    time.sleep(random.randint(2,3))