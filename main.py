import random
import sys

from PyQt5 import uic
from PyQt5.QtGui import QPaintEvent, QPainter, QColor
from PyQt5.QtWidgets import QColorDialog, QApplication, QMainWindow


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("Ui.ui", self)
        self.painting = False
        self.pushButton.clicked.connect(self.startPaint)

    def startPaint(self):
        self.painting = True
        self.update()

    def paintEvent(self, event: QPaintEvent):
        if self.painting:
            paint = QPainter()
            paint.begin(self)
            self.draw(paint)
            paint.end()
            self.painting = False

    def draw(self, qp: QPainter):
        qp.setBrush(QColor(255, 255, 0))
        a = random.randint(1, 300)
        qp.drawEllipse(300, 200, a, a)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    wndw = Window()
    wndw.show()
    app.exec()
