import sys

from PyQt5.QtWidgets import QApplication

from model import model
from view import view

class controller():
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def run(self):
        app = QApplication(sys.argv)
        self.view.show()
        sys.exit(app.exec_())
