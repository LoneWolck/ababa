import random
import UI
from PyQt5.QtGui import QColor, QPainter
from PyQt5.QtWidgets import QApplication
import sys


class FirstForm(UI.Ui_Form):
    def __init__(self):
        super().__init__()
        self.UI_init()

    def UI_init(self):
        self.do_paint = False
        self.btn.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_flag(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        a = random.randint(15, 150)
        qp.drawEllipse(10, 10, a, a)
        a = random.randint(15, 150)
        qp.drawEllipse(510, 10, a, a)
        a = random.randint(15, 150)
        qp.drawEllipse(250, 150, a, a)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = FirstForm()
    ex.show()
    sys.exit(app.exec())