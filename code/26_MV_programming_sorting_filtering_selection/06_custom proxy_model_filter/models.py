from PySide6.QtCore import QAbstractTableModel, QModelIndex, Qt


class CsvModel(QAbstractTableModel):
    
    def __init__(self, parent=None):
        
        super().__init__(parent)
        
        self.header = ['Indicator', 'Value (%)',
                       'Aggregate', 'Include in report']
        self.csv_data = [
            ['GDP',       2.4,  1, True],
            ['CPI',       8.7,  1, True],
            ['Jobs',      0.3,  0, True],
            ['Confidence',74.0, 0, True],
            ['Industry',  91.5, 1, True],
            ['Retail',    3.1,  1, True],
            ['Inflation', 0.1,  1, True],
            ['PMI',       62.3, 0, True],
            ['Trade',     88.0, 1, True],
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
        
        value = self.csv_data[index.row()][index.column()]

        if role == Qt.ItemDataRole.DisplayRole:
            return value
        if role == Qt.ItemDataRole.EditRole:
            return value
    
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
                    Qt.ItemFlag.ItemIsEditable)

    def headerData(self, section, orientation, role):
        if orientation == Qt.Orientation.Horizontal:
            if role == Qt.ItemDataRole.DisplayRole:
                return self.header[section]
