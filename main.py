import sys
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic
import random


class Progr(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.start()

    def start(self):
        self.do_paint = False
        self.pushButton.clicked.connect(self.run)

    def paintEvent(self, event):
        if self.do_paint:
            a = random.randrange(100)
            qp = QPainter()
            qp.begin(self)
            qp.setBrush(QColor(255, 255, 0))
            qp.drawEllipse(random.randrange(75, 400 - a), random.randrange(75, 500 - a), a, a)
            qp.end()

    def run(self):
        self.do_paint = True
        print(self.do_paint)
        self.repaint()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Progr()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
