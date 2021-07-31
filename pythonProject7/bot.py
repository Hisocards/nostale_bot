import pyautogui
import time
import os, os.path
import numpy
import pyautogui
import threading
from PIL import Image, ImageGrab


firstpos = (1821, 105)
secondpos = (1848, 76)
thirdpos = (1886, 86)
cancel_animation = (1540, 514)
walking_timer = 30
attack_timer = 25
respawn_timer = 20

def get_pixel_color():
    for x in range(int(walking_timer + numpy.ceil(attack_timer * 2) + respawn_timer)): #100% als Puffer für die Time-sleeps in der Funktion attack
        s = pyautogui.screenshot()
        if s.getpixel((150, 36))[0] >= 230:
            pyautogui.press('e')
        time.sleep(1)

def walk_first_point():
    pyautogui.click(firstpos, clicks=2)

def walk_second_point():
    pyautogui.click(secondpos, clicks=2)

def walk_third_point():
    pyautogui.click(thirdpos, clicks=2)

def attack():
    for x in range(attack_timer):
        pyautogui.press('space', presses=3)
        time.sleep(0.1)
        pyautogui.click(cancel_animation, clicks=2)
        time.sleep(0.1)
        pyautogui.press('space', presses=3)
        time.sleep(0.5)
        pyautogui.press('3')
        time.sleep(1)

def automatisation():
    walk_first_point()
    time.sleep(walking_timer/2)
    walk_second_point()
    time.sleep(walking_timer/3 - 2)
    walk_third_point()
    time.sleep(walking_timer/6)
    attack()
    time.sleep(respawn_timer)

while True:
    threading.Thread(target=get_pixel_color).start()
    threading.Thread(target=automatisation()).start()