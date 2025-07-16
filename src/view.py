from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QIcon

class view(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("AO Fisher")
        self.setGeometry(0, 0, 500, 500)
        self.setWindowIcon(QIcon('icons/fish.png'))