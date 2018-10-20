# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

from metamodelo import *

import pygraphviz as pgv

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

    
class Ui_mainw(object):

    def updateAutom(self):
        G = pgv.AGraph( \
            automata2dot( \
                mm.model_from_str(self.plainTextEdit.toPlainText()) \
            ) \
        )
        G.layout(prog='dot')
        G.draw('tmp/autom.png')
        self.pviewer.setPhoto(QtGui.QPixmap('tmp/autom.png'))
        
    def setupUi(self, mainw):
        def wip(e):
            print('work in progress')
        mainw.setObjectName(_fromUtf8("mainw"))
        mainw.resize(1092, 640)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("minimalist_gengar_icon__free_to_use__by_jedflah-dadvg7c.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        mainw.setWindowIcon(icon)
        mainw.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        mainw.setDocumentMode(False)
        self.centralwidget = QtGui.QWidget(mainw)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 721, 351))
        self.groupBox.setStyleSheet(_fromUtf8("QGroupBox { \n"
"     border: 2px solid gray; \n"
"     border-radius: 3px; \n"
" } "))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.pushButton = QtGui.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(50, 20, 41, 41))
        self.pushButton.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("document-open.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(32, 32))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_7 = QtGui.QPushButton(self.groupBox)
        self.pushButton_7.setGeometry(QtCore.QRect(90, 20, 41, 41))
        self.pushButton_7.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("document-save.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_7.setIcon(icon2)
        self.pushButton_7.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.pushButton_2 = QtGui.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 20, 41, 41))
        self.pushButton_2.setText(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("document-new.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon3)
        self.pushButton_2.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_5 = QtGui.QPushButton(self.groupBox)
        self.pushButton_5.setGeometry(QtCore.QRect(90, 250, 99, 27))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.pushButton_3 = QtGui.QPushButton(self.groupBox)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 250, 81, 27))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.treeWidget = QtGui.QTreeWidget(self.groupBox)
        self.treeWidget.setGeometry(QtCore.QRect(10, 70, 181, 181))
        self.treeWidget.setObjectName(_fromUtf8("treeWidget"))
        item_0 = QtGui.QTreeWidgetItem(self.treeWidget)
        # item_0 = QtGui.QTreeWidgetItem(self.treeWidget)
        # item_0 = QtGui.QTreeWidgetItem(self.treeWidget)
        # item_0 = QtGui.QTreeWidgetItem(self.treeWidget)
        # item_0 = QtGui.QTreeWidgetItem(self.treeWidget)
        # item_0 = QtGui.QTreeWidgetItem(self.treeWidget)
        # item_0 = QtGui.QTreeWidgetItem(self.treeWidget)
        # item_0 = QtGui.QTreeWidgetItem(self.treeWidget)
        # item_0 = QtGui.QTreeWidgetItem(self.treeWidget)
        # item_0 = QtGui.QTreeWidgetItem(self.treeWidget)
        # item_0 = QtGui.QTreeWidgetItem(self.treeWidget)
        # item_0 = QtGui.QTreeWidgetItem(self.treeWidget)
        # item_0 = QtGui.QTreeWidgetItem(self.treeWidget)
        self.tabWidget_2 = QtGui.QTabWidget(self.groupBox)
        self.tabWidget_2.setGeometry(QtCore.QRect(200, 10, 511, 331))
        self.tabWidget_2.setObjectName(_fromUtf8("tabWidget_2"))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.plainTextEdit = QtGui.QPlainTextEdit(self.tab_3)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 10, 481, 281))
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.plainTextEdit.setPlainText(automstr)
        
        self.tabWidget_2.addTab(self.tab_3, _fromUtf8(""))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))

        self.pviewer = PhotoViewer(self.tab_4)
        self.pviewer.setGeometry(QtCore.QRect(10, 10, 481, 281))
        self.pviewer.setPhoto(QtGui.QPixmap('tmp/autom.png'))
        self.pviewer.setObjectName(_fromUtf8("pviewer"))

        self.tabWidget_2.addTab(self.tab_4, _fromUtf8(""))
        self.groupBox_3 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(740, 10, 341, 601))
        self.groupBox_3.setStyleSheet(_fromUtf8("QGroupBox { \n"
"     border: 2px solid gray; \n"
"     border-radius: 3px; \n"
" } "))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.treeWidget_3 = QtGui.QTreeWidget(self.groupBox_3)
        self.treeWidget_3.setGeometry(QtCore.QRect(10, 50, 321, 241))
        self.treeWidget_3.setObjectName(_fromUtf8("treeWidget_3"))
        item_0 = QtGui.QTreeWidgetItem(self.treeWidget_3)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        self.treeWidget_4 = QtGui.QTreeWidget(self.groupBox_3)
        self.treeWidget_4.setGeometry(QtCore.QRect(10, 310, 321, 231))
        self.treeWidget_4.setObjectName(_fromUtf8("treeWidget_4"))
        item_0 = QtGui.QTreeWidgetItem(self.treeWidget_4)
        item_0 = QtGui.QTreeWidgetItem(self.treeWidget_4)
        item_0 = QtGui.QTreeWidgetItem(self.treeWidget_4)
        self.pushButton_15 = QtGui.QPushButton(self.groupBox_3)
        self.pushButton_15.setGeometry(QtCore.QRect(10, 540, 161, 31))
        self.pushButton_15.setObjectName(_fromUtf8("pushButton_15"))
        self.pushButton_16 = QtGui.QPushButton(self.groupBox_3)
        self.pushButton_16.setGeometry(QtCore.QRect(170, 540, 161, 31))
        self.pushButton_16.setObjectName(_fromUtf8("pushButton_16"))
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 360, 721, 251))
        self.groupBox_2.setStyleSheet(_fromUtf8("QGroupBox { \n"
"     border: 2px solid gray; \n"
"     border-radius: 3px; \n"
" } "))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.pushButton_8 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_8.setGeometry(QtCore.QRect(50, 30, 41, 41))
        self.pushButton_8.setText(_fromUtf8(""))
        self.pushButton_8.setIcon(icon1)
        self.pushButton_8.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))
        self.pushButton_9 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_9.setGeometry(QtCore.QRect(90, 30, 41, 41))
        self.pushButton_9.setText(_fromUtf8(""))
        self.pushButton_9.setIcon(icon2)
        self.pushButton_9.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_9.setObjectName(_fromUtf8("pushButton_9"))
        self.pushButton_10 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_10.setGeometry(QtCore.QRect(10, 30, 41, 41))
        self.pushButton_10.setText(_fromUtf8(""))
        self.pushButton_10.setIcon(icon3)
        self.pushButton_10.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_10.setObjectName(_fromUtf8("pushButton_10"))
        self.pushButton_6 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_6.setGeometry(QtCore.QRect(90, 200, 99, 27))
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.treeWidget_2 = QtGui.QTreeWidget(self.groupBox_2)
        self.treeWidget_2.setGeometry(QtCore.QRect(10, 80, 181, 121))
        self.treeWidget_2.setObjectName(_fromUtf8("treeWidget_2"))
        item_0 = QtGui.QTreeWidgetItem(self.treeWidget_2)
        # item_0 = QtGui.QTreeWidgetItem(self.treeWidget_2)
        self.pushButton_4 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 200, 81, 27))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.textBrowser = QtGui.QTextBrowser(self.groupBox_2)
        self.textBrowser.setGeometry(QtCore.QRect(220, 30, 481, 61))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.textEdit = QtGui.QTextEdit(self.groupBox_2)
        self.textEdit.setGeometry(QtCore.QRect(220, 120, 481, 71))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.pushButton_11 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_11.setGeometry(QtCore.QRect(320, 190, 41, 41))
        self.pushButton_11.setText(_fromUtf8(""))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8("arrow-right.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_11.setIcon(icon4)
        self.pushButton_11.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_11.setObjectName(_fromUtf8("pushButton_11"))
        self.pushButton_12 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_12.setGeometry(QtCore.QRect(240, 190, 41, 41))
        self.pushButton_12.setText(_fromUtf8(""))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8("arrow-left-double.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_12.setIcon(icon5)
        self.pushButton_12.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_12.setObjectName(_fromUtf8("pushButton_12"))
        self.pushButton_13 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_13.setGeometry(QtCore.QRect(360, 190, 41, 41))
        self.pushButton_13.setText(_fromUtf8(""))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8("arrow-right-double.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_13.setIcon(icon6)
        self.pushButton_13.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_13.setObjectName(_fromUtf8("pushButton_13"))
        self.pushButton_14 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_14.setGeometry(QtCore.QRect(280, 190, 41, 41))
        self.pushButton_14.setText(_fromUtf8(""))
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8("arrow-left.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_14.setIcon(icon7)
        self.pushButton_14.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_14.setObjectName(_fromUtf8("pushButton_14"))
        self.label_2 = QtGui.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(220, 10, 141, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(220, 100, 101, 17))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        mainw.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(mainw)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1092, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuAutomata = QtGui.QMenu(self.menubar)
        self.menuAutomata.setObjectName(_fromUtf8("menuAutomata"))
        self.menuGeneration = QtGui.QMenu(self.menubar)
        self.menuGeneration.setObjectName(_fromUtf8("menuGeneration"))
        self.menuAnalysis = QtGui.QMenu(self.menubar)
        self.menuAnalysis.setObjectName(_fromUtf8("menuAnalysis"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        mainw.setMenuBar(self.menubar)
        self.actionMaestra = QtGui.QAction(mainw)
        self.actionMaestra.setObjectName(_fromUtf8("actionMaestra"))
        self.actionOpen = QtGui.QAction(mainw)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionSave = QtGui.QAction(mainw)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionNew = QtGui.QAction(mainw)
        self.actionNew.setObjectName(_fromUtf8("actionNew"))
        self.actionGenerate_trace = QtGui.QAction(mainw)
        self.actionGenerate_trace.setObjectName(_fromUtf8("actionGenerate_trace"))
        self.actionStep_by_step = QtGui.QAction(mainw)
        self.actionStep_by_step.setObjectName(_fromUtf8("actionStep_by_step"))
        self.actionResults_table = QtGui.QAction(mainw)
        self.actionResults_table.setObjectName(_fromUtf8("actionResults_table"))
        self.menuAutomata.addAction(self.actionNew)
        self.menuAutomata.addAction(self.actionOpen)
        self.menuAutomata.addAction(self.actionSave)
        self.menuGeneration.addAction(self.actionGenerate_trace)
        self.menuAnalysis.addAction(self.actionStep_by_step)
        self.menuAnalysis.addAction(self.actionResults_table)
        self.menubar.addAction(self.menuAutomata.menuAction())
        self.menubar.addAction(self.menuGeneration.menuAction())
        self.menubar.addAction(self.menuAnalysis.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(mainw)
        self.tabWidget_2.setCurrentIndex(0)


        self.pushButton.clicked.connect(wip)
        self.pushButton_10.clicked.connect(wip)
        self.pushButton_11.clicked.connect(wip)
        self.pushButton_12.clicked.connect(wip)
        self.pushButton_13.clicked.connect(wip)
        self.pushButton_14.clicked.connect(wip)
        self.pushButton_15.clicked.connect(wip)
        self.pushButton_16.clicked.connect(wip)
        self.pushButton_2.clicked.connect(wip)
        self.pushButton_3.clicked.connect(wip)
        self.pushButton_4.clicked.connect(wip)
        self.pushButton_5.clicked.connect(wip)
        self.pushButton_6.clicked.connect(wip)
        self.pushButton_7.clicked.connect(wip)
        self.pushButton_8.clicked.connect(wip)
        self.pushButton_9.clicked.connect(wip)

        def foo(e):
            self.updateAutom()
        
        self.tabWidget_2.currentChanged.connect(foo)
        
        QtCore.QMetaObject.connectSlotsByName(mainw)



        
    def retranslateUi(self, mainw):
        mainw.setWindowTitle(_translate("mainw", "AUNTY", None))
        self.groupBox.setTitle(_translate("mainw", "Automata", None))
        self.pushButton_5.setText(_translate("mainw", "Remove", None))
        self.pushButton_3.setText(_translate("mainw", "Duplicate", None))
        self.treeWidget.headerItem().setText(0, _translate("mainw", "Automata", None))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, _translate("mainw", "Automaton1", None))
        # self.treeWidget.topLevelItem(1).setText(0, _translate("mainw", "Automaton2", None))
        # self.treeWidget.topLevelItem(2).setText(0, _translate("mainw", "Automaton1 (1)", None))
        # self.treeWidget.topLevelItem(3).setText(0, _translate("mainw", "Automaton1 (2)", None))
        # self.treeWidget.topLevelItem(4).setText(0, _translate("mainw", "Automaton1 (3)", None))
        # self.treeWidget.topLevelItem(5).setText(0, _translate("mainw", "Automaton1 (4)", None))
        # self.treeWidget.topLevelItem(6).setText(0, _translate("mainw", "Automaton1 (5)", None))
        # self.treeWidget.topLevelItem(7).setText(0, _translate("mainw", "Automaton1 (6)", None))
        # self.treeWidget.topLevelItem(8).setText(0, _translate("mainw", "Automaton1 (7)", None))
        # self.treeWidget.topLevelItem(9).setText(0, _translate("mainw", "Automaton1 (8)", None))
        # self.treeWidget.topLevelItem(10).setText(0, _translate("mainw", "Automaton1 (9)", None))
        # self.treeWidget.topLevelItem(11).setText(0, _translate("mainw", "Automaton1 (10)", None))
        # self.treeWidget.topLevelItem(12).setText(0, _translate("mainw", "Automaton1 (11)", None))
        self.treeWidget.setSortingEnabled(__sortingEnabled)
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), _translate("mainw", "Source code", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), _translate("mainw", "Graph render", None))
        self.groupBox_3.setTitle(_translate("mainw", "Analysis", None))
        self.treeWidget_3.headerItem().setText(0, _translate("mainw", "State/Variable", None))
        self.treeWidget_3.headerItem().setText(1, _translate("mainw", "GoC/Value", None))
        __sortingEnabled = self.treeWidget_3.isSortingEnabled()
        self.treeWidget_3.setSortingEnabled(False)
        self.treeWidget_3.topLevelItem(0).setText(0, _translate("mainw", "q39", None))
        self.treeWidget_3.topLevelItem(0).setText(1, _translate("mainw", "0.586", None))
        self.treeWidget_3.topLevelItem(0).child(0).setText(0, _translate("mainw", "min", None))
        self.treeWidget_3.topLevelItem(0).child(0).setText(1, _translate("mainw", "5", None))
        self.treeWidget_3.topLevelItem(0).child(1).setText(0, _translate("mainw", "branchGoC", None))
        self.treeWidget_3.topLevelItem(0).child(1).setText(1, _translate("mainw", "0.721", None))
        self.treeWidget_3.setSortingEnabled(__sortingEnabled)
        self.treeWidget_4.headerItem().setText(0, _translate("mainw", "Registered outputs", None))
        __sortingEnabled = self.treeWidget_4.isSortingEnabled()
        self.treeWidget_4.setSortingEnabled(False)
        self.treeWidget_4.topLevelItem(0).setText(0, _translate("mainw", "!ok(2,0.09)", None))
        self.treeWidget_4.topLevelItem(1).setText(0, _translate("mainw", "!recordAlarm(2,0.15)", None))
        self.treeWidget_4.topLevelItem(2).setText(0, _translate("mainw", "!recordAlarm(3,0.15)", None))
        self.treeWidget_4.setSortingEnabled(__sortingEnabled)
        self.pushButton_15.setText(_translate("mainw", "Clear selected", None))
        self.pushButton_16.setText(_translate("mainw", "Clear all", None))
        self.groupBox_2.setTitle(_translate("mainw", "Trace generation", None))
        self.pushButton_6.setText(_translate("mainw", "Remove", None))
        self.treeWidget_2.headerItem().setText(0, _translate("mainw", "Traces", None))
        __sortingEnabled = self.treeWidget_2.isSortingEnabled()
        self.treeWidget_2.setSortingEnabled(False)
        self.treeWidget_2.topLevelItem(0).setText(0, _translate("mainw", "Trace1", None))
        # self.treeWidget_2.topLevelItem(1).setText(0, _translate("mainw", "Trace2", None))
        self.treeWidget_2.setSortingEnabled(__sortingEnabled)
        self.pushButton_4.setText(_translate("mainw", "Duplicate", None))
        self.textBrowser.setHtml(_translate("mainw", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p></body></html>", None))
        


        self.textEdit.setHtml(_translate("mainw", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">?checkGender(0), ?checkAge(69), ?minute(1), ?readBPM(74), ?readRR(811), ?readRR(817), ?readRR(789), ?readRR(792), ?readRR(789), ?readRR(814), ?readRR(653), ?readRR(997), ?readRR(844), ?readRR(811), ?readRR(792), ?readRR(767), ?readRR(842), ?readRR(853), ?readRR(822), ?readRR(828), ?readRR(825), ?readRR(797), ?readRR(792), ?readRR(794), ?readRR(819), ?readRR(869), ?readRR(825), ?readRR(783), ?readRR(786), ?readRR(781), ?readRR(789), ?readRR(808), ?readRR(819), ?readRR(828), ?readRR(844), ?readRR(803), ?readRR(778), ?readRR(800), ?readRR(786), ?readRR(858), ?readRR(842), ?readRR(828), ?readRR(800), ?readRR(833), ?readRR(797), ?readRR(783), ?readRR(822), ?readRR(844), ?readRR(878), ?readRR(828), ?readRR(775), ?readRR(806), ?readRR(811), ?readRR(794), ?readRR(836), ?readRR(833), ?readRR(825), ?readRR(811), ?readRR(783), ?readRR(783), ?readRR(808), ?readRR(844), ?readRR(833), ?readRR(822), ?readRR(814), ?readRR(775), ?readRR(794), ?readRR(781), ?readRR(797), ?readRR(853), ?readRR(847), ?readRR(822), ?readRR(789), ?readRR(783), ?readRR(786), ?readRR(814), ?readRR(814), ?readRR(847), ?noMorePendingRR(1), ?minute(2), ?readBPM(74), ?readRR(836), ?readRR(811), ?readRR(781), ?readRR(772), ?readRR(789), ?readRR(803), ?readRR(839), ?readRR(825), ?readRR(817), ?readRR(775), ?readRR(797), ?readRR(792), ?readRR(800), ?readRR(817), ?readRR(856), ?readRR(831), ?readRR(789), ?readRR(781), ?readRR(792), ?readRR(831), ?readRR(825), ?readRR(828), ?readRR(833), ?readRR(822), ?readRR(797), ?readRR(781), ?readRR(792), ?readRR(811), ?readRR(861), ?readRR(847), ?readRR(817), ?readRR(792), ?readRR(789), ?readRR(792), ?readRR(811), ?readRR(825), ?readRR(844), ?readRR(856), ?readRR(808), ?readRR(769), ?readRR(797), ?readRR(800), ?readRR(819), ?readRR(836), ?readRR(819), ?readRR(828), ?readRR(800), ?readRR(781), ?readRR(778), ?readRR(811), ?readRR(825), ?readRR(864), ?readRR(828), ?readRR(792), ?readRR(789), ?readRR(800), ?readRR(792), ?readRR(814), ?readRR(836), ?readRR(836), ?readRR(822), ?readRR(769), ?readRR(753), ?readRR(797), ?readRR(819), ?readRR(811), ?readRR(833), ?readRR(828), ?readRR(783), ?readRR(739), ?readRR(833), ?readRR(781), ?readRR(831), ?readRR(864), ?noMorePendingRR(2), ?minute(3), ?readBPM(76), ?readRR(825), ?readRR(800), ?readRR(781), ?readRR(783), ?readRR(800), ?readRR(797), ?readRR(814), ?readRR(844), ?readRR(828), ?readRR(778), ?readRR(758), ?readRR(783), ?readRR(769), ?readRR(828), ?readRR(819), ?readRR(806), ?readRR(786), ?readRR(786), ?readRR(778), ?readRR(761), ?readRR(789), ?readRR(814), ?readRR(850), ?readRR(808), ?readRR(772), ?readRR(778), ?readRR(789), ?readRR(783), ?readRR(800), ?readRR(819), ?readRR(822), ?readRR(803), ?readRR(775), ?readRR(772), ?readRR(772), ?readRR(808), ?readRR(808), ?readRR(825), ?readRR(800), ?readRR(772), ?readRR(775), ?readRR(775), ?readRR(778), ?readRR(792), ?readRR(822), ?readRR(825), ?readRR(783), ?readRR(753), ?readRR(772), ?readRR(783), ?readRR(792), ?readRR(814), ?readRR(828), ?readRR(828), ?readRR(803), ?readRR(769), ?readRR(772), ?readRR(800), ?readRR(811), ?readRR(836), ?readRR(844), ?readRR(800), ?readRR(794), ?readRR(800), ?readRR(786), ?readRR(792), ?readRR(831), ?readRR(844), ?readRR(836), ?readRR(800), ?readRR(756), ?readRR(797), ?readRR(803), ?readRR(811), ?readRR(825), ?readRR(828), ?noMorePendingRR(3), ?minute(4), ?readBPM(74), ?readRR(806), ?readRR(794), ?readRR(772), ?readRR(775), ?readRR(825), ?readRR(519), ?readRR(942), ?readRR(839), ?readRR(819), ?readRR(778), ?readRR(819), ?readRR(808), ?readRR(811), ?readRR(847), ?readRR(869), ?readRR(817), ?readRR(767), ?readRR(789), ?readRR(792), ?readRR(831), ?readRR(828), ?readRR(833), ?readRR(847), ?readRR(817), ?readRR(775), ?readRR(794), ?readRR(819), ?readRR(844), ?readRR(858), ?readRR(828), ?readRR(797), ?readRR(794), ?readRR(789), ?readRR(608), ?readRR(964), ?readRR(831), ?readRR(836), ?readRR(836), ?readRR(781), ?readRR(753), ?readRR(800), ?readRR(811), ?readRR(828), ?readRR(806), ?readRR(828), ?readRR(800), ?readRR(792), ?readRR(764), ?readRR(797), ?readRR(839), ?readRR(839), ?readRR(833), ?readRR(811), ?readRR(797), ?readRR(783), ?readRR(797), ?readRR(811), ?readRR(831), ?readRR(844), ?readRR(842), ?readRR(803), ?readRR(789), ?readRR(783), ?readRR(839), ?readRR(861), ?readRR(844), ?readRR(836), ?readRR(836), ?readRR(811), ?readRR(772), ?readRR(808), ?readRR(836), ?readRR(853), ?readRR(839), ?noMorePendingRR(4), ?minute(5), ?readBPM(74),  ?readRR(825), ?readRR(800), ?readRR(794), ?readRR(806), ?readRR(806), ?readRR(831), ?readRR(842), ?readRR(833), ?readRR(800), ?readRR(783), ?readRR(789), ?readRR(828), ?readRR(844), ?readRR(819), ?readRR(847), ?readRR(808), ?readRR(781), ?readRR(789), ?readRR(811), ?readRR(819), ?readRR(869), ?readRR(836), ?readRR(800), ?readRR(803), ?readRR(775), ?readRR(808), ?readRR(833), ?readRR(839), ?readRR(842), ?readRR(856), ?readRR(794), ?readRR(772), ?readRR(778), ?readRR(814), ?readRR(853), ?readRR(828), ?readRR(819), ?readRR(814), ?readRR(811), ?readRR(781), ?readRR(781), ?readRR(811), ?readRR(831), ?readRR(550), ?readRR(975), ?readRR(797), ?readRR(775), ?readRR(792), ?readRR(806), ?readRR(800), ?readRR(814), ?readRR(800), ?readRR(817), ?readRR(783), ?readRR(764), ?readRR(786), ?readRR(822), ?readRR(828), ?readRR(817), ?readRR(833), ?readRR(783), ?readRR(794), ?readRR(800), ?readRR(800), ?readRR(833), ?readRR(856), ?readRR(828), ?readRR(800), ?readRR(783), ?readRR(769), ?readRR(808), ?readRR(828), ?readRR(822), ?readRR(825), ?noMorePendingRR(5)</p></body></html>", None))
        self.label_2.setText(_translate("mainw", "Applied trace", None))
        self.label_3.setText(_translate("mainw", "Pending trace", None))
        self.menuAutomata.setTitle(_translate("mainw", "Automata", None))
        self.menuGeneration.setTitle(_translate("mainw", "Trace generation", None))
        self.menuAnalysis.setTitle(_translate("mainw", "Analysis", None))
        self.menuHelp.setTitle(_translate("mainw", "Help", None))
        self.actionMaestra.setText(_translate("mainw", "Maestra", None))
        self.actionOpen.setText(_translate("mainw", "Open", None))
        self.actionSave.setText(_translate("mainw", "Save", None))
        self.actionNew.setText(_translate("mainw", "New", None))
        self.actionGenerate_trace.setText(_translate("mainw", "Trace from patient", None))
        self.actionStep_by_step.setText(_translate("mainw", "Step by step", None))
        self.actionResults_table.setText(_translate("mainw", "Results table", None))

class PhotoViewer(QtGui.QGraphicsView):
    photoClicked = QtCore.pyqtSignal(QtCore.QPoint)

    def __init__(self, parent):
        super(PhotoViewer, self).__init__(parent)
        self._zoom = 0
        self._empty = True
        self._scene = QtGui.QGraphicsScene(self)
        self._photo = QtGui.QGraphicsPixmapItem()
        self._scene.addItem(self._photo)
        self.setScene(self._scene)
        self.setTransformationAnchor(QtGui.QGraphicsView.AnchorUnderMouse)
        self.setResizeAnchor(QtGui.QGraphicsView.AnchorUnderMouse)
        self.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.setBackgroundBrush(QtGui.QBrush(QtGui.QColor(30, 30, 30)))
        self.setFrameShape(QtGui.QFrame.NoFrame)

    def hasPhoto(self):
        return not self._empty

    def fitInView(self, scale=True):
        rect = QtCore.QRectF(self._photo.pixmap().rect())
        if not rect.isNull():
            self.setSceneRect(rect)
            if self.hasPhoto():
                unity = self.transform().mapRect(QtCore.QRectF(0, 0, 1, 1))
                self.scale(1 / unity.width(), 1 / unity.height())
                viewrect = self.viewport().rect()
                scenerect = self.transform().mapRect(rect)
                factor = min(viewrect.width() / scenerect.width(),
                             viewrect.height() / scenerect.height())
                self.scale(factor, factor)
            self._zoom = 0

    def setPhoto(self, pixmap=None):
        self._zoom = 0
        if pixmap and not pixmap.isNull():
            self._empty = False
            self.setDragMode(QtGui.QGraphicsView.ScrollHandDrag)
            self._photo.setPixmap(pixmap)
        else:
            self._empty = True
            self.setDragMode(QtGui.QGraphicsView.NoDrag)
            self._photo.setPixmap(QtGui.QPixmap())
        self.fitInView()

    def wheelEvent(self, event):
        if self.hasPhoto():
            if event.delta() > 0:
                factor = 1.25
                self._zoom += 1
            else:
                factor = 0.8
                self._zoom -= 1
            if self._zoom > 0:
                self.scale(factor, factor)
            elif self._zoom == 0:
                self.fitInView()
            else:
                self._zoom = 0

    def toggleDragMode(self):
        if self.dragMode() == QtGui.QGraphicsView.ScrollHandDrag:
            self.setDragMode(QtGui.QGraphicsView.NoDrag)
        elif not self._photo.pixmap().isNull():
            self.setDragMode(QtGui.QGraphicsView.ScrollHandDrag)

    def mousePressEvent(self, event):
        if self._photo.isUnderMouse():
            self.photoClicked.emit(QtCore.QPoint(event.pos()))
        super(PhotoViewer, self).mousePressEvent(event)



if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    mainw = QtGui.QMainWindow()
    ui = Ui_mainw()
    ui.setupUi(mainw)
    mainw.show()
    sys.exit(app.exec_())

