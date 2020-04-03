# http://codetorial.net/pyqt5/paint/drawing_ellipse.html
## Ex 8-6. 타원 그리기 (drawEllipse).

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
        self.setWindowTitle('drawEllipse')
        self.show()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.draw_ellipse(qp)
        qp.end()

    def draw_ellipse(self, qp):
        qp.setPen(QPen(Qt.black, 3))
        qp.drawEllipse(40, 20, 80, 100)

        qp.setPen(QPen(Qt.green, 5, Qt.DashLine))
        qp.setBrush(QBrush(Qt.CrossPattern))
        qp.drawEllipse(70, 140, 180, 120)

        qp.setPen(QPen(Qt.red, 2, Qt.DashDotDotLine))
        qp.setBrush((QBrush(Qt.blue, Qt.FDiagPattern)))
        qp.drawEllipse(290, 100, 80, 120)

if __name__=='__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())