import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from inheritance import Ui_MainWindow

class A(QMainWindow):
    def __init__(self):
        super(A, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

class B(A):
    def __init__(self):
        super(B, self).__init__()

        self.ui.b_pushButton.clicked.connect(self.pushB)

    def pushB(self):
        print('You pushed the "B" button')
        print()

class C(A):
    def __init__(self):
        super(C, self).__init__()

        self.ui.c_pushButton.clicked.connect(self.pushC)

    def pushC(self):
        print('You pushed the "C" button')
        print()

class Dummy(B, C):
    pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = Dummy()
    main.show()
    sys.exit(app.exec_())

