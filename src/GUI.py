import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout,
    QHBoxLayout, QPushButton, QLabel
)
from PyQt6.QtCore import Qt, QPropertyAnimation, QRect, pyqtProperty, QEasingCurve
from PyQt6.QtGui import QColor, QPainter, QBrush, QPen, QFont, QFontDatabase
from FishLoop import FishEventLoop
from RegionDrawEventHandler import RegionDrawEventHandle
from Structs import Rect
import threading

STYLE = """
QMainWindow, QWidget#central {
    background-color: #0d1b2a;
}
 
QLabel#title {
    color: #7ecfdb;
    font-size: 13px;
    letter-spacing: 4px;
}
 
QPushButton#selectBtn {
    background-color: transparent;
    color: #7ecfdb;
    border: 1px solid #2a5f6e;
    border-radius: 6px;
    padding: 12px 28px;
    font-size: 13px;
    letter-spacing: 2px;
}
QPushButton#selectBtn:hover {
    background-color: #162736;
    border-color: #7ecfdb;
    color: #b0e8f0;
}
QPushButton#selectBtn:pressed {
    background-color: #1e3a4a;
}
"""
 
 
class ToggleSwitch(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedSize(52, 28)
        self._checked = False
        self._thumb_x = 4
 
        self._anim = QPropertyAnimation(self, b"thumb_x", self)
        self._anim.setDuration(180)
        self._anim.setEasingCurve(QEasingCurve.Type.InOutQuad)
 
        self.setCursor(Qt.CursorShape.PointingHandCursor)
 
    def get_thumb_x(self):
        return self._thumb_x
 
    def set_thumb_x(self, value):
        self._thumb_x = value
        self.update()
 
    thumb_x = pyqtProperty(int, get_thumb_x, set_thumb_x)
 
    def isChecked(self):
        return self._checked
 
    def mousePressEvent(self, event):
        self._checked = not self._checked
        end = 26 if self._checked else 4
        self._anim.setStartValue(self._thumb_x)
        self._anim.setEndValue(end)
        self._anim.start()
 
    def paintEvent(self, event):
        p = QPainter(self)
        p.setRenderHint(QPainter.RenderHint.Antialiasing)
 
        # Track
        track_color = QColor("#2a7a8a") if self._checked else QColor("#1e3040")
        p.setBrush(QBrush(track_color))
        p.setPen(QPen(QColor("#2a5f6e"), 1))
        p.drawRoundedRect(0, 4, 52, 20, 10, 10)
 
        # Thumb
        thumb_color = QColor("#7ecfdb") if self._checked else QColor("#3a6070")
        p.setBrush(QBrush(thumb_color))
        p.setPen(Qt.PenStyle.NoPen)
        p.drawEllipse(self._thumb_x, 2, 24, 24)
        p.end()
 
 
class MainWindow(QMainWindow):
    def __init__(self, LoopManger: FishEventLoop, RegionManager: RegionDrawEventHandle):
        super().__init__()
        self.setWindowTitle("Fish Bot")
        self.setFixedSize(320, 200)
        self.setStyleSheet(STYLE)
 
        central = QWidget()
        central.setObjectName("central")
        self.setCentralWidget(central)
 
        layout = QVBoxLayout(central)
        layout.setContentsMargins(36, 32, 36, 32)
        layout.setSpacing(28)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
 
        # Title
        title = QLabel("FISH BOT")
        title.setObjectName("title")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title)
 
        # Button
        self.select_btn = QPushButton("SELECT PROMPT REGION")
        self.select_btn.setObjectName("selectBtn")
        self.select_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        self.select_btn.clicked.connect(self.on_select)
        layout.addWidget(self.select_btn)
 
        # Switch row
        switch_row = QHBoxLayout()
        switch_row.setSpacing(12)
        switch_row.setAlignment(Qt.AlignmentFlag.AlignCenter)
 
        switch_label = QLabel("START FISHING")
        switch_label.setStyleSheet("color: #4a8a96; font-size: 11px; letter-spacing: 2px;")
 
        self.toggle = ToggleSwitch()
        self.toggle.mousePressEvent = self.on_toggle_click
 
        switch_row.addWidget(switch_label)
        switch_row.addWidget(self.toggle)
        layout.addLayout(switch_row)

        self.loopManager = LoopManger 
        self.regionManager = RegionManager
 

    def on_select(self):
        self.regionManager.start()
        rect = Rect(self.regionManager.RegionDrawEvent.x0,
                         self.regionManager.RegionDrawEvent.y0,
                         self.regionManager.RegionDrawEvent.x1,
                         self.regionManager.RegionDrawEvent.y1)
        self.loopManager.set_rect(rect)

    def on_toggle_click(self, event):
        ToggleSwitch.mousePressEvent(self.toggle, event)
        if self.toggle.isChecked():
            self.loopManager.set_is_fishing(True)
            self.fishing_thread = threading.Thread(target = self.loopManager.start, daemon=True)
            self.fishing_thread.start()
        else: 
            self.loopManager.set_is_fishing(False)


