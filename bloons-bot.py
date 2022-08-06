

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
sub = Vision('sub.jpg')
longerRange = Vision('longerRange.jpg')
twinGuns = Vision('twinGuns.jpg')
airburstDarts = Vision('airburstDarts.jpg')
advancedIntel = Vision('advancedintel.jpg')
submerge = Vision('submerge.jpg')
reactor = Vision('reactor.jpg')
start = Vision('start.jpg')
pirate = Vision('pirate.jpg')
grapeShot = Vision('grapeShot.jpg')
hotShot = Vision('hotShot.jpg')
cannon = Vision('cannon.jpg')
monkeyPirates = Vision('monkeyPirates.jpg')
skill1 = Vision('skill1.jpg')
nextButton = Vision('next.jpg')
homeButton = Vision('home.jpg')
playButton = Vision('play2.jpg')
expertButton = Vision('expert.jpg')
rightArrow = Vision('rightArrow.jpg')
ouchMap = Vision('ouchMap.jpg')
difficulty1 = Vision('difficulty1.jpg')
standardButton = Vision('standard.jpg')
collectButton = Vision('collect.jpg')
levelUp = Vision('levelUp.jpg')
restartButton = Vision('restart.jpg')
restartButton2 = Vision('restart2.jpg')
normal = Vision('normal.jpg')
uncommon = Vision('uncommon.jpg')
continueButton = Vision('continue.jpg')
book = Vision('book.jpg')
monkeScreen = Vision('monkeScreen.jpg')
goBack = Vision('goBack.jpg')

counter = 0
step = 0
loop_time = time()
runOnce = True
# while(looping):
#     autogui.getMousePos()
while(looping):
    counter += 1
    sleep(0.5)
    screenshot = wincap.get_screenshot()
    print(step)
    if(runOnce):
        step = 0
        runOnce = False

    if(counter == 10):
        points = levelUp.find(screenshot, 0.6, 'rectangles')

        if points:
            autogui.MoveAndClick(points, True)
            
        points = restartButton.find(screenshot, 0.6, 'rectangles')

        if points:
            autogui.MoveAndClick(points)

            
        points = restartButton2.find(screenshot, 0.6, 'rectangles')

        if points:
            autogui.MoveAndClick(points, True)
            step = 0

        points = book.find(screenshot, 0.6, 'rectangles')
        
        if points:
            autogui.MoveAndClick(points, True)

        points = monkeScreen.find(screenshot, 0.6, 'rectangles')
        if points:    
            print('Monkey Screen')
            points = goBack.find(screenshot, 0.6, 'rectangles')
            if points:
                autogui.MoveAndClick(points, True)
        counter = 0

    if step == 19:
        points = standardButton.find(screenshot, 0.6, 'rectangles')
        if points:
            autogui.MoveAndClick(points)
            
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            step = 0

    if step == 18:
        points = difficulty1.find(screenshot, 0.6, 'rectangles')
        if points:
            autogui.MoveAndClick(points)
            
            
            step = step+1


    if step == 17:
        points = ouchMap.find(screenshot, 0.6, 'rectangles')
        if points:
            autogui.MoveAndClick(points)
            
            
            step = step+1

    if step == 16:
        points = rightArrow.find(screenshot, 0.6, 'rectangles')
        if points:
            autogui.MoveAndClick(points)
            
            
            step = step+1

    if step == 15:
        points = expertButton.find(screenshot, 0.6, 'rectangles')
        if points:
            autogui.MoveAndClick(points)
            step = step+1
        else:
            points = collectButton.find(screenshot, 0.6, 'rectangles')
            if points:
                autogui.MoveAndClick(points)
                    
            points = normal.find(screenshot, 0.6, 'rectangles')
            if points:
                autogui.MoveAndClick(points, True)
                sleep(0.5)
                autogui.MoveAndClick(points, True)
                sleep(0.5)
                autogui.MoveAndClick(points, True)
                sleep(0.5)
                autogui.MoveAndClick(points, True)
                sleep(0.5)
                autogui.MoveAndClick(points, True)
            
            points = uncommon.find(screenshot, 0.6, 'rectangles')
            if points:
                autogui.MoveAndClick(points, True)
                sleep(0.5)
                autogui.MoveAndClick(points, True)
                sleep(0.5)
                autogui.MoveAndClick(points, True)
                sleep(0.5)
                autogui.MoveAndClick(points, True)
                sleep(0.5)
                autogui.MoveAndClick(points, True)

            points = continueButton.find(screenshot, 0.7, 'rectangles')
            if points:
                autogui.MoveAndClick(points, True)
                step = 14
            points = playButton.find(screenshot, 0.7, 'rectangles')
            if points:
                autogui.MoveAndClick(points, True)
                step = 15


    if step == 14:
        points = playButton.find(screenshot, 0.6, 'rectangles')
        if points:
            autogui.MoveAndClick(points)    
            step = step+1
        points = collectButton.find(screenshot, 0.6, 'rectangles')
        if points:
            autogui.MoveAndClick(points)
            step = step+1

    if step == 13:
        points = homeButton.find(screenshot, 0.6, 'rectangles')
        if points:
            autogui.MoveAndClick(points)
            
            
            step = step+1


    if step == 12:
        points = skill1.find(screenshot, 0.7, 'rectangles')
        if points:
            autogui.MoveAndClick(points, speed=0.1)
        else:
            points = nextButton.find(screenshot, 0.7, 'rectangles')
            if points:
                autogui.MoveAndClick(points, speed=0.5)
                step = step + 1

    if step == 11:
        points = monkeyPirates.find(screenshot, 0.6, 'rectangles')
        if points:
            autogui.MoveAndClick(points)
            
            
            step = step+1

    if step == 10:
        points = cannon.find(screenshot, 0.6, 'rectangles')
        if points:
            autogui.MoveAndClick(points)
            
            
            step = step+1

    if step == 9:
        points = hotShot.find(screenshot, 0.6, 'rectangles')
        if points:
            autogui.MoveAndClick(points)
            
            step = step+1

    if step == 8:
        points = grapeShot.find(screenshot, 0.6, 'rectangles')
        if points:
            autogui.MoveAndClick(points)
            
            autogui.MoveAndClick([(62,265)], speed=0.2)
            step = step+1

    if step == 7:
        points = pirate.find(screenshot, 0.8, 'rectangles')
        if points:
            autogui.MoveAndClick(points)
            autogui.MoveAndClick([(678,401)], True)
            step = step+1

    if step == 6:
        points = reactor.find(screenshot, 0.6, 'rectangles')
        if points:
            autogui.MoveAndClick(points)
            
            autogui.MoveAndClick([(62,265)], speed=0.2)
            step = step+1

    if step == 5:
        points = submerge.find(screenshot, 0.6, 'rectangles')
        if points:
            autogui.MoveAndClick(points)
            autogui.MoveAndClick([(256,265)], speed=0.2)
            step = step+1

    if step == 4:
        points = advancedIntel.find(screenshot, 0.6, 'rectangles')
        if points:
            autogui.MoveAndClick(points)
            step = step+1

    if step == 3:
        points = airburstDarts.find(screenshot, 0.6, 'rectangles')
        if points:
            autogui.MoveAndClick(points)
            step = step+1

    if step == 2:
        points = twinGuns.find(screenshot, 0.6, 'rectangles')
        if points:
            autogui.MoveAndClick(points)
            step = step+1

    if step == 1:
        points = longerRange.find(screenshot, 0.6, 'rectangles')
        if points:
            autogui.MoveAndClick(points)
            points = start.find(screenshot, 0.8, 'rectangles')
            autogui.MoveAndClick(points, True)
            step = step+1

    if step == 0:
        points = sub.find(screenshot, 0.6, 'rectangles')
        if points:
            autogui.MoveAndClick(points)
            autogui.MoveAndClick([(600,390)], True)
            step = step+1
    

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
