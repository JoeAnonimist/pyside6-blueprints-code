import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QApplication, 
    QWidget, QVBoxLayout, QTableView)
from PySide6.QtSql import (QSqlDatabase, QSqlQueryModel, QSqlQuery)


class Window(QWidget):
    
    def __init__(self, parent=None):

        super().__init__(parent)
        self.resize(850, 350)
        layout = QVBoxLayout()
        self.setLayout(layout)

        self.db = QSqlDatabase.addDatabase('QSQLITE')
        self.db.setConnectOptions('QSQLITE_OPEN_URI')
        self.db.setDatabaseName('file:finance_demo.sqlite?mode=rw')
        
        if not self.db.open():
            print(f'Database error : {self.db.lastError().text()}')
            return
        
        QSqlQuery().exec('PRAGMA foreign_keys = ON;')
        
        # 1. Get the query text.
        
        with open('account_summary.sql', 'r') as f:
            query_str = f.read()
        
        # 2. Create the model and query the database.
        
        self.model = QSqlQueryModel()
        self.model.setQuery(query_str)
        
        if self.model.query().lastError().isValid():
            print(f'Query error: {self.table_model.query().lastError().text()}')
            return
        
        headers = [
            'Account ID', 'Account Name', 'Owner',
            'Category', 'Transaction Count', 'Total Amount',
            'Avg Transaction', 'Net Balance'
        ]

        for col, text in enumerate(headers):
            self.model.setHeaderData(
                col, Qt.Orientation.Horizontal, text)
        
        # 3. Create the view and assign the model to it.
        
        self.view = QTableView()        
        self.view.setModel(self.model)
        self.view.setAlternatingRowColors(True)
        
        layout.addWidget(self.view)


if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    main_window = Window()
    main_window.show()
    sys.exit(app.exec())
