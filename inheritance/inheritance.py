# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'inheritance.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(452, 246)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.b_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.b_pushButton.setGeometry(QtCore.QRect(40, 50, 151, 81))
        self.b_pushButton.setObjectName("b_pushButton")
        self.c_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.c_pushButton.setGeometry(QtCore.QRect(230, 50, 151, 81))
        self.c_pushButton.setObjectName("c_pushButton")
        self.b_checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.b_checkBox.setGeometry(QtCore.QRect(50, 130, 131, 20))
        self.b_checkBox.setObjectName("b_checkBox")
        self.c_checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.c_checkBox.setGeometry(QtCore.QRect(240, 130, 131, 20))
        self.c_checkBox.setObjectName("c_checkBox")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 452, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.b_pushButton.setText(_translate("MainWindow", "B"))
        self.c_pushButton.setText(_translate("MainWindow", "C"))
        self.b_checkBox.setText(_translate("MainWindow", "Check to print B"))
        self.c_checkBox.setText(_translate("MainWindow", "Check to print C"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

