# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CharCreation.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QMessageBox
import sqlite3

class Creation(QDialog):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(577, 406)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineCharCreationName = QtWidgets.QLineEdit(Form)
        self.lineCharCreationName.setObjectName("lineCharCreationName")
        self.horizontalLayout.addWidget(self.lineCharCreationName)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.lineCharCreationAge = QtWidgets.QLineEdit(Form)
        self.lineCharCreationAge.setObjectName("lineCharCreationAge")
        self.horizontalLayout_3.addWidget(self.lineCharCreationAge)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.lineCharCreationStatus = QtWidgets.QLineEdit(Form)
        self.lineCharCreationStatus.setObjectName("lineCharCreationStatus")
        self.horizontalLayout_4.addWidget(self.lineCharCreationStatus)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.lineCharCreationReligion = QtWidgets.QLineEdit(Form)
        self.lineCharCreationReligion.setObjectName("lineCharCreationReligion")
        self.horizontalLayout_5.addWidget(self.lineCharCreationReligion)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_6.addWidget(self.label_6)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.lineCharCreationStory = QtWidgets.QTextEdit(Form)
        self.lineCharCreationStory.setObjectName("lineCharCreationStory")
        self.horizontalLayout_7.addWidget(self.lineCharCreationStory)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.buttonCharCreationApply = QtWidgets.QPushButton(Form)
        self.buttonCharCreationApply.setObjectName("buttonCharCreationApply")
        self.horizontalLayout_8.addWidget(self.buttonCharCreationApply)
        self.verticalLayout.addLayout(self.horizontalLayout_8)

        #The Signal(s)

        self.buttonCharCreationApply.clicked.connect(self.createChar)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Charaktererstellung"))
        self.label.setText(_translate("Form", "Charaktername:"))
        self.label_2.setText(_translate("Form", "Optional"))
        self.label_3.setText(_translate("Form", "Alter     "))
        self.label_4.setText(_translate("Form", "Status   "))
        self.label_5.setText(_translate("Form", "Religion"))
        self.label_6.setText(_translate("Form", "Story:"))
        self.buttonCharCreationApply.setText(_translate("Form", "Übernehmen"))

    def createChar(self):

        charData = {
            "name" : str(self.lineCharCreationName.text()),
            "age" : str(self.lineCharCreationAge.text()),
            "gild" : "",
            "status" : str(self.lineCharCreationStatus.text()),
            "job" : "",
            "religion" : str(self.lineCharCreationReligion.text()),
            "rpitems" : "",
            "story" : str(self.lineCharCreationStory.toPlainText()),
            "alive" : 1
        }
        miscData = {
            "name" : str(self.lineCharCreationName.text()),
            "notes" : "",
            "design" : "None",
        }
        #Check the Input

        if charData["name"] == "":
            #if name empty, throw errorbox
            Creation.errorDetectet(self, "Fehler beim Namen", "Der Charakter muss mindestens einen Namen haben")
            return
        if charData["age"] != "":
            try:
                tmp = int(charData["age"])
            except:
                Creation.errorDetectet(self, "Fehler beim Alter", "Das Alter sollte nur aus Zahlen bestehen")
                return
            finally:
                charData["age"] = str(charData["age"])

        #Create the SQL statements
        sqlTest = "SELECT name FROM characters"
        sqlChar = "INSERT INTO characters VALUES(:name, :age, :gild, :status, :job, :religion, :rpitems, :story, :alive)"
        sqlMisc = "INSERT INTO misc VALUES(:name, :notes, :design)"
        connection = sqlite3.connect("../data/database.db")
        cursor = connection.cursor()

        #First, test if the Character already exists
        cursor.execute(sqlTest)
        testingTupel = cursor.fetchall()

        if any(charData["name"] in code for code in testingTupel):
            Creation.errorDetectet(self, "Keine Gute Idee...", "Ein Charakter mit diesem Namen existiert bereits.")
            return
        else:
            #Everything seems to be fine, lets pass the information to the database
            try:
                cursor.execute(sqlChar, charData)
                cursor.execute(sqlMisc, miscData)
                connection.commit()
                #Creation.errorDetectet(self, "Geschafft!", "Es scheint alles funktiert zu haben :)\n"
                #"Du kannst das Fenser Schließen.\nViel Spaß!")
                self.errorDetectet("Yiha.", "Scheint funktioniert zu haben! Have fun :3")

            except:
                Creation.errorDetectet(self, "Oh Oh...", "Da ging was schief...\nIst die Datenbank noch da?")
            return

    def errorDetectet(self, title, message):

        msgBox = QMessageBox()
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.exec()
        return



class CharCreation(QDialog):


    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Creation()
        self.ui.setupUi(self)

