from PyQt4.QtGui import QTreeWidgetItem

def wip():
    print("work in progress...")
def processtrigger(q):
    print(q.text())
def tree(row=None, col=None):
    print("tree {} {}".format(row,col))
def treeadd(treew):
    def tree(row=None, col=None):
        QTreeWidgetItem(treew,['new'])
        print(treew.selectedItems()[0].setText(0,'clicked'))
    return tree

