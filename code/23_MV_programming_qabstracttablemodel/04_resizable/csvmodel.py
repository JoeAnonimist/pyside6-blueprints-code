import csv
from PySide6.QtCore import QAbstractTableModel, QModelIndex, Qt

# 1. Create the model.

class CsvModel(QAbstractTableModel):
    
    def __init__(self, source, parent=None):
        
        super().__init__(parent)
        
        self.csv_data = []
        with open(source) as csv_file:
            reader = csv.reader(csv_file)
            self.header = next(reader)
            for row in reader:
                self.csv_data.append(row)
                
    def rowCount(self, parent=QModelIndex()):
        if parent.isValid():
            return 0
        return len(self.csv_data)
    
    def columnCount(self, parent=QModelIndex()):
        if parent.isValid():
            return 0
        return 4
    
    def data(self, index, role):
        if role in (Qt.ItemDataRole.DisplayRole,
                    Qt.ItemDataRole.EditRole):
            return self.csv_data[index.row()][index.column()]

    # Editable models implement setData() and flags()
    
    def setData(self, index, value, role):
        if role == Qt.ItemDataRole.EditRole:
            if self.csv_data[index.row()][index.column()] != value:
                self.csv_data[index.row()][index.column()] = value
                self.dataChanged.emit(index, index)
                return True
            return False
        return False
    
    def flags(self, index):
        if not index.isValid():
            return Qt.ItemFlags()
        return (super().flags(index) |
            Qt.ItemFlags.ItemIsEditable)
    
    def insertRows(self, row, count, parent=QModelIndex()):
        if 0 <= row <= self.rowCount():
            self.beginInsertRows(parent, row, row)
            self.csv_data.insert(row, ['', '', '', ''])
            self.endInsertRows()
            return True
        else:
            return False
        
    def removeRows(self, row, count, parent=QModelIndex()):
        if 0 <= row < len(self.csv_data):
            self.beginRemoveRows(parent, row, row)
            self.csv_data[row:row + 1] = []
            self.endRemoveRows()
            return True
        else:
            return False

    def headerData(self, section, orientation, role):
        if orientation == Qt.Orientation.Horizontal:
            if role == Qt.ItemDataRole.DisplayRole:
                return self.header[section]
