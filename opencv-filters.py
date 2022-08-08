

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
from matplotlib import pyplot as plt

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

wincap = WindowCapture()

counter = 0
step = 0
loop_time = time()
runOnce = True

thr = 0
thr2 = 0
aperture = 3

images=[]
# while(looping):
#     autogui.getMousePos()

def on_change1(value):
    print(value)
    global thr
    thr = value
    thresh_callback()

def on_change2(value):
    print(value)
    global thr2
    thr2 = value
    thresh_callback()

def on_change3(value):
    print(value)
    global aperture
    aperture = value
    thresh_callback()

def thresh_callback():
    # ret, edges = cv.threshold(screenshot,thr,thr2,cv.THRESH_BINARY)
    edges = cv.GaussianBlur(screenshot,(aperture,aperture), sigmaX=0, sigmaY=0)
    edges = cv.medianBlur(screenshot, aperture)
    edges = cv.Canny(image=edges, threshold1=thr, threshold2=thr2, apertureSize=3)
    cv.imshow(windowName, edges)


while(looping):
    sleep(0.5)
    print('FPS {}'.format(1 / (time() - loop_time)))
    loop_time = time()
    screenshot = wincap.get_screenshot()
    # screenshot1 = wincap.get_screenshot()
    # screenshot = screenshot1[0:190, 1170:1370]
    # img_blur = cv.GaussianBlur(screenshot,(3,3), sigmaX=0, sigmaY=0) 
    # screenshot = cv.cvtColor(screenshot, cv.COLOR_RGB2GRAY)
    # Canny Edge Detection
    # Thresholding
    # ret, edges = cv.threshold(screenshot,thr,thr2,cv.THRESH_BINARY)
    edges = cv.medianBlur(screenshot, 31)
    # edges = cv.GaussianBlur(screenshot,(1,1), sigmaX=0, sigmaY=0)
    edges = cv.Canny(image=screenshot, threshold1=thr, threshold2=thr2, apertureSize=3)
    images.append(edges)
    
    windowName = 'image'
    cv.imshow(windowName, edges)
    
    cv.createTrackbar('slider1', windowName, 1, 1000, on_change1)
    cv.createTrackbar('slider2', windowName, 1, 1000, on_change2)
    cv.createTrackbar('slider3', windowName, 1, 31, on_change3)
    keyCode = cv.waitKey(0)

    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break
cv.destroyAllWindows()
print('Done.')
