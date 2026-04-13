import sys
from PySide6.QtCore import Slot
from PySide6.QtWidgets import (QApplication, 
    QWidget, QPushButton, QVBoxLayout)
from PySide6.QtSql import QSqlDatabase, QSqlQuery


class Window(QWidget):
    
    def __init__(self):

        super().__init__()
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        with open('finance_demo.sql', 'r') as f:
            self.query_string = f.read()

        self.button = QPushButton('(Re)generate database')
        self.button.clicked.connect(self.on_button_clicked)
        layout.addWidget(self.button)
        
        self.db = QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('finance_demo.sqlite')
        
        result = self.db.open()
        if result:
            print('Connected!')
        else:
            self.button.setDisabled(True)
            print('Failed to connect to the database')
    
    @Slot()
    def on_button_clicked(self, checked):
        statements = [s.strip() for s in self.query_string.split(';') if s.strip()]

        for statement in statements:
            query = QSqlQuery()
            if not query.exec(statement):
                print(f"Error in statement:\n{statement}")
                print(query.lastError().text())
                return

        print('Database generated')
    

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    main_window = Window()
    main_window.show()
    sys.exit(app.exec())
