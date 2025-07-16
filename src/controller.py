import sys
from PyQt5.QtWidgets import QApplication
from .model import model
from .view import view
from .utils import switch 
from typing import Callable

class controller:
    def __init__(self, model: model):
        self.model = model

    def run(self):
        app = QApplication(sys.argv)
        self.view = view(850, 500)
        self.initRun()
        self.view.rgbEditor(self.gonnaRun)
        self.view.show()
        sys.exit(app.exec_())

    def initRun(self):
        self._runApp = switch(self.model.run)
        self.view.RunButton(self._runApp.toggleRun)

    def gonnaRun(self):
        print("running")


