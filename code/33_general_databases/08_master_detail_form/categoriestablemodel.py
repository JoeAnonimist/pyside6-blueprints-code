from PySide6.QtCore import Qt
from PySide6.QtSql import QSqlTableModel

class CategoriesTableModel(QSqlTableModel):
    
    def flags(self, index):
        flags = super().flags(index)
        if index.column() == 0:
            flags &= ~Qt.ItemFlag.ItemIsEditable
        return flags
    
    def record(self):
        rec = super().record()
        rec.setGenerated(0, False)
        return rec