import sys
from PyQt5.QtWidgets import QApplication
from .model import model
from .view import view

class controller:
    def __init__(self, model: model):
        self.model = model

    def run(self):
        app = QApplication(sys.argv)
        View = view(850, 500)
        View.initRun(self.gonnaRun)
        View.show()
        sys.exit(app.exec_())

    def gonnaRun(self):
        print("Running")
