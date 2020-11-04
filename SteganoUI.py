# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.




from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import QFileDialog, QPixmap, QMessageBox, QDialog
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from LoadingScreen import *

from AESStego import *
from Stego import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
            MainWindow.setObjectName("MainWindow")
            MainWindow.resize(1519, 858)
            self.centralwidget = QtWidgets.QWidget(MainWindow)
            self.centralwidget.setObjectName("centralwidget")
            self.frame = QtWidgets.QFrame(self.centralwidget)
            self.frame.setGeometry(QtCore.QRect(30, 30, 1021, 251))
            self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
            self.frame.setObjectName("frame")
            self.keyTextBox = QtWidgets.QLineEdit(self.frame)
            self.keyTextBox.setGeometry(QtCore.QRect(140, 150, 221, 31))
            self.keyTextBox.setObjectName("keyTextBox")
            self.keyTextBox.setMaxLength(16)
            self.key = QtWidgets.QLabel(self.frame)
            self.key.setGeometry(QtCore.QRect(10, 140, 101, 31))
            self.key.setObjectName("key")
            self.plainText = QtWidgets.QLabel(self.frame)
            self.plainText.setGeometry(QtCore.QRect(20, 40, 101, 31))
            self.plainText.setObjectName("plainText")
            self.generateKey = QtWidgets.QPushButton(self.frame)
            self.generateKey.setGeometry(QtCore.QRect(390, 150, 141, 31))
            self.generateKey.setObjectName("generateKey")
            self.plainTextEdit = QtWidgets.QPlainTextEdit(self.frame)
            self.plainTextEdit.setGeometry(QtCore.QRect(140, 10, 221, 121))
            self.plainTextEdit.setObjectName("plainTextEdit")
            self.pushButton_2 = QtWidgets.QPushButton(self.frame)
            self.pushButton_2.setGeometry(QtCore.QRect(390, 40, 181, 34))
            self.pushButton_2.setObjectName("pushButton_2")
            self.cipherText = QtWidgets.QLabel(self.frame)
            self.cipherText.setGeometry(QtCore.QRect(620, 40, 101, 31))
            self.cipherText.setObjectName("cipherText")
            self.decrypt = QtWidgets.QPushButton(self.centralwidget)
            self.decrypt.setGeometry(QtCore.QRect(1020, 300, 111, 51))
            icon1 = QtGui.QIcon()
            icon1.addPixmap(QtGui.QPixmap("images/decrypt.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.decrypt.setIcon(icon1)
            self.decrypt.setObjectName("decrypt")
            self.radioButton_2 = QtWidgets.QRadioButton(self.frame)
            self.radioButton_2.setGeometry(QtCore.QRect(390, 210, 119, 23))
            self.radioButton_2.setObjectName("radioButton_2")
            self.radioButton = QtWidgets.QRadioButton(self.frame)
            self.radioButton.setGeometry(QtCore.QRect(220, 210, 119, 23))
            self.radioButton.setObjectName("radioButton")
            self.radioButton.setChecked(True)
            self.encrypt = QtWidgets.QPushButton(self.centralwidget)
            self.encrypt.setGeometry(QtCore.QRect(860, 300, 111, 51))
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("images/encrypt.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.encrypt.setIcon(icon)
            self.encrypt.setObjectName("encrypt")
            self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.frame)
            self.plainTextEdit_2.setGeometry(QtCore.QRect(720, 10, 271, 141))
            self.plainTextEdit_2.setObjectName("plainTextEdit_2")
            self.plainTextEdit_2.setReadOnly(True)
            self.key_2 = QtWidgets.QLabel(self.frame)
            self.key_2.setGeometry(QtCore.QRect(10, 200, 131, 31))
            self.key_2.setObjectName("key_2")


            self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
            self.scrollArea.setGeometry(QtCore.QRect(30, 400, 1091, 411))
            self.scrollArea.setWidgetResizable(True)
            self.scrollArea.setObjectName("scrollArea")
            self.scrollAreaWidgetContents = QtWidgets.QWidget()
            self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1089, 409))
            self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
            self.inputImage = QtWidgets.QLabel(self.scrollAreaWidgetContents)
            self.inputImage.setGeometry(QtCore.QRect(0, 10, 1081, 381))
            self.inputImage.setObjectName("label")

            self.vbox = QtWidgets.QVBoxLayout()
            self.vbox.addWidget(self.inputImage)
            self.scrollAreaWidgetContents.setLayout(self.vbox)
            self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
            self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
            self.scrollArea.setWidgetResizable(True)
            self.scrollArea.setWidget(self.scrollAreaWidgetContents)

            self.scrollArea.setStyleSheet("background-color : rgba(0, 0, 0, 0);border : 1px");

            self.widget = QtWidgets.QWidget(self.centralwidget)
            self.widget.setGeometry(QtCore.QRect(30, 260, 811, 131))
            self.widget.setObjectName("widget")
            self.imagepath_2 = QtWidgets.QLineEdit(self.widget)
            self.imagepath_2.setGeometry(QtCore.QRect(20, 20, 441, 31))
            self.imagepath_2.setObjectName("imagepath_2")
            self.imagepath_2.setReadOnly(True)
            self.pushButton = QtWidgets.QPushButton(self.widget)
            self.pushButton.setGeometry(QtCore.QRect(500, 20, 271, 34))
            self.pushButton.setObjectName("pushButton")
            self.pushButton_3 = QtWidgets.QPushButton(self.widget)
            self.pushButton_3.setGeometry(QtCore.QRect(500, 70, 271, 34))
            self.pushButton_3.setObjectName("pushButton_3")
            self.imagepath_3 = QtWidgets.QLineEdit(self.widget)
            self.imagepath_3.setGeometry(QtCore.QRect(20, 70, 441, 31))
            self.imagepath_3.setText("")
            self.imagepath_3.setObjectName("imagepath_3")
            self.imagepath_3.setReadOnly(True)
            self.plainImageSize = QtWidgets.QLabel(self.centralwidget)
            self.plainImageSize.setGeometry(QtCore.QRect(1290, 90, 131, 31))
            self.plainImageSize.setText("")
            self.plainImageSize.setObjectName("plainImageSize")
            self.StegoImageSize = QtWidgets.QLabel(self.centralwidget)
            self.StegoImageSize.setGeometry(QtCore.QRect(1290, 130, 151, 31))
            self.StegoImageSize.setText("")
            self.StegoImageSize.setObjectName("StegoImageSize")
            self.plainText_4 = QtWidgets.QLabel(self.centralwidget)
            self.plainText_4.setGeometry(QtCore.QRect(1290, 170, 141, 31))
            self.plainText_4.setText("")
            self.plainText_4.setObjectName("plainText_4")
            self.plainImageSize_2 = QtWidgets.QLabel(self.centralwidget)
            self.plainImageSize_2.setGeometry(QtCore.QRect(1100, 90, 191, 31))
            self.plainImageSize_2.setObjectName("plainImageSize_2")
            self.StegoImageSize_2 = QtWidgets.QLabel(self.centralwidget)
            self.StegoImageSize_2.setGeometry(QtCore.QRect(1100, 130, 191, 31))
            self.StegoImageSize_2.setObjectName("StegoImageSize_2")
            self.secretMessageSize = QtWidgets.QLabel(self.centralwidget)
            self.secretMessageSize.setGeometry(QtCore.QRect(1100, 170, 181, 31))
            self.secretMessageSize.setObjectName("secretMessageSize")

            MainWindow.setCentralWidget(self.centralwidget)
            self.menubar = QtWidgets.QMenuBar(MainWindow)
            self.menubar.setGeometry(QtCore.QRect(0, 0, 1519, 31))
            self.menubar.setObjectName("menubar")
            MainWindow.setMenuBar(self.menubar)
            self.statusbar = QtWidgets.QStatusBar(MainWindow)
            self.statusbar.setObjectName("statusbar")
            MainWindow.setStatusBar(self.statusbar)

            self.progressBar = QtWidgets.QProgressBar(self.frame)
            self.progressBar.setGeometry(QtCore.QRect(630, 170, 331, 34))
            self.progressBar.setObjectName("progressBar")
            self.progressBar.setAlignment(Qt.AlignCenter)
            self.progressBar.setStyleSheet("QProgressBar"
                                      "{"
                                      "background-color : rgba(0, 0, 0, 0);"
                                      "border : 1px"
                                      "}")


            self.encrypt.clicked.connect(self.encrypt_InputImage)
            self.decrypt.clicked.connect(self.show_OutputImage)
            self.pushButton.clicked.connect(self.originalImagePath)
            self.pushButton_3.clicked.connect(self.stegoImagePath)
            self.generateKey.clicked.connect(self.get_key)
            self.pushButton_2.clicked.connect(self.browse_plainText)

            self.encrypt.setStyleSheet("background-color : lightblue")
            self.decrypt.setStyleSheet("background-color : lightblue")
            self.pushButton.setStyleSheet("background-color : lightblue")
            self.pushButton_3.setStyleSheet("background-color : lightblue")
            self.generateKey.setStyleSheet("background-color : lightblue")
            self.pushButton_2.setStyleSheet("background-color : lightblue")

            self.radioButton_2.clicked.connect(self.enable_disableButton)
            self.radioButton.clicked.connect(self.enable_disableButton)

            self.retranslateUi(MainWindow)
            QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def retranslateUi(self, MainWindow):
            _translate = QtCore.QCoreApplication.translate
            MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
            self.encrypt.setText(_translate("MainWindow", "Encrypt"))
            self.key.setText(_translate("MainWindow", "Key"))
            self.plainText.setText(_translate("MainWindow", "Plain Text"))
            self.generateKey.setText(_translate("MainWindow", "Generate Key"))

            self.cipherText.setText(_translate("MainWindow", "Cipher Text"))
            self.pushButton_2.setText(_translate("MainWindow", "Browse Secret Message"))
            self.decrypt.setText(_translate("MainWindow", "Decrypt"))
            self.key_2.setText(_translate("MainWindow", "Select the Method"))

            self.pushButton.setText(_translate("MainWindow", "Browse OriginalImage"))
            self.pushButton_3.setText(_translate("MainWindow", "Browse StegoImage"))
            self.radioButton.setText(_translate("MainWindow", "AES + LSB"))
            self.radioButton_2.setText(_translate("MainWindow", "New Algo"))
            self.plainImageSize_2.setText(_translate("MainWindow", "Original Image Size : "))
            self.StegoImageSize_2.setText(_translate("MainWindow", "Stego Image Size : " ))
            self.secretMessageSize.setText(_translate("MainWindow", "Secret Image Size : "))

    def encrypt_InputImage(self):
        #self.loading = LoadingScreen()
        #self.loading.startLoading()
        self.progressBar.setFormat("Encrypting...")
        self.step = 0
        self.progressBar.setValue(self.step)
        if self.radioButton_2.isChecked():
            if(self.plainTextEdit.toPlainText()==""):
                QMessageBox.about(None, "Title", "Enter Plain Text")
                return
            elif(self.imagepath_2.text()==""):
                QMessageBox.about(None, "Title", "Choose Input Image")
                return
            self.progressBar.setValue(self.step+15)
            s1.encoded_message_image = s1.generate_encoded_image_from_text(self.plainTextEdit.toPlainText())
            self.progressBar.setValue(self.step+30)
            s1.hide()
            self.progressBar.setValue(self.step+55)
            self.inputImage.setPixmap(QtGui.QPixmap('images/o1.png'))
            self.inputImage.adjustSize()
            img = Image.open('images/o1.png')
            width, height = img.size
            self.progressBar.setValue(self.step+75)
            self.StegoImageSize.setText(str(width * height)+" pixels")
            self.StegoImageSize.setStyleSheet("background-color: lightgreen")
            self.progressBar.setValue(self.step+100)

        if self.radioButton.isChecked():
            if(self.plainTextEdit.toPlainText()==""):
                QMessageBox.about(None, "Title", "Enter Plain Text")
                return
            elif(self.imagepath_2.text()==""):
                QMessageBox.about(None, "Title", "Choose Input Image")
                return
            elif(self.keyTextBox.text()==""):
                QMessageBox.about(None, "Title", "Enter the Key")
                return
            self.progressBar.setValue(self.step+5)
            data = s2.encode(self.plainTextEdit.toPlainText(),self.keyTextBox.text(),self.imagepath_2.text())
            self.progressBar.setValue(self.step+20)
            img = Image.open('images/aes.png')
            width, height = img.size
            self.progressBar.setValue(self.step+35)
            self.StegoImageSize.setText(str(width * height)+" pixels")
            self.progressBar.setValue(self.step+50)
            self.StegoImageSize.setStyleSheet("background-color: lightgreen")
            self.plainTextEdit.setPlainText("")
            self.progressBar.setValue(self.step+75)
            self.plainTextEdit_2.setPlainText(str(data))
            self.progressBar.setValue(self.step+100)
        #self.loading.stopLoading()
        self.progressBar.setFormat("Encrypted 100%..")
        QMessageBox.about(None, "Info", "Encryption is successful")
        
    def show_OutputImage(self):
        #self.loading = LoadingScreen()
        self.progressBar.setFormat("Decrypting...")
        self.step = 0
        if self.radioButton_2.isChecked():
            if(self.imagepath_2.text()==""):
                QMessageBox.about(None, "Title", "Choose Original Image")
                return
            elif(self.imagepath_3.text()==""):
                QMessageBox.about(None, "Title", "Choose Stego Image")
                return
            self.progressBar.setValue(self.step+20)
            s1.unhide(self.imagepath_2.text(),self.imagepath_3.text())
            self.progressBar.setValue(self.step+50)
            self.inputImage.setPixmap(QtGui.QPixmap('images/message.png'))
            self.progressBar.setValue(self.step+60)
            self.inputImage.adjustSize()
            img = Image.open('images/message.png')
            width, height = img.size
            self.progressBar.setValue(self.step+75)
            self.plainText_4.setText(str(width * height)+" pixels")
            self.plainText_4.setStyleSheet("background-color: lightgreen")
            self.progressBar.setValue(self.step+100)

        if self.radioButton.isChecked():
            if(self.keyTextBox.text()==""):
                QMessageBox.about(None, "Title", "Enter the Key")
                return
            elif(self.imagepath_3.text()==""):
                QMessageBox.about(None, "Title", "Choose Stego Image")
                return
            self.progressBar.setValue(self.step+20)
            data = s2.decode(self.keyTextBox.text(),self.imagepath_3.text())
            self.progressBar.setValue(self.step+50)
            self.plainTextEdit.setPlainText(data)
            self.progressBar.setValue(self.step+75)
            self.inputImage.setText(data)
            self.inputImage.setWordWrap(True)
            self.inputImage.adjustSize()
            self.progressBar.setValue(self.step+100)
        #self.loading.stopLoading()
        self.progressBar.setFormat("Decrypted 100%...")
        QMessageBox.about(None, "Info", "Decryption is successful")
        
    def getImage(self):
        fname = QFileDialog.getOpenFileName(None, 'Open file','c:\\', "Image files (*.jpg *.png)")
        if fname != ('', ''):
            return fname[0]
        
    def originalImagePath(self):
        imagepath = self.getImage()
        if imagepath != None:
            s1.getOriginalImage(imagepath)
            self.imagepath_2.setText(imagepath);
            self.inputImage.setPixmap(QtGui.QPixmap(imagepath))
            self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
            self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
            self.inputImage.adjustSize()
            img = Image.open(imagepath)
            width, height = img.size
            self.plainImageSize.setText(str(width * height)+" pixels")
            self.plainImageSize.setStyleSheet("background-color: lightgreen")
    
    def stegoImagePath(self):
        imagepath = self.getImage()
        if imagepath != None:
            self.imagepath_3.setText(imagepath);
            self.inputImage.setPixmap(QtGui.QPixmap(imagepath))
            img = Image.open(imagepath)
            width, height = img.size
            self.StegoImageSize.setText(str(width * height)+" pixels")
            self.StegoImageSize.setStyleSheet("background-color: lightgreen")
            self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
            self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
    
    def browse_plainText(self):
        fname = QFileDialog.getOpenFileName(None, 'Open file','c:\\', "Image files (*.txt)")
        if fname != ('', ''):
            file1 = open(fname[0],"r")
            plainText = file1.read()
            self.plainTextEdit.setPlainText(plainText)
        
    def get_key(self):
        if self.radioButton.isChecked():
            key = s2.get_random_string(16)
            self.keyTextBox.setText(key)
        
    def enable_disableButton(self):
        if self.radioButton_2.isChecked(): 
            self.keyTextBox.setText("")
            self.plainTextEdit.setPlainText("")
            self.plainTextEdit_2.setPlainText("")
            self.plainImageSize.setText("")
            self.StegoImageSize.setText("")
            self.plainText_4.setText("")
            self.imagepath_2.setText("")
            self.imagepath_3.setText("")
            self.plainImageSize.setStyleSheet("")
            self.StegoImageSize.setStyleSheet("")
            self.plainText_4.setStyleSheet("")
            self.generateKey.setEnabled(False)
            self.keyTextBox.setEnabled(False)
            self.progressBar.reset()

        if self.radioButton.isChecked():
            self.keyTextBox.setText("")
            self.plainTextEdit.setPlainText("")
            self.plainTextEdit_2.setPlainText("")
            self.plainImageSize.setText("")
            self.StegoImageSize.setText("")
            self.imagepath_2.setText("")
            self.imagepath_3.setText("")
            self.plainText_4.setText("")
            self.plainImageSize.setStyleSheet("")
            self.StegoImageSize.setStyleSheet("")
            self.plainText_4.setStyleSheet("")
            self.generateKey.setEnabled(True)
            self.keyTextBox.setEnabled(True)
            self.progressBar.reset()



          
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    s1 = Stego()
    s2 = AESStego()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
