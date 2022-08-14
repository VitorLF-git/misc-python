# Bring in mss

from mss import mss

# Bring in opencv for rendering
import cv2

import numpy as np

class ImageCapture:
    # Setup the game area
    def collect_frame(left, top, width, height):
        game_area = {"left": left, "top": top, "width": width, "height": height}
        capture = mss()
        gamecap = np.array(capture.grab(game_area))
        return gamecap
        cv2.imshow('gamecap.jpg', gamecap)


    def collect_screen():
        game_area = {"left": 0, "top": 0, "width": 1920, "height": 1080}
        capture = mss()
        gamecap = np.array(capture.grab(game_area))
        return gamecap


    if __name__ == '__main__':
        collect_frame()
        print('done')