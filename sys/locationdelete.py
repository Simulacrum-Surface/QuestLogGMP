# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LocationDelete.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

import sqlite3
import swapspace


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QMessageBox


class DeletePlace(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(397, 203)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.linePlaceName = QtWidgets.QLineEdit(Form)
        self.linePlaceName.setObjectName("linePlaceName")
        self.verticalLayout.addWidget(self.linePlaceName)
        self.buttonAccept = QtWidgets.QPushButton(Form)
        self.buttonAccept.setObjectName("buttonAccept")
        self.verticalLayout.addWidget(self.buttonAccept)

        self.buttonAccept.clicked.connect(self.deleteLocation)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Quest löschen"))
        self.label.setText(_translate("Form", "Name der Orts:\n"
            "WARNUNG! Alle Quests in diesem Ort werden entfernt"))
        self.buttonAccept.setText(_translate("Form", "Ort löschen"))

        return


    def deleteLocation(self):

        connection = sqlite3.connect("../data/database.db")
        cursor = connection.cursor()

        locationName = str(self.linePlaceName.text())

        try:
            sql = "SELECT name FROM locations"
            cursor.execute(sql)
            existingLocations = cursor.fetchall()

            if any(locationName in code for code in existingLocations):
                data = {"name": locationName, "charname": swapspace.activeChar["name"]}
                sql = "DELETE FROM locations WHERE name=(:name) AND char=(:charname)"
                cursor.execute(sql, data)
                connection.commit()

                data2 = {"location" : locationName, "charname": swapspace.activeChar["name"]}
                sql2 = "DELETE FROM quests WHERE location=(:location) AND char=(:charname)"
                cursor.execute(sql, data)
                connection.commit()
                self.errorDetectet("Ort löschen", "Der Ort" + locationName + " wurde aus der Datenbank entfernt")

            else:
                self.errorDetectet("Ort löschen", "Es wurde kein Ort mit diesem Namen gefunden")
                return

        except:
            return

        return

    def errorDetectet(self, title, message):
        msgBox = QMessageBox()
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.exec()
        return



class LocationDelete(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = DeletePlace()
        self.ui.setupUi(self)

