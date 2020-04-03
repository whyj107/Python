# http://codetorial.net/pyqt5/paint/drawing_chord.html
## Ex 8-8. 현 그리기 (drawChord).
## x, y, width, height, start-angle, span-angle

import sys
from PyQt5.QtWidgets import  QWidget, QApplication
from PyQt5.QtGui import QPainter, QPen, QColor, QBrush
from PyQt5.QtCore import Qt

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 400, 300)
        self.setWindowTitle('drawChord')
        self.show()

    def paintEvent(self, QPaintEvent):
        qp = QPainter()
        qp.begin(self)
        self.draw_chord(qp)
        qp.end()

    def draw_chord(self, qp):
        qp.setPen(QPen(Qt.black, 3))
        qp.drawChord(20, 20, 100, 100, 0 * 16, 30 * 16)
        qp.drawText(60, 100, '30°')

        qp.drawChord(150, 20, 100, 100, 0 * 16, 60 * 16)
        qp.drawText(190, 100, '60°')

        qp.drawChord(280, 20, 100, 100, 0 * 16, 90 * 16)
        qp.drawText(320, 100, '90°')

        qp.drawChord(20, 140, 100, 100, 0 * 16, 180 * 16)
        qp.drawText(60, 270, '180°')

        qp.drawChord(150, 140, 100, 100, 0 * 16, 270 * 16)
        qp.drawText(190, 270, '270°')

        qp.drawChord(280, 140, 100, 100, 0 * 16, 360 * 16)
        qp.drawText(320, 270, '360°')

if __name__=='__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())