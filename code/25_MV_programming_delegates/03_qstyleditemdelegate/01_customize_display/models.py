from PySide6.QtCore import QAbstractTableModel, QModelIndex, Qt


class CsvModel(QAbstractTableModel):
    
    def __init__(self, parent=None):
        
        super().__init__(parent)
        
        self.header = ['Indicator', 'Change (%)', 
            'Aggregate', 'Include in report']
        self.csv_data = [
            ['GDP', 3, True, True],
            ['CPI', 6, True, True],
            ['Jobs', 5, False, True],
            ['Confidence', 75, False, True],
            ['Industry', 92, False, True],
            ['Retail', 4, True, True],
        ]

    def rowCount(self, parent=QModelIndex()):
        if parent.isValid():
            return 0
        return len(self.csv_data)
    
    def columnCount(self, parent=QModelIndex()):
        if parent.isValid():
            return 0
        return len(self.header)
    
    def data(self, index, role):

        if not index.isValid():
            return None

        row, col = index.row(), index.column()
        value = self.csv_data[row][col]

        if role == Qt.ItemDataRole.DisplayRole:
            if isinstance(value, bool):
                return None
            return value

        if role == Qt.ItemDataRole.EditRole:
            return value

        return None
    
    def setData(self, index, value, role):
        if role == Qt.ItemDataRole.EditRole:
            if self.csv_data[index.row()][index.column()] != value:
                self.csv_data[index.row()][index.column()] = value
                self.dataChanged.emit(index, index)
                return True
            return False
        return False
    
    def flags(self, index) -> Qt.ItemFlag:
        if not index.isValid():
            return Qt.ItemFlags()
        return (super().flags(index) |
                    Qt.ItemFlag.ItemIsEditable)

    def headerData(self, section, orientation, role):
        if orientation == Qt.Orientation.Horizontal:
            if role == Qt.ItemDataRole.DisplayRole:
                return self.header[section]
