# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../ui/LocationAdding.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!
import sqlite3
import swapspace
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QDialog


class Loading(object):

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(338, 208)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.listLoading = QtWidgets.QListWidget(Form)
        self.listLoading.setObjectName("listLoading")
        self.verticalLayout.addWidget(self.listLoading)
        self.loadingButton = QtWidgets.QPushButton(Form)
        self.loadingButton.setObjectName("loadingButton")
        self.verticalLayout.addWidget(self.loadingButton)

        self.refreshButton = QtWidgets.QPushButton(Form)
        self.refreshButton.setObjectName("refreshButton")
        self.verticalLayout.addWidget(self.refreshButton)

        self.loadChar()

        self.loadingButton.clicked.connect(self.commit)
        self.refreshButton.clicked.connect(self.loadChar)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Charackter laden"))
        self.loadingButton.setText(_translate("Form", "Charakter laden"))
        self.refreshButton.setText(_translate("Form", "Liste aktualisieren"))




    def loadChar(self):

        connection = sqlite3.connect("../data/database.db")
        cursor = connection.cursor()

        # Get some space
        self.listLoading.clear()

        # Get the SQL done
        try:
            sql = "SELECT name FROM characters"
            cursor.execute(sql)
            loadCharsTupel = cursor.fetchall()
            loadCharsList = []
            for y in loadCharsTupel:
                for m in y:
                    loadCharsList.append(m)


            for b in loadCharsList:
                self.item_0 = QtWidgets.QListWidgetItem(self.listLoading)
                self.listLoading.addItem(self.item_0)
                self.item_0.setText(b)
        except:
            print("failure")
        return


    def commit(self): # Gets to run when the "load" button is clicked

        connection = sqlite3.connect("../data/database.db")
        cursor = connection.cursor()

        try:
            data = {"name" : str(self.listLoading.currentItem().text())}

            sqlChar = "SELECT * FROM characters WHERE name=(:name)"
            cursor.execute(sqlChar, data)
            charValues = cursor.fetchall()
            # values is now the tupel containing all the char data
            name, age, gild, status, job, religion, rpitems, story, alive = charValues[0]

            # Lets make this knowledge accessible for the other classes
            swapspace.activeChar = {
                "name": name,
                "age": age,
                "gild": gild,
                "status": status,
                "job": job,
                "religion": religion,
                "rpitems": rpitems,
                "story": story,
                "alive": 1
            }
            sqlMisc = "SELECT * FROM misc WHERE char=(:name)"
            cursor.execute(sqlMisc, data)
            miscValue = cursor.fetchall()
            char, notes, design = miscValue[0]
            swapspace.activeMisc = {
                "char": char,
                "notes": notes,
                "design": design
            }

        except:
            print("failure")
        return
    """
    def loadChar(self):
        connection = sqlite3.connect("../data/database.db")
        cursor = connection.cursor()
        # TODO fix this shit, it crashes when a user attempts to load a char that doesnt exist.

        try:
            # First, get the Name from the textLine
            charData = {"name" : str(self.charToLoad.text())}
            #Now Check if the Char is existing
            sqlTest = "SELECT name FROM characters"
            cursor.execute(sqlTest)
            testTupel = cursor.fetchall()
            if any(charData["name"] in code for code in testTupel):
                # Seems to be existing :)
                # Now, lets get the Data from the Char

                sqlChar = "SELECT * FROM characters WHERE name=(:name)"
                cursor.execute(sqlChar, charData)
                charValues = cursor.fetchall()
                # values is now the tupel containing all the char data
                name, age, gild, status, job, religion, rpitems, story, alive = charValues[0]

                # Lets make this knowledge accessible for the other classes
                swapspace.activeChar = {
                    "name": name,
                    "age": age,
                    "gild": gild,
                    "status": status,
                    "job": job,
                    "religion": religion,
                    "rpitems": rpitems,
                    "story": story,
                    "alive": 1
                }
                sqlMisc = "SELECT * FROM misc WHERE char=(:name)"
                cursor.execute(sqlMisc, charData)
                miscValue = cursor.fetchall()
                char, notes, design = miscValue[0]
                swapspace.activeMisc = {
                    "char": char,
                    "notes": notes,
                    "design": design
                }
            else:
                Loading.errorDetectet(self, "Fehler", "Dieser Charakter existiert nicht.")
                return
        except:
            self.errorDetectet("Charakter laden", "Dieser Charakter scheint nicht zu existieren")


        return
    """
    def errorDetectet(self, title, message):

        msgBox = QMessageBox()
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.exec()
        return



class CharLoading(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Loading()
        self.ui.setupUi(self)

