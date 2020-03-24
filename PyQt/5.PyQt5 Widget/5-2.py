# http://codetorial.net/pyqt5/widget/qlabel.html
## Ex 5-2. QLabel.

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 라벨텍스트와 부모 위젯
        label1 = QLabel('First Label', self)
        # 라벨 센터 배치
        label1.setAlignment(Qt.AlignCenter)

        label2 = QLabel('Second Label', self)
        # 라벨 수직 센터 배치
        label2.setAlignment(Qt.AlignVCenter)

        # 라벨 수평 센터 배치
        #label2.setAlignment(Qt.AlignHCenter)

        font1 = label1.font()
        # 폰트 사이즈 설정(기본 13)
        font1.setPointSize(20)

        font2 = label2.font()
        # 폰트 종류 설정
        font2.setFamily('Times New Roman')
        # 폰트 진하게 설정
        font2.setBold(True)

        label1.setFont(font1)
        label2.setFont(font2)

        layout = QVBoxLayout()
        layout.addWidget(label1)
        layout.addWidget(label2)

        self.setLayout(layout)

        self.setWindowTitle('QLabel')
        self.setGeometry(300,300,300,200)
        self.show()

if __name__=='__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())