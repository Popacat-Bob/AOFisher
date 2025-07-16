from PyQt5.QtWidgets import QMainWindow, QLabel
from PyQt5.QtGui import QIcon, QFont, QGuiApplication

class view(QMainWindow):
    def __init__(self, sizeWidth: int, sizeHeight: int):
        
        super().__init__()
        self._screenSize = QGuiApplication.primaryScreen().size()
        self.setWindowTitle("AO Fisher")
        self.openCenter(sizeWidth, sizeHeight)
        self.setWindowIcon(QIcon('icons/fish.png'))

    def openCenter(self, width: int, height: int):

        x = (self._screenSize.width() - width)//2
        y = (self._screenSize.height() - height)//2
        self.setGeometry(x, y, width, height)
