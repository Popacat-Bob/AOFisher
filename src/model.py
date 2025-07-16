from pyautogui import click
from time import sleep
from mss import mss
import numpy as np


class colorCaptureModel:

    def __init__(self, topLeft: tuple[int, int], botRight: tuple[int, int], tolerance: int):
        self._topLeft = topLeft
        self._botRight = botRight
        self._tolerance = tolerance

        if topLeft[0] > botRight[0]:
            raise ValueError("Initial x coordinate should be smaller than final x coordinate")

        if topLeft[1] > botRight[1]:
            raise ValueError("Initial y coordinate should be smaller than final y coordinate")

    @property
    def topLeft(self):
        return self._topLeft

    @property
    def botRight(self):
        return self._botRight

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
            img = np.array(sct.grab(region), dtype=np.uint8)
            img = np.flip(img[:, :, :3], 2)

        diff = np.abs(img - np.array(targetRGB))
        masking = np.all(diff <= self._tolerance, axis=2)

        return np.any(masking)

class model:

    def __init__(self,
                 capture: colorCaptureModel,
                 color: tuple[int, int, int],
                 scanDelay: float = 1,
                 clickDelay: float = 0.5,
                 postFishDelay: float = 5,
                 clicks: int = 10,
                 ):

        self._scanDelay = scanDelay
        self._postFishDelay = postFishDelay
        self._color = color
        self._capturer = capture
        self._clickDelay = clickDelay
        self._clicks = clicks

    @property
    def clickDelay(self):
        return self._clickDelay

    @property
    def clicks(self):
        return self._clicks

    def setColor(self, color: tuple[int, int, int]):
        self._color = color

    def setDelay(self, clickDelay: float):
        self._clickDelay = clickDelay

    def setClicks(self, clicks: int):
        self._clicks = clicks

    def setPostFishDelay(self, postFishDelay: float):
        self._postFishDelay = postFishDelay

    def run(self):

        while True:

            if self._capturer.capture(self._color):
                self._catch()
                print("Logged catch")
                sleep(self._postFishDelay)
                click()
                return

            sleep(self._scanDelay)


    def _catch(self):
        for _ in range(self._clicks):
            click()
            sleep(self._clickDelay)







