# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QComboBox.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.t1 = QtWidgets.QLineEdit(Form)
        self.t1.setObjectName("t1")
        self.horizontalLayout.addWidget(self.t1)
        self.b1 = QtWidgets.QPushButton(Form)
        self.b1.setObjectName("b1")
        self.horizontalLayout.addWidget(self.b1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.combo1 = QtWidgets.QComboBox(Form)
        self.combo1.setObjectName("combo1")
        self.combo1.addItem("")
        self.combo1.addItem("")
        self.combo1.addItem("")
        self.combo1.addItem("")
        self.horizontalLayout_3.addWidget(self.combo1)
        spacerItem = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.b2 = QtWidgets.QPushButton(Form)
        self.b2.setObjectName("b2")
        self.horizontalLayout_3.addWidget(self.b2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.t2 = QtWidgets.QLineEdit(Form)
        self.t2.setObjectName("t2")
        self.verticalLayout.addWidget(self.t2)
        self.b2.clicked.connect(self.rmitem)
        self.b1.clicked.connect(self.additem) 


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.b1.setText(_translate("Form", "Add"))
        self.combo1.setItemText(0, _translate("Form", "C"))
        self.combo1.setItemText(1, _translate("Form", "C++"))
        self.combo1.setItemText(2, _translate("Form", "Java"))
        self.combo1.setItemText(3, _translate("Form", "Python"))
        self.b2.setText(_translate("Form", "Remove"))

    def rmitem(self):
        indx=self.combo1.currentIndex()
        item=self.combo1.currentText()
        self.t2.setText(item+" is removed from combobox")
        self.combo1.removeItem(indx)
    def additem(self):
        self.combo1.addItem(self.t1.text())
        self.t2.setText(self.t1.text()+" is added to combobox") 


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

