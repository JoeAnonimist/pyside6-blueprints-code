from PySide6.QtCore import QAbstractTableModel, QModelIndex, Qt
from PySide6.QtGui import QFont, QBrush, QColor


# 1. Create the model class.

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
        
        self.plus_brush = QBrush(QColor("#d9fdd3"))
        self.minus_brush = QBrush(QColor("#fce4e4"))

    def rowCount(self, parent=QModelIndex()):
        if parent.isValid():
            return 0
        return len(self.csv_data)
    
    def columnCount(self, parent=QModelIndex()):
        if parent.isValid():
            return 0
        return len(self.header)
    
    # 2. Customize the data() method.
    
    def data(self, index, role):

        if not index.isValid():
            return None
        
        row, col = index.row(), index.column()
        value = self.csv_data[row][col]

        if role == Qt.ItemDataRole.DisplayRole:
            if col in (2, 3):
                return 'YES' if value else 'NO'
            return value

        if role == Qt.ItemDataRole.EditRole:
            return value

        if role == Qt.ItemDataRole.CheckStateRole:
            if col == 3:
                if value:
                    return Qt.CheckState.Checked
                else:
                    return Qt.CheckState.Unchecked
            return None

        if role == Qt.ItemDataRole.BackgroundRole:
            if col == 1:
                if value >= 0:
                    return self.plus_brush
                else:
                    return self.minus_brush
            if col in (2, 3):
                if value:
                    return self.plus_brush
                else:
                    return self.minus_brush

        if role == Qt.ItemDataRole.FontRole:
            font = QFont()
            if ((col == 1 and value <= 0)
                or (col in (2, 3) and not value)):
                font.setItalic(True)
            return font

        if role == Qt.ItemDataRole.TextAlignmentRole:
            if col in (1, 2, 3):
                return Qt.AlignmentFlag.AlignCenter
            
        return None
    
    # 3. Customize setData().
    
    def setData(self, index, value, role):

        if not index.isValid():
            return False

        row, col = index.row(), index.column()

        if role == Qt.ItemDataRole.EditRole:
            if self.csv_data[row][col] != value:
                self.csv_data[row][col] = value
                self.dataChanged.emit(index, index)
                return True
            return False

        if role == Qt.ItemDataRole.CheckStateRole:
            if col == 3:
                checked = bool(value)
                if self.csv_data[row][col] != checked:
                    self.csv_data[row][col] = checked
                    self.dataChanged.emit(index, index)
                    return True
                return False
    
    # 4. Customize flags().
    
    def flags(self, index) -> Qt.ItemFlags:
        if not index.isValid():
            return Qt.ItemFlags()
        flags = super().flags(index)
        if index.column() in (1, 2):
            flags |= Qt.ItemFlags.ItemIsEditable
        if index.column() == 3:      # checkbox lives here
            flags |= Qt.ItemFlags.ItemIsUserCheckable
        return flags

    def headerData(self, section, orientation, role):
        if (orientation == Qt.Orientation.Horizontal
            and role == Qt.ItemDataRole.DisplayRole):
            return self.header[section]
        return super().headerData(section, orientation, role)
