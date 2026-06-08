from pynput import mouse 
from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import Qt, QMetaObject
from .RectangleWidget import RectOverlay
from .ScreenshotOverlay import ScreenshotOverlay
import sys 

class MouseDrawRectEvent:
    def __init__(self, app: QApplication):
        self.app = app
        self.x0: int = 0
        self.y0: int = 0 
        self.x1: int = 0
        self.y1: int = 0
          
        self.is_done = None
    
    def _invoke(self, obj, method):
        QMetaObject.invokeMethod(obj, method, Qt.ConnectionType.QueuedConnection)

    def reset(self):
        self.is_done = None 

    def on_move(self, x, y):
        if self.is_done is None: return 
        self.rect.update_rect(self.x0, self.y0, x, y)

    def on_click(self, x, y, button, pressed):
        if button == mouse.Button.left and pressed:
            print(f'Coordinate start at x0={x}, y0={y}')
            self.x0, self.y0 = x, y
            self.is_done = False
            self._invoke(self.ss_overlay, "show")
            self._invoke(self.rect, "show")
            self._invoke(self.rect, "raise")

        if button == mouse.Button.left and not pressed:
            print(f'Coordinate end at x1={x}, y1={y}')
            self.x1, self.y1 = x, y
            self.is_done = True 
            self._invoke(self.rect, "hide")
            self._invoke(self.ss_overlay, "hide")
            self.stop()

    def start(self):
        self.listener = mouse.Listener(
                on_move = self.on_move,
                on_click = self.on_click,
                )

        self.rect = RectOverlay(0, 0, 0, 0)
        self.ss_overlay = ScreenshotOverlay()

        self.listener.start()
    
    def stop(self):
        self.listener.stop()
