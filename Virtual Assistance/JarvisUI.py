# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'suhaviui.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(902, 626)
        Form.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(50, -70, 761, 491))
        self.label.setStyleSheet("border : 2 px solid white;")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("images/background.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.Gif = QtWidgets.QLabel(Form) 
        self.Gif.setGeometry(QtCore.QRect(240, 60, 391, 231))
        self.Gif.setStyleSheet("Qlabel{\n"
"url(:/newPrefix/images/gifloader.gif)\n"
"}")
        self.Gif.setText("")
        self.Gif.setPixmap(QtGui.QPixmap("images/gifloader.gif"))
        self.Gif.setScaledContents(True)
        self.Gif.setObjectName("Gif")
        self.start = QtWidgets.QPushButton(Form)
        self.start.setGeometry(QtCore.QRect(230, 350, 75, 41))
        self.start.setStyleSheet("background-color: rgb(85, 255, 0);\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"border: 1px solid white;")
        self.start.setObjectName("start")
        self.end = QtWidgets.QPushButton(Form)
        self.end.setGeometry(QtCore.QRect(544, 350, 81, 41))
        self.end.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"border : 1px solid white;")
        self.end.setObjectName("end")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(40, 420, 781, 181))
        self.label_2.setStyleSheet("border-color: rgb(255, 255, 255);\n"
"border : 2px solid white;")
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.start.setText(_translate("Form", "START"))
        self.end.setText(_translate("Form", "END"))
        self.label_2.setText(_translate("Form", "TextLabel"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
