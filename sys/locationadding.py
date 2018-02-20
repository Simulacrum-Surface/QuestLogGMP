# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LocationAdding.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QMessageBox
import sqlite3
import re
import swapspace

class Location(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 104)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.locationToAdd = QtWidgets.QLineEdit(Form)
        self.locationToAdd.setObjectName("locationToAdd")
        self.verticalLayout.addWidget(self.locationToAdd)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.buttonAddLocation = QtWidgets.QPushButton(Form)
        self.buttonAddLocation.setObjectName("buttonAddLocation")
        self.horizontalLayout.addWidget(self.buttonAddLocation)
        self.buttonStop = QtWidgets.QPushButton(Form)
        self.buttonStop.setObjectName("buttonStop")
        self.horizontalLayout.addWidget(self.buttonStop)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.buttonAddLocation.clicked.connect(self.addLocation)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Ort hinzufügen"))
        self.buttonAddLocation.setText(_translate("Form", "Ort hinzufügen"))
        self.buttonStop.setText(_translate("Form", "Abbrechen"))


    def addLocation(self):

        connection = sqlite3.connect("../data/database.db")
        cursor = connection.cursor()

        name = str(self.locationToAdd.text())

        regexp = re.compile(r"[a-zA-Z]+")
        nameOK = re.match(regexp, name)

        #Test the location name (already existing?)

        data = {"name": name, "char": swapspace.activeChar["name"]}
        sql = "SELECT name FROM locations WHERE name=(:name) AND char=(:char)"

        try:
            cursor.execute(sql, data)
            testdata = cursor.fetchall()

            if len(testdata) != 0:
                self.errorDetectet("Ort hinzufügen", "Es gibt bereits einen Ort mit diesem Namen")
            else:
                data = {"name": name, "char": swapspace.activeChar["name"]}
                sql = "INSERT INTO locations VALUES(:name, :char)"
                if nameOK:
                    try:
                        cursor.execute(sql, data)
                        connection.commit()
                    except:
                        self.errorDetectet("Ort hinzufügen", "Da hat was nicht geklappt")
                else:
                    self.errorDetectet("Ort hinzufügen", "Der Name darf nur aus Groß- und Kleinbuchstaben bestehen.")
                return
        except:
            self.errorDetectet("LocationChecking", "checking the location name failed")





    def errorDetectet(self, title, message):

        msgBox = QMessageBox()
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.exec()
        return



class LocationAdding(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Location()
        self.ui.setupUi(self)

