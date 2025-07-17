import sys
from PyQt5.QtWidgets import QApplication
from .model import model
from .view import view
from .utils import switch 
from typing import Callable
import json

class controller:
    def __init__(self, model: model):
        self.model = model

    def run(self):
        app = QApplication(sys.argv)
        self.view = view(850, 500)
        self.initRun()
        self.view.RGBSection((self.changeRColor, 
                              self.changeGColor, 
                              self.changeBColor
                              ))
        self.view.show()
        sys.exit(app.exec_())

    def initRun(self):
        self._runApp = switch(self.model.run)
        self.view.RunButton(self._runApp.toggleRun)

    def changeRColor(self, color: str):

        try:
            RCol = int(color)
            with open('data/config.json', 'r') as f:
                data = json.load(f)

            data['FisherModelSettings']['color'][0] = RCol
            with open('data/config.json', 'w') as f:
                json.dump(data, f, indent=2)

            colorR = RCol
            colorG = data['FisherModelSettings']['color'][1]
            colorB = data['FisherModelSettings']['color'][2]

            self.model.setColor((colorR, colorG, colorB))

        except:
            self.view.invalidColorPrompt(color)

    def changeGColor(self, color: str):

        try:
            GCol = int(color)
            with open('data/config.json', 'r') as f:
                data = json.load(f)

            data['FisherModelSettings']['color'][1] = GCol
            with open('data/config.json', 'w') as f:
                json.dump(data, f, indent=2)

            colorR = data['FisherModelSettings']['color'][0]
            colorG = GCol
            colorB = data['FisherModelSettings']['color'][2]

            self.model.setColor((colorR, colorG, colorB))

        except:
            self.view.invalidColorPrompt(color)

    def changeBColor(self, color: str):

        try:
            BCol = int(color)
            with open('data/config.json', 'r') as f:
                data = json.load(f)

            data['FisherModelSettings']['color'][2] = BCol
            with open('data/config.json', 'w') as f:
                json.dump(data, f, indent=2)

            colorR = data['FisherModelSettings']['color'][0]
            colorG = data['FisherModelSettings']['color'][1]
            colorB = BCol

            self.model.setColor((colorR, colorG, colorB))

        except:
            self.view.invalidColorPrompt(color)

    def gonnaRun(self):
        print("running")


