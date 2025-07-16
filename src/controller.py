import sys
from PyQt5.QtWidgets import QApplication
from .model import model
from .view import view
from utils import switch
from typing import Callable

class controller:
    def __init__(self, model: model):
        self.model = model

    def run(self):
        app = QApplication(sys.argv)
        self.view = view(850, 500)
        self.initRun()
        self.view.show()
        sys.exit(app.exec_())

    def initRun(self):
        run = switch(self.gonnaRun)
        self.view.initRun(run.toggleRun)

    def gonnaRun(self):
        print("Running")


