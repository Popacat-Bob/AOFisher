from PyQt5.QtWidgets import QMainWindow, QLabel, QPushButton, QLineEdit, QHBoxLayout, QWidget, QMessageBox
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

    def RTextBox(self, func: Callable):
        self._RTextBox = QLineEdit()
        self._RTextBox.textEdited.connect(Callable)

    def RunButton(self, run: Callable):
        self._runButton = QPushButton("Run", self)
        x = self.center_x(self._sizeWidth, 800)
        self._runButton.setGeometry(
            x,
            375,
            800,
            100
        )

        self._runButton.setCheckable(True)
        self._runButton.toggled.connect(run)

    def invalidColorPrompt(self, text: str):
        msg = QMessageBox()
        msg.setWindowTitle("Moron Alert")
        msg.setText(f'Inputted RGB Value: {text} is not a fucking RGB Value')
        msg.setIcon(QMessageBox.Critical)
        msg.setStandardButtons(QMessageBox.Ok)
        result = msg.exec_()

    def openCenter(self, width: int, height: int):
        x = (self._screenSize.width() - width)//2
        y = (self._screenSize.height() - height)//2
        self.setGeometry(x, y, width, height)

    def center_x(self, parentWidth: int, width: int):
        return (parentWidth - width) // 2
    
    def center_y(self, parentHeight: int, height: int):
        return (parentHeight - height) // 2