import os, sys
from PyQt4         import QtGui, QtCore
from metamodel.grammar import *
import gui.mainwindow as mainwindow
from handlers import *
import pygraphviz as pgv
from gui.PhotoViewer import PhotoViewer

prevdir = os.getcwd()
tempdir = os.path.dirname(os.path.abspath(__file__))

class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = mainwindow.Ui_mainw()
        self.ui.setupUi(self) 
        self.pviewer = PhotoViewer(self.ui.automata_renderer)
        self.pviewer.setGeometry(QtCore.QRect(10, 10, 481, 281))
        os.chdir(tempdir)
        self.pviewer.setPhoto(QtGui.QPixmap('tmp/autom.png'))
        os.chdir(prevdir)
        self.pviewer.setObjectName("pviewer")
        
        def update_render(e):
            self.updateRender()
            
        self.ui.automata_tabs.currentChanged.connect(update_render)

        self.ui.automata_plaintext.setPlainText( ("HAMACHER\n"
                                                  "X,Y,Z\n"
                                                  "s0,s1,s2,s3\n"
                                                  "s0\n"
                                                  "s0,s1\n"
                                                  "!O1 X*9\n"
                                                  "HAMACHER\n"
                                                  "X<=4 [0.62]\n"
                                                  "Identity\n"
                                                  "s0,s2\n"
                                                  "?Input2 X,Y,Z\n"
                                                  "HAMACHER true\n"
                                                  "X=Y*Z/3, Y=0\n"
                                                  "s0,s3\n"
                                                  "!O1 X*9\n"
                                                  "HAMACHER\n"
                                                  "X<=4 [0.62]\n"
                                                  "Identity\n"
                                                  "s0,s3\n"
                                                  "?Input2 X,Y,Z\n"
                                                  "PRODUCT\n"
                                                  "Y=X+1 [0.2], Z<=5<=X [0.7]\n"
                                                  "X=Y*Z/3, Y=0") )
        self.ui.trace_textBrowser.setPlainText('')
        self.ui.trace_textEdit.setPlainText('')
#        print(self.ui.trace_textEdit.toPlainText())

        self.controller = Controller(self)
        
        QtCore.QObject.connect(self.ui.automata_new, QtCore.SIGNAL("clicked()"), self.ui.automata_actionNew.trigger)
        QtCore.QObject.connect(self.ui.automata_open, QtCore.SIGNAL("clicked()"), self.ui.automata_actionOpen.trigger)
        QtCore.QObject.connect(self.ui.automata_save, QtCore.SIGNAL("clicked()"), self.ui.automata_actionSave.trigger)
        QtCore.QObject.connect(self.ui.automata_duplicate, QtCore.SIGNAL("clicked()"), self.ui.automata_actionDuplicate.trigger)
        QtCore.QObject.connect(self.ui.automata_remove, QtCore.SIGNAL("clicked()"), self.ui.automata_actionRemove.trigger)

        QtCore.QObject.connect(self.ui.trace_new, QtCore.SIGNAL("clicked()"), self.ui.trace_actionNew.trigger)
        QtCore.QObject.connect(self.ui.trace_open, QtCore.SIGNAL("clicked()"), self.ui.trace_actionOpen.trigger)
        QtCore.QObject.connect(self.ui.trace_save, QtCore.SIGNAL("clicked()"), self.ui.trace_actionSave.trigger)
        QtCore.QObject.connect(self.ui.trace_duplicate, QtCore.SIGNAL("clicked()"), self.ui.trace_actionDuplicate.trigger)
        QtCore.QObject.connect(self.ui.trace_remove, QtCore.SIGNAL("clicked()"), self.ui.trace_actionRemove.trigger)

        QtCore.QObject.connect(self.ui.trace_fastbackward, QtCore.SIGNAL("clicked()"), self.ui.trace_actionFastBackward.trigger)
        QtCore.QObject.connect(self.ui.trace_backward, QtCore.SIGNAL("clicked()"), self.ui.trace_actionBackward.trigger)
        QtCore.QObject.connect(self.ui.trace_forward, QtCore.SIGNAL("clicked()"), self.ui.trace_actionForward.trigger)
        QtCore.QObject.connect(self.ui.trace_fastforward, QtCore.SIGNAL("clicked()"), self.ui.trace_actionFastForward.trigger)

        QtCore.QObject.connect(self.ui.analysis_clearselected, QtCore.SIGNAL("clicked()"), self.ui.analysis_actionClearSelected.trigger)
        QtCore.QObject.connect(self.ui.analysis_clearall, QtCore.SIGNAL("clicked()"), self.ui.analysis_actionClearAll.trigger)

        self.ui.automata_actionNew.triggered.connect(self.controller.automata_new)
        self.ui.automata_actionOpen.triggered.connect(self.controller.automata_open)
        self.ui.automata_actionSave.triggered.connect(self.controller.automata_save)
        self.ui.automata_actionDuplicate.triggered.connect(self.controller.automata_duplicate)
        self.ui.automata_actionRemove.triggered.connect(self.controller.automata_remove)
        
        self.ui.trace_actionNew.triggered.connect(self.controller.trace_new)
        self.ui.trace_actionOpen.triggered.connect(self.controller.trace_open)
        self.ui.trace_actionSave.triggered.connect(self.controller.trace_save)
        self.ui.trace_actionDuplicate.triggered.connect(self.controller.trace_duplicate)
        self.ui.trace_actionRemove.triggered.connect(self.controller.trace_remove)

        self.ui.trace_actionFastBackward.triggered.connect(self.controller.trace_fastbackward)
        self.ui.trace_actionBackward.triggered.connect(self.controller.trace_backward)
        self.ui.trace_actionForward.triggered.connect(self.controller.trace_forward)
        self.ui.trace_actionFastForward.triggered.connect(self.controller.trace_fastforward)

        self.ui.analysis_actionClearSelected.triggered.connect(self.controller.analysis_clearselected)
        self.ui.analysis_actionClearAll.triggered.connect(self.controller.analysis_clearall)
        
        self.ui.analysis_outputs.clicked.connect(self.controller.analysis_outputs)
        self.ui.trace_list.clicked.connect(self.controller.trace_list)
        self.ui.automata_list.clicked.connect(self.controller.automata_list)
        self.ui.analysis_states.clicked.connect(self.controller.analysis_states)
        
        self.ui.trace_list.clear()
        self.ui.analysis_outputs.clear()
        self.ui.analysis_states.clear()
        self.ui.automata_list.clear()
#        item_0 = QtGui.QTreeWidgetItem(self.ui.analysis_states,['1','2'])
#        self.ui.analysis_states.setCurrentItem(item_0)
#        item_1 = QtGui.QTreeWidgetItem(self.ui.automata_list, ['Automata unico'])
#        self.ui.automata_list.setCurrentItem(item_1)
        
#        self.ui.analysis_states.clicked.connect(None)

        def h(foo=None):
            print(QtGui.QFileDialog.getSaveFileName())
            self.ui.automata_open.setEnabled(False)
            self.ui.automata_actionOpen.setEnabled(False)
        
    def updateRender(self):       #### TODO: FIX THIS
        source_code = "e.e" # automata2dot(mm.model_from_str(self.plainTextEdit.toPlainText()))
        G = pgv.AGraph(source_code)
        G.layout(prog='dot')
        os.chdir(tempdir)
        G.draw('tmp/autom.png')
        self.ui.pviewer.setPhoto(QtGui.QPixmap('tmp/autom.png'))
        os.chdir(prevdir)

def main():
    app = QtGui.QApplication(sys.argv)
    os.chdir(tempdir)
    window = MainWindow()
    os.chdir(prevdir)
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
