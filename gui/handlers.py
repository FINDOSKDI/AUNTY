from PyQt4.QtGui import QTreeWidgetItem

def wip():
    print("work in progress...")
def processtrigger(q):
    print(q.text())
def tree(row=None, col=None):
    print("tree {} {}".format(row,col))
def treeadd(treew):
    def tree(row=None, col=None):
        root = QTreeWidgetItem(treew,['new', 'element'])
        QTreeWidgetItem(root, ['new', 'subelement'])
        print(treew.selectedItems()[0].setText(0,'element'))
        print(treew.selectedItems()[0].setText(1,'clicked'))
    return tree

