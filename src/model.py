from pyautogui import click
from time import sleep, time
from mss import mss
import numpy as np
import keyboard


class colorCaptureModel:

    def __init__(self, topLeft: tuple[int, int], botRight: tuple[int, int], tolerance: int):
        self._topLeft = topLeft
        self._botRight = botRight
        self._tolerance = tolerance

        if topLeft[0] > botRight[0]:
            print("Initial x coordinate should be smaller than final x coordinate")

        if topLeft[1] > botRight[1]:
            print("Initial y coordinate should be smaller than final y coordinate")

    @property
    def topLeft(self):
        return self._topLeft

    @property
    def botRight(self):
        return self._botRight

    @property
    def tolerance(self):
        return self._tolerance

    #setter methods for each parameter
    def setTopLeft(self, topLeft: tuple[int, int]):
        self._topLeft = topLeft

    def setBotRight(self, botRight: tuple[int, int]):
        self._botRight = botRight

    def setTolerance(self, tolerance: int):
        self._tolerance = tolerance

    #scans the screen for the target color based on the region selected
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
                 timeEatInterval: int = 1200,
                 brewEatInterval: int = 360,
                 resetDuration: int = 60
                 ):

        self._scanDelay = scanDelay
        self._postFishDelay = postFishDelay

        self._color = color
        self._capturer = capture
        self._clickDelay = clickDelay
        self._clicks = clicks

        self._timeEatStart = None
        self._timeEatInterval = timeEatInterval

        self._timeFishStart = None
        self._resetDuration = resetDuration

        self._brewEatInterval = brewEatInterval
        self._brewsToEat = 0
        self._brewEatStart = None
        self._brewEat = False

        self._running = False

    @property 
    def timeEatInterval(self):
        return self._timeEatInterval
    
    @property
    def resetDuration(self):
        return self._resetDuration 
    
    @property
    def clickDelay(self):
        return self._clickDelay

    @property
    def clicks(self):
        return self._clicks
    
    @property
    def color(self): 
        return self._color
    
    @property 
    def scanDelay(self):
        return self._scanDelay
    
    @property
    def postFishDelay(self):
        return self._postFishDelay
    
    @property
    def colorCapture(self):
        return self._capturer

    def setTimeEatInterval(self, timeEatInterval: int):
        self._timeEatInterval = timeEatInterval

    def setResetDuration(self, resetDuration: int):
        self._resetDuration = resetDuration

    def setColor(self, color: tuple[int, int, int]):
        self._color = color

    def setClickDelay(self, clickDelay: float):
        self._clickDelay = clickDelay

    def setClicks(self, clicks: int):
        self._clicks = clicks

    def setPostFishDelay(self, postFishDelay: float):
        self._postFishDelay = postFishDelay

    def setScanDelay(self, scanDelay: float):
        self._scanDelay = scanDelay

    def setRunning(self, running: bool):
        self._running = running

        if self._running:
            print("Running")
        else:
            print("Stopped")

    def setBrewEatInterval(self, brewEatInterval: int):
        self._brewEatInterval = brewEatInterval

    def flipBrewEat(self):
        self._brewEat = not self._brewEat

    def _isGreaterthanDuration(self, start, duration):
        return True if time() - start >= duration else False

    #actions for eating
    def _eatAction(self):
        print("Logged eating")
        keyboard.press_and_release('9')
        sleep(0.5)
        click()
        sleep(2)
        keyboard.press_and_release('0')
        click()

    #actions for restting broken fishing
    def _resetAction(self):
        print('Resetting sequence')
        click()
        sleep(0.5)
        keyboard.press_and_release('9')
        sleep(0.5)
        keyboard.press_and_release('0')
        sleep(0.5)
        click()

    def _reFishAction(self):
        keyboard.press_and_release('0')
        sleep(0.5)
        keyboard.press_and_release('0')
        sleep(self._postFishDelay)
        click()

    def _placeBrew(self):
        print("Placing brew")
        keyboard.press_and_release('8')
        sleep(0.5)

    def _brewAction(self):
        print("Eating brew")
        keyboard.press_and_release('e')
        sleep(0.5)
        keyboard.press_and_release('0')
        sleep(0.5)

    #connects all actions
    def run(self):

        if not self._timeEatStart:
            self._timeEatStart = time()

        if self._isGreaterthanDuration(self._timeEatStart, self._timeEatInterval):
            self._eatAction()
            self._timeEatStart = time()

        if self._brewEat:

            if not self._brewsToEat:
                self._placeBrew()
                self._brewAction()
                self._brewsToEat = 4
                self._brewEatStart = None

            if not self._brewEatStart:
                self._brewEatStart = time()

            if self._isGreaterthanDuration(self._brewEatStart, self._brewEatInterval):
                self._brewAction()
                self._brewsToEat-= 1
                self._brewEatStart = None
        else:
            self._brewsToEat = 0

        while self._running:

            if not self._timeFishStart:
                self._timeFishStart = time()

            if self._isGreaterthanDuration(self._timeFishStart, self._resetDuration):
                self._resetAction()
                self._timeFishStart = None
                return

            if self._capturer.capture(self._color):
                print("Logged catch")
                self._catch()

                if not self._running:
                    return

                self._reFishAction()
                self._timeFishStart = None
                return

            sleep(self._scanDelay)

    #catches fish based on clicks and click interval parameters
    def _catch(self):
        for _ in range(self._clicks):

            if not self._running:
                break

            click()
            sleep(self._clickDelay)


