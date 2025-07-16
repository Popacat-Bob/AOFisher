from PyQt5.QtWidgets import QMainWindow, QLabel, QPushButton
from PyQt5.QtGui import QIcon, QFont, QGuiApplication
from typing import Callable

class view(QMainWindow):
    def __init__(self, sizeWidth: int, sizeHeight: int):
        
        super().__init__()
        self._screenSize = QGuiApplication.primaryScreen().size()
        self.setWindowTitle("AO Fisher")

        self.openCenter(sizeWidth, sizeHeight)
        self.setWindowIcon(QIcon('icons/fish.png'))

        self._sizeWidth = sizeWidth
        self._sizeHeight = sizeHeight

    def openCenter(self, width: int, height: int):

        x = (self._screenSize.width() - width)//2
        y = (self._screenSize.height() - height)//2
        self.setGeometry(x, y, width, height)

    def initRun(self, run: Callable):
        self._runButton = QPushButton("Run", self)
        self._runButton.setGeometry(
            self.center_x(
                self._sizeWidth,
                200
            ),
                200,
                200,
                200
        )
        
        self._runButton.setCheckable(True)
        self._runButton.toggled.connect(run)

    def center_x(self, parentWidth: int, width: int):
        return (parentWidth - width) // 2