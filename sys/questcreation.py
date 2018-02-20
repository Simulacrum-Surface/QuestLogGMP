# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QuestAdding.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!
import re
import sqlite3
import swapspace

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QMessageBox


class Quest(object):

    connection = sqlite3.connect("../data/database.db")
    cursor = connection.cursor()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(687, 548)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_8.addWidget(self.label_8)
        self.lineQuestname = QtWidgets.QLineEdit(Form)
        self.lineQuestname.setObjectName("lineQuestname")
        self.horizontalLayout_8.addWidget(self.lineQuestname)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.lineClient = QtWidgets.QLineEdit(Form)
        self.lineClient.setObjectName("lineClient")
        self.horizontalLayout.addWidget(self.lineClient)
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineDeadline = QtWidgets.QLineEdit(Form)
        self.lineDeadline.setObjectName("lineDeadline")
        self.horizontalLayout.addWidget(self.lineDeadline)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.lineItems = QtWidgets.QLineEdit(Form)
        self.lineItems.setObjectName("lineItems")
        self.horizontalLayout_2.addWidget(self.lineItems)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.lineReward = QtWidgets.QLineEdit(Form)
        self.lineReward.setObjectName("lineReward")
        self.horizontalLayout_3.addWidget(self.lineReward)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setContentsMargins(-1, -1, -1, 10)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_7.addWidget(self.label_7)
        self.listExistingQuests = QtWidgets.QListWidget(Form)
        self.listExistingQuests.setObjectName("listExistingQuests")
        self.horizontalLayout_7.addWidget(self.listExistingQuests)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_6.addWidget(self.label_5)
        self.lineDescription = QtWidgets.QTextEdit(Form)
        self.lineDescription.setObjectName("lineDescription")
        self.horizontalLayout_6.addWidget(self.lineDescription)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_5.addWidget(self.label_6)
        self.lineDetails = QtWidgets.QTextEdit(Form)
        self.lineDetails.setObjectName("lineDetails")
        self.horizontalLayout_5.addWidget(self.lineDetails)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.buttonDone = QtWidgets.QPushButton(Form)
        self.buttonDone.setObjectName("buttonDone")
        self.horizontalLayout_4.addWidget(self.buttonDone)
        self.buttonRefresh = QtWidgets.QPushButton(Form)
        self.buttonRefresh.setObjectName("buttonCancel")
        self.horizontalLayout_4.addWidget(self.buttonRefresh)
        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.buttonDone.clicked.connect(self.createQuest)
        self.buttonRefresh.clicked.connect(self.fillList)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Neue Quest"))
        self.label_8.setText(_translate("Form", "Questname          "))
        self.label_2.setText(_translate("Form", "Auftraggeber       "))
        self.label.setText(_translate("Form", "DeadLine"))
        self.label_3.setText(_translate("Form", "Benötigte Items   "))
        self.label_4.setText(_translate("Form", "Belohnung           "))
        self.label_7.setText(_translate("Form", "Ort:                      "))
        self.label_5.setText(_translate("Form", "Beschreibung  "))
        self.label_6.setText(_translate("Form", "Details            "))
        self.buttonDone.setText(_translate("Form", "Fertig"))
        self.buttonRefresh.setText(_translate("Form", "Orte aktualisieren"))

        self.fillList()



    def fillList(self):
        self.listExistingQuests.clear()
        sql = "SELECT name FROM locations WHERE char=(:activechar)"
        data = {"activechar" : swapspace.activeChar["name"]}

        try:
            self.cursor.execute(sql, data)
            locationList = self.cursor.fetchall()
        except:
            print("wrong SQL query")

        for x in locationList:
            name, = x
            self.listExistingQuests.addItem(name)
            #self.item_0.setText(0, x)

        return


    def createQuest(self):
        data = {
            "name" : str(self.lineQuestname.text()),
            "location" : str(self.listExistingQuests.currentItem().text()),
            "char" : swapspace.activeChar["name"],
            "client" : str(self.lineClient.text()),
            "deadline" : str(self.lineDeadline.text()),
            "items" : str(self.lineItems.text()),
            "reward" : str(self.lineReward.text()),
            "description" : str(self.lineDescription.toPlainText()),
            "details" : str(self.lineDetails.toPlainText()),
            "status" : 0
        }

        # Check if the Questname is already existing

        sql = "SELECT name FROM quests WHERE char=(:charname)"
        checkData = {"charname" : swapspace.activeChar["name"]}
        nameToCompare = str(self.lineQuestname.text())

        try:
            self.cursor.execute(sql, checkData)
            tmp = self.cursor.fetchall()
        except:
            print("sql ind questcreation (test for existing questname) failed")
        print(tmp)
        if any(nameToCompare in code for code in tmp):
            self.errorDetectet("Questerstellung", "Dieser Questname ist bereits vorhanden.\n"
                                                  "Bitte wähle einen einzigartigen")
            return

        else:
            locationCheck = re.compile(r"[a-zA-Z]+")
            locationOK = locationCheck.match(data["name"])

            if locationOK:
                locationName= {"name" : data["location"]}
                sql = "SELECT name FROM locations WHERE name=(:name)"
                self.cursor.execute(sql, locationName)
                locationExisting = self.cursor.fetchall()
                print(locationExisting)
                if len(locationExisting) != 0:
                    try:
                        sql = "INSERT INTO quests VALUES(:name, :location, :char, :client, :deadline, " \
                              ":items, :reward, :description, :details, :status)"
                        self.cursor.execute(sql, data)
                        self.connection.commit()
                    except:
                        print("Error while writing data to the database")

                else:
                    self.errorDetectet("Quest erstellen", "Diesen Ort gibt es nicht.")

            else:
                self.errorDetectet("Quest erstellen", "Das ist ein ungültiger QuestName. Nur Buchstaben sind erlaubt.")



            return

    def errorDetectet(self, title, message):

        msgBox = QMessageBox()
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.exec()
        return



class QuestAdding(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Quest()
        self.ui.setupUi(self)

