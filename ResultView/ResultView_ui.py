# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ResultView.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(600, 400)
        Form.setStyleSheet("background-color: rgb(72, 72, 72);")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 30, 81, 18))
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.OutputResult = QtWidgets.QPlainTextEdit(Form)
        self.OutputResult.setGeometry(QtCore.QRect(110, 60, 391, 241))
        self.OutputResult.setStyleSheet("background-color: rgb(229, 229, 229);")
        self.OutputResult.setObjectName("OutputResult")
        self.ButtonInit = QtWidgets.QPushButton(Form)
        self.ButtonInit.setGeometry(QtCore.QRect(220, 330, 151, 34))
        self.ButtonInit.setStyleSheet("background-color: rgb(0, 37, 97);\n"
"border-color: rgb(47, 111, 126);\n"
"color: rgb(255, 255, 255)")
        self.ButtonInit.setObjectName("ButtonInit")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Resultados"))
        self.ButtonInit.setText(_translate("Form", "Inicio"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

