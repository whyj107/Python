## Ex 3-1. 창 띄우기.
# 필요한 모듈 불러오기
import sys
from PyQt5.QtWidgets import  QApplication, QWidget

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 타이틀바에 나타나는 창의 제목
        self.setWindowTitle("My First Application")
        # 위젯을 스크린의 (300, 300)px의 위치로 이동
        self.move(300, 300)
        # 위젯의 크기를 (400, 200)px로 조절
        self.resize(400, 200)
        # 위젯을 스크린에 보여줌
        self.show()

# __name__ 은 현재 모듈의 이름이 저장되는 내장 변수
if __name__=='__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())