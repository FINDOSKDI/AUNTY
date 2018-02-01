# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fachada.ui'
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
        mainw.resize(1040, 640)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("minimalist_gengar_icon__free_to_use__by_jedflah-dadvg7c.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        mainw.setWindowIcon(icon)
        mainw.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        mainw.setDocumentMode(False)
        self.centralwidget = QtGui.QWidget(mainw)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 781, 351))
        self.groupBox.setStyleSheet(_fromUtf8("QGroupBox { \n"
"     border: 2px solid gray; \n"
"     border-radius: 3px; \n"
" } "))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.pushButton = QtGui.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(40, 20, 41, 41))
        self.pushButton.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("document-open.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(32, 32))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_7 = QtGui.QPushButton(self.groupBox)
        self.pushButton_7.setGeometry(QtCore.QRect(80, 20, 41, 41))
        self.pushButton_7.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("document-save.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_7.setIcon(icon2)
        self.pushButton_7.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.pushButton_2 = QtGui.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(0, 20, 41, 41))
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
        item_0 = QtGui.QTreeWidgetItem(self.treeWidget)
        item_0 = QtGui.QTreeWidgetItem(self.treeWidget)
        item_0 = QtGui.QTreeWidgetItem(self.treeWidget)
        item_0 = QtGui.QTreeWidgetItem(self.treeWidget)
        item_0 = QtGui.QTreeWidgetItem(self.treeWidget)
        item_0 = QtGui.QTreeWidgetItem(self.treeWidget)
        item_0 = QtGui.QTreeWidgetItem(self.treeWidget)
        item_0 = QtGui.QTreeWidgetItem(self.treeWidget)
        item_0 = QtGui.QTreeWidgetItem(self.treeWidget)
        item_0 = QtGui.QTreeWidgetItem(self.treeWidget)
        item_0 = QtGui.QTreeWidgetItem(self.treeWidget)
        item_0 = QtGui.QTreeWidgetItem(self.treeWidget)
        self.tabWidget_2 = QtGui.QTabWidget(self.groupBox)
        self.tabWidget_2.setGeometry(QtCore.QRect(200, 10, 511, 331))
        self.tabWidget_2.setObjectName(_fromUtf8("tabWidget_2"))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.plainTextEdit = QtGui.QPlainTextEdit(self.tab_3)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 10, 481, 281))
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.tabWidget_2.addTab(self.tab_3, _fromUtf8(""))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))

        self.pviewer = PhotoViewer(self.tab_4)
        self.pviewer.setGeometry(QtCore.QRect(10, 10, 481, 281))
        self.pviewer.setPhoto(QtGui.QPixmap('automatadot.png'))
        self.pviewer.setObjectName(_fromUtf8("pviewer"))

        self.tabWidget_2.addTab(self.tab_4, _fromUtf8(""))
        self.groupBox_3 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(830, 40, 171, 511))
        self.groupBox_3.setStyleSheet(_fromUtf8("QGroupBox { \n"
"     border: 2px solid gray; \n"
"     border-radius: 3px; \n"
" } "))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.pushButton_11 = QtGui.QPushButton(self.groupBox_3)
        self.pushButton_11.setGeometry(QtCore.QRect(10, 20, 41, 41))
        self.pushButton_11.setText(_fromUtf8(""))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8("arrow-right.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_11.setIcon(icon4)
        self.pushButton_11.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_11.setObjectName(_fromUtf8("pushButton_11"))
        self.tabWidget = QtGui.QTabWidget(self.groupBox_3)
        self.tabWidget.setGeometry(QtCore.QRect(20, 130, 391, 311))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.tableWidget = QtGui.QTableWidget(self.tab)
        self.tableWidget.setGeometry(QtCore.QRect(70, 20, 461, 211))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(2)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 360, 781, 251))
        self.groupBox_2.setStyleSheet(_fromUtf8("QGroupBox { \n"
"     border: 2px solid gray; \n"
"     border-radius: 3px; \n"
" } "))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.pushButton_8 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_8.setGeometry(QtCore.QRect(290, 200, 41, 41))
        self.pushButton_8.setText(_fromUtf8(""))
        self.pushButton_8.setIcon(icon1)
        self.pushButton_8.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))
        self.pushButton_9 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_9.setGeometry(QtCore.QRect(330, 200, 41, 41))
        self.pushButton_9.setText(_fromUtf8(""))
        self.pushButton_9.setIcon(icon2)
        self.pushButton_9.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_9.setObjectName(_fromUtf8("pushButton_9"))
        self.pushButton_10 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_10.setGeometry(QtCore.QRect(250, 200, 41, 41))
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
        item_0 = QtGui.QTreeWidgetItem(self.treeWidget_2)
        self.pushButton_4 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 200, 81, 27))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.textBrowser = QtGui.QTextBrowser(self.groupBox_2)
        self.textBrowser.setGeometry(QtCore.QRect(240, 110, 451, 91))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.textEdit = QtGui.QTextEdit(self.groupBox_2)
        self.textEdit.setGeometry(QtCore.QRect(240, 20, 451, 91))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        mainw.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(mainw)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1040, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuCristo = QtGui.QMenu(self.menubar)
        self.menuCristo.setObjectName(_fromUtf8("menuCristo"))
        self.menuEsto_es_un_cristo = QtGui.QMenu(self.menubar)
        self.menuEsto_es_un_cristo.setObjectName(_fromUtf8("menuEsto_es_un_cristo"))
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
        self.menuCristo.addAction(self.actionNew)
        self.menuCristo.addAction(self.actionOpen)
        self.menuCristo.addAction(self.actionSave)
        self.menuEsto_es_un_cristo.addAction(self.actionGenerate_trace)
        self.menuAnalysis.addAction(self.actionStep_by_step)
        self.menuAnalysis.addAction(self.actionResults_table)
        self.menubar.addAction(self.menuCristo.menuAction())
        self.menubar.addAction(self.menuEsto_es_un_cristo.menuAction())
        self.menubar.addAction(self.menuAnalysis.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(mainw)
        self.tabWidget_2.setCurrentIndex(1)
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
        self.treeWidget.topLevelItem(1).setText(0, _translate("mainw", "New Item", None))
        self.treeWidget.topLevelItem(2).setText(0, _translate("mainw", "New Item", None))
        self.treeWidget.topLevelItem(3).setText(0, _translate("mainw", "New Item", None))
        self.treeWidget.topLevelItem(4).setText(0, _translate("mainw", "New Item", None))
        self.treeWidget.topLevelItem(5).setText(0, _translate("mainw", "New Item", None))
        self.treeWidget.topLevelItem(6).setText(0, _translate("mainw", "New Item", None))
        self.treeWidget.topLevelItem(7).setText(0, _translate("mainw", "New Item", None))
        self.treeWidget.topLevelItem(8).setText(0, _translate("mainw", "New Item", None))
        self.treeWidget.topLevelItem(9).setText(0, _translate("mainw", "New Item", None))
        self.treeWidget.topLevelItem(10).setText(0, _translate("mainw", "New Item", None))
        self.treeWidget.topLevelItem(11).setText(0, _translate("mainw", "New Item", None))
        self.treeWidget.topLevelItem(12).setText(0, _translate("mainw", "New Item", None))
        self.treeWidget.setSortingEnabled(__sortingEnabled)
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), _translate("mainw", "Tab 1", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), _translate("mainw", "Tab 2", None))
        self.groupBox_3.setTitle(_translate("mainw", "Analysis", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("mainw", "Tab 2", None))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("mainw", "New Row", None))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("mainw", "New Row", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("mainw", "New Column", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("mainw", "New Column", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("mainw", "New Column", None))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("mainw", "New Column", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("mainw", "Tab 1", None))
        self.groupBox_2.setTitle(_translate("mainw", "Trace generation", None))
        self.pushButton_6.setText(_translate("mainw", "Remove", None))
        self.treeWidget_2.headerItem().setText(0, _translate("mainw", "Traces", None))
        __sortingEnabled = self.treeWidget_2.isSortingEnabled()
        self.treeWidget_2.setSortingEnabled(False)
        self.treeWidget_2.topLevelItem(0).setText(0, _translate("mainw", "Trace1", None))
        self.treeWidget_2.topLevelItem(1).setText(0, _translate("mainw", "Trace2", None))
        self.treeWidget_2.setSortingEnabled(__sortingEnabled)
        self.pushButton_4.setText(_translate("mainw", "Duplicate", None))
        self.textBrowser.setHtml(_translate("mainw", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">sdafsa sadfasdf as</p></body></html>", None))
        self.textEdit.setHtml(_translate("mainw", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">dsaf </span>ssaf<span style=\" font-weight:600;\"> sad</span>s sa<span style=\" font-weight:600;\">fd</span>saf<span style=\" font-weight:600;\"> as</span> sf</p></body></html>", None))
        self.menuCristo.setTitle(_translate("mainw", "Automata", None))
        self.menuEsto_es_un_cristo.setTitle(_translate("mainw", "Trace generation", None))
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
            self._photo.setPixmap(QtCore.QPixmap())
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

