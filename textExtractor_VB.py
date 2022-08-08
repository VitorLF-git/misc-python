

from cmath import log
from multiprocessing.sharedctypes import Value
from unicodedata import name
import cv2 as cv
import numpy as np
import os

from time import time
from time import sleep

from utils.windowcapture import WindowCapture
from utils.vision import Vision
from utils import autogui

from pynput import keyboard
import datetime

import pyautogui
from towers import tower

from PIL import Image
from pytesseract import pytesseract
import win32api

import json

# Change the working directory to the folder this script is in.
# Doing this because I'll be putting the files from each video in their own folder on GitHub
os.chdir(os.path.dirname(os.path.abspath(__file__)))

class Skill:
    name = ""
    amount = 0
    isSpecial = False

class Unit:
    name = ''
    health = 0
    power = 0
    defence = 0
    speed = 0
    wisdom = 0
    growth = ''
    types = []
    skills = [Skill()]
    cost = 0
    internalAffairsName = ''
    internalAffairs = 0
looping = True
def on_release(key):
    global looping
    if key == keyboard.Key.esc:
        looping = False
        return False
listener = keyboard.Listener(on_release=on_release)
listener.start()

#Define path to tessaract.exe

path_to_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
pytesseract.tesseract_cmd = path_to_tesseract
#Define path to image
path_to_image = 'sample4.jpg'
# initialize the WindowCapture class
wincap = WindowCapture()
# initialize the Vision class
counter = 0
step = 0
loop_time = time()
runOnce = True
x1 = 0
y1 = 0
x2 = 0
y2 = 0
mousepos = (0,0)
skillList = []
state_left = win32api.GetKeyState(0x01) 
while(looping):
    # print('looping')
    print(win32api.GetCursorPos())
    sleep(0.1)
    a = win32api.GetKeyState(0x01)
    if a != state_left:  # Button state changed
        state_left = a
        if a < 0:
            print('Left Button Pressed')
        else:
            print('Left Button Released')
            mousepos = win32api.GetCursorPos()
            win32api.GetCursorPos()
            print(mousepos[0])
            if counter == 1:
                x2 = mousepos[0]
                y2 = mousepos[1]
                counter += 1
            elif counter == 0:
                x1 = mousepos[0]
                y1 = mousepos[1]
                counter += 1

    if cv.waitKey(1) == ord('q'):
        looping = False
        break

    if counter == 2:
        break
#Point tessaract_cmd to tessaract.exe
type = [[44,523]]
unit = [[138,513]]
unitLenght = 0
unitWidth = 0
step = 0
while(looping):
    # sleep(1)
    autogui.MoveAndClick(unit, False, 0.1)
    if unitWidth < 4:
        if unitLenght < 7:
            unit[0][0] += 100
            unitLenght += 1
        else:
            unit[0][0] = 138
            unit[0][1] += 125
            unitLenght = 0
            unitWidth += 1
    else:
        autogui.MoveAndClick(type, False, 0.1) 
        unitWidth = 0
        type[0][1] += 30
        unit[0][1] = 513
        step += 1
    if step == 15:
        with open("file.json", "w+") as f:
            json.dump(skillList, f)
        break
    # 812 27, 683 375
    # counter += 1
    screenshot1 = wincap.get_screenshot()
    if x1 > x2:
        x1, x2 = x2, x1
    if y1 > y2:
        y1, y2 = y2, y1
    if y1-15 < 0:
        y1 = 0
    if x1-15 < 0:
        x1 = 0
    screenshot = screenshot1[y1:y2, x1:x2]
    # screenshot = cv.cvtColor(screenshot, cv.COLOR_BGR2RGB)
    if counter == 2:
        cv.imshow('image', screenshot)
        while cv.getWindowProperty('image', cv.WND_PROP_VISIBLE) >= 1 and looping:
            cv.waitKey(100)
        counter += 1
    #Open image with PIL
    # img = Image.open(path_to_image)

        #Extract text from image
    text = pytesseract.image_to_string(screenshot)
    # print('----------------------------------------------------')
    # print(repr(text))
    # print('----------------------------------------------------')
    # split line breaks
    splitText = text.split('\n')
    for skills in splitText:
        # split definition
        splitSkills = skills.split(':')
        for i,skillText in enumerate(splitSkills):
            splitSkills[i] = skillText.strip()
        # if theres 2 skills, split the skills and rearange
        if len(splitSkills) == 2:
            skillList.append(splitSkills[0])
        if len(splitSkills) == 3:
            val2 = splitSkills[1].split(' ',1)
            splitSkills[1] = val2[0]
            splitSkills.append(splitSkills[2])
            splitSkills[2] = val2[1]
            skillList.append(splitSkills[0])
            skillList.append(splitSkills[2])
        elif len(splitSkills) > 3:
            raise Exception("Val cant be higher than 3") 
        skills[:skills.find(':')] + skills[skills.find(':'):skills.find(' ')]

        # text = text.split('\n')
        # with open("file.json", "w+") as f:
        #     json.dump(object_to_write, f)
    # debug the loop rate
    # print('FPS {}'.format(1 / (time() - loop_time)))
    loop_time = time()
    print('----------------------------------------------------')
    skillList = list( dict.fromkeys(skillList) )
    print(skillList)
    print('----------------------------------------------------')
    
    # press 'q' with the output window focused to exit.
    # waits 1 ms every loop to process key presses
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break
cv.destroyAllWindows()
print('Done.')


