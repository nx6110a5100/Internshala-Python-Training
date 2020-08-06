# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QRadioButton.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.t1 = QtWidgets.QLineEdit(Form)
        self.t1.setGeometry(QtCore.QRect(130, 30, 113, 22))
        self.t1.setObjectName("t1")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(19, 130, 361,200))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.r1 = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.r1.setObjectName("r1")
        self.horizontalLayout.addWidget(self.r1)
        self.r2 = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.r2.setObjectName("r2")
        self.horizontalLayout.addWidget(self.r2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.r1.toggled.connect(self.checkstate)
        self.r2.toggled.connect(self.checkstate) 

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.r1.setText(_translate("Form", "RadioButton"))
        self.r2.setText(_translate("Form", "RadioButton"))
    def checkstate(self):
        state1='OFF'
        state2='OFF'
        if self.r1.isChecked()==True:
            state1='ON'
        else:
            state1='OFF'
        if self.r2.isChecked()==True:
            state2='ON'
        else:
            state2='OFF'
        self.t1.setText("Button1 is {} Button2 is {}".format(state1,state2)) 


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

