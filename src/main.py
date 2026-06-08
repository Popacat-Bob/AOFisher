from FishLoop import FishEventLoop 
from RegionDrawEventHandler import RegionDrawEventHandle 
from Structs import *
from GUI import * 

RECT = Rect(0, 0, 0, 0)
TOL = 10 
COLOR = RGB(244, 244, 244)
CLICKS = 75


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    LoopManager = FishEventLoop(fish_prompt_region=RECT, tolerance=TOL, color=COLOR, clicks=CLICKS)
    RegionDrawManager = RegionDrawEventHandle(app)
    win = MainWindow(LoopManager, RegionDrawManager)
    win.show() 
    sys.exit(app.exec())

