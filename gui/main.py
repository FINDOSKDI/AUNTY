import os, sys
from PyQt4         import QtGui, QtCore
import mainwindow
from ..metamodel.grammar import *
from handlers import *
import pygraphviz as pgv
from PhotoViewer import PhotoViewer

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
        self.pviewer.setPhoto(QtGui.QPixmap('../tmp/autom.png'))
        os.chdir(prevdir)
        self.pviewer.setObjectName("pviewer")
        
        def update_render(e):
            self.updateRender()
            
        self.ui.automata_tabs.currentChanged.connect(update_render)
        self.ui.analysis_states.clicked.connect(treeadd(self.ui.analysis_states))

        
    def updateRender(self):       #### TODO: FIX THIS
        G = pgv.AGraph( \
            automata2dot( \
                mm.model_from_str(self.plainTextEdit.toPlainText()) \
            ) \
        )
        G.layout(prog='dot')
        os.chdir(tempdir)
        G.draw('../tmp/autom.png')
        self.pviewer.setPhoto(QtGui.QPixmap('../tmp/autom.png'))
        os.chdir(prevdir)

        """

#        self.plainTextEdit.setPlainText(automstr)
   


        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL("clicked()"), self.actionOpen.trigger) # ???
        self.menubar.triggered[QtGui.QAction].connect(processtrigger) # ???

        self.tabWidget_2.setCurrentIndex(0)


#        self.pushButton.clicked.connect(wip)
#        self.pushButton_10.clicked.connect(wip)
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
#        self.pushButton_9.clicked.connect(wip)

        


"""     
        
    def DoSomething(self):
        print "button clicked" #    or message box  or something else


def main():
    app = QtGui.QApplication(sys.argv)
    os.chdir(tempdir)
    window = MainWindow()
    os.chdir(prevdir)
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
