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
        
        self.row_indices = list(range(len(self.csv_data)))

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
        
        sorted_row = self.row_indices[index.row()]
        value = self.csv_data[sorted_row][index.column()]

        if role == Qt.ItemDataRole.DisplayRole:
            return value
        if role == Qt.ItemDataRole.EditRole:
            if index.column() == 2:
                return value == 1
            else:
                return value
    
    def setData(self, index, value, role):
        
        if role == Qt.ItemDataRole.EditRole:
            if index.column() == 2:
                value = 1 if value else 0
            if self.csv_data[index.row()][index.column()] != value:
                self.csv_data[index.row()][index.column()] = value
                self.dataChanged.emit(index, index)
                return True
            return False
        return False

    def sort(self, column, order):
        
        self.layoutAboutToBeChanged.emit()
        
        old_row_indices = self.row_indices[:]
        
        self.row_indices.sort(
            key=lambda i: self.csv_data[i][column],
            reverse=(order == Qt.SortOrder.DescendingOrder)
        )
        
        new_position = {}
        for new_row, source_row in enumerate(self.row_indices):
            new_position[source_row] = new_row

        old_indices = self.persistentIndexList()
        new_indices = []
        for idx in old_indices:
            source_row = old_row_indices[idx.row()]
            new_row = new_position[source_row]
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
