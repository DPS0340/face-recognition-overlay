from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from time import sleep
from main import get_faces


class Overlay(QtWidgets.QWidget):
    def __init__(self, steps=5, *args, **kwargs):
        super(QtWidgets.QWidget, self).__init__()
        self.grid = QtWidgets.QGridLayout()
        self.rects = []
        # self.setGeometry(100, 100, 100, 100)
        self.setStyleSheet("background-color: transparent;")
        # self.setStyleSheet("background-color: yellow;")
        self.setAttribute(Qt.WA_NoSystemBackground)
        self.setAttribute(Qt.WA_TransparentForMouseEvents)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint |
                            QtCore.Qt.CustomizeWindowHint)
        self.setWindowFlags(QtCore.Qt.Window)
        self.showMaximized()
        # self.editor = QtWidgets.QTextEdit()
        # self.editor.setPlainText("OVERLAY" * 100)
        # self.grid.addWidget(self.editor)
        self.setLayout(self.grid)
        # self.renderer = Renderer(painter=QtGui.QPainter(self), overlay=self)
        # self.renderer.start()
        self.show()

    def removeRectangles(self):
        painter = QtGui.QPainter(self)
        painter.begin()
        for xy, name in self.rects:
            self.painter.eraseRect(xy)
        painter.end()
        self.update()
        self.rects.clear()

    def paintEvent(self, QPaintEvent):
        pass
        # self.sizeObject = QtWidgets.QDesktopWidget().screenGeometry()
        # painter = QtGui.QPainter(self)
        # painter.eraseRect(0, 0, self.sizeObject.width(),
        #                   self.sizeObject.height())
        # QColor = QtGui.QColor(0, 255, 0, 255)
        # face_locations, face_names = get_faces()
        # painter.setRenderHint(QtGui.QPainter.Antialiasing)
        # painter.setPen(QtGui.QPen(QtGui.QBrush(QColor), 2))
        # painter.setBrush(QColor)
        # # painter.begin(self)
        # # self.rects += list(zip(face_locations, face_names))
        # for (top, right, bottom, left), name in zip(face_locations, face_names):
        #     painter.drawLine(top, left, top, right)
        #     painter.drawLine(bottom, left, bottom, right)
        #     painter.drawLine(top, left, bottom, left)
        #     painter.drawLine(top, right, bottom, right)
        #     # painter.drawRect(left - 20, top - 20,
        #     #                  right + 20, bottom + 20)
        #     # painter.fillRect(left - 20, bottom - 15,
        #     #                  right + 20, bottom + 20)
        #     painter.drawText(left - 20, bottom + 15,
        #                      name)
        # painter.end()
        # # painter.drawPath(path)
        # # painter.drawRect(0, 0, self.rect().width()-1, self.rect().height()-1)
        # self.update()


class Renderer(QtCore.QThread):
    def __init__(self, painter=None, overlay=None):
        QtCore.QThread.__init__(self)
        self.painter = painter
        self.overlay = overlay
        self._status = True

    def __del__(self):
        self.wait()

    def run(self):
        while True:
            # self.removeRectangles()
            self.sizeObject = QtWidgets.QDesktopWidget().screenGeometry()
            painter = self.painter
            painter.begin(self.overlay)
            painter.eraseRect(0, 0, self.sizeObject.width(),
                              self.sizeObject.height())
            QColor = QtGui.QColor(0, 255, 0, 255)
            face_locations, face_names = get_faces()
            painter.setRenderHint(QtGui.QPainter.Antialiasing)
            painter.setPen(QtGui.QPen(QtGui.QBrush(QColor), 2))
            painter.setBrush(QColor)
            # painter.begin(self)
            # self.rects += list(zip(face_locations, face_names))
            for (top, right, bottom, left), name in zip(face_locations, face_names):
                painter.drawLine(top, left, top, right)
                painter.drawLine(bottom, left, bottom, right)
                painter.drawLine(top, left, bottom, left)
                painter.drawLine(top, right, bottom, right)
                # painter.drawRect(left - 20, top - 20,
                #                  right + 20, bottom + 20)
                # painter.fillRect(left - 20, bottom - 15,
                #                  right + 20, bottom + 20)
                painter.drawText(left - 20, bottom + 15,
                                 name)
            painter.end()
            # painter.drawPath(path)
            # painter.drawRect(0, 0, self.rect().width()-1, self.rect().height()-1)
            self.overlay.update()
            # self.rects.append()


def main():
    app = QtWidgets.QApplication([])
    overlay = Overlay()
    app.exec_()


if __name__ == "__main__":
    main()
