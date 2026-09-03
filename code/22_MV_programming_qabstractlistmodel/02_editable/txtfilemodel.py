from PySide6.QtCore import QAbstractListModel, Qt

# 1. Create a QAbstractListModel subclass
#    and make the data available to it.

class TxtFileModel(QAbstractListModel):
    
    def __init__(self, source, parent=None):
        
        super().__init__(parent)

        self.txt_data = []
        self.header = 'Clients'
        with open(source) as txt_file:
            for line in txt_file:
                self.txt_data.append(line.strip())
    
    # 2. Implement the rowCount() and data() methods
    
    def rowCount(self, parent) -> int:
        return len(self.txt_data)
    
    def data(self, index, role=Qt.ItemDataRole.DisplayRole) -> object|None:
        if role in [Qt.ItemDataRole.DisplayRole, Qt.ItemDataRole.EditRole]:
            return self.txt_data[index.row()]
        return None
    
    # 3. Implement the setData() method
    
    def setData(self, index, value, role) -> bool:
        if not index.isValid():
            return False
        if role == Qt.ItemDataRole.EditRole:
            if self.txt_data[index.row()] != value:
                self.txt_data[index.row()] = value
                self.dataChanged.emit(index, index, [role])
                return True
            return False
        return False
    
    # 4. Implement the flags() method
    
    def flags(self, index) -> Qt.ItemFlags:
        '''
        The tester specifically checks flags(QModelIndex())
        and expects it to return either 0 (no drop support
        on the root, which is correct for the simple
        editable list) or exactly Qt.ItemIsDropEnabled
        (to indicate drop-on-viewport support).
        Returning ItemIsEditable (or any other flags)
        for an invalid index violates this expectation,
        as editable doesn't make sense on the root.
        qt.modeltest: FAIL! flags == Qt::ItemIsDropEnabled || flags == 0 ()
        returned FALSE (/home/qt/work/qt/qtbase/src/testlib/qabstractitemmodeltester.cpp:377)
        '''
        if not index.isValid():
            return Qt.ItemFlags()
        return super().flags(index) | Qt.ItemFlags.ItemIsEditable

    def headerData(self, section, orientation, role) -> object | None:
        if orientation == Qt.Orientation.Horizontal:
            if role == Qt.ItemDataRole.DisplayRole:
                return self.header
