from pyautogui import click
from time import sleep
from pynput.mouse import Listener, Button
from mss import mss
import numpy as np

class fisherModel:

    def __init__(self, delay: float = 0.5, clicks: int = 10):
        self.screenTopLeft: int = -1
        self.screenBotRight: int = -1
        self._delay = delay
        self._clicks = clicks

    @property
    def delay(self):
        return self._delay

    @property
    def clicks(self):
        return self._clicks

    def changeDelay(self, delay: float):
        self._delay = delay

    def changeClicks(self, clicks: int):
        self._clicks = clicks

    def catch(self, isPrompted: bool):

        if self.screenTopLeft < 0 and self.screenBotRight < 0:
            raise ValueError("Screen Coordinates not set")

        if isPrompted:

            for _ in range(self._clicks):
                click()
                sleep(self._delay)

class ColorCaptureModel:

    def __init__(self, topLeft: tuple[int, int], botRight: tuple[int, int], tolerance: int):
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
            img = np.array(sct.grab(region), dtype=np.uint8)
            img = np.flip(img[:, :, :3], 2)

        diff = np.abs(img - np.array(targetRGB))
        masking = np.all(diff <= self._tolerance, axis=2)

        return np.any(masking)

# captures screen region coordinates for scanning
class mouseScreenCaptureModel:
    def capture(self):

        topLeft: tuple[int, int] = None
        botRight: tuple[int, int] = None

        def on_click(x, y, button, pressed):
            nonlocal topLeft, botRight

            if pressed and button == Button.left:
                topLeft = (x, y)
            elif not pressed and button == Button.left:
                botRight = (x, y)
                return False

        with Listener(on_click=on_click) as listener:
            listener.join()

        return topLeft, botRight


# gets the rgb value of the color in the mouse position
class getColorAtMouseModel:
    def capture(self):
        color: tuple[int, int, int] | None = None

        def on_click(x, y, button, pressed):
            nonlocal color

            if pressed and button == Button.left:
                with mss() as sct:
                    region = {"top": y, "left": x, "width": 1, "height": 1}
                    img = np.array(sct.grab(region), dtype=np.uint8)
                    img = np.flip(img[:, :, :3], 2)
                    color = tuple(int(i) for i in img[0, 0])
                return False

        with Listener(on_click=on_click) as listener:
            listener.join()

        print(color)
        return color




