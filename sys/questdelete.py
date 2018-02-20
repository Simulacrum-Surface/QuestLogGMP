# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QuestDelete.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

import sqlite3

import swapspace

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QMessageBox


class DeleteQuest(object):
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

        self.buttonDelete.clicked.connect(self.do)
        self.buttonCancel.clicked.connect(self.fillList)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.buttonDelete.setText(_translate("Form", "Löschen"))
        self.buttonCancel.setText(_translate("Form", "Abbrechen"))


    def fillList(self):
        self.listQuestDelete.clear()
        sql = "SELECT name FROM quests WHERE char=(:activechar)"
        data = {"activechar" : swapspace.activeChar["name"]}

        try:
            print(sql, data["activechar"])
            self.cursor.execute(sql, data)
            print("penis")
            questlist = self.cursor.fetchall()
        except:
            print("wrong SQL query")

        for x in questlist:
            name, = x
            self.listQuestDelete.addItem(name)
            #self.item_0.setText(0, x)

        return


    def do(self):

        connection = sqlite3.connect("../data/database.db")
        cursor = connection.cursor()

        questName = str(self.lineQuestName.text())

        try:
            sql = "SELECT name FROM quests"
            cursor.execute(sql)
            existingQuests = cursor.fetchall()

            if any(questName in code for code in existingQuests):
                data = {"name" : questName, "charname" : swapspace.activeChar["name"]}
                sql = "DELETE FROM quests WHERE name=(:name) AND char=(:charname)"

                cursor.execute(sql, data)
                connection.commit()
                self.errorDetectet("Quest löschen", "Die Quest " + questName + " wurde aus der Datenbank entfernt")

            else:
                self.errorDetectet("Quest löschen", "Es wurde keine Quest mit diesem Namen gefunden")
                return

        except:
            return

    def errorDetectet(self, title, message):
        msgBox = QMessageBox()
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.exec()
        return



class QuestDelete(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = DeleteQuest()
        self.ui.setupUi(self)

