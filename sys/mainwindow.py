#! /usr/bin/python
#!-*- coding: utf-8 -*-


"""
TODO:

necessery:
    b4 beta:
    - Automaticly closing windows # CHRIIIIIIIIIIS :D


    while beta:
    - about this programm


optional:

    - implement styles
    - implement IG time
    - implement popup for PM in board
    - implement playerslist

"""

import charcreation
import datahandler
import locationadding
import charloading
import swapspace
import questcreation
import questdelete
import locationdelete
import chardelete

import webbrowser
import sqlite3


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QMessageBox



class MainClass(object):

    print("calling datahandler")
    datahandler.checkExistingDatabase()



    connection = sqlite3.connect("../data/database.db")
    cursor = connection.cursor()


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1080, 791)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabQuests = QtWidgets.QTabWidget(self.centralwidget)
        self.tabQuests.setObjectName("tabQuests")
        self.QuestTab = QtWidgets.QWidget()
        self.tabQuests.setEnabled(False)
        self.QuestTab.setObjectName("QuestTab")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.QuestTab)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.QuestTab)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setIndent(-1)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.treeQuests = QtWidgets.QTreeWidget(self.QuestTab)
        self.treeQuests.setObjectName("treeQuests")
        #item_0 = QtWidgets.QTreeWidgetItem(self.treeQuests)
        #item_1 = QtWidgets.QTreeWidgetItem(item_0)
        #item_1 = QtWidgets.QTreeWidgetItem(item_0)
        #item_0 = QtWidgets.QTreeWidgetItem(self.treeQuests)
        #item_1 = QtWidgets.QTreeWidgetItem(item_0)
        #item_0 = QtWidgets.QTreeWidgetItem(self.treeQuests)
        self.gridLayout.addWidget(self.treeQuests, 1, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(5, -1, 5, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.buttonNewPlace = QtWidgets.QPushButton(self.QuestTab)
        self.buttonNewPlace.setObjectName("buttonNewPlace")
        self.horizontalLayout_2.addWidget(self.buttonNewPlace)
        self.buttonDeletePlace = QtWidgets.QPushButton(self.QuestTab)
        self.buttonDeletePlace.setObjectName("buttonDeletePlace")
        self.horizontalLayout_2.addWidget(self.buttonDeletePlace)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.buttonNewQuest = QtWidgets.QPushButton(self.QuestTab)
        self.buttonNewQuest.setObjectName("buttonNewQuest")
        self.horizontalLayout_2.addWidget(self.buttonNewQuest)
        self.buttonQuestDone = QtWidgets.QPushButton(self.QuestTab)
        self.buttonQuestDone.setObjectName("buttonQuestDone")
        self.horizontalLayout_2.addWidget(self.buttonQuestDone)
        self.buttonQuestFailed = QtWidgets.QPushButton(self.QuestTab)
        self.buttonQuestFailed.setObjectName("buttonQuestFailed")
        self.horizontalLayout_2.addWidget(self.buttonQuestFailed)
        self.buttonQuestDelete = QtWidgets.QPushButton(self.QuestTab)
        self.buttonQuestDelete.setObjectName("buttonQuestDelete")
        self.horizontalLayout_2.addWidget(self.buttonQuestDelete)
        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setContentsMargins(10, 10, 10, 10)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.textQuestDetails = QtWidgets.QTextEdit(self.QuestTab)
        self.textQuestDetails.setObjectName("textQuestDetails")
        self.gridLayout_2.addWidget(self.textQuestDetails, 9, 0, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.QuestTab)
        self.label_16.setObjectName("label_16")
        self.gridLayout_2.addWidget(self.label_16, 8, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.QuestTab)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_7 = QtWidgets.QLabel(self.QuestTab)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_6.addWidget(self.label_7)
        self.lineQuestRewards = QtWidgets.QLineEdit(self.QuestTab)
        self.lineQuestRewards.setObjectName("lineQuestRewards")
        self.horizontalLayout_6.addWidget(self.lineQuestRewards)
        self.gridLayout_2.addLayout(self.horizontalLayout_6, 5, 0, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.QuestTab)
        self.label_15.setObjectName("label_15")
        self.gridLayout_2.addWidget(self.label_15, 6, 0, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_6 = QtWidgets.QLabel(self.QuestTab)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_5.addWidget(self.label_6)
        self.lineQuestItems = QtWidgets.QLineEdit(self.QuestTab)
        self.lineQuestItems.setObjectName("lineQuestItems")
        self.horizontalLayout_5.addWidget(self.lineQuestItems)
        self.gridLayout_2.addLayout(self.horizontalLayout_5, 4, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lineQuestClient = QtWidgets.QLineEdit(self.QuestTab)
        self.lineQuestClient.setObjectName("lineQuestClient")
        self.horizontalLayout_4.addWidget(self.lineQuestClient)
        self.lineQuestDeadline = QtWidgets.QLineEdit(self.QuestTab)
        self.lineQuestDeadline.setObjectName("lineQuestDeadline")
        self.horizontalLayout_4.addWidget(self.lineQuestDeadline)
        #self.lineQuestRemainingTime = QtWidgets.QLineEdit(self.QuestTab)
        #self.lineQuestRemainingTime.setEnabled(False)
        #self.lineQuestRemainingTime.setObjectName("lineQuestRemainingTime")
        #self.horizontalLayout_4.addWidget(self.lineQuestRemainingTime)
        self.gridLayout_2.addLayout(self.horizontalLayout_4, 3, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_5 = QtWidgets.QLabel(self.QuestTab)
        self.label_5.setTextFormat(QtCore.Qt.AutoText)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.label_4 = QtWidgets.QLabel(self.QuestTab)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        #self.label_3 = QtWidgets.QLabel(self.QuestTab)
        #self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        #self.label_3.setObjectName("label_3")
        #self.horizontalLayout_3.addWidget(self.label_3)
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)
        self.buttonSaveQuestChanges = QtWidgets.QPushButton(self.QuestTab)
        self.buttonSaveQuestChanges.setObjectName("buttonSaveQuestChanges")
        self.gridLayout_2.addWidget(self.buttonSaveQuestChanges, 10, 0, 1, 1)
        self.textQuestDesription = QtWidgets.QTextEdit(self.QuestTab)
        self.textQuestDesription.setEnabled(True)
        self.textQuestDesription.setObjectName("textQuestDesription")
        self.gridLayout_2.addWidget(self.textQuestDesription, 7, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout_2)
        self.tabQuests.addTab(self.QuestTab, "")
        self.charTab = QtWidgets.QWidget()
        self.charTab.setObjectName("charTab")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.charTab)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_10 = QtWidgets.QLabel(self.charTab)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_7.addWidget(self.label_10)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem1)
        self.lineCharName = QtWidgets.QLineEdit(self.charTab)
        self.lineCharName.setEnabled(False)
        self.lineCharName.setObjectName("lineCharName")
        self.horizontalLayout_7.addWidget(self.lineCharName)
        self.verticalLayout_5.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_8 = QtWidgets.QLabel(self.charTab)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_9.addWidget(self.label_8)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem2)
        self.lineCharAge = QtWidgets.QLineEdit(self.charTab)
        self.lineCharAge.setObjectName("lineCharAge")
        self.horizontalLayout_9.addWidget(self.lineCharAge)
        self.verticalLayout_5.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_9 = QtWidgets.QLabel(self.charTab)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_10.addWidget(self.label_9)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem3)
        self.lineCharGild = QtWidgets.QLineEdit(self.charTab)
        self.lineCharGild.setObjectName("lineCharGild")
        self.horizontalLayout_10.addWidget(self.lineCharGild)
        self.verticalLayout_5.addLayout(self.horizontalLayout_10)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_11 = QtWidgets.QLabel(self.charTab)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_6.addWidget(self.label_11)
        self.textCharItems = QtWidgets.QTextEdit(self.charTab)
        self.textCharItems.setObjectName("textCharItems")
        self.verticalLayout_6.addWidget(self.textCharItems)
        self.label_12 = QtWidgets.QLabel(self.charTab)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_6.addWidget(self.label_12)
        self.textCharStory = QtWidgets.QTextEdit(self.charTab)
        self.textCharStory.setObjectName("textCharStory")
        self.verticalLayout_6.addWidget(self.textCharStory)
        self.verticalLayout_5.addLayout(self.verticalLayout_6)
        self.buttonSaveCharChanges = QtWidgets.QPushButton(self.charTab)
        self.buttonSaveCharChanges.setObjectName("buttonSaveCharChanges")
        self.verticalLayout_5.addWidget(self.buttonSaveCharChanges)
        self.horizontalLayout_8.addLayout(self.verticalLayout_5)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_17 = QtWidgets.QLabel(self.charTab)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_13.addWidget(self.label_17)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem4)
        self.lineCharStatus = QtWidgets.QLineEdit(self.charTab)
        self.lineCharStatus.setObjectName("lineCharStatus")
        self.horizontalLayout_13.addWidget(self.lineCharStatus)
        self.verticalLayout_3.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.label_19 = QtWidgets.QLabel(self.charTab)
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_15.addWidget(self.label_19)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem5)
        self.lineCharJob = QtWidgets.QLineEdit(self.charTab)
        self.lineCharJob.setObjectName("lineCharJob")
        self.horizontalLayout_15.addWidget(self.lineCharJob)
        self.verticalLayout_3.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_18 = QtWidgets.QLabel(self.charTab)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_14.addWidget(self.label_18)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem6)
        self.lineCharReligion = QtWidgets.QLineEdit(self.charTab)
        self.lineCharReligion.setObjectName("lineCharReligion")
        self.horizontalLayout_14.addWidget(self.lineCharReligion)
        self.verticalLayout_3.addLayout(self.horizontalLayout_14)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setContentsMargins(10, 12, 10, 10)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_13 = QtWidgets.QLabel(self.charTab)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_8.addWidget(self.label_13)
        self.listQuestsDone = QtWidgets.QListWidget(self.charTab)
        self.listQuestsDone.setObjectName("treeQuestsDone")
        self.verticalLayout_8.addWidget(self.listQuestsDone)
        self.label_14 = QtWidgets.QLabel(self.charTab)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_8.addWidget(self.label_14)
        self.textQuestDoneDetails = QtWidgets.QTextEdit(self.charTab)
        self.textQuestDoneDetails.setObjectName("textQuestDoneDetails")
        self.verticalLayout_8.addWidget(self.textQuestDoneDetails)
        self.verticalLayout_3.addLayout(self.verticalLayout_8)
        self.buttonCharOlder = QtWidgets.QPushButton(self.charTab)
        self.buttonCharOlder.setObjectName("buttonCharOlder")
        self.verticalLayout_3.addWidget(self.buttonCharOlder)
        self.horizontalLayout_8.addLayout(self.verticalLayout_3)
        self.tabQuests.addTab(self.charTab, "")
        self.tabNotes = QtWidgets.QWidget()
        self.tabNotes.setObjectName("tabNotes")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tabNotes)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.textNotes = QtWidgets.QTextEdit(self.tabNotes)
        self.textNotes.setObjectName("textNotes")
        self.gridLayout_3.addWidget(self.textNotes, 1, 0, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.tabNotes)
        self.label_21.setObjectName("label_21")
        self.gridLayout_3.addWidget(self.label_21, 0, 0, 1, 1)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.buttonNotesSave = QtWidgets.QPushButton(self.tabNotes)
        self.buttonNotesSave.setObjectName("buttonNotesSave")
        self.horizontalLayout_16.addWidget(self.buttonNotesSave)
        self.buttonNotesClear = QtWidgets.QPushButton(self.tabNotes)
        self.buttonNotesClear.setObjectName("buttonNotesClear")
        self.horizontalLayout_16.addWidget(self.buttonNotesClear)
        self.gridLayout_3.addLayout(self.horizontalLayout_16, 2, 0, 1, 1)
        self.tabQuests.addTab(self.tabNotes, "")
        self.tabMisc = QtWidgets.QWidget()
        self.tabMisc.setObjectName("tabMisc")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.tabMisc)
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.textAbout = QtWidgets.QTextEdit(self.tabMisc)
        self.textAbout.setEnabled(False)
        self.textAbout.setObjectName("textAbout")
        self.horizontalLayout_12.addWidget(self.textAbout)
        self.horizontalLayout_11.addLayout(self.horizontalLayout_12)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.checkStyle = QtWidgets.QCheckBox(self.tabMisc)
        self.checkStyle.setObjectName("checkStyle")
        self.verticalLayout_4.addWidget(self.checkStyle)
        self.radioAdanosStyle = QtWidgets.QRadioButton(self.tabMisc)
        self.radioAdanosStyle.setEnabled(False)
        self.radioAdanosStyle.setObjectName("radioAdanosStyle")
        self.verticalLayout_4.addWidget(self.radioAdanosStyle)
        self.radioBeliarStyle = QtWidgets.QRadioButton(self.tabMisc)
        self.radioBeliarStyle.setEnabled(False)
        self.radioBeliarStyle.setObjectName("radioBeliarStyle")
        self.verticalLayout_4.addWidget(self.radioBeliarStyle)
        self.radioInnosStyle = QtWidgets.QRadioButton(self.tabMisc)
        self.radioInnosStyle.setEnabled(False)
        self.radioInnosStyle.setObjectName("radioInnosStyle")
        self.verticalLayout_4.addWidget(self.radioInnosStyle)
        self.buttonCallBoard = QtWidgets.QPushButton(self.tabMisc)
        self.buttonCallBoard.setObjectName("buttonCallBoard")
        self.verticalLayout_4.addWidget(self.buttonCallBoard)
        self.buttonCallWiki = QtWidgets.QPushButton(self.tabMisc)
        self.buttonCallWiki.setObjectName("buttonCallWiki")
        self.verticalLayout_4.addWidget(self.buttonCallWiki)
        self.buttonGetTime = QtWidgets.QPushButton(self.tabMisc)
        self.buttonGetTime.setObjectName("buttonGetTime")
        self.verticalLayout_4.addWidget(self.buttonGetTime)
        self.buttonGetPlayers = QtWidgets.QPushButton(self.tabMisc)
        self.buttonGetPlayers.setObjectName("buttonGetPlayers")
        self.verticalLayout_4.addWidget(self.buttonGetPlayers)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem7)
        self.horizontalLayout_11.addLayout(self.verticalLayout_4)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem8)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(10, -1, -1, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_20 = QtWidgets.QLabel(self.tabMisc)
        self.label_20.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_20.setObjectName("label_20")
        self.verticalLayout_2.addWidget(self.label_20)
        self.textEdit_6 = QtWidgets.QTextEdit(self.tabMisc)
        self.textEdit_6.setEnabled(False)
        self.textEdit_6.setMaximumSize(QtCore.QSize(346, 748))
        self.textEdit_6.setStyleSheet("background-image: url(\"../img/mud.jpg\");\n"
"background-repeat: no-repeat;\n"
"")
        self.textEdit_6.setObjectName("textEdit_6")
        self.verticalLayout_2.addWidget(self.textEdit_6)
        self.horizontalLayout_11.addLayout(self.verticalLayout_2)
        self.tabQuests.addTab(self.tabMisc, "")
        self.verticalLayout.addWidget(self.tabQuests)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1080, 21))
        self.menubar.setObjectName("menubar")
        self.menuFunktionen = QtWidgets.QMenu(self.menubar)
        self.menuFunktionen.setObjectName("menuFunktionen")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNewChar = QtWidgets.QAction(MainWindow)
        self.actionNewChar.setObjectName("actionNewChar")
        self.actionSaveAll = QtWidgets.QAction(MainWindow)
        self.actionSaveAll.setObjectName("actionSaveAll")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionDeleteChar = QtWidgets.QAction(MainWindow)
        self.actionDeleteChar.setObjectName("actionDeleteChar")
        self.actionLoadChar = QtWidgets.QAction(MainWindow)
        self.actionLoadChar.setObjectName("actionLoadChar")
        self.menuFunktionen.addAction(self.actionNewChar)
        self.menuFunktionen.addAction(self.actionSaveAll)
        self.menuFunktionen.addAction(self.actionLoadChar)
        self.menuFunktionen.addAction(self.actionDeleteChar)
        self.menuFunktionen.addSeparator()
        self.menuFunktionen.addAction(self.actionExit)
        self.menubar.addAction(self.menuFunktionen.menuAction())

        # The Windows ... and stuff
        self.charCreationWindow = charcreation.CharCreation()
        self.charLoadingWindow = charloading.CharLoading()
        self.locationAddingWindow = locationadding.LocationAdding()
        self.questAddingWindow = questcreation.QuestAdding()
        self.questDeletingWindow = questdelete.QuestDelete()
        self.locationDeletingWindow = locationdelete.LocationDelete()
        self.charDeleteWindow = chardelete.DeleteChar()

        self.treeQuests.setSortingEnabled(True)


        ##################################################
        # Connecting Signals and Slots                   #
        ##################################################

        #The Menu
        self.actionNewChar.triggered.connect(self.newChar)
        self.actionLoadChar.triggered.connect(self.loadChar)
        self.actionDeleteChar.triggered.connect(self.deleteChar)
        self.actionSaveAll.triggered.connect(self.saveAll)

        self.actionExit.triggered.connect(exit)

        self.actionSaveAll.setEnabled(False)
        #The Item Signals
        self.treeQuests.itemSelectionChanged.connect(self.itemSelection)
        self.listQuestsDone.itemSelectionChanged.connect(self.detailsAlumini)

        #The Buttons in Tab Misc
        self.buttonNotesSave.clicked.connect(self.saveMisc)
        self.buttonNotesClear.clicked.connect(self.clearMisc)

        #The Buttons in Tab Char
        self.buttonSaveCharChanges.clicked.connect(self.saveCharData)
        self.buttonCharOlder.clicked.connect(self.makeCharOlder)

        #The Buttons in Tab Quests
        self.buttonNewPlace.clicked.connect(self.newPlace)
        self.buttonDeletePlace.clicked.connect(self.deletePlace)

        self.buttonNewQuest.clicked.connect(self.newQuest)
        self.buttonQuestDone.clicked.connect(self.questDone)
        self.buttonQuestFailed.clicked.connect(self.questFailed)
        self.buttonSaveQuestChanges.clicked.connect(self.questChanged)
        self.buttonQuestDelete.clicked.connect(self.questDelete)

        #The Buttons in Tab Other
        self.buttonCallBoard.clicked.connect(self.callBoard)
        self.buttonCallWiki.clicked.connect(self.callWiki)
        self.checkStyle.stateChanged.connect(self.enableStyle)

        #self.buttonGetTime.clicked.connect(self.getTime)
        #self.buttonGetPlayers.clicked.connect(self.getPlayers)


        # Disable forthcoming features
        self.buttonGetPlayers.setEnabled(False)
        self.buttonGetTime.setEnabled(False)


        self.radioAdanosStyle.toggled.connect(self.setStyle)
        self.radioBeliarStyle.toggled.connect(self.setStyle)
        self.radioInnosStyle.toggled.connect(self.setStyle)


        self.retranslateUi(MainWindow)
        self.tabQuests.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "GMP - Questlog v1.0"))
        self.label.setText(_translate("MainWindow", "Übersicht"))
        self.treeQuests.headerItem().setText(0, _translate("MainWindow", "Quests"))
        __sortingEnabled = self.treeQuests.isSortingEnabled()
        self.treeQuests.setSortingEnabled(False)
        self.buttonNewPlace.setText(_translate("MainWindow", "Neuer Ort"))
        self.buttonDeletePlace.setText(_translate("MainWindow", "Ort löschen"))
        self.buttonNewQuest.setToolTip(_translate("MainWindow", "<html><head/><body><p>Neue Quest erstellen</p></body></html>"))
        self.buttonNewQuest.setText(_translate("MainWindow", "Neue Quest"))
        self.buttonQuestDone.setToolTip(_translate("MainWindow", "<html><head/><body><p>Quest als erledigt markieren</p></body></html>"))
        self.buttonQuestDone.setText(_translate("MainWindow", "Quest Erledigt"))
        self.buttonQuestFailed.setText(_translate("MainWindow", "Quest Gescheitert"))
        self.buttonQuestDelete.setToolTip(_translate("MainWindow", "<html><head/><body><p>Quest permanent löschen</p></body></html>"))
        self.buttonQuestDelete.setText(_translate("MainWindow", "Quest Löschen"))
        self.label_16.setText(_translate("MainWindow", "Details, weiter Infos:"))
        self.label_2.setText(_translate("MainWindow", "Details"))
        self.label_7.setText(_translate("MainWindow", "Belohnung:          "))
        self.label_15.setText(_translate("MainWindow", "Beschreibung"))
        self.label_6.setText(_translate("MainWindow", "Benötigte Items: "))
        self.label_5.setText(_translate("MainWindow", "Auftraggeber"))
        self.label_4.setText(_translate("MainWindow", "DeadLine"))
        #self.label_3.setText(_translate("MainWindow", "Übrige Zeit"))
        self.buttonSaveQuestChanges.setText(_translate("MainWindow", "Bearbeitetes Speichern"))
        self.textQuestDesription.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.tabQuests.setTabText(self.tabQuests.indexOf(self.QuestTab), _translate("MainWindow", "Quests"))
        self.label_10.setText(_translate("MainWindow", "Name"))
        self.label_8.setText(_translate("MainWindow", "Alter "))
        self.label_9.setText(_translate("MainWindow", "Gilde "))
        self.label_11.setText(_translate("MainWindow", "RP-Items:"))
        self.label_12.setText(_translate("MainWindow", "Charakter-Story:"))
        self.buttonCharOlder.setText(_translate("MainWindow", "Alter erhöhen"))
        self.label_17.setText(_translate("MainWindow", "Status  "))
        self.label_19.setText(_translate("MainWindow", "Beruf    "))
        self.label_18.setText(_translate("MainWindow", "Glaube "))
        self.label_13.setText(_translate("MainWindow", "Erledigte Quests:"))
        self.label_14.setText(_translate("MainWindow", "Quest-Details:"))
        self.buttonSaveCharChanges.setText(_translate("MainWindow", "Änderungen am Charakter übernehmen"))
        self.tabQuests.setTabText(self.tabQuests.indexOf(self.charTab), _translate("MainWindow", "Charakter"))
        self.label_21.setText(_translate("MainWindow", "Notizen:"))
        self.buttonNotesSave.setText(_translate("MainWindow", "Speichern"))
        self.buttonNotesClear.setText(_translate("MainWindow", "Notizen löschen"))
        self.tabQuests.setTabText(self.tabQuests.indexOf(self.tabNotes), _translate("MainWindow", "Notizen"))
        self.textAbout.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">bla blab about this program bla</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">thx to the testers</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">bla</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">kein PP kein MG</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">bla</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">rougen?</p></body></html>"))
        self.checkStyle.setText(_translate("MainWindow", "Use a Design"))
        self.radioAdanosStyle.setText(_translate("MainWindow", "Adanos"))
        self.radioBeliarStyle.setText(_translate("MainWindow", "Beliar"))
        self.radioInnosStyle.setText(_translate("MainWindow", "Innos"))
        self.buttonCallBoard.setText(_translate("MainWindow", "Forum aufrufen"))
        self.buttonCallWiki.setText(_translate("MainWindow", "CK Wiki aufrufen"))
        self.buttonGetTime.setText(_translate("MainWindow", "akt. IG Zeit"))
        self.buttonGetPlayers.setText(_translate("MainWindow", "Spielerliste (online)"))
        self.label_20.setText(_translate("MainWindow", "Here is some space for coming features. Until they appear,\nMud will have an eye on you:"))
        self.tabQuests.setTabText(self.tabQuests.indexOf(self.tabMisc), _translate("MainWindow", "Sonstiges"))
        self.menuFunktionen.setTitle(_translate("MainWindow", "Funktionen"))
        self.actionNewChar.setText(_translate("MainWindow", "Neuer Charakter"))
        self.actionExit.setText(_translate("MainWindow", "Beenden"))
        self.actionDeleteChar.setText(_translate("MainWindow", "Charakter löschen"))
        self.actionLoadChar.setText(_translate("MainWindow", "Charakter laden"))
        self.actionSaveAll.setText(_translate("MainWindow", "&Alles speichern"))


    def callBoard(self):
        webbrowser.open("http://www.classickhorinis.de/wbb/", 2)
        return

    def callWiki(self):
        webbrowser.open("http://wiki.classickhorinis.de/index.php?title=Hauptseite", 2)
        return


    def newChar(self):
        self.charCreationWindow.exec()
        #self.updateOpenQuests()
        return

    def saveAll(self):

        self.saveMisc()
        self.saveCharData()
        self.questChanged()


        return

    def deleteChar(self):
        self.charDeleteWindow.exec()
        self.updateOpenQuests()

        return

    def loadChar(self):
        self.actionSaveAll.setEnabled(True)
        self.charLoadingWindow.exec_()
        self.statusbar.showMessage("Aktiver Charakter: " + swapspace.activeChar["name"])

        if swapspace.activeChar["name"] != "":
            self.lineCharName.setText(swapspace.activeChar["name"])
            self.lineCharAge.setText(swapspace.activeChar["age"])
            self.lineCharGild.setText(swapspace.activeChar["gild"])
            self.lineCharStatus.setText(swapspace.activeChar["status"])
            self.lineCharJob.setText(swapspace.activeChar["job"])
            self.lineCharReligion.setText(swapspace.activeChar["religion"])
            self.textCharItems.setText(swapspace.activeChar["rpitems"])
            self.textCharStory.setText(swapspace.activeChar["story"])

            self.textNotes.setText(swapspace.activeMisc["notes"])



            self.tabQuests.setEnabled(True)
            self.updateOpenQuests()

        return

    def saveMisc(self):
        miscText = str(self.textNotes.toPlainText())
        miscData = {"notes" : miscText, "char" : swapspace.activeChar["name"]}
        miscSQL = "UPDATE misc SET notes=(:notes) WHERE char=(:char)"


        print(swapspace.activeChar)

        try:
            self.cursor.execute(miscSQL, miscData)
            self.connection.commit()
        except:
            self.errorDetectet("Error", "Speichern Fehlgeschlagen")
            return
        return

    def clearMisc(self):
        self.textNotes.setText("")
        return

    def saveCharData(self):
        data = {
            "name" : swapspace.activeChar["name"],
            "age" : str(self.lineCharAge.text()),
            "gild" : str(self.lineCharGild.text()),
            "status" : str(self.lineCharStatus.text()),
            "job" : str(self.lineCharJob.text()),
            "rpitems" : str(self.textCharItems.toPlainText()),
            "story" : str(self.textCharStory.toPlainText()),
        }
        sql = "UPDATE characters SET age=(:age), gild=(:gild), status=(:status), job=(:job), rpitems=(:rpitems), story=(:story) WHERE name=(:name)"
        print(data["name"])
        try:
            self.cursor.execute(sql, data)
            self.connection.commit()
        except:
            self.errorDetectet("Oh Oh", "Speichern fehlgeschlagen")

        return

    def makeCharOlder(self):

        age = self.lineCharAge.text()
        if age != "":
            try:
                age = int(age)
                age += 1
                age = str(age)
                self.lineCharAge.setText(age)
            except:
                self.errorDetectet("Öhm..", "Dir ist klar das ein Alter nur aus Zahlen besteht?")

    def newPlace(self):
        self.locationAddingWindow.exec()
        self.updateOpenQuests()
        return

    def deletePlace(self):
        self.locationDeletingWindow.exec()
        self.updateOpenQuests()
        return

    def newQuest(self):

        self.questAddingWindow.exec()
        self.updateOpenQuests()

        return

    def questChanged(self):


        try:

            data = {
                "questName": str(self.treeQuests.currentItem().text(0)),
                "client": str(self.lineQuestClient.text()),
                "deadLine": str(self.lineQuestDeadline.text()),
                "items": str(self.lineQuestItems.text()),
                "reward": str(self.lineQuestRewards.text()),
                "description": str(self.textQuestDesription.toPlainText()),
                "details": str(self.textQuestDetails.toPlainText())
            }

            sqlTest = "SELECT name FROM quests"

            self.cursor.execute(sqlTest)
            check = self.cursor.fetchall()

            if any(data["questName"] in code for code in check):
                try:
                    sqlFinal = "UPDATE quests SET client=(:client), deadline=(:deadLine), items=(:items), reward=(:reward), description=(:description), details=(:details) WHERE name=(:questName)"
                    self.cursor.execute(sqlFinal, data)
                    self.connection.commit()

                except:
                    self.errorDetectet("Questbearbeitung", "Etwas ging beim Eintragen in die Datenbank schief")

            return

        except:
            print("smth went horribly wrong")

        return

    def questDone(self):
        try:
            sqlTest = "SELECT name FROM locations"
            name = self.treeQuests.currentItem().text(0)
            self.cursor.execute(sqlTest)
            tupelToCheck = self.cursor.fetchall()

            if any(name in code for code in tupelToCheck):
                return
            else:

                sql = "UPDATE quests SET status=(:newstatus) WHERE name=(:questname)"
                data = {"newstatus": 1, "questname": self.treeQuests.currentItem().text(0)}

                try:
                    self.cursor.execute(sql, data)
                    self.connection.commit()
                    self.updateOpenQuests()
                except:
                    print("error on injection")
                return
        except:
            print("failure")




    def questDelete(self):

        self.questDeletingWindow.exec()
        self.updateOpenQuests()
        return

    def questFailed(self):
        try:
            sqlTest = "SELECT name FROM locations"
            name = self.treeQuests.currentItem().text(0)
            self.cursor.execute(sqlTest)
            tupelToCheck = self.cursor.fetchall()

            if any(name in code for code in tupelToCheck):
                return
            else:

                sql = "UPDATE quests SET status=(:newstatus) WHERE name=(:questname)"
                data = {"newstatus": 2, "questname": self.treeQuests.currentItem().text(0)}

                print(self.treeQuests.currentItem().text(0))


                try:
                    self.cursor.execute(sql, data)
                    self.connection.commit()
                    self.updateOpenQuests()
                except:
                    print("error on injection")
                return
        except:
            print("failure")

    def getTime(self):
        self.errorDetectet("Not Implemented", "Feature not implemented")
        #TODO
        return

    def getPlayers(self):
        self.errorDetectet("Not Implemented", "Feature not implemented")
        #TODO
        return

    def enableStyle(self):
        if self.checkStyle.isChecked():


            self.radioAdanosStyle.setEnabled(True)
            self.radioBeliarStyle.setEnabled(True)
            self.radioInnosStyle.setEnabled(True)

            return

        else:
            #self.errorDetectet("Not Implemented", "Feature not implemented")
            self.radioAdanosStyle.setEnabled(False)
            self.radioBeliarStyle.setEnabled(False)
            self.radioInnosStyle.setEnabled(False)
            return

        return


    def setStyle(self):
        #TODO : make the design persistent -> database misc, TEXT
        if self.radioInnosStyle.isChecked():
            MainWindow.setStyleSheet("background-color: rgb(85, 0, 0);\ncolor: rgb(255, 255, 0);")
            return
        if self.radioBeliarStyle.isChecked():
            MainWindow.setStyleSheet("background-color: rgb(6, 5, 5);\ncolor: rgb(159, 0, 0);")
            return
        if self.radioAdanosStyle.isChecked():
            MainWindow.setStyleSheet("background-color: rgb(2, 7, 45);\ncolor: rgb(47, 141, 33);")
            return


    def itemSelection(self):

        self.lineQuestClient.setText("")
        self.lineQuestDeadline.setText("")
        self.lineQuestItems.setText("")
        self.lineQuestRewards.setText("")
        self.textQuestDetails.setText("")
        self.textQuestDesription.setText("")


        # Get the name of the current quest
        data = {"questname" : self.treeQuests.currentItem().text(0)}
        sql = "SELECT * FROM quests WHERE name=(:questname)"
        try:

            self.cursor.execute(sql, data)
            questDataTupel = self.cursor.fetchall()

            questDataList = []
            for x in questDataTupel[0]:
                questDataList.append(x)

            if questDataList[9] == 0:
                self.lineQuestClient.setText(questDataList[3])
                self.lineQuestDeadline.setText(questDataList[4])
                self.lineQuestItems.setText(questDataList[5])
                self.lineQuestRewards.setText(questDataList[6])
                self.textQuestDetails.setText(questDataList[8])
                self.textQuestDesription.setText(questDataList[7])

        except:
            print("that didnt work")

        return

    def updateOpenQuests(self):

        ###############################################################
        # Get the Questes and the Locations done                      #
        ###############################################################

        # Get some space
        self.treeQuests.clear()
        self.lineQuestClient.setText("")
        self.lineQuestRewards.setText("")
        self.lineQuestItems.setText("")
        self.textQuestDetails.setText("")
        self.textQuestDesription.setText("")
        #Get the SQL done

        sql = "SELECT name FROM locations WHERE char=(:charname)"
        data = {
            "charname" : swapspace.activeChar["name"]
        }

        try:
            self.cursor.execute(sql, data)
            locationTupel = self.cursor.fetchall()
        except:
            print("sql error while getting the locations")

        locationList = []
        for x in locationTupel:
            locationList.append(x[0])

        # This is putting the Quests in the tree which are not done yet
        for x in locationList:
            self.item_0 = QtWidgets.QTreeWidgetItem(self.treeQuests)
            self.treeQuests.addTopLevelItem(self.item_0)
            self.item_0.setText(0, x)



            try:
                sql = "SELECT name FROM quests WHERE location=(:location) AND char=(:char) AND status=(:status)"
                data = {"location" : x, "char" : swapspace.activeChar["name"], "status" : 0}
                self.cursor.execute(sql, data)
                questForCurrentLocTupel = self.cursor.fetchall()
                questForCurrentLocList = []
                for y in questForCurrentLocTupel:
                    questForCurrentLocList.append(y[0])

                for z in questForCurrentLocList:
                    self.item_1 = QtWidgets.QTreeWidgetItem(self.item_0)
                    self.item_0.addChild(self.item_1)
                    self.item_1.setText(0, z)
            except:
                print("error while getting the quest in dependecy of the location")

        self.treeQuests.sortItems(0, QtCore.Qt.AscendingOrder)
        self.updateAlumini()

    def updateAlumini(self):
        ###############################################################
        # Get the expired Questes and the Locations done              #
        ###############################################################

        # Get some space
        self.listQuestsDone.clear()
        self.textQuestDoneDetails.setText("")

        # Get the SQL done
        try:
            sql = "SELECT name, location, status FROM quests WHERE char=(:char) AND status>(:status)"
            data = {"char": swapspace.activeChar["name"], "status": 0}
            self.cursor.execute(sql, data)
            questsDoneTupel = self.cursor.fetchall()

            for z in questsDoneTupel:
                if z[2] == 2:
                    self.item_0 = QtWidgets.QListWidgetItem(self.listQuestsDone)
                    self.listQuestsDone.addItem(self.item_0)
                    self.item_0.setText("(-)" + (z[1] + " -> " + z[0]))

                else:
                    if z[2] == 1:
                        self.item_0 = QtWidgets.QListWidgetItem(self.listQuestsDone)
                        self.listQuestsDone.addItem(self.item_0)
                        self.item_0.setText(("(+)" + z[1] + " -> " + z[0]))


        except:
            print("error while getting the quest in dependecy of the location")


        return

    def detailsAlumini(self):
        # Get the name of the current quest
        data = {"questname": (self.listQuestsDone.currentItem().text().split("-> "))[1]}
        sql = "SELECT * FROM quests WHERE name=(:questname)"

        try:
            self.cursor.execute(sql, data)
            questDataTupel = self.cursor.fetchall()
            print(questDataTupel)
            print("sql done")

            questDataList = []

            for x in questDataTupel[0]:
                questDataList.append(x)

            self.textQuestDoneDetails.setText(
                    "Quest Name: " + str(questDataList[0]) + "\n\n\n\n" +
                    "Ort: " + str(questDataList[1]) + "\n\n\n\n" +
                    "Questgeber: " + str(questDataList[3]) + "\n\n\n\n" +
                    "DeadLine: " +  str(questDataList[4]) + "\n\n\n\n" +
                    "Benötigte Items: \n" + str(questDataList[5]) + "\n\n\n\n" +
                    "Belohnung: \n" + str(questDataList[6]) + "\n\n\n\n" +
                    "Details: \n" + str(questDataList[8]) + "\n\n\n\n" +
                    "Beschreibung: \n" + str(questDataList[7]) + "\n\n\n\n"
                )

            self.textQuestDoneDetails.setText(
                    "Quest Name: " + str(questDataList[0]) + "\n\n\n\n" +
                    "Ort: " + str(questDataList[1]) + "\n\n\n\n" +
                    "Questgeber: " + str(questDataList[3]) + "\n\n\n\n" +
                    "DeadLine: " + str(questDataList[4]) + "\n\n\n\n" +
                    "Benötigte Items: \n" + str(questDataList[5]) + "\n\n\n\n" +
                    "Belohnung: \n" + str(questDataList[6]) + "\n\n\n\n" +
                    "Details: \n" + str(questDataList[8]) + "\n\n\n\n" +
                    "Beschreibung: \n" + str(questDataList[7]) + "\n\n\n\n"
                )

        except:
            print("Failed to update Alumini")

        return

    def updateStatusBar(self):
        # TODO this is bad and i should feel bad
        self.statusbar.showMessage(swapspace.activeChar["name"])
        return

    def errorDetectet(self, title, message):

        msgBox = QMessageBox()
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.exec()
        return

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = MainClass()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

