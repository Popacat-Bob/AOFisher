from PyQt5.QtWidgets import QMainWindow, QLabel, QPushButton, QLineEdit, QHBoxLayout, QWidget, QMessageBox, QVBoxLayout, QSizePolicy
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
        
        self._leftLayout = QVBoxLayout()
        self._leftLayout.setSpacing(0)
        self._leftLayout.setContentsMargins(0, 0, 0, 0)
        self._leftWidget = QWidget()
        self._leftWidget.setLayout(self._leftLayout)

        self._rightLayout = QVBoxLayout()
        self._rightLayout.setSpacing(0)
        self._rightLayout.setContentsMargins(0, 0, 0, 0)
        self._rightWidget = QWidget()
        self._rightWidget.setLayout(self._rightLayout)

        self._configLayout = QHBoxLayout()
        self._configLayout.addWidget(self._leftWidget)
        self._configLayout.addWidget(self._rightWidget)

        self._configWidget = QWidget()
        self._configWidget.setLayout(self._configLayout)

        self._mainLayout = QVBoxLayout()
        self._mainLayout.addWidget(self._configWidget)

        self._widget = QWidget()
        self._widget.setLayout(self._mainLayout)
        self.setCentralWidget(self._widget)
    
    def captureColorButton(self, func: Callable):

        CaptureColorButton = QPushButton("Capture Color")
        CaptureColorButton.clicked.connect(func)

        self._leftLayout.addWidget(CaptureColorButton)

    def onRunButton(self):
        self._RunButton.setText("Stop Fishing")
        self._RunButton.setStyleSheet("background-color: green")

    def offRunButton(self):
        self._RunButton.setText("Start Fishing")
        self._RunButton.setStyleSheet("background-color: gray")

    def RunButton(self, func: Callable):
        
        self._RunButton = QPushButton("Start Fishing")
        self._RunButton.setCheckable(True)

        self._RunButton.toggled.connect(func)

        self._mainLayout.addWidget(self._RunButton)


    def SelectRegionButton(self, func: Callable):
        
        SelectRegionButton = QPushButton("Select rectangular region")
        SelectRegionButton.clicked.connect(func)
        
        self._rightLayout.addWidget(SelectRegionButton)
        
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
        self._rightLayout.addWidget(ToleranceWidget)

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
        self._leftLayout.addWidget(ClicksWidget)

    def BotRightConfig(self, funcs: tuple[Callable], currents: tuple[str]): 

        BotrightLayout = QHBoxLayout()

        BotrightLabel = QLabel("Bottom Right")
        self._RightTextBox = QLineEdit(currents[0])
        self._BottomTextBox = QLineEdit(currents[1])

        self._RightTextBox.returnPressed.connect(lambda: funcs[0](self._RightTextBox.text()))
        self._BottomTextBox.returnPressed.connect(lambda: funcs[1](self._BottomTextBox.text()))
        
        BotrightLayout.addWidget(BotrightLabel)
        BotrightLayout.addWidget(self._RightTextBox)
        BotrightLayout.addWidget(self._BottomTextBox)

        BotrightWidget = QWidget()
        BotrightWidget.setLayout(BotrightLayout)
        BotrightWidget.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        self._rightLayout.addWidget(BotrightWidget)

    def changeBottomTextDisplay(self, new: str):
        self._BottomTextBox.setText(new)

    def changeRightTextDisplay(self, new: str):
        self._RightTextBox.setText(new)

    def TopLeftConfig(self, funcs: tuple[Callable], currents: tuple[str]): 

        TopleftLayout = QHBoxLayout()

        TopleftLabel = QLabel("Top Left")
        self._LeftTextBox = QLineEdit(currents[0])
        self._TopTextBox = QLineEdit(currents[1])

        self._LeftTextBox.returnPressed.connect(lambda: funcs[0](self._LeftTextBox.text()))
        self._TopTextBox.returnPressed.connect(lambda: funcs[1](self._TopTextBox.text()))

        TopleftLayout.addWidget(TopleftLabel)
        TopleftLayout.addWidget(self._LeftTextBox)
        TopleftLayout.addWidget(self._TopTextBox)

        TopleftWidget = QWidget()
        TopleftWidget.setLayout(TopleftLayout)
        TopleftWidget.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        self._rightLayout.addWidget(TopleftWidget)

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
        self._leftLayout.addWidget(FishWidget)

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
        self._leftLayout.addWidget(ClickWidget)

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
        self._leftLayout.addWidget(ScanWidget)
        

    def RGBSection(self, funcs: tuple[Callable], currents: tuple[str]): 
        
        RGBLayout = QHBoxLayout()
        RGBLabel = QLabel("RGB", self)

        self._RTextBox = QLineEdit(currents[0])
        self._RTextBox.returnPressed.connect(lambda: funcs[0](self._RTextBox.text()))

        self._GTextBox = QLineEdit(currents[1])
        self._GTextBox.returnPressed.connect(lambda: funcs[1](self._GTextBox.text()))

        self._BTextBox = QLineEdit(currents[2])
        self._BTextBox.returnPressed.connect(lambda: funcs[2](self._BTextBox.text()))

        RGBLayout.addWidget(RGBLabel)
        RGBLayout.addWidget(self._RTextBox)
        RGBLayout.addWidget(self._GTextBox)
        RGBLayout.addWidget(self._BTextBox)

        rgbWidget = QWidget()
        rgbWidget.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        rgbWidget.setLayout(RGBLayout)
        self._leftLayout.addWidget(rgbWidget)

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
