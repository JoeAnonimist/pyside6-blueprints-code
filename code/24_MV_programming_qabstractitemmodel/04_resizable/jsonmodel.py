from PySide6.QtCore import QAbstractItemModel, QModelIndex, Qt
from treeitem import TreeItem


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
        
        if role == Qt.ItemDataRole.DisplayRole \
           or role == Qt.ItemDataRole.EditRole:
            item = index.internalPointer()
            return item.data(index.column())
        
    def headerData(self, section, orientation, role):
        if orientation == Qt.Orientation.Horizontal:
            if role == Qt.ItemDataRole.DisplayRole:
                return self.header[section]

    def index(self, row, column, parent=QModelIndex()):

        if not self.hasIndex(row, column, parent):
            return QModelIndex()

        if not parent.isValid():
            parent_item = self.root_item
        else:
            parent_item = parent.internalPointer()

        childItem = parent_item.child(row)
        if childItem:
            return self.createIndex(row, column, childItem)
        else:
            return QModelIndex()

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

    def flags(self, index) -> Qt.ItemFlag:
        if not index.isValid():
            return Qt.ItemFlags()
        return (super().flags(index) |
                    Qt.ItemFlag.ItemIsEditable)
   
    def setData(self, index, value, role):
        if role == Qt.ItemDataRole.EditRole:
            tree_item = index.internalPointer()
            if tree_item.data(index.column()) != value:
                tree_item.set_data(index.column(), value)
                self.dataChanged.emit(index, index)
                return True
            return False
        return False
    
    
    # 3. Implement insertRows().
    
    def insertRows(self, row, count, parent=QModelIndex()):

        if 0 <= row <= self.rowCount(parent):
            self.beginInsertRows(parent, row, row + count - 1)
            if parent.isValid():
                parent_item = parent.internalPointer()
            else:
                parent_item = self.root_item
            parent_item.insert_child(row)
            self.endInsertRows()
            return True
        return False
    
    # 4. Implement removeRows().
    
    def removeRows(self, row, count, parent=QModelIndex()):

        self.beginRemoveRows(parent, row, row + count - 1)
        if parent.isValid():
            parent_item = parent.internalPointer()
        else:
            parent_item = self.root_item
        parent_item.remove_child(row)
        self.endRemoveRows()
        return True
