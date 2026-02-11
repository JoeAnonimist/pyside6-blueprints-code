import csv
from PySide6.QtCore import QAbstractTableModel, QModelIndex, Qt

# 1. Create a QAbstractTableModel subclass.
#    We read the data from a csv file using Python's csv.reader
#    Each row in a reader object is a list making self.csv_data
#    a two-dimensional list suitable for use
#    with QAbstractTableModel.

class CsvModel(QAbstractTableModel):
    
    def __init__(self, source, parent=None):
        
        super().__init__(parent)
        
        self.csv_data = []
        with open(source) as csv_file:
            reader = csv.reader(csv_file)
            self.header = next(reader)
            for row in reader:
                self.csv_data.append(row)

    # 2. Implement the rowCount() and columnCount() methods

    def rowCount(self, parent=QModelIndex()) -> int:
        # Must return zero if parent is valid
        if parent.isValid():
            return 0
        return len(self.csv_data)

    def columnCount(self, parent=QModelIndex()) -> int:
        # Must return zero if parent is valid
        if parent.isValid():
            return 0
        return 4
    
    # 3. Implement the data() method
    
    def data(self, index, role):
        if role == Qt.ItemDataRole.DisplayRole:
            return self.csv_data[index.row()][index.column()]
        
    # QTableView can have a header
    # but implementing headerData() is still optional.

    def headerData(self, section, orientation, role):
        if orientation == Qt.Orientation.Horizontal:
            if role == Qt.ItemDataRole.DisplayRole:
                return self.header[section]
