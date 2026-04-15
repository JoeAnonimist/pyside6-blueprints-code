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
        
        if role in (Qt.ItemDataRole.DisplayRole,
                    Qt.ItemDataRole.EditRole):
            row, col = index.row(), index.column()
            value = self.csv_data[row][col]
            return value
    
    # 2. Convert the value from string to integer
    #    and store it.
    
    def setData(self, index, value, role):
        if not index.isValid():
            return False

        row, col = index.row(), index.column()

        if role == Qt.ItemDataRole.EditRole:
            print(value)
            if col == 1:
                try:
                    value = int(value)
                except (ValueError, TypeError):
                    print(value)
                    return False

            if self.csv_data[row][col] != value:
                self.csv_data[row][col] = value
                self.dataChanged.emit(index, index)
                return True
        return False

    def flags(self, index):
        if not index.isValid():
            return Qt.ItemFlags()
        flags = super().flags(index)
        flags |= Qt.ItemFlags.ItemIsEditable
        return flags

    def headerData(self, section, orientation, role):
        if (orientation == Qt.Orientation.Horizontal 
            and role == Qt.ItemDataRole.DisplayRole):
            return self.header[section]
        return super().headerData(section, orientation, role)
    