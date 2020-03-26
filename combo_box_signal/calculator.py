import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication
from test import Ui_MainWindow
import pandas as pd


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Create combo box for Col1
        combo_box_1 = QtWidgets.QComboBox() 
        combo_box_1.addItems(['Item 1', 'Item 2', 'Item 3'])
        combo_box_1.currentIndexChanged[str].connect(self.print_selected_text)
        self.ui.tab_1_table.setCellWidget(0, 0, combo_box_1) 
       
        # Connect add row buttons to functions
        self.ui.add_tab_1_button.clicked.connect(self.add_row)
        
        ### Test section ###
        # Create combo box for Col2
        self.combo_box_2 = QtWidgets.QComboBox()
        self.ui.tab_1_table.setCellWidget(0, 1, self.combo_box_2)
        self.combo_box_2.addItems(['Item A', 'Item B', 'Item C'])
        self.combo_box_2.currentIndexChanged[str].connect(self.print_selected_text)
        ##################

    def add_row(self):
        """Add row and insert combo box in column.."""

        rowPos = self.ui.tab_1_table.rowCount()

        # Create new instance of a combo boxes
        new_combo_box_1 = QtWidgets.QComboBox() 
        new_combo_box_1.addItems(['Item 1', 'Item 2', 'Item 3'])
        new_combo_box_1.currentIndexChanged[str].connect(self.print_selected_text)

        # Insert new row and add combo boxes
        self.ui.tab_1_table.insertRow(rowPos)
        self.ui.tab_1_table.setCellWidget(rowPos, 0, new_combo_box_1) 

    def print_selected_text(self, text):
        """Test function to see if cell text will be printed whenever it changes."""
        print(text)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())
