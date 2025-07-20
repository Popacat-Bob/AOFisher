from typing import Callable
import numpy as np
from mss import mss
from pynput.mouse import Button, Listener
from threading import Thread
from time import sleep
from PyQt5.QtWidgets import QApplication, QLabel
from PyQt5.QtGui import QPixmap, QGuiApplication, QPaintEvent
from PyQt5.QtCore import Qt

# captures screen region coordinates for scanning
class mouseScreenCaptureModel:
    def capture(self):

        topLeft: tuple[int, int] | None = None
        botRight: tuple[int, int] | None = None

        class DrawableWindow(QLabel):

            def __init__(self):
                super().__init__()

                screen = QGuiApplication.primaryScreen()
                screenshot = screen.grabWindow(0)

                self.setPixmap(screenshot)
                self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool)
                self.setGeometry(QGuiApplication.primaryScreen().geometry())
                self.showFullScreen()

        ss: None | DrawableWindow = None

        def on_click(x, y, button, pressed):
            nonlocal topLeft, botRight
            nonlocal ss

            if pressed and button == Button.left:
                topLeft = (x, y)
                ss = DrawableWindow()

            elif not pressed and button == Button.left:
                botRight = (x, y)
                if ss:
                    ss.close()

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

        return color
    

#multi-threading switch to run custom funcs based on PyQt5 checkable buttons
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
