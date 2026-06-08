from aux.RegionDrawer import MouseDrawRectEvent
from PyQt6.QtWidgets import QApplication
from Structs import Rect

class RegionDrawEventHandle:
    def __init__(self, app: QApplication):
        self.app = app
        self.RegionDrawEvent = MouseDrawRectEvent(self.app)
        self.Rect: Rect | None = None

    def start(self):
        self.RegionDrawEvent.start()
        self.RegionDrawEvent.reset()

