

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


counter = 0
step = 0
loop_time = time()
runOnce = True
# while(looping):
#     autogui.getMousePos()
points = [[925,435]]
pyautogui.keyDown('ctrl')
while(looping):
    autogui.MoveAndClick(points, False, 0.1)
    # sleep(0.2)
    counter += 1
    if counter < 5:
        points[0][1] += 38
    else:
        points[0][0] += 38
        points[0][1] = 435
        counter = 0
        step += 1
    if step == 12:
        pyautogui.keyUp('ctrl')
        break
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
