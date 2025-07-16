from PyQt5.QtWidgets import QApplication, QMainWindow

class view(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("AO Fisher")
        self.setGeometry(0, 0, 500, 500)