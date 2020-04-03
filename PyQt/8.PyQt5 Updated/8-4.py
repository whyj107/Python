# http://codetorial.net/pyqt5/paint/drawing_roundedrect.html
## Ex 8-4. 둥근 직사각형 그리기 (drawRoundedRect).

import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QPen, QColor, QBrush
from PyQt5.QtCore import Qt

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 400, 300)
        self.setWindowTitle('drawRoundedRect')
        self.show()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.draw_roundedrect(qp)
        qp.end()

    """
    def draw_roundedrect(self, qp):
        qp.setPen(QPen(Qt.black, 3))

        qp.drawRoundedRect(20, 20, 100, 100, 0, 0)
        qp.drawText(40, 140, 'radius: 0')

        qp.drawRoundedRect(150, 20, 100, 100, 10, 10)
        qp.drawText(170, 140, 'radius: 10')

        qp.drawRoundedRect(280, 20, 100, 100, 20, 20)
        qp.drawText(300, 140, 'radius: 20')

        qp.drawRoundedRect(20, 160, 100, 100, 30, 30)
        qp.drawText(40, 280, 'radius: 30')

        qp.drawRoundedRect(150, 160, 100, 100, 40, 40)
        qp.drawText(170, 280, 'radius: 40')

        qp.drawRoundedRect(280, 160, 100, 100, 50, 50)
        qp.drawText(300, 280, 'radius: 50')
    """

    def draw_roundedrect(self, qp):
        brush = QBrush(Qt.SolidPattern)
        qp.setBrush(brush)
        qp.drawRoundedRect(20, 10, 100, 60, 15, 15)
        qp.drawText(20, 90, 'Qt.SolidPattern')

        brush = QBrush(Qt.Dense1Pattern)
        qp.setBrush(brush)
        qp.drawRoundedRect(150, 10, 100, 60, 15, 15)
        qp.drawText(150, 90, 'Qt.Dense1Pattern')

        brush = QBrush(Qt.Dense2Pattern)
        qp.setBrush(brush)
        qp.drawRoundedRect(280, 10, 100, 60, 15, 15)
        qp.drawText(280, 90, 'Qt.Dense2Pattern')

        brush = QBrush(Qt.HorPattern)
        qp.setBrush(brush)
        qp.drawRoundedRect(20, 110, 100, 60, 15, 15)
        qp.drawText(20, 190, 'Qt.HorPattern')

        brush = QBrush(Qt.VerPattern)
        qp.setBrush(brush)
        qp.drawRoundedRect(150, 110, 100, 60, 15, 15)
        qp.drawText(150, 190, 'Qt.VerPattern')

        brush = QBrush(Qt.CrossPattern)
        qp.setBrush(brush)
        qp.drawRoundedRect(280, 110, 100, 60, 15, 15)
        qp.drawText(280, 190, 'Qt.CrossPattern')

        brush = QBrush(Qt.BDiagPattern)
        qp.setBrush(brush)
        qp.drawRoundedRect(20, 210, 100, 60, 15, 15)
        qp.drawText(20, 290, 'Qt.BDiagPattern')

        brush = QBrush(Qt.FDiagPattern)
        qp.setBrush(brush)
        qp.drawRoundedRect(150, 210, 100, 60, 15, 15)
        qp.drawText(150, 290, 'Qt.FDiagPattern')

        brush = QBrush(Qt.DiagCrossPattern)
        qp.setBrush(brush)
        qp.drawRoundedRect(280, 210, 100, 60, 15, 15)
        qp.drawText(280, 290, 'Qt.DiagCrossPattern')

if __name__=='__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())