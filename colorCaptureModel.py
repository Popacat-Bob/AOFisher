from mss import mss
import numpy as np
from pyautogui import position, screenshot

class ColorCaptureModel:

    def __init__(self, topLeft: int, botRight: int, tolerance: int):
        self._topLeft = topLeft
        self._botRight = botRight
        self._tolerance = tolerance

    def setTopLeft(self, topLeft: int):
        self._topLeft = topLeft

    def setBotRight(self, botRight: int):
        self._botRight = botRight

    def setTolerance(self, tolerance: int):
        self._tolerance = tolerance

    def capture(self, targetRGB: tuple[int, int, int]):
        left, top = self._topLeft
        right, bottom = self._botRight
        width = right - left
        height = bottom - top

        with mss() as sct:
            region = {"top": top, "left": left, "width": width, "height": height}
            img = np.array(sct.grab(region),dtype=np.uint8)
            img = np.flip(img[:, :, :3], 2)

        diff = np.abs(img - np.array(targetRGB))
        masking = np.all(diff <= self._tolerance, axis = 2)

        if (np.any(masking)):
            print(True)
            
        return np.any(masking)
