from PySide6.QtCore import QAbstractTableModel, QModelIndex, Qt


class CsvModel(QAbstractTableModel):
    
    def __init__(self, parent=None):
        
        super().__init__(parent)
        
        self.header = ['Indicator', 'Description']
        self.csv_data = [
            ['GDP', 'Measures total economic output'],
            ['CPI', 'Tracks consumer price changes'],
            ['Jobs', 'Employment level indicator'],
            ['Confidence', 'Consumer sentiment index'],
            ['Industry', 'Manufacturing activity gauge'],
            ['Retail', 'Consumer spending on goods'],
            ['Unemployment', 'Percentage of jobless workforce'],
            ['Inflation', 'Rate of price increase'],
            ['PPI', 'Producer price index'],
            ['Trade Balance', 'Export minus import value']
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
