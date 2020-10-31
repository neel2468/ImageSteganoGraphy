from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import QFileDialog, QPixmap, QMessageBox, QDialog
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class LoadingScreen(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.setFixedSize(200, 200)
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.CustomizeWindowHint)

        self.animation_lable = QtWidgets.QLabel(self)
        self.movie = QtGui.QMovie('images/loading3.gif')
        self.animation_lable.setMovie(self.movie)

        #timer = QtCore.QTimer(self)
        self.startLoading()
        #timer.singleShot(15000, self.stopLoading)

        #self.show()

    def startLoading(self):
        self.movie.start()
        self.show()

    def stopLoading(self):
        self.movie.stop()
        self.close()
