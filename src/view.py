from PyQt5.QtWidgets import QMainWindow, QLabel, QPushButton, QLineEdit, QHBoxLayout, QWidget, QMessageBox, QVBoxLayout, \
    QSizePolicy, QTabWidget
from PyQt5.QtGui import QIcon, QFont, QGuiApplication
from typing import Callable
from pynput import keyboard

class view(QMainWindow):
    def __init__(self, sizeWidth: int, sizeHeight: int):
        
        super().__init__()
        self._screenSize = QGuiApplication.primaryScreen().size()
        self.setWindowTitle("AO Fisher")

        self.openCenter(sizeWidth, sizeHeight)
        self.setWindowIcon(QIcon('icons/fish.png'))

        self._sizeWidth = sizeWidth
        self._sizeHeight = sizeHeight
        
        self._fishingLayout = QVBoxLayout()
        self._fishingLayout.setSpacing(0)
        self._fishingLayout.setContentsMargins(0, 0, 0, 0)
        self._fishingWidget = QWidget()
        self._fishingWidget.setLayout(self._fishingLayout)

        self._regionLayout = QVBoxLayout()
        self._regionLayout.setSpacing(0)
        self._regionLayout.setContentsMargins(0, 0, 0, 0)
        self._regionWidget = QWidget()
        self._regionWidget.setLayout(self._regionLayout)

        self._miscLayout = QVBoxLayout()
        self._miscLayout.setSpacing(0)
        self._miscLayout.setContentsMargins(0, 0, 0, 0)
        self._miscWidget = QWidget()
        self._miscWidget.setLayout(self._miscLayout)

        tabs = QTabWidget()
        tabs.addTab(self._fishingWidget, "Fishing")
        tabs.addTab(self._miscWidget, "Misc")
        tabs.addTab(self._regionWidget, "Region")

        layout = QHBoxLayout()
        layout.addWidget(tabs)

        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)

        centralWidget.setLayout(layout)

    def ToleranceSettingNotify(self, func: Callable, current: str):

        ToleranceLayout = QHBoxLayout()
        ToleranceLabel = QLabel("Tolerance")
        ToleranceTextBox = QLineEdit(current)

        ToleranceTextBox.returnPressed.connect(lambda: func(ToleranceTextBox.text()))

        ToleranceLayout.addWidget(ToleranceLabel)
        ToleranceLayout.addWidget(ToleranceTextBox)

        ToleranceWidget = QWidget()
        ToleranceWidget.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        ToleranceWidget.setLayout(ToleranceLayout)
        self._RGBLayoutNotify.addWidget(ToleranceWidget)

    def RGBSectionNotify(self, funcs: tuple[Callable[[str], None], ...], currents: tuple[str, ...]):

        self._RGBLayoutNotify = QHBoxLayout()
        RGBLabel = QLabel("RGB (Notify)", self)

        self._RTextBoxNotify = QLineEdit(currents[0])
        self._RTextBoxNotify.returnPressed.connect(lambda: funcs[0](self._RTextBoxNotify.text()))

        self._GTextBoxNotify= QLineEdit(currents[1])
        self._GTextBoxNotify.returnPressed.connect(lambda: funcs[1](self._GTextBoxNotify.text()))

        self._BTextBoxNotify= QLineEdit(currents[2])
        self._BTextBoxNotify.returnPressed.connect(lambda: funcs[2](self._BTextBoxNotify.text()))

        self._RGBLayoutNotify.addWidget(RGBLabel)
        self._RGBLayoutNotify.addWidget(self._RTextBoxNotify)
        self._RGBLayoutNotify.addWidget(self._GTextBoxNotify)
        self._RGBLayoutNotify.addWidget(self._BTextBoxNotify)

        rgbWidget = QWidget()
        rgbWidget.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        rgbWidget.setLayout(self._RGBLayoutNotify)
        self._fishingLayout.addWidget(rgbWidget)

    def captureColorButtonNotify(self, func: Callable):

        CaptureColorButton = QPushButton("Capture Color")
        CaptureColorButton.clicked.connect(func)

        self._RGBLayoutNotify.addWidget(CaptureColorButton)

    def changeRTextBoxNotify(self, new: str):
        self._RTextBoxNotify.setText(new)

    def changeGTextBoxNotify(self, new: str):
        self._GTextBoxNotify.setText(new)

    def changeBTextBoxNotify(self, new: str):
        self._BTextBoxNotify.setText(new)

    def TopLeftConfigNotify(self, funcs: tuple[Callable[[str], None], ...], currents: tuple[str, ...]):

        TopfishingLayout = QHBoxLayout()

        TopleftLabel = QLabel("Top Left")
        self._LeftTextBoxNotify = QLineEdit(currents[0])
        self._TopTextBoxNotify = QLineEdit(currents[1])

        self._LeftTextBoxNotify.returnPressed.connect(lambda: funcs[0](self._LeftTextBoxNotify.text()))
        self._TopTextBoxNotify.returnPressed.connect(lambda: funcs[1](self._TopTextBoxNotify.text()))

        TopfishingLayout.addWidget(TopleftLabel)
        TopfishingLayout.addWidget(self._LeftTextBoxNotify)
        TopfishingLayout.addWidget(self._TopTextBoxNotify)

        TopleftWidget = QWidget()
        TopleftWidget.setLayout(TopfishingLayout)
        TopleftWidget.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        self._regionLayout.addWidget(TopleftWidget)

    def changeLeftTextNotify(self, text: str):
        self._LeftTextBoxNotify.setText(text)

    def changeTopTextNotify(self, text: str):
        self._TopTextBoxNotify.setText(text)

    def BotRightConfigNotify(self, funcs: tuple[Callable[[str], None], ...], currents: tuple[str, ...]):

        BotmiscLayout = QHBoxLayout()

        BotrightLabel = QLabel("Bottom Right")
        self._RightTextBoxNotify = QLineEdit(currents[0])
        self._BottomTextBoxNotify = QLineEdit(currents[1])

        self._RightTextBoxNotify.returnPressed.connect(lambda: funcs[0](self._RightTextBoxNotify.text()))
        self._BottomTextBoxNotify.returnPressed.connect(lambda: funcs[1](self._BottomTextBoxNotify.text()))

        BotmiscLayout.addWidget(BotrightLabel)
        BotmiscLayout.addWidget(self._RightTextBoxNotify)
        BotmiscLayout.addWidget(self._BottomTextBoxNotify)

        BotrightWidget = QWidget()
        BotrightWidget.setLayout(BotmiscLayout)
        BotrightWidget.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        self._regionLayout.addWidget(BotrightWidget)

    def changeRightTextNotify(self, text: str):
        self._RightTextBoxNotify.setText(text)

    def changeBotTextNotify(self, text: str):
        self._BottomTextBoxNotify.setText(text)

    def SelectRegionButtonNotify(self, func: Callable):

        SelectRegionButton = QPushButton("Select rectangular region (Notify)")
        SelectRegionButton.clicked.connect(func)

        self._regionLayout.addWidget(SelectRegionButton)

    def brewSection(self, func: Callable, func_1: Callable[[str], None], current: str):

        brewSectionLayout = QHBoxLayout()
        brewSectionLabel = QLabel("Brew settings\n Place brew at slot 8")

        brewEatIntervalLine = QLineEdit(current)
        self._brewEatButton = QPushButton('Start eating brew (H)')
        self._brewEatButton.setCheckable(True)

        brewEatIntervalLine.returnPressed.connect(lambda: func_1(brewEatIntervalLine.text()))
        self._brewEatButton.toggled.connect(func)

        brewSectionLayout.addWidget(brewSectionLabel)
        brewSectionLayout.addWidget(brewEatIntervalLine)
        brewSectionLayout.addWidget(self._brewEatButton)

        brewSectionWidget = QWidget()
        brewSectionWidget.setLayout(brewSectionLayout)
        brewSectionWidget.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)

        self._miscLayout.addWidget(brewSectionWidget)

    def onBrewButton(self):
        self._brewEatButton.setText("Stop eating brew (H)")
        self._brewEatButton.setStyleSheet("background-color: green")

    def offBrewButton(self):
        self._brewEatButton.setText("Start eating brew (H)")
        self._brewEatButton.setStyleSheet("background-color: gray")

    def timeEatIntervalSection(self, func: Callable[[str], None], current: str):

        timeEatIntervalLayout = QHBoxLayout()
        timeEatIntervalLabel = QLabel("Eat Intervals\nPlace food at slot 9")
        timeEatIntervalLine = QLineEdit(current)

        timeEatIntervalLine.returnPressed.connect(lambda: func(timeEatIntervalLine.text()))

        timeEatIntervalLayout.addWidget(timeEatIntervalLabel)
        timeEatIntervalLayout.addWidget(timeEatIntervalLine)

        timeEatIntervalWidget = QWidget()
        timeEatIntervalWidget.setLayout(timeEatIntervalLayout)
        timeEatIntervalWidget.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        self._miscLayout.addWidget(timeEatIntervalWidget)

    def captureColorButton(self, func: Callable):

        CaptureColorButton = QPushButton("Capture Color")
        CaptureColorButton.clicked.connect(func)

        self._RGBLayout.addWidget(CaptureColorButton)

    def keyRunTrigger(self):

        def on_press(key):
            try:
                if key.char.lower() == 'y':
                    self._RunButton.toggle()

                if key.char.lower() == 'h':
                    self._brewEatButton.toggle()
            except:
                pass

        self.listener = keyboard.Listener(on_press=on_press)
        self.listener.start()

    def onRunButton(self):
        self._RunButton.setText("Stop Fishing (Y)")
        self._RunButton.setStyleSheet("background-color: green")

    def offRunButton(self):
        self._RunButton.setText("Start Fishing (Y)")
        self._RunButton.setStyleSheet("background-color: gray")

    def RunButton(self, func: Callable):
        
        self._RunButton = QPushButton("Start Fishing (Y)")
        self._RunButton.setCheckable(True)

        self._RunButton.toggled.connect(func)

        self._fishingLayout.addWidget(self._RunButton)


    def SelectRegionButtonPrompt(self, func: Callable):
        
        SelectRegionButton = QPushButton("Select rectangular region (Prompt)")
        SelectRegionButton.clicked.connect(func)
        
        self._regionLayout.addWidget(SelectRegionButton)
        
    def ToleranceSetting(self, func: Callable, current: str):
        
        ToleranceLayout = QHBoxLayout()
        ToleranceLabel = QLabel("Tolerance")
        ToleranceTextBox = QLineEdit(current)

        ToleranceTextBox.returnPressed.connect(lambda: func(ToleranceTextBox.text()))

        ToleranceLayout.addWidget(ToleranceLabel)
        ToleranceLayout.addWidget(ToleranceTextBox)

        ToleranceWidget = QWidget()
        ToleranceWidget.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        ToleranceWidget.setLayout(ToleranceLayout)
        self._RGBLayout.addWidget(ToleranceWidget)

    def ClicksNumberSection(self, func: Callable, current: str):

        ClicksLayout = QHBoxLayout()
        ClicksLabel = QLabel("Clicks")
        ClicksTextBox = QLineEdit(current)
        ClicksTextBox.returnPressed.connect(lambda: func(ClicksTextBox.text()))

        ClicksLayout.addWidget(ClicksLabel)
        ClicksLayout.addWidget(ClicksTextBox)

        ClicksWidget = QWidget()
        ClicksWidget.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        ClicksWidget.setLayout(ClicksLayout)
        self._fishingLayout.addWidget(ClicksWidget)

    def BotRightConfig(self, funcs: tuple[Callable[[str], None], ...], currents: tuple[str, ...]):

        BotmiscLayout = QHBoxLayout()

        BotrightLabel = QLabel("Bottom Right")
        self._RightTextBox = QLineEdit(currents[0])
        self._BottomTextBox = QLineEdit(currents[1])

        self._RightTextBox.returnPressed.connect(lambda: funcs[0](self._RightTextBox.text()))
        self._BottomTextBox.returnPressed.connect(lambda: funcs[1](self._BottomTextBox.text()))
        
        BotmiscLayout.addWidget(BotrightLabel)
        BotmiscLayout.addWidget(self._RightTextBox)
        BotmiscLayout.addWidget(self._BottomTextBox)

        BotrightWidget = QWidget()
        BotrightWidget.setLayout(BotmiscLayout)
        BotrightWidget.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        self._regionLayout.addWidget(BotrightWidget)

    def changeBottomTextDisplay(self, new: str):
        self._BottomTextBox.setText(new)

    def changeRightTextDisplay(self, new: str):
        self._RightTextBox.setText(new)

    def TopLeftConfig(self, funcs: tuple[Callable[[str], None], ...], currents: tuple[str, ...]):

        TopfishingLayout = QHBoxLayout()

        TopleftLabel = QLabel("Top Left")
        self._LeftTextBox = QLineEdit(currents[0])
        self._TopTextBox = QLineEdit(currents[1])

        self._LeftTextBox.returnPressed.connect(lambda: funcs[0](self._LeftTextBox.text()))
        self._TopTextBox.returnPressed.connect(lambda: funcs[1](self._TopTextBox.text()))

        TopfishingLayout.addWidget(TopleftLabel)
        TopfishingLayout.addWidget(self._LeftTextBox)
        TopfishingLayout.addWidget(self._TopTextBox)

        TopleftWidget = QWidget()
        TopleftWidget.setLayout(TopfishingLayout)
        TopleftWidget.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        self._regionLayout.addWidget(TopleftWidget)

    def changeTopTextDisplay(self, new: str):
        self._TopTextBox.setText(new)

    def changeLeftTextDisplay(self, new: str):
        self._LeftTextBox.setText(new)


    def FishDelaySection(self, func: Callable, current: str):

        FishLayout = QHBoxLayout()
        FishLabel = QLabel("Fish Delay")
        FishTextBox = QLineEdit(current)
        FishTextBox.returnPressed.connect(lambda: func(FishTextBox.text()))

        FishLayout.addWidget(FishLabel)
        FishLayout.addWidget(FishTextBox)

        FishWidget = QWidget()
        FishWidget.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        FishWidget.setLayout(FishLayout)
        self._fishingLayout.addWidget(FishWidget)

    def ClickConfigSection(self, func: Callable, current: str):
        ClickLayout = QHBoxLayout()
        ClickLabel = QLabel("Click Delay")
        ClickTextBox = QLineEdit(current)
        ClickTextBox.returnPressed.connect(lambda: func(ClickTextBox.text()))

        ClickLayout.addWidget(ClickLabel)
        ClickLayout.addWidget(ClickTextBox)

        ClickWidget = QWidget()
        ClickWidget.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        ClickWidget.setLayout(ClickLayout)
        self._fishingLayout.addWidget(ClickWidget)

    def ScanConfigSection(self, func: Callable, current: str): 

        ScanLayout = QHBoxLayout()
        ScanLabel = QLabel("Scan Delay")
        ScanTextBox = QLineEdit(current)
        ScanTextBox.returnPressed.connect(lambda: func(ScanTextBox.text()))

        ScanLayout.addWidget(ScanLabel)
        ScanLayout.addWidget(ScanTextBox)

        ScanWidget = QWidget()
        ScanWidget.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        ScanWidget.setLayout(ScanLayout)
        self._fishingLayout.addWidget(ScanWidget)
        
    def resetDurationSection(self, func: Callable, current: str):

        resetDurationLayout = QHBoxLayout()

        resetDurationLabel = QLabel("Reset Delay")
        resetDurationBox = QLineEdit(current)

        resetDurationLayout.addWidget(resetDurationLabel)
        resetDurationLayout.addWidget(resetDurationBox)

        resetDurationBox.returnPressed.connect(lambda: func(resetDurationBox.text()))

        resetDurationWidget = QWidget()
        resetDurationWidget.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        resetDurationWidget.setLayout(resetDurationLayout)
        self._fishingLayout.addWidget(resetDurationWidget)


    def RGBSection(self, funcs: tuple[Callable[[str], None], ...], currents: tuple[str, ...]):
        
        self._RGBLayout = QHBoxLayout()
        RGBLabel = QLabel("RGB (Prompt)", self)

        self._RTextBox = QLineEdit(currents[0])
        self._RTextBox.returnPressed.connect(lambda: funcs[0](self._RTextBox.text()))

        self._GTextBox = QLineEdit(currents[1])
        self._GTextBox.returnPressed.connect(lambda: funcs[1](self._GTextBox.text()))

        self._BTextBox = QLineEdit(currents[2])
        self._BTextBox.returnPressed.connect(lambda: funcs[2](self._BTextBox.text()))

        self._RGBLayout.addWidget(RGBLabel)
        self._RGBLayout.addWidget(self._RTextBox)
        self._RGBLayout.addWidget(self._GTextBox)
        self._RGBLayout.addWidget(self._BTextBox)

        rgbWidget = QWidget()
        rgbWidget.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        rgbWidget.setLayout(self._RGBLayout)
        self._fishingLayout.addWidget(rgbWidget)

    def changeRTextBox(self, new: str):
        self._RTextBox.setText(new)

    def changeGTextBox(self, new: str):
        self._GTextBox.setText(new)

    def changeBTextBox(self, new: str):
        self._BTextBox.setText(new)

    def invalidColorPrompt(self, text: str):
        msg = QMessageBox()
        msg.setWindowTitle("Moron Alert")
        msg.setText(f'Inputted RGB Value: {text} is not a fucking RGB Value')
        msg.setIcon(QMessageBox.Critical)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    def invalidFloatPrompt(self, text: str):
        msg = QMessageBox()
        msg.setWindowTitle("Moron Alert")
        msg.setText(f'Inputted value: {text} is not a fucking float')
        msg.setIcon(QMessageBox.Critical)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    def invalidIntPrompt(self, text: str):
        msg = QMessageBox()
        msg.setWindowTitle("Moron Alert")
        msg.setText(f'Inputted value: {text} is not a fucking int')
        msg.setIcon(QMessageBox.Critical)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()


    def openCenter(self, width: int, height: int):
        x = (self._screenSize.width() - width)//2
        y = (self._screenSize.height() - height)//2
        self.setGeometry(x, y, width, height)
