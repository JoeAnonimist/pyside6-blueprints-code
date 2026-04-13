import sys
from PySide6.QtCore import Slot
from PySide6.QtWidgets import (QApplication, 
    QWidget, QPushButton, QVBoxLayout, QLineEdit)
from PySide6.QtSql import QSqlDatabase, QSqlQuery


class Window(QWidget):
    
    def __init__(self):

        super().__init__()
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        self.name_edit = QLineEdit()
        self.name_edit.setPlaceholderText('Enter user name')
        self.email_edit = QLineEdit()
        self.email_edit.setPlaceholderText('Enter e-mail')

        self.button = QPushButton('Add user')
        self.button.clicked.connect(self.on_button_clicked)
        
        layout.addWidget(self.name_edit)
        layout.addWidget(self.email_edit)
        layout.addWidget(self.button)
        
        # 1. Connect to the database
        
        self.db = QSqlDatabase.addDatabase('QSQLITE')
        self.db.setConnectOptions('QSQLITE_OPEN_URI')
        self.db.setDatabaseName('file:finance_demo.sqlite?mode=rw')
        
        result = self.db.open()
        if result:
            print('Connected!')
        else:
            self.button.setDisabled(True)
            print('Failed to connect to the database')
    
    @Slot()
    def on_button_clicked(self):
        
        # 2. Get and validate user-entered data
        
        username = self.name_edit.text().strip()
        email = self.email_edit.text().strip()
        
        if not username:
            print('Username cannot be empty')
            return
        if not email:
            print('Email cannot be empty')
            return
        
        query = QSqlQuery()
        query.prepare('''
            Insert Into Users (username, email)
            Values (:username, :email)
            ''')

        query.bindValue(':username', username)
        query.bindValue(':email', email)
        
        # 3. Execute the query and display the outcome
        
        if query.exec():
            print('User added successfully')
            self.name_edit.clear()
            self.email_edit.clear()
        else:
            print(query.lastError().text())
    

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    main_window = Window()
    main_window.show()
    sys.exit(app.exec())
