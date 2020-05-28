from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt


class Overlay(QtWidgets.QWidget):
    def __init__(self, steps=5, *args, **kwargs):
        super(QtWidgets.QWidget, self).__init__()
        self.resize(1920, 1080)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setLayout(QtGui.QHBoxLayout())


def main():
    app = QtWidgets.QApplication([])
    overlay = Overlay()
    overlay.show()
    app.exec_()


if __name__ == "__main__":
    main()
