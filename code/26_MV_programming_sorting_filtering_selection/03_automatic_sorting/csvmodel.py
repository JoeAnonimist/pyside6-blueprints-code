from PySide6.QtCore import QAbstractTableModel, QModelIndex, Qt


class CsvModel(QAbstractTableModel):
    
    def __init__(self, parent=None):
        
        super().__init__(parent)
        
        self.header = ['Indicator', 'Value (%)', 
            'Aggregate', 'Include in report']
        self.csv_data = [
            ['GDP', 3, 1, True],
            ['CPI', 6, 1, True],
            ['Jobs', 5, 0, True],
            ['Confidence', 75, 0, True],
            ['Industry', 92, 0, True],
            ['Retail', 4, 1, True],
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
            if index.column() == 2:
                return value == 1
            else:
                return value
    
    # 2. Sort the data whenever it is modified.
    
    def setData(self, index, value, role):
        
        if role == Qt.ItemDataRole.EditRole:
            if index.column() == 2:
                value = 1 if value else 0
            if self.csv_data[index.row()][index.column()] != value:
                self.csv_data[index.row()][index.column()] = value
                if index.column() == 0:
                    self.sort(0)
                self.dataChanged.emit(index, index)
                return True
            return False
        return False
    
    # 1. Implement the sort() method.
    
    def sort(self, column, order=Qt.SortOrder.AscendingOrder):
        
        self.layoutAboutToBeChanged.emit()
        
        # backup
        old_order = self.csv_data[:]
        
        self.csv_data.sort(
            key=lambda row: row[column],
            reverse=(order == Qt.SortOrder.DescendingOrder)
        )
        
        new_position = {}
        for i, row in enumerate(self.csv_data):
            new_position[id(row)] = i
            
        old_indices = self.persistentIndexList()
        new_indices = []
        for idx in old_indices:
            new_row = new_position[id(old_order[idx.row()])]
            new_indices.append(self.index(new_row, idx.column()))
        self.changePersistentIndexList(old_indices, new_indices)

        self.layoutChanged.emit()
    
    def flags(self, index):
        if not index.isValid():
            return Qt.ItemFlags()
        return (super().flags(index) |
                    Qt.ItemFlag.ItemIsEditable)

    def headerData(self, section, orientation, role):
        if orientation == Qt.Orientation.Horizontal:
            if role == Qt.ItemDataRole.DisplayRole:
                return self.header[section]
