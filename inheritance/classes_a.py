import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from inheritance import Ui_MainWindow

class A(QMainWindow):
    def __init__(self):
        super(A, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.B = B()
        self.C = C()
        
        self.ui.b_pushButton.clicked.connect(self.B.pushB)
        self.ui.c_pushButton.clicked.connect(self.C.pushC)

class B():
    def pushB(self):
        if self.b_checkBox.isChecked():
            print('You pushed the "B" button')
            print()
        else:
            print('Check the check box to print the correct statement.')

class C():
    def pushC(self):
        if self.c_checkBox.isChecked():
            print('You pushed the "C" button')
            print()
        else:
            print('Check the check box to print the correct statement.')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = A()
    main.show()
    sys.exit(app.exec_())
    
