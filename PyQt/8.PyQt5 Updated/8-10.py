# http://codetorial.net/pyqt5/paint/drawing_text.html
## Ex 8-10. 텍스트 그리기 (drawText).

import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QPen, QColor, QBrush, QFont
from PyQt5.QtCore import Qt, QRect


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 450, 300)
        self.setWindowTitle('drawText')
        self.show()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.draw_text(qp)
        qp.end()
    """
    def draw_text(self, qp):
        qp.drawText(20, 40, 'Default')

        qp.setFont(QFont('Arial', 16))
        qp.drawText(150, 40, 'Arial, 16 pts')

        qp.setFont(QFont('Arial', 18))
        qp.drawText(290, 40, 'Arial, 18 pts')

        qp.setFont(QFont('Times New Roman', 14))
        qp.drawText(20, 90, 'Times New Roman')
        qp.drawText(20, 110, '14 pts')

        qp.setFont(QFont('Times New Roman', 16))
        qp.drawText(150, 90, 'Times New Roman')
        qp.drawText(150, 110, '16 pts')

        qp.setFont(QFont('Times New Roman', 18))
        qp.drawText(290, 90, 'Times New Roman')
        qp.drawText(290, 110, '18 pts')

        qp.setFont(QFont('Consolas', 14))
        qp.drawText(20, 160, 'Consolas')
        qp.drawText(20, 180, '14 pts')

        qp.setFont(QFont('Consolas', 16))
        qp.drawText(150, 160, 'Consolas')
        qp.drawText(150, 180, '16 pts')

        qp.setFont(QFont('Consolas', 18))
        qp.drawText(290, 160, 'Consolas')
        qp.drawText(290, 180, '18 pts')

        qp.setFont(QFont('Courier New', 14, italic=True))
        qp.drawText(20, 220, 'Courier New')
        qp.drawText(20, 240, '14 pts')
        qp.drawText(20, 260, 'Italic')

        qp.setFont(QFont('Courier New', 16, italic=True))
        qp.drawText(150, 220, 'Courier New')
        qp.drawText(150, 240, '16 pts')
        qp.drawText(150, 260, 'Italic')

        qp.setFont(QFont('Courier New', 18, italic=True))
        qp.drawText(290, 220, 'Courier New')
        qp.drawText(290, 240, '18 pts')
        qp.drawText(290, 260, 'Italic')
    """

    def draw_text(self, qp):
        rect1 = QRect(10, 15, 210, 60)
        qp.drawRect(rect1)
        qp.drawText(rect1, Qt.AlignHCenter, 'AlignHCenter')

        rect2 = QRect(230, 15, 210, 60)
        qp.drawRect(rect2)
        qp.drawText(rect2, Qt.AlignRight, 'AlignRight')

        rect3 = QRect(10, 85, 210, 60)
        qp.drawRect(rect3)
        qp.drawText(rect3, Qt.AlignVCenter, 'AlignVCenter')

        rect4 = QRect(230, 85, 210, 60)
        qp.drawRect(rect4)
        qp.drawText(rect4, Qt.AlignCenter, 'AlignCenter')

        rect5 = QRect(10, 155, 210, 60)
        qp.drawRect(rect5)
        qp.drawText(rect5, Qt.AlignVCenter | Qt.AlignRight, 'AlignVCenter | AlignRight')

        rect6 = QRect(230, 155, 210, 60)
        qp.drawRect(rect6)
        qp.drawText(rect6, Qt.AlignBottom, 'AlignBottom')

        rect7 = QRect(10, 225, 210, 60)
        qp.drawRect(rect7)
        qp.drawText(rect7, Qt.AlignBottom | Qt.AlignHCenter, 'AlignBottom | AlignHCenter')

        rect8 = QRect(230, 225, 210, 60)
        qp.drawRect(rect8)
        qp.drawText(rect8, Qt.AlignBottom | Qt.AlignRight, 'AlignBottom | AlignRight')

if __name__=='__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())