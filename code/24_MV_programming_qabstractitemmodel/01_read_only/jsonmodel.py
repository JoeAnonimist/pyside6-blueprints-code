from PySide6.QtCore import QAbstractItemModel, QModelIndex, Qt
from treeitem import TreeItem


# 2. Create the QAbstractItemModel subclass
#    and implement rowCount(), columnCount(),
#    data() and headerData().

class JsonModel(QAbstractItemModel):

    def __init__(self, source, parent=None):

        super().__init__(parent)
        self.root_item = TreeItem.build_tree(source)

    def rowCount(self, parent=QModelIndex()):

        if parent.isValid():
            return len(parent.internalPointer().children)
        return len(self.root_item.children)

    def columnCount(self, parent=QModelIndex()):
        return 1

    def data(self, index, role):

        if role == Qt.ItemDataRole.DisplayRole:
            return index.internalPointer().value
        return None
    
    def headerData(self, section, orientation, role):
        if orientation == Qt.Orientation.Horizontal:
            if role == Qt.ItemDataRole.DisplayRole:
                return 'Employee Name'
    
    # 3. Implement index()
    
    def index(self, row, column, parent=QModelIndex()):

        if not self.hasIndex(row, column, parent):
            return QModelIndex()

        if parent.isValid():
            parent_item = parent.internalPointer()
        else:
            parent_item = self.root_item
        return self.createIndex(
            row, column, parent_item.children[row])

    # 4. Implement parent()

    def parent(self, index):

        if not index.isValid():
            return QModelIndex()

        item = index.internalPointer()
        parent_item = item.parent

        if parent_item == self.root_item:
            return QModelIndex()
        
        row = parent_item.parent.children.index(parent_item)
        return self.createIndex(row, 0, parent_item)
