

from cmath import log
import cv2 as cv
import numpy as np
import os

from time import time
from time import sleep

from utils.windowcapture import WindowCapture
from image_capture import ImageCapture

from pynput import keyboard

from pytesseract import pytesseract
import win32api
# Change the working directory to the folder this script is in.
# Doing this because I'll be putting the files from each video in their own folder on GitHub
os.chdir(os.path.dirname(os.path.abspath(__file__)))

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
state_left = win32api.GetKeyState(0x01) 
while(looping):
    # print('looping')
    print(win32api.GetCursorPos())
    sleep(0.2)
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
            if counter == 0:
                x1 = mousepos[0]
                y1 = mousepos[1]
                counter += 1
            elif counter == 1:
                x2 = mousepos[0]
                y2 = mousepos[1]
                counter += 1

    if cv.waitKey(1) == ord('q'):
        looping = False
        break

    if counter == 2:
        break
#Point tessaract_cmd to tessaract.exe
while(looping):
    # 812 27, 683 375
    # counter += 1
    print('x1: {} y1: {} x2: {} y2: {}'.format(x1, y1, x2, y2))
    sleep(1)
    screenshot1 = wincap.get_screenshot()
    print('screenshot1: {}'.format(screenshot1))
    screenshot1 = ImageCapture.collect_screen()
    print('screenshot1: {}'.format(screenshot1))
    if x1 > x2:
        x1, x2 = x2, x1
    if y1 > y2:
        y1, y2 = y2, y1
    x1 = x1 - 15
    y1 = y1 - 15
    if y1 < 0:
        y1 = 0
    if x1 < 0:
        x1 = 0
    print('x1: {} y1: {} x2: {} y2: {}'.format(x1, y1, x2, y2))
    screenshot = screenshot1[y1:y2, x1:x2]
    cv.imshow('image', screenshot)
    while cv.getWindowProperty('image', cv.WND_PROP_VISIBLE) >= 1 and looping:
            cv.waitKey(100)

    text = pytesseract.image_to_string(screenshot)
    print(text)
    loop_time = time()

    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break
cv.destroyAllWindows()
print('Done.')
