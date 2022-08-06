import pyautogui
from utils import autogui
from utils.vision import Vision

def PlaceTower(image : Vision, screenshot, towerLocation, threshold=0.9, speed=1):
    #find sub image
    points = image.find(screenshot, threshold, 'rectangles')
    if(points):
        #print(points[0][0])
        autogui.MoveAndClick(points)
        autogui.MoveAndClick(towerLocation, True)
        return True
    return False

def PressStart(start : Vision, screenshot, speed=1):
    points = start.find(screenshot, 0.5, 'rectangles')
    autogui.MoveAndClick(points, True)


def UpgradeTower(upgrade : Vision, screenshot, speed=1): 
    points = upgrade.find(screenshot, 0.9, 'rectangles')
    return autogui.MoveAndClick(points)