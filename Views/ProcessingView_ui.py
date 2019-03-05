# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ProcessingView.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ImageContainer(object):
    def setupUi(self, ImageContainer):
        ImageContainer.setObjectName("ImageContainer")
        ImageContainer.resize(600, 400)
        ImageContainer.setStyleSheet("background-color: rgb(72, 72, 72);")
        self.verticalLayoutWidget = QtWidgets.QWidget(ImageContainer)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 20, 561, 291))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(ImageContainer)
        self.label.setGeometry(QtCore.QRect(20, 320, 58, 18))
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.ProgressBar = QtWidgets.QProgressBar(ImageContainer)
        self.ProgressBar.setGeometry(QtCore.QRect(20, 352, 561, 21))
        self.ProgressBar.setStyleSheet("color: rgb(47, 111, 126);\n"
"background-color: rgb(229, 229, 229);")
        self.ProgressBar.setProperty("value", 0)
        self.ProgressBar.setObjectName("ProgressBar")

        self.retranslateUi(ImageContainer)
        QtCore.QMetaObject.connectSlotsByName(ImageContainer)

    def retranslateUi(self, ImageContainer):
        _translate = QtCore.QCoreApplication.translate
        ImageContainer.setWindowTitle(_translate("ImageContainer", "Form"))
        self.label.setText(_translate("ImageContainer", "Progreso"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ImageContainer = QtWidgets.QWidget()
    ui = Ui_ImageContainer()
    ui.setupUi(ImageContainer)
    ImageContainer.show()
    sys.exit(app.exec_())

