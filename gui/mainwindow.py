# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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
    def setupUi(self, mainw):
        mainw.setObjectName(_fromUtf8("mainw"))
        mainw.resize(1092, 640)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../img/minimalist_gengar_icon__free_to_use__by_jedflah-dadvg7c.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        mainw.setWindowIcon(icon)
        mainw.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        mainw.setDocumentMode(False)
        self.centralwidget = QtGui.QWidget(mainw)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.automataGB = QtGui.QGroupBox(self.centralwidget)
        self.automataGB.setGeometry(QtCore.QRect(10, 10, 721, 351))
        self.automataGB.setStyleSheet(_fromUtf8("QGroupBox { \n"
"     border: 2px solid gray; \n"
"     border-radius: 3px; \n"
" } "))
        self.automataGB.setObjectName(_fromUtf8("automataGB"))
        self.automata_open = QtGui.QPushButton(self.automataGB)
        self.automata_open.setGeometry(QtCore.QRect(50, 20, 41, 41))
        self.automata_open.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("../img/document-open.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.automata_open.setIcon(icon1)
        self.automata_open.setIconSize(QtCore.QSize(32, 32))
        self.automata_open.setObjectName(_fromUtf8("automata_open"))
        self.automata_save = QtGui.QPushButton(self.automataGB)
        self.automata_save.setGeometry(QtCore.QRect(90, 20, 41, 41))
        self.automata_save.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("../img/document-save.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.automata_save.setIcon(icon2)
        self.automata_save.setIconSize(QtCore.QSize(32, 32))
        self.automata_save.setObjectName(_fromUtf8("automata_save"))
        self.automata_new = QtGui.QPushButton(self.automataGB)
        self.automata_new.setGeometry(QtCore.QRect(10, 20, 41, 41))
        self.automata_new.setText(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("../img/document-new.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.automata_new.setIcon(icon3)
        self.automata_new.setIconSize(QtCore.QSize(32, 32))
        self.automata_new.setObjectName(_fromUtf8("automata_new"))
        self.automata_remove = QtGui.QPushButton(self.automataGB)
        self.automata_remove.setGeometry(QtCore.QRect(90, 250, 99, 27))
        self.automata_remove.setObjectName(_fromUtf8("automata_remove"))
        self.automata_duplicate = QtGui.QPushButton(self.automataGB)
        self.automata_duplicate.setGeometry(QtCore.QRect(10, 250, 81, 27))
        self.automata_duplicate.setObjectName(_fromUtf8("automata_duplicate"))
        self.automata_list = QtGui.QTreeWidget(self.automataGB)
        self.automata_list.setGeometry(QtCore.QRect(10, 70, 181, 181))
        self.automata_list.setObjectName(_fromUtf8("automata_list"))
        item_0 = QtGui.QTreeWidgetItem(self.automata_list)
        self.automata_tabs = QtGui.QTabWidget(self.automataGB)
        self.automata_tabs.setGeometry(QtCore.QRect(200, 10, 511, 331))
        self.automata_tabs.setObjectName(_fromUtf8("automata_tabs"))
        self.automata_sourcecode = QtGui.QWidget()
        self.automata_sourcecode.setObjectName(_fromUtf8("automata_sourcecode"))
        self.automata_plaintext = QtGui.QPlainTextEdit(self.automata_sourcecode)
        self.automata_plaintext.setGeometry(QtCore.QRect(10, 10, 481, 281))
        self.automata_plaintext.setObjectName(_fromUtf8("automata_plaintext"))
        self.automata_tabs.addTab(self.automata_sourcecode, _fromUtf8(""))
        self.automata_renderer = QtGui.QWidget()
        self.automata_renderer.setObjectName(_fromUtf8("automata_renderer"))
        self.automata_tabs.addTab(self.automata_renderer, _fromUtf8(""))
        self.analysisGB = QtGui.QGroupBox(self.centralwidget)
        self.analysisGB.setGeometry(QtCore.QRect(740, 10, 341, 601))
        self.analysisGB.setStyleSheet(_fromUtf8("QGroupBox { \n"
"     border: 2px solid gray; \n"
"     border-radius: 3px; \n"
" } "))
        self.analysisGB.setObjectName(_fromUtf8("analysisGB"))
        self.analysis_states = QtGui.QTreeWidget(self.analysisGB)
        self.analysis_states.setGeometry(QtCore.QRect(10, 50, 321, 241))
        self.analysis_states.setObjectName(_fromUtf8("analysis_states"))
        item_0 = QtGui.QTreeWidgetItem(self.analysis_states)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        self.analysis_outputs = QtGui.QTreeWidget(self.analysisGB)
        self.analysis_outputs.setGeometry(QtCore.QRect(10, 310, 321, 231))
        self.analysis_outputs.setObjectName(_fromUtf8("analysis_outputs"))
        item_0 = QtGui.QTreeWidgetItem(self.analysis_outputs)
        self.analysis_clearselected = QtGui.QPushButton(self.analysisGB)
        self.analysis_clearselected.setGeometry(QtCore.QRect(10, 540, 161, 31))
        self.analysis_clearselected.setObjectName(_fromUtf8("analysis_clearselected"))
        self.analysis_clearall = QtGui.QPushButton(self.analysisGB)
        self.analysis_clearall.setGeometry(QtCore.QRect(170, 540, 161, 31))
        self.analysis_clearall.setObjectName(_fromUtf8("analysis_clearall"))
        self.traceGB = QtGui.QGroupBox(self.centralwidget)
        self.traceGB.setGeometry(QtCore.QRect(10, 360, 721, 251))
        self.traceGB.setStyleSheet(_fromUtf8("QGroupBox { \n"
"     border: 2px solid gray; \n"
"     border-radius: 3px; \n"
" } "))
        self.traceGB.setObjectName(_fromUtf8("traceGB"))
        self.trace_open = QtGui.QPushButton(self.traceGB)
        self.trace_open.setGeometry(QtCore.QRect(50, 30, 41, 41))
        self.trace_open.setText(_fromUtf8(""))
        self.trace_open.setIcon(icon1)
        self.trace_open.setIconSize(QtCore.QSize(32, 32))
        self.trace_open.setObjectName(_fromUtf8("trace_open"))
        self.trace_save = QtGui.QPushButton(self.traceGB)
        self.trace_save.setGeometry(QtCore.QRect(90, 30, 41, 41))
        self.trace_save.setText(_fromUtf8(""))
        self.trace_save.setIcon(icon2)
        self.trace_save.setIconSize(QtCore.QSize(32, 32))
        self.trace_save.setObjectName(_fromUtf8("trace_save"))
        self.trace_new = QtGui.QPushButton(self.traceGB)
        self.trace_new.setGeometry(QtCore.QRect(10, 30, 41, 41))
        self.trace_new.setText(_fromUtf8(""))
        self.trace_new.setIcon(icon3)
        self.trace_new.setIconSize(QtCore.QSize(32, 32))
        self.trace_new.setObjectName(_fromUtf8("trace_new"))
        self.trace_remove = QtGui.QPushButton(self.traceGB)
        self.trace_remove.setGeometry(QtCore.QRect(90, 200, 99, 27))
        self.trace_remove.setObjectName(_fromUtf8("trace_remove"))
        self.trace_list = QtGui.QTreeWidget(self.traceGB)
        self.trace_list.setGeometry(QtCore.QRect(10, 80, 181, 121))
        self.trace_list.setObjectName(_fromUtf8("trace_list"))
        item_0 = QtGui.QTreeWidgetItem(self.trace_list)
        self.trace_duplicate = QtGui.QPushButton(self.traceGB)
        self.trace_duplicate.setGeometry(QtCore.QRect(10, 200, 81, 27))
        self.trace_duplicate.setObjectName(_fromUtf8("trace_duplicate"))
        self.textBrowser = QtGui.QTextBrowser(self.traceGB)
        self.textBrowser.setGeometry(QtCore.QRect(220, 30, 481, 61))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.textEdit = QtGui.QTextEdit(self.traceGB)
        self.textEdit.setGeometry(QtCore.QRect(220, 120, 481, 71))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.trace_forward = QtGui.QPushButton(self.traceGB)
        self.trace_forward.setGeometry(QtCore.QRect(320, 190, 41, 41))
        self.trace_forward.setText(_fromUtf8(""))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8("../img/arrow-right.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.trace_forward.setIcon(icon4)
        self.trace_forward.setIconSize(QtCore.QSize(32, 32))
        self.trace_forward.setObjectName(_fromUtf8("trace_forward"))
        self.trace_fastbackward = QtGui.QPushButton(self.traceGB)
        self.trace_fastbackward.setGeometry(QtCore.QRect(240, 190, 41, 41))
        self.trace_fastbackward.setText(_fromUtf8(""))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8("../img/arrow-left-double.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.trace_fastbackward.setIcon(icon5)
        self.trace_fastbackward.setIconSize(QtCore.QSize(32, 32))
        self.trace_fastbackward.setObjectName(_fromUtf8("trace_fastbackward"))
        self.trace_fastforward = QtGui.QPushButton(self.traceGB)
        self.trace_fastforward.setGeometry(QtCore.QRect(360, 190, 41, 41))
        self.trace_fastforward.setText(_fromUtf8(""))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8("../img/arrow-right-double.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.trace_fastforward.setIcon(icon6)
        self.trace_fastforward.setIconSize(QtCore.QSize(32, 32))
        self.trace_fastforward.setObjectName(_fromUtf8("trace_fastforward"))
        self.trace_backward = QtGui.QPushButton(self.traceGB)
        self.trace_backward.setGeometry(QtCore.QRect(280, 190, 41, 41))
        self.trace_backward.setText(_fromUtf8(""))
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8("../img/arrow-left.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.trace_backward.setIcon(icon7)
        self.trace_backward.setIconSize(QtCore.QSize(32, 32))
        self.trace_backward.setObjectName(_fromUtf8("trace_backward"))
        self.label_applied = QtGui.QLabel(self.traceGB)
        self.label_applied.setGeometry(QtCore.QRect(220, 10, 471, 17))
        self.label_applied.setObjectName(_fromUtf8("label_applied"))
        self.label_pending = QtGui.QLabel(self.traceGB)
        self.label_pending.setGeometry(QtCore.QRect(220, 100, 471, 17))
        self.label_pending.setObjectName(_fromUtf8("label_pending"))
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

        self.retranslateUi(mainw)
        self.automata_tabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(mainw)

    def retranslateUi(self, mainw):
        mainw.setWindowTitle(_translate("mainw", "AUNTY", None))
        self.automataGB.setTitle(_translate("mainw", "Automata", None))
        self.automata_remove.setText(_translate("mainw", "Remove", None))
        self.automata_duplicate.setText(_translate("mainw", "Duplicate", None))
        self.automata_list.headerItem().setText(0, _translate("mainw", "Automata", None))
        __sortingEnabled = self.automata_list.isSortingEnabled()
        self.automata_list.setSortingEnabled(False)
        self.automata_list.topLevelItem(0).setText(0, _translate("mainw", "Automaton1", None))
        self.automata_list.setSortingEnabled(__sortingEnabled)
        self.automata_tabs.setTabText(self.automata_tabs.indexOf(self.automata_sourcecode), _translate("mainw", "Source code", None))
        self.automata_tabs.setTabText(self.automata_tabs.indexOf(self.automata_renderer), _translate("mainw", "Graph render", None))
        self.analysisGB.setTitle(_translate("mainw", "Analysis", None))
        self.analysis_states.headerItem().setText(0, _translate("mainw", "State/Variable", None))
        self.analysis_states.headerItem().setText(1, _translate("mainw", "GoC/Value", None))
        __sortingEnabled = self.analysis_states.isSortingEnabled()
        self.analysis_states.setSortingEnabled(False)
        self.analysis_states.topLevelItem(0).setText(0, _translate("mainw", "q39", None))
        self.analysis_states.topLevelItem(0).setText(1, _translate("mainw", "0.586", None))
        self.analysis_states.topLevelItem(0).child(0).setText(0, _translate("mainw", "min", None))
        self.analysis_states.topLevelItem(0).child(0).setText(1, _translate("mainw", "5", None))
        self.analysis_states.topLevelItem(0).child(1).setText(0, _translate("mainw", "branchGoC", None))
        self.analysis_states.topLevelItem(0).child(1).setText(1, _translate("mainw", "0.721", None))
        self.analysis_states.setSortingEnabled(__sortingEnabled)
        self.analysis_outputs.headerItem().setText(0, _translate("mainw", "Registered outputs", None))
        __sortingEnabled = self.analysis_outputs.isSortingEnabled()
        self.analysis_outputs.setSortingEnabled(False)
        self.analysis_outputs.topLevelItem(0).setText(0, _translate("mainw", "!ok(2,0.09)", None))
        self.analysis_outputs.setSortingEnabled(__sortingEnabled)
        self.analysis_clearselected.setText(_translate("mainw", "Clear selected", None))
        self.analysis_clearall.setText(_translate("mainw", "Clear all", None))
        self.traceGB.setTitle(_translate("mainw", "Trace generation", None))
        self.trace_remove.setText(_translate("mainw", "Remove", None))
        self.trace_list.headerItem().setText(0, _translate("mainw", "Traces", None))
        __sortingEnabled = self.trace_list.isSortingEnabled()
        self.trace_list.setSortingEnabled(False)
        self.trace_list.topLevelItem(0).setText(0, _translate("mainw", "Trace1", None))
        self.trace_list.setSortingEnabled(__sortingEnabled)
        self.trace_duplicate.setText(_translate("mainw", "Duplicate", None))
        self.textBrowser.setHtml(_translate("mainw", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">?checkGender(0), ?checkAge(69), ?minute(1), ?readBPM(74), ?readRR(811), ?readRR(817), ?readRR(789), ?readRR(792), ?readRR(789), ?readRR(814), ?readRR(653), ?readRR(997), ?readRR(844), ?readRR(811), ?readRR(792), ?readRR(767), ?readRR(842), ?readRR(853), ?readRR(822), ?readRR(828), ?readRR(825), ?readRR(797), ?readRR(792), ?readRR(794), ?readRR(819), ?readRR(869), ?readRR(825), ?readRR(783), ?readRR(786), ?readRR(781), ?readRR(789), ?readRR(808), ?readRR(819), ?readRR(828), ?readRR(844), ?readRR(803), ?readRR(778), ?readRR(800), ?readRR(786), ?readRR(858), ?readRR(842), ?readRR(828), ?readRR(800), ?readRR(833), ?readRR(797), ?readRR(783), ?readRR(822), ?readRR(844), ?readRR(878), ?readRR(828), ?readRR(775), ?readRR(806), ?readRR(811), ?readRR(794), ?readRR(836), ?readRR(833), ?readRR(825), ?readRR(811), ?readRR(783), ?readRR(783), ?readRR(808), ?readRR(844), ?readRR(833), ?readRR(822), ?readRR(814), ?readRR(775), ?readRR(794), ?readRR(781), ?readRR(797), ?readRR(853), ?readRR(847), ?readRR(822), ?readRR(789), ?readRR(783), ?readRR(786), ?readRR(814), ?readRR(814), ?readRR(847), ?noMorePendingRR(1), ?minute(2), ?readBPM(74), ?readRR(836), ?readRR(811), ?readRR(781), ?readRR(772), ?readRR(789), ?readRR(803), ?readRR(839), ?readRR(825), ?readRR(817), ?readRR(775), ?readRR(797), ?readRR(792), ?readRR(800), ?readRR(817), ?readRR(856), ?readRR(831), ?readRR(789), ?readRR(781), ?readRR(792), ?readRR(831), ?readRR(825), ?readRR(828), ?readRR(833), ?readRR(822), ?readRR(797), ?readRR(781), ?readRR(792), ?readRR(811), ?readRR(861), ?readRR(847), ?readRR(817), ?readRR(792), ?readRR(789), ?readRR(792), ?readRR(811), ?readRR(825), ?readRR(844), ?readRR(856), ?readRR(808), ?readRR(769), ?readRR(797), ?readRR(800), ?readRR(819), ?readRR(836), ?readRR(819), ?readRR(828), ?readRR(800), ?readRR(781), ?readRR(778), ?readRR(811), ?readRR(825), ?readRR(864), ?readRR(828), ?readRR(792), ?readRR(789), ?readRR(800), ?readRR(792), ?readRR(814), ?readRR(836), ?readRR(836), ?readRR(822), ?readRR(769), ?readRR(753), ?readRR(797), ?readRR(819), ?readRR(811), ?readRR(833), ?readRR(828), ?readRR(783), ?readRR(739), ?readRR(833), ?readRR(781), ?readRR(831), ?readRR(864), ?noMorePendingRR(2), ?minute(3), ?readBPM(76), ?readRR(825), ?readRR(800), ?readRR(781), ?readRR(783), ?readRR(800), ?readRR(797), ?readRR(814), ?readRR(844), ?readRR(828), ?readRR(778), ?readRR(758), ?readRR(783), ?readRR(769), ?readRR(828), ?readRR(819), ?readRR(806), ?readRR(786), ?readRR(786), ?readRR(778), ?readRR(761), ?readRR(789), ?readRR(814), ?readRR(850), ?readRR(808), ?readRR(772), ?readRR(778), ?readRR(789), ?readRR(783), ?readRR(800), ?readRR(819), ?readRR(822), ?readRR(803), ?readRR(775), ?readRR(772), ?readRR(772), ?readRR(808), ?readRR(808), ?readRR(825), ?readRR(800), ?readRR(772), ?readRR(775), ?readRR(775), ?readRR(778), ?readRR(792), ?readRR(822), ?readRR(825), ?readRR(783), ?readRR(753), ?readRR(772), ?readRR(783), ?readRR(792), ?readRR(814), ?readRR(828), ?readRR(828), ?readRR(803), ?readRR(769), ?readRR(772), ?readRR(800), ?readRR(811), ?readRR(836), ?readRR(844), ?readRR(800), ?readRR(794), ?readRR(800), ?readRR(786), ?readRR(792), ?readRR(831), ?readRR(844), ?readRR(836), ?readRR(800), ?readRR(756), ?readRR(797), ?readRR(803), ?readRR(811), ?readRR(825), ?readRR(828), ?noMorePendingRR(3), ?minute(4), ?readBPM(74), ?readRR(806), ?readRR(794), ?readRR(772), ?readRR(775), ?readRR(825), ?readRR(519), ?readRR(942), ?readRR(839), ?readRR(819), ?readRR(778), ?readRR(819), ?readRR(808), ?readRR(811), ?readRR(847), ?readRR(869), ?readRR(817), ?readRR(767), ?readRR(789), ?readRR(792), ?readRR(831), ?readRR(828), ?readRR(833), ?readRR(847), ?readRR(817), ?readRR(775), ?readRR(794), ?readRR(819), ?readRR(844), ?readRR(858), ?readRR(828), ?readRR(797), ?readRR(794), ?readRR(789), ?readRR(608), ?readRR(964), ?readRR(831), ?readRR(836), ?readRR(836), ?readRR(781), ?readRR(753), ?readRR(800), ?readRR(811), ?readRR(828), ?readRR(806), ?readRR(828), ?readRR(800), ?readRR(792), ?readRR(764), ?readRR(797), ?readRR(839), ?readRR(839), ?readRR(833), ?readRR(811), ?readRR(797), ?readRR(783), ?readRR(797), ?readRR(811), ?readRR(831), ?readRR(844), ?readRR(842), ?readRR(803), ?readRR(789), ?readRR(783), ?readRR(839), ?readRR(861), ?readRR(844), ?readRR(836), ?readRR(836), ?readRR(811), ?readRR(772), ?readRR(808), ?readRR(836), ?readRR(853), ?readRR(839), ?noMorePendingRR(4), ?minute(5), ?readBPM(74),  ?readRR(825)</p></body></html>", None))
        self.textEdit.setHtml(_translate("mainw", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">?readRR(800), ?readRR(794), ?readRR(806), ?readRR(806), ?readRR(831), ?readRR(842), ?readRR(833), ?readRR(800), ?readRR(783), ?readRR(789), ?readRR(828), ?readRR(844), ?readRR(819), ?readRR(847), ?readRR(808), ?readRR(781), ?readRR(789), ?readRR(811), ?readRR(819), ?readRR(869), ?readRR(836), ?readRR(800), ?readRR(803), ?readRR(775), ?readRR(808), ?readRR(833), ?readRR(839), ?readRR(842), ?readRR(856), ?readRR(794), ?readRR(772), ?readRR(778), ?readRR(814), ?readRR(853), ?readRR(828), ?readRR(819), ?readRR(814), ?readRR(811), ?readRR(781), ?readRR(781), ?readRR(811), ?readRR(831), ?readRR(550), ?readRR(975), ?readRR(797), ?readRR(775), ?readRR(792), ?readRR(806), ?readRR(800), ?readRR(814), ?readRR(800), ?readRR(817), ?readRR(783), ?readRR(764), ?readRR(786), ?readRR(822), ?readRR(828), ?readRR(817), ?readRR(833), ?readRR(783), ?readRR(794), ?readRR(800), ?readRR(800), ?readRR(833), ?readRR(856), ?readRR(828), ?readRR(800), ?readRR(783), ?readRR(769), ?readRR(808), ?readRR(828), ?readRR(822), ?readRR(825), ?noMorePendingRR(5)</p></body></html>", None))
        self.label_applied.setText(_translate("mainw", "Applied trace", None))
        self.label_pending.setText(_translate("mainw", "Pending trace", None))
        self.menuAutomata.setTitle(_translate("mainw", "Automata", None))
        self.menuGeneration.setTitle(_translate("mainw", "Trace generation", None))
        self.menuAnalysis.setTitle(_translate("mainw", "Analysis", None))
        self.actionMaestra.setText(_translate("mainw", "Maestra", None))
        self.actionOpen.setText(_translate("mainw", "Open", None))
        self.actionSave.setText(_translate("mainw", "Save", None))
        self.actionNew.setText(_translate("mainw", "New", None))
        self.actionGenerate_trace.setText(_translate("mainw", "Trace from patient", None))
        self.actionStep_by_step.setText(_translate("mainw", "Step by step", None))
        self.actionResults_table.setText(_translate("mainw", "Results table", None))

