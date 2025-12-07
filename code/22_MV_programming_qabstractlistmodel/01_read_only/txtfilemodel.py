from PySide6.QtCore import QAbstractListModel, Qt

# 1. Create a QAbstractListModel subclass.
#    The data is read from a text file
#    and stored in a Python list.

class TxtFileModel(QAbstractListModel):
    
    def __init__(self, source, parent=None):
        
        super().__init__(parent)

        self.txt_data = []
        self.header = 'Clients'
        with open(source) as txt_file:
            for line in txt_file:
                self.txt_data.append(line.strip())
    
    # 2. Implement the rowCount() method
    
    def rowCount(self, parent) -> int:
        return len(self.txt_data)
    
    # 3. Implement the data() method
    
    def data(self, index, role=Qt.ItemDataRole.DisplayRole) -> object|None:
        if role == Qt.ItemDataRole.DisplayRole:
            return self.txt_data[index.row()]
        return None
    
    # 4. Optionally, implement the headerData() method
    #    QListView does not have a header
    #    so this is never executed!

    def headerData(self, section, orientation, role) -> object | None:
        if orientation == Qt.Orientation.Horizontal:
            if role == Qt.ItemDataRole.DisplayRole:
                return self.header
