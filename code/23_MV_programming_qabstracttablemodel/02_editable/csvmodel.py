import csv
from PySide6.QtCore import (QAbstractTableModel,
    QModelIndex, Qt)

# 1. Create a QAbstractTableModel subclass
#    same as in the read-only subclass example.

class CsvModel(QAbstractTableModel):
    
    def __init__(self, source, parent=None):
        
        super().__init__(parent)
        
        self.csv_data = []
        with open(source) as csv_file:
            reader = csv.reader(csv_file)
            self.header = next(reader)
            for row in reader:
                self.csv_data.append(row)

    # 2. Implement rowCount(), columnCount() and data()

    def rowCount(self, parent=QModelIndex()):
        # If parent is valid rowCount() must return zero
        if parent.isValid():
            return 0
        return len(self.csv_data)
    
    def columnCount(self, parent=QModelIndex()):
        # If parent is valid columnCount() must return zero
        if parent.isValid():
            return 0
        return 4
    
    def data(self, index, role):
        if role in (Qt.ItemDataRole.DisplayRole,
                    Qt.ItemDataRole.EditRole):
            return self.csv_data[index.row()][index.column()]

    # 3. Implement setData()
    
    def setData(self, index, value,
                role: int = Qt.ItemDataRole.EditRole) -> bool:
        if role == Qt.ItemDataRole.EditRole:
            if self.csv_data[index.row()][index.column()] != value:
                self.csv_data[index.row()][index.column()] = value
                self.dataChanged.emit(index, index)
                return True
            return False
        return False
    
    # 4. Implement flags()
    
    def flags(self, index) -> Qt.ItemFlag:
        if not index.isValid():
            return Qt.ItemFlags()
        return (super().flags(index) |
                    Qt.ItemFlag.ItemIsEditable)

    # QTableViews can have a header

    def headerData(self, section, orientation, role):
        if orientation == Qt.Orientation.Horizontal:
            if role == Qt.ItemDataRole.DisplayRole:
                return self.header[section]
