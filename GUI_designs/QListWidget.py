# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QListWidget.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(827, 755)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(9, 9, 801, 411))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.verticalLayoutWidget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.list1 = QtWidgets.QListWidget(self.verticalLayoutWidget)
        self.list1.setObjectName("list1")
        item = QtWidgets.QListWidgetItem()
        self.list1.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.list1.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.list1.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.list1.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.list1.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.list1.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.list1.addItem(item)
        self.horizontalLayout_3.addWidget(self.list1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.list2 = QtWidgets.QListWidget(self.verticalLayoutWidget)
        self.list2.setObjectName("list2")
        self.horizontalLayout_3.addWidget(self.list2)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 450, 771, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.list1.itemDoubleClicked.connect(self.removelist1)
        self.list2.itemDoubleClicked.connect(self.removelist2) 

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        __sortingEnabled = self.list1.isSortingEnabled()
        self.list1.setSortingEnabled(False)
        item = self.list1.item(0)
        item.setText(_translate("Form", "Kohli"))
        item = self.list1.item(1)
        item.setText(_translate("Form", "Dhoni"))
        item = self.list1.item(2)
        item.setText(_translate("Form", "Rohit"))
        item = self.list1.item(3)
        item.setText(_translate("Form", "Rahane"))
        item = self.list1.item(4)
        item.setText(_translate("Form", "Bhuvaneshwar"))
        item = self.list1.item(5)
        item.setText(_translate("Form", "Ashwin"))
        item = self.list1.item(6)
        item.setText(_translate("Form", "Jadeja"))
        self.list1.setSortingEnabled(__sortingEnabled)
        self.label_2.setText(_translate("Form", "               Available Players"))
        self.label_3.setText(_translate("Form", "                  Selected Players"))

    def removelist1(self, item): 
        self.list1.takeItem(self.list1.row(item))
        self.list2.addItem(item.text())

    def removelist2(self, item):
        self.list2.takeItem(self.list2.row(item))
        self.list1.addItem(item.text()) 


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

