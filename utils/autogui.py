import pyautogui

def Keyboard(keyboard, singleKey=False):
    if singleKey:
        pyautogui.press(keyboard)
    else:
        pyautogui.write(keyboard)

def getMousePos():
    print(pyautogui.position())

def MoveAndClick(points, doubleClick=False, speed=0.5):
    if(points):
        index = 0
        for p in points:
            pyautogui.moveTo(points[index][0], points[index][1], speed)
            pyautogui.click()
            if(doubleClick):
                pyautogui.click()
            index = index + 1
        return True
    else:
        return False

