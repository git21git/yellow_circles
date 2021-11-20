import random
import sys

from PyQt5 import uic
from PyQt5.QtCore import QPoint
from PyQt5.QtGui import QColor, QBrush, QPainter, QPen
from PyQt5.QtWidgets import QMainWindow, QApplication


class Example(QMainWindow):
    def __init__(self):
        super(Example, self).__init__()
        uic.loadUi('UI.ui', self)
        self.setFixedSize(800, 600)
        self.btn.clicked.connect(self.paint)
        self.setMouseTracking(True)
        self.flag = False

    def paint(self):
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            painter = QPainter()
            painter.begin(self)
            painter.setBrush(QBrush(QColor(255, 255, 100)))
            painter.setPen(QPen(QColor(255, 255, 100), 10))
            d = random.choice(range(10, 300))
            cx, cy = random.randrange(100, 700, 10), random.randrange(100, 500, 10)
            radius = d // 2
            painter.drawEllipse(QPoint(cx - radius, cy - radius), 2 * radius, 2 * radius)
            painter.end()


# будет выводить понятно ошибку
def expert_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    sys.__excepthook__ = expert_hook
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
