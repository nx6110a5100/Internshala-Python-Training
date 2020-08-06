# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QCheckBox.ui'
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
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(19, 130, 361, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.b1 = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.b1.setObjectName("b1")
        self.horizontalLayout.addWidget(self.b1)
        self.b2 = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.b2.setObjectName("b2")
        self.horizontalLayout.addWidget(self.b2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.b1.stateChanged.connect(self.checkstate)
        self.b2.stateChanged.connect(self.checkstate) 

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.b1.setText(_translate("Form", "RadioButton"))
        self.b2.setText(_translate("Form", "RadioButton"))

    def checkstate(self):
        state1='Unchecked'
        state2='Unchecked'
        if self.b1.isChecked()==True:
          state1='Checked'
        else:
          state1='Unchecked'
        if self.b2.isChecked()==True:
          state2='Checked'
        else:
          state2='Unchecked'
        self.t1.setText("cb1 is {} cb2 is {}".format(state1,state2)) 


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

