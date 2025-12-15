from PySide6.QtCore import QAbstractListModel, QModelIndex, Qt


class TxtFileModel(QAbstractListModel):
    
    def __init__(self, source, parent=None):
        
        super().__init__(parent)
        
        self.txt_data = []
        self.header = 'Clients'
        with open(source) as txt_file:
            for line in txt_file:
                self.txt_data.append(line.strip())
                
    def rowCount(self, parent=QModelIndex()) -> int:
        return len(self.txt_data)
    
    def data(self, index, role=Qt.ItemDataRole.DisplayRole) -> object|None:
        if role == Qt.ItemDataRole.DisplayRole \
        or role == Qt.ItemDataRole.EditRole:
            return self.txt_data[index.row()]
    
    def setData(self, index, value, role) -> bool:
        if not index.isValid():
            return False
        if role == Qt.ItemDataRole.EditRole:
            if self.txt_data[index.row()] != value:
                self.txt_data[index.row()] = value
                self.dataChanged.emit(index, index, [role])
                return True
            return False
        return False
    
    def flags(self, index) -> Qt.ItemFlags:
        return super().flags(index) | Qt.ItemFlags.ItemIsEditable
    
    def insertRows(self, row, count, parent=QModelIndex()):
        if 0 <= row <= self.rowCount():
            self.beginInsertRows(parent, row, row)
            self.txt_data.insert(row, '')
            self.endInsertRows()
            return True
        return False

    def removeRows(self, row, count, parent=QModelIndex()):
        if 0 <= row < len(self.txt_data):
            self.beginRemoveRows(parent, row, row + 1)
            self.txt_data[row:row + 1] = []
            self.endRemoveRows()
            return True
        return False

    # QListView does not have a header
    # so this is never executed!

    def headerData(self, section, orientation, role):
        if orientation == Qt.Orientation.Horizontal:
            if role == Qt.ItemDataRole.DisplayRole:
                return self.header
