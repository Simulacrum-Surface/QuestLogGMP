# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CharDelete.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

import sqlite3
import swapspace

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QMessageBox


class CharDelete(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(397, 203)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.lineCharName = QtWidgets.QLineEdit(Form)
        self.lineCharName.setObjectName("linePlaceName")
        self.verticalLayout.addWidget(self.lineCharName)
        self.buttonAccept = QtWidgets.QPushButton(Form)
        self.buttonAccept.setObjectName("buttonAccept")
        self.verticalLayout.addWidget(self.buttonAccept)


        self.buttonAccept.clicked.connect(self.deleteChar)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def deleteChar(self):
        connection = sqlite3.connect("../data/database.db")
        cursor = connection.cursor()

        sqlTest = "SELECT name FROM characters"
        currentChar = swapspace.activeChar["name"]
        charToDelete = str(self.lineCharName.text())

        if charToDelete != currentChar:
            try:
                cursor.execute(sqlTest)
                nameListCheck = cursor.fetchall()
                if any(charToDelete in code for code in nameListCheck):
                    data = {"name" : charToDelete}
                    sqlFinalCHARS = "DELETE FROM characters WHERE name=(:name)"
                    sqlFinalQUESTS = "DELETE FROM quests WHERE char=(:name)"
                    sqlFinalLOCATIONS = "DELETE FROM locations WHERE char=(:name)"

                    cursor.execute(sqlFinalCHARS, data)
                    connection.commit()

                    cursor.execute(sqlFinalQUESTS, data)
                    connection.commit()

                    cursor.execute(sqlFinalLOCATIONS, data)
                    connection.commit()

                    self.errorDetectet("Char gelöscht", "Der Charakter wurder erfolgreich aus der Datenbank entfernt")

            except:
                self.errorDetectet("Charakter löschen", "Der Charakter scheint nicht zu existieren")

        else:
            self.errorDetectet("Char löschen", "Der zu löschenden Char darf nicht geladen sein")
        return

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Quest löschen"))
        self.label.setText(_translate("Form", "Name des Charakters:\n"
"WARNUNG! Alle Quests, alle Orte werde entfernt."))
        self.buttonAccept.setText(_translate("Form", "Charakter löschen"))

    def errorDetectet(self, title, message):

        msgBox = QMessageBox()
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.exec()
        return



class DeleteChar(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = CharDelete()
        self.ui.setupUi(self)


