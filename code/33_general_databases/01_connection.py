import sys
from PySide6.QtCore import Slot
from PySide6.QtWidgets import (QApplication, 
    QWidget, QPushButton, QVBoxLayout)
from PySide6.QtSql import QSqlDatabase


class Window(QWidget):
    
    def __init__(self):

        super().__init__()
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        self.connect_button = QPushButton('Connect to the database')
        self.connect_button.clicked.connect(self.connect_to_db)
        
        self.disconnect_button = QPushButton('Disconnect')
        self.disconnect_button.setEnabled(False)
        self.disconnect_button.clicked.connect(self.disconnect_from_db)

        self.info_button = QPushButton('Print database info')
        self.info_button.setEnabled(False)
        self.info_button.clicked.connect(self.print_db_info)
        
        layout.addWidget(self.connect_button)
        layout.addWidget(self.disconnect_button)
        layout.addWidget(self.info_button)
        
        # 1. Create a QSqlDatabase object
        #    and set the connection options.
        
        self.db = QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('finance_demo.sqlite')
        self.db.setConnectOptions('QSQLITE_OPEN_READONLY')
    
    @Slot()
    def connect_to_db(self):
        
        # 2. Connect to the database
        
        result = self.db.open()
        if result:
            print('Connected!')
            self.connect_button.setEnabled(False)
            self.info_button.setEnabled(True)
            self.disconnect_button.setEnabled(True)
        else:
            self.info_button.setEnabled(False)
            print('Failed to connect to the database')
            print(self.db.lastError().text())
            
    @Slot()
    def disconnect_from_db(self):
        if self.db.isOpen():
            self.connect_button.setEnabled(True)
            self.disconnect_button.setEnabled(False)
            self.info_button.setEnabled(False)
            self.db.close()
    
    # 3. Print database information
    
    @Slot()
    def print_db_info(self):
        print('Name: ', self.db.databaseName())
        print('Driver: ', self.db.driverName())
        print('Tables: ')
        for table in self.db.tables():
            print(f'\t{table}')
        

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    main_window = Window()
    main_window.show()
    sys.exit(app.exec())
