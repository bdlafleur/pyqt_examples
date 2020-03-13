from PyQt5 import QtCore, QtWidgets


class DropList(QtWidgets.QListWidget):
    def __init__(self, parent=None):
        super(DropList, self).__init__(parent)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
        else:
            event.ignore()

    def dropEvent(self, event):
        md = event.mimeData()
        if md.hasUrls():
            for url in md.urls():
                self.addItem(url.toLocalFile())
            event.acceptProposedAction()

class DropLineEdit(QtWidgets.QLineEdit):
    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event):
        md = event.mimeData()

        if md.hasUrls():
            files = []
            for url in md.urls():
                files.append(url.toLocalFile())
            self.setText(" ".join(files))
            event.acceptProposedAction()

