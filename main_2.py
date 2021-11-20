import random
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QPoint
from PyQt5.QtGui import QColor, QBrush, QPainter, QPen
from PyQt5.QtWidgets import QMainWindow, QApplication


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn = QtWidgets.QPushButton(self.centralwidget)
        self.btn.setGeometry(QtCore.QRect(350, 250, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn.setFont(font)
        self.btn.setDefault(True)
        self.btn.setObjectName("btn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Git и случайные окружности"))
        self.btn.setText(_translate("MainWindow", "Нажать"))


class Example(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Example, self).__init__()
        self.setupUi(self)
        self.setFixedSize(800, 600)
        self.btn.clicked.connect(self.paint)
        self.setMouseTracking(True)
        self.flag = False

    def paint(self):
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            r, g, b = random.choices(range(256), k=3)
            painter = QPainter()
            painter.begin(self)
            painter.setBrush(QBrush(QColor(r, g, b)))
            painter.setPen(QPen(QColor(r, g, b), 10))
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

# pyuic5 UI.ui -o UI.py
