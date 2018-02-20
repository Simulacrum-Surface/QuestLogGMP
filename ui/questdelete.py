# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'questDelete.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(645, 463)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.listQuestDelete = QtWidgets.QListWidget(Form)
        self.listQuestDelete.setObjectName("listQuestDelete")
        self.verticalLayout.addWidget(self.listQuestDelete)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.buttonDelete = QtWidgets.QPushButton(Form)
        self.buttonDelete.setObjectName("buttonDelete")
        self.horizontalLayout.addWidget(self.buttonDelete)
        self.buttonCancel = QtWidgets.QPushButton(Form)
        self.buttonCancel.setObjectName("buttonCancel")
        self.horizontalLayout.addWidget(self.buttonCancel)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.buttonDelete.setText(_translate("Form", "Löschen"))
        self.buttonCancel.setText(_translate("Form", "Abbrechen"))

