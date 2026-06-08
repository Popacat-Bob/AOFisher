import sys
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPainter, QPixmap, QScreen
 
 
class ScreenshotOverlay(QWidget):
    def __init__(self):
        super().__init__()
 
        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint |
            Qt.WindowType.WindowStaysOnTopHint |
            Qt.WindowType.Tool
        )
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
 
        self._pixmap = self._take_screenshot()
 
        # Cover the full screen
        screen = QApplication.primaryScreen().geometry()
        self.setGeometry(screen)
 
    def _take_screenshot(self) -> QPixmap:
        screen: QScreen = QApplication.primaryScreen()
        return screen.grabWindow(0)
 
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(0, 0, self._pixmap)
        painter.end()
 
    def refresh(self):
        """Retake the screenshot and redraw."""
        self._pixmap = self._take_screenshot()
        self.update()
 
 
if __name__ == "__main__":
    app = QApplication(sys.argv)
    overlay = ScreenshotOverlay()
    overlay.show()
    print("Screenshot overlay active. Ctrl+C to quit.")
    sys.exit(app.exec())

