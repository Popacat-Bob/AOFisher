from typing import Callable
import numpy as np
from mss import mss
from pynput.mouse import Button, Listener
from threading import Thread
from time import sleep
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
    

class switch:
    def __init__(self, func: Callable[[], None]):
        self._toggle = False
        self._func = func
        self._thread = None

    def toggleRun(self, checked: bool):
        self._toggle = checked 

        if self._toggle and (self._thread is None or not self._thread.is_alive()):
            self._thread = Thread(target=self._runTask, daemon=True)
            self._thread.start()

    def _runTask(self):
        while self._toggle:
            self._func()
            sleep(0.5)