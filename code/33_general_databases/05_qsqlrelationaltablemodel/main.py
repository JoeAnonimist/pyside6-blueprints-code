import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QApplication, 
    QWidget, QVBoxLayout, QTableView)
from PySide6.QtSql import (QSqlDatabase, 
    QSqlRelationalDelegate, QSqlQuery)
from models import TransactionsTableModel


class Window(QWidget):
    
    def __init__(self):

        super().__init__()
        self.resize(650, 400)
        
        layout = QVBoxLayout()
        self.setLayout(layout)

        self.db = QSqlDatabase.addDatabase('QSQLITE')
        self.db.setConnectOptions('QSQLITE_OPEN_URI')
        self.db.setDatabaseName('file:finance_demo.sqlite?mode=rw')
        
        if not self.db.open():
            print(f'Database error : {self.db.lastError().text()}')
            return
        
        QSqlQuery().exec('PRAGMA foreign_keys = ON;')
        
        # 2. Create a model instance.
        
        self.model = TransactionsTableModel()
        
        headers = [
            'ID', 'Account', 'Category',
            'Amount', 'Date', 'Description'
        ]
        for col, text in enumerate(headers):
            self.model.setHeaderData(col, Qt.Horizontal, text)
        
        self.model.select()
        # print(self.model.query().lastQuery())
        
        # 3. Create a view instance.
        
        self.view = QTableView()        
        self.view.setModel(self.model)
        
        # 4. Provide comboboxes

        delegate = QSqlRelationalDelegate(self.view)
        self.view.setItemDelegate(delegate)
        layout.addWidget(self.view)


if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    main_window = Window()
    main_window.show()
    sys.exit(app.exec())
