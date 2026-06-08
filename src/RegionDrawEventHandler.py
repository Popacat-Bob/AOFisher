from aux.RegionDrawer import MouseDrawRectEvent
from PyQt6.QtWidgets import QApplication 
from Structs import Rect
import sys

class RegionDrawEventHandle:
    def __init__(self): 
        self.app = QApplication(sys.argv)
        self.RegionDrawEvent = MouseDrawRectEvent(self.app)
        self.Rect: Rect | None = None 
    def start(self):
        self.RegionDrawEvent.start() 
        self.app.exec()
        self.Rect= Rect(self.RegionDrawEvent.x0,
                        self.RegionDrawEvent.y0,
                        self.RegionDrawEvent.x1,
                        self.RegionDrawEvent.y1
                        ) 

        self.RegionDrawEvent.reset()


RegionDrawEventHandle().start()
