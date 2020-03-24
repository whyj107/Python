# http://codetorial.net/pyqt5/widget/qpushbutton.html
## Ex 5-1. QPushButton

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # short cut : alt + b
        btn1 = QPushButton('&Button1', self)
        # 선택 상태 유지
        btn1.setCheckable(True)
        # 시작할 때 선택
        btn1.toggle()

        btn2 = QPushButton(self)
        # short cut : alt + 2
        btn2.setText('Button&2')

        btn3 = QPushButton('Button3', self)
        # 버튼 사용 불가
        btn3.setEnabled(False)

        vbox = QVBoxLayout()
        vbox.addWidget(btn1)
        vbox.addWidget(btn2)
        vbox.addWidget(btn3)

        self.setLayout(vbox)
        self.setWindowTitle('QPushButton')
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())