# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BigEyeInit.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 400)
        MainWindow.setStyleSheet("background-color: rgb(72, 72, 72);\n"
"selection-background-color: rgb(47, 111, 126);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.EntryVideoPath = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.EntryVideoPath.setGeometry(QtCore.QRect(20, 20, 371, 31))
        self.EntryVideoPath.setStyleSheet("background-color: rgb(229, 229, 229);")
        self.EntryVideoPath.setPlaceholderText("")
        self.EntryVideoPath.setObjectName("EntryVideoPath")
        self.ButtonSearchVideo = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonSearchVideo.setGeometry(QtCore.QRect(427, 20, 151, 34))
        self.ButtonSearchVideo.setStyleSheet("background-color: rgb(0, 37, 97);\n"
"border-color: rgb(47, 111, 126);\n"
"color: rgb(255, 255, 255)")
        self.ButtonSearchVideo.setObjectName("ButtonSearchVideo")
        self.EntryResultPath = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.EntryResultPath.setGeometry(QtCore.QRect(20, 80, 371, 31))
        self.EntryResultPath.setStyleSheet("background-color: rgb(229, 229, 229);")
        self.EntryResultPath.setPlaceholderText("")
        self.EntryResultPath.setObjectName("EntryResultPath")
        self.ButtonSetDestinyResults = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonSetDestinyResults.setGeometry(QtCore.QRect(427, 80, 151, 34))
        self.ButtonSetDestinyResults.setStyleSheet("background-color: rgb(0, 37, 97);\n"
"border-color: rgb(47, 111, 126);\n"
"color: rgb(255, 255, 255)")
        self.ButtonSetDestinyResults.setObjectName("ButtonSetDestinyResults")
        self.ButtonAnalyze = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonAnalyze.setGeometry(QtCore.QRect(220, 290, 151, 34))
        self.ButtonAnalyze.setStyleSheet("background-color: rgb(0, 37, 97);\n"
"border-color: rgb(47, 111, 126);\n"
"color: rgb(255, 255, 255)")
        self.ButtonAnalyze.setObjectName("ButtonAnalyze")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "BigEye - Inicio"))
        self.ButtonSearchVideo.setText(_translate("MainWindow", "Buscar Video"))
        self.ButtonSetDestinyResults.setText(_translate("MainWindow", "Elegir Carpeta"))
        self.ButtonAnalyze.setText(_translate("MainWindow", "Analizar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

