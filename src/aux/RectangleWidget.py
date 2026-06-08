
import sys
import threading
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtCore import Qt, QMetaObject, Q_ARG, QGenericArgument
from PyQt6.QtGui import QRegion, QPainter, QBrush, QColor
 
BORDER = 3  # outline thickness in px
 
 
class RectOverlay(QWidget):
    def __init__(self, x1: int, y1: int, x2: int, y2: int):
        super().__init__()
 
        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint |
            Qt.WindowType.WindowStaysOnTopHint |
            Qt.WindowType.Tool
        )
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents)
 
        self.update_rect(x1, y1, x2, y2)
 
    def update_rect(self, x1: int, y1: int, x2: int, y2: int):
        """ Redraw the widget based on coordinates"""
        w = max(x2 - x1, BORDER * 2 + 1)
        h = max(y2 - y1, BORDER * 2 + 1)
        self.setGeometry(x1, y1, w, h)
        outer = QRegion(self.rect())
        inner = QRegion(BORDER, BORDER, w - BORDER * 2, h - BORDER * 2)
        self.setMask(outer.subtracted(inner))
        self.update()
 
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(Qt.PenStyle.NoPen)
        painter.setBrush(QBrush(QColor("darkCyan")))
        painter.drawRect(self.rect())
        painter.end()

