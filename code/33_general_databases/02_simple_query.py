import sys
from PySide6.QtCore import Slot
from PySide6.QtWidgets import (QApplication, 
    QWidget, QPushButton, QComboBox, QVBoxLayout)
from PySide6.QtSql import QSqlDatabase, QSqlQuery, QSql


class Window(QWidget):
    
    def __init__(self):

        super().__init__()
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.query_string = ''
        self.tables = QComboBox()
        self.tables.currentIndexChanged.connect(self.update_query_string)

        self.button = QPushButton('Execute query')
        self.button.clicked.connect(self.execute_query)
        
        layout.addWidget(self.tables)
        layout.addWidget(self.button)
        
        # 1. Connect to the database
        
        self.db = QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('finance_demo.sqlite')
        self.db.setConnectOptions('QSQLITE_OPEN_READONLY')
        
        # 2. Populate the combobox with table names.
        
        result = self.db.open()
        if result:
            print('Connected!')
            self.tables.addItems(
                [table for table in self.db.tables(QSql.TableType.Tables)
                 if not table.startswith('sqlite_')])
        else:
            self.button.setDisabled(True)
            print('Failed to connect to the database')
    
    @Slot()
    def execute_query(self):
        
        # 3. Execute the query and process the results.
        
        query = QSqlQuery()
        result = query.exec(self.query_string)
        
        if result:
            while query.next():
                record = query.record()
                for i in range(record.count()):
                    print(f'{query.value(i)}\t', end='')
                print()
        else:
            print(query.lastError().text())
            
    @Slot()
    def update_query_string(self):
        table_name = self.tables.currentText()
        self.query_string = f'Select * From {table_name}'
        print(f'Current query: {self.query_string}')
    

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    main_window = Window()
    main_window.show()
    sys.exit(app.exec())
