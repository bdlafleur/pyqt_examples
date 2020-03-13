# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'example_dragdrop.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(589, 267)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.files_listWidget = DropList(self.centralwidget)
        self.files_listWidget.setGeometry(QtCore.QRect(40, 40, 511, 81))
        self.files_listWidget.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)
        self.files_listWidget.setAlternatingRowColors(True)
        self.files_listWidget.setObjectName("files_listWidget")
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(260, 20, 91, 21))
        self.label_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_1.setObjectName("label_1")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(160, 160, 91, 21))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.codes_listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.codes_listWidget.setGeometry(QtCore.QRect(60, 180, 291, 81))
        self.codes_listWidget.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)
        self.codes_listWidget.setAlternatingRowColors(True)
        self.codes_listWidget.setObjectName("codes_listWidget")
        self.availCodes_listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.availCodes_listWidget.setGeometry(QtCore.QRect(380, 180, 101, 81))
        self.availCodes_listWidget.setDragEnabled(True)
        self.availCodes_listWidget.setDragDropMode(QtWidgets.QAbstractItemView.DragOnly)
        self.availCodes_listWidget.setAlternatingRowColors(True)
        self.availCodes_listWidget.setObjectName("availCodes_listWidget")
        item = QtWidgets.QListWidgetItem()
        self.availCodes_listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.availCodes_listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.availCodes_listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.availCodes_listWidget.addItem(item)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(380, 160, 91, 21))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.lineEdit = DropLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(110, 130, 441, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 130, 91, 21))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 589, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Drag & Drop List Widget"))
        self.label_1.setText(_translate("MainWindow", "Files List"))
        self.label_2.setText(_translate("MainWindow", "Codes List"))
        __sortingEnabled = self.availCodes_listWidget.isSortingEnabled()
        self.availCodes_listWidget.setSortingEnabled(False)
        item = self.availCodes_listWidget.item(0)
        item.setText(_translate("MainWindow", "Python"))
        item = self.availCodes_listWidget.item(1)
        item.setText(_translate("MainWindow", "C++"))
        item = self.availCodes_listWidget.item(2)
        item.setText(_translate("MainWindow", "Ruby"))
        item = self.availCodes_listWidget.item(3)
        item.setText(_translate("MainWindow", "Perl"))
        self.availCodes_listWidget.setSortingEnabled(__sortingEnabled)
        self.label_3.setText(_translate("MainWindow", "Codes"))
        self.label_4.setText(_translate("MainWindow", "Line Edit"))
from dropwidgets import DropLineEdit, DropList


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
