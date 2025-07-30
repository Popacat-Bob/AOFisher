import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt
from .model import model
from .view import view
from .utils import switch, mouseScreenCaptureModel, getColorAtMouseModel
from typing import Callable
import json

class controller:
    def __init__(self, model: model):
        self.model = model

    def run(self):
        app = QApplication(sys.argv)
        self.view = view(850, 500)
        self.view.RGBSection((self.changeRColor, 
                              self.changeGColor, 
                              self.changeBColor
                              ), tuple(map(str, self.model.color)))
        
        self.view.ScanConfigSection(
            self.changeScanDelay,
            str(self.model.scanDelay)
                                    )
        
        self.view.ClickConfigSection(
            self.changeClickDelay,
            str(self.model.clickDelay)
        )

        self.view.FishDelaySection(
            self.changeFishDelay,
            str(self.model.postFishDelay)
        )

        self.view.ClicksNumberSection(
            self.changeClicks,
            str(self.model.clicks)
        )

        self.view.TopLeftConfig(
            (self.changeLeft, self.changeTop),
            tuple(map(str, self.model.colorCapture.topLeft))
        )

        self.view.BotRightConfig(
            (self.changeRight, self.changeBottom),
            tuple(map(str, self.model.colorCapture.botRight))
        )

        self.view.ToleranceSetting(
            self.changeTolerance,
            str(self.model.colorCapture.tolerance)
        )


        self.view.SelectRegionButton(self.getRegion)

        self.view.timeEatIntervalSection(self.setTimeEatInterval, str(self.model.timeEatInterval))

        self.view.resetDurationSection(self.setResetDuration, str(self.model.resetDuration))

        self.view.captureColorButton(
            self.setRGB
        )


        self.initRun()
        self.view.keyRunTrigger()

        self.view.installEventFilter(self.view)
        self.view.setWindowFlag(Qt.WindowStaysOnTopHint)
        self.view.show()
        sys.exit(app.exec_())
    
    def initRun(self):
        self._runApp = switch(self.model.run)

        def toggle(checked: bool):
            self._runApp.toggleRun(checked)
            self.model.setRunning(checked)

            if checked: self.view.onRunButton()
            else: self.view.offRunButton()


        self.view.RunButton(toggle)
    
    def setTimeEatInterval(self, TimeEatInterval: str):

        try:
            
            TimeEatInterval = int(TimeEatInterval)
            with open('data/config.json', 'r') as f:
                data = json.load(f)

            data['FisherModelSettings']['time_eat_interval'] = TimeEatInterval

            with open('data/config.json', 'w') as f:
                json.dump(data, f, indent = 4)

            self.model.setTimeEatInterval(TimeEatInterval)

        #ADD AN ACTUAL HANDLER TO THIS
        except Exception as e:
            print(e)

    def setResetDuration(self, resetDuration: str):

        try:
            resetDuration = int(resetDuration)
            
            with open('data/config.json', 'r') as f:
                data = json.load(f)

            data['FisherModelSettings']['reset_duration'] = resetDuration

            with open('data/config.json', 'w') as f:
                json.dump(data, f, indent = 4)

            self.model.setResetDuration(resetDuration)

        #ADD AN ACTUAL HANDLER TO THIS
        except Exception as e:
            print(e)

    def setRGB(self):

        try:
            color = getColorAtMouseModel().capture()

            with open('data/config.json', 'r') as f:
                data = json.load(f)

            data['FisherModelSettings']['color'] = color

            with open('data/config.json', 'w') as f:
                json.dump(data, f)

            self.model.setColor(color)
            self.view.changeRTextBox(str(color[0]))
            self.view.changeGTextBox(str(color[1]))
            self.view.changeBTextBox(str(color[2]))

        #ADD AN ACTUAL HANDLER TO THIS
        except:
            pass

    def getRegion(self):

        try:
            topLeft, botRight = mouseScreenCaptureModel().capture()

            with open('data/config.json', 'r') as f:
                data = json.load(f)

            data['ColorCaptureSettings']['topLeft'] = topLeft
            data['ColorCaptureSettings']['bottomRight'] = botRight

            with open('data/config.json', 'w') as f:
                json.dump(data, f, indent=4)

            self.model.colorCapture.setTopLeft(topLeft)
            self.model.colorCapture.setBotRight(botRight)

            self.view.changeLeftTextDisplay(str(topLeft[0]))
            self.view.changeTopTextDisplay(str(topLeft[1]))
            self.view.changeRightTextDisplay(str(botRight[0]))
            self.view.changeBottomTextDisplay(str(botRight[1]))

        except:
            pass

    def changeTolerance(self, tolerance: str):
        
        try:

            tolerance = int(tolerance)
            with open('data/config.json', 'r') as f:
                data = json.load(f)

            data['ColorCaptureSettings']['tolerance']= tolerance

            with open('data/config.json', 'w') as f:
                json.dump(data, f, indent=4)

            self.model.colorCapture.setTolerance(tolerance)

        except Exception as e:
            self.view.invalidIntPrompt(tolerance)
            print(e)

    def changeBottom(self, y: str):

        try:
            y = int(y)
            with open('data/config.json', 'r') as f:
                data = json.load(f)

            data['ColorCaptureSettings']['bottomRight'][1] = y

            with open('data/config.json', 'w') as f:
                json.dump(data, f, indent=4)

            self.model.colorCapture.setTopLeft(tuple(data['ColorCaptureSettings']['bottomRight']))

        except Exception as e:
            self.view.invalidIntPrompt(y)

    def changeRight(self, x: str):
        
        try:
            x = int(x)
            with open('data/config.json', 'r') as f:
                data = json.load(f)

            data['ColorCaptureSettings']['bottomRight'][0] = x

            with open('data/config.json', 'w') as f:
                json.dump(data, f, indent=4)

            self.model.colorCapture.setTopLeft(tuple(data['ColorCaptureSettings']['bottomRight']))

        except Exception as e:
            self.view.invalidIntPrompt(x)

    def changeTop(self, y: str):
        
        try:
            y = int(y)
            with open('data/config.json', 'r') as f:
                data = json.load(f)

            data['ColorCaptureSettings']['topLeft'][1] = y

            with open('data/config.json', 'w') as f:
                json.dump(data, f, indent=4)

            self.model.colorCapture.setTopLeft(tuple(data['ColorCaptureSettings']['topLeft']))

        except Exception as e:
            self.view.invalidIntPrompt(y)

    def changeLeft(self, x: str):
        
        try:
            x = int(x)
            with open('data/config.json', 'r') as f:
                data = json.load(f)

            data['ColorCaptureSettings']['topLeft'][0] = x

            with open('data/config.json', 'w') as f:
                json.dump(data, f, indent=4)

            self.model.colorCapture.setTopLeft(tuple(data['ColorCaptureSettings']['topLeft']))

        except Exception as e:
            self.view.invalidIntPrompt(x)
    
    def changeClicks(self, clicks: str):

        try:
            clicks = int(clicks)
            with open('data/config.json', 'r') as f:
                data = json.load(f)

            data['FisherModelSettings']['clicks'] = clicks

            with open('data/config.json', 'w') as f:
                json.dump(data, f, indent=4)

            self.model.setClicks(clicks)

        except Exception as e:
            self.view.invalidIntPrompt(clicks)

    def changeClickDelay(self, delay: str):

        try:
            delay = float(delay)
            with open('data/config.json', 'r') as f:
                data = json.load(f)

            data['FisherModelSettings']['click_delay'] = delay

            with open('data/config.json', 'w') as f:
                json.dump(data, f, indent=4)

            self.model.setClickDelay(delay)

        except Exception as e:
            self.view.invalidFloatPrompt(delay)

    def changeFishDelay(self, delay: str): 

        try:
            delay = float(delay)
            with open('data/config.json', 'r') as f:
                data = json.load(f)

            data['FisherModelSettings']['post_fish_delay'] = delay

            with open('data/config.json', 'w') as f:
                json.dump(data, f, indent=4)

            self.model.setPostFishDelay(delay)

        except Exception as e:
            self.view.invalidFloatPrompt(delay)

    def changeScanDelay(self, delay: str): 

        try:
            delay = float(delay)
            with open('data/config.json', 'r') as f:
                data = json.load(f)

            data['FisherModelSettings']['scan_delay'] = delay

            with open('data/config.json', 'w') as f:
                json.dump(data, f, indent=4)

            self.model.setScanDelay(delay)

        except Exception as e:
            self.view.invalidFloatPrompt(delay)

    def changeRColor(self, color: str):

        try:
            RCol = int(color)
            with open('data/config.json', 'r') as f:
                data = json.load(f)

            data['FisherModelSettings']['color'][0] = RCol
            with open('data/config.json', 'w') as f:
                json.dump(data, f, indent=4)

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
                json.dump(data, f, indent=4)

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
                json.dump(data, f, indent=4)

            colorR = data['FisherModelSettings']['color'][0]
            colorG = data['FisherModelSettings']['color'][1]
            colorB = BCol

            self.model.setColor((colorR, colorG, colorB))

        except:
            self.view.invalidColorPrompt(color)

    def gonnaRun(self):
        print("running")


