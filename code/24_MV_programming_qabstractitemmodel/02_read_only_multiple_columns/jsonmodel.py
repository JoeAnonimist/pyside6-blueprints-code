from PySide6.QtCore import QAbstractItemModel, QModelIndex, Qt
from treeitem import TreeItem


# 2. Create the QAbstractItemModel subclass
#    and implement rowCount(), columnCount(),
#    data() and headerData()

class JsonModel(QAbstractItemModel):

    def __init__(self, source, parent=None):

        super().__init__(parent)
        self.root_item = TreeItem.build_tree(source)
        self.header = [c.capitalize() for c in TreeItem.COLUMNS]

    def rowCount(self, parent=QModelIndex()):
        if parent.isValid():
            if parent.column() != 0:
                return 0
            parent_item = parent.internalPointer()
        else:
            parent_item = self.root_item
        return parent_item.child_count()

    def columnCount(self, parent=QModelIndex()):
        if parent.isValid():
            return parent.internalPointer().column_count()
        else:
            return self.root_item.column_count()

    def data(self, index, role):
        
        if role == Qt.ItemDataRole.DisplayRole:
            item = index.internalPointer()
            return item.data(index.column())
        return None

    def headerData(self, section, orientation, role):
        if orientation == Qt.Orientation.Horizontal:
            if role == Qt.ItemDataRole.DisplayRole:
                return self.header[section]
    
    # 3. Implement index() and parent()
    
    def index(self, row, column, parent=QModelIndex()):

        if not self.hasIndex(row, column, parent):
            return QModelIndex()

        if parent.isValid():
            parent_item = parent.internalPointer()
        else:
            parent_item = self.root_item

        childItem = parent_item.child(row)
        return self.createIndex(row, column, childItem)

    def parent(self, index):

        if not index.isValid():
            return QModelIndex()

        item = index.internalPointer()
        parent_item = item.parent

        if parent_item == self.root_item:
            return QModelIndex()
        else:
            row = parent_item.row()
            return self.createIndex(row, 0, parent_item)
