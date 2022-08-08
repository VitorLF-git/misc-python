# Bring in mss

from mss import mss

# Bring in opencv for rendering
import cv2

import numpy as np

class ImageCapture:
    # Setup the game area
    game_area = {"left": 0, "top": 0, "width": 960, "height": 540}
    capture = mss()
    def collect_frames():
        gamecap = np.array(capture.grab(game_area))
        cv2.imshow('gamecap.jpg', gamecap)

    if __name__ == '__main__':
        collect_frames()
        print('done')