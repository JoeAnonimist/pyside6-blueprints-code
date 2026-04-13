from PySide6.QtCore import Qt
from PySide6.QtSql import QSqlRelationalTableModel, QSqlRelation

# 1. Subclass the QSqlRelationalTableModel class

class TransactionsTableModel(QSqlRelationalTableModel):
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.tablename = 'Transactions'
        self.setTable(self.tablename)
        self.setRelation(1,
            QSqlRelation('Accounts', 'account_id', 'account_name'))
        self.setRelation(2,
            QSqlRelation('Categories', 'category_id', 'category_name'))

    def flags(self, index):
        flags = super().flags(index)
        # We know PK is the first column.
        if index.column() == 0:
            flags &= ~Qt.ItemFlag.ItemIsEditable
        return flags