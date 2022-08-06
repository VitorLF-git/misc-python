

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

# initialize the WindowCapture class
wincap = WindowCapture()
# initialize the Vision class
fish = Vision('fish.jpg')
square = Vision('square.jpg')
square2 = Vision('square2.jpg')
square3 = Vision('square3.jpg')

counter = 0
step = 0
loop_time = time()
runOnce = True
# while(looping):
#     autogui.getMousePos()
while(looping):
    # 812 27, 683 375
    counter += 1
    sleep(0.1)
    screenshot = wincap.get_screenshot()
    print(step)
    if(runOnce):
        step = 0
        runOnce = False

    if(step == 1):
        # pyautogui.keyDown('ctrl')
        # sleep(2)
        pyautogui.press('8')
        sleep(0.5)
        pyautogui.press('9')
        sleep(0.5)
        pyautogui.rightClick()
        counter = 0
        step = 0

    if step == 0:
        points = fish.find(screenshot, 0.6, 'rectangles')
        squarePos = square.find(screenshot, 0.6, 'rectangles')
        squarePos2 = square2.find(screenshot, 0.6, 'rectangles')
        squarePos3 = square3.find(screenshot, 0.6, 'rectangles')
        if not points:
            print('No fish found')
            print(counter)
            pyautogui.keyUp('right')
            pyautogui.keyUp('left')
            if counter > 75:
                step = 1


        if points and squarePos:
            print('found fish')
            counter = 0
            if squarePos[0][0] < points[0][0]:
                pyautogui.keyUp('left')
                pyautogui.keyDown('right')
                print('right')
            if squarePos[0][0] > points[0][0]:
                pyautogui.keyUp('right')
                pyautogui.keyDown('left')
                print('left')

        if points and squarePos2:
            counter = 0
            print('square2')
            if squarePos2[0][0] < points[0][0]:
                pyautogui.keyUp('left')
                pyautogui.keyDown('right')
                print('right')
            if squarePos2[0][0] > points[0][0]:
                pyautogui.keyUp('right')
                pyautogui.keyDown('left')
                print('left')
        
        if points and squarePos3:
            counter = 0
            print('square3')
            if squarePos3[0][0] < points[0][0]:
                pyautogui.keyUp('left')
                pyautogui.keyDown('right')
                print('right')
            if squarePos3[0][0] > points[0][0]:
                pyautogui.keyUp('right')
                pyautogui.keyDown('left')
                print('left')

    # if step == 0:
    #     points = sub.find(screenshot, 0.6, 'rectangles')
    #     if points:
    #         autogui.MoveAndClick(points)
    #         autogui.MoveAndClick([(600,390)], True)
    #         step = step+1
    

    # debug the loop rate
    print('FPS {}'.format(1 / (time() - loop_time)))
    loop_time = time()

    # press 'q' with the output window focused to exit.
    # waits 1 ms every loop to process key presses
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break
cv.destroyAllWindows()
print('Done.')
