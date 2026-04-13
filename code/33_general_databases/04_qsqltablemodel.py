import sys
from PySide6.QtCore import Slot, QModelIndex, Qt
from PySide6.QtWidgets import (QApplication, QTableView, 
    QWidget, QVBoxLayout, QLabel)
from PySide6.QtSql import QSqlDatabase, QSqlTableModel, QSqlQuery


class Window(QWidget):
    
    def __init__(self):

        super().__init__()
        self.resize(450, 200)
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        # 1. Connect to the database.

        self.db = QSqlDatabase.addDatabase('QSQLITE')
        self.db.setConnectOptions('QSQLITE_OPEN_URI')
        self.db.setDatabaseName('file:finance_demo.sqlite?mode=rw')
        
        if not self.db.open():
            print(f'Database error : {self.db.lastError().text()}')
            return
        
        QSqlQuery().exec('PRAGMA foreign_keys = ON;')
        
        # 2. Create the model.
        
        self.model = QSqlTableModel()
        self.model.setTable('Accounts')
        self.model.setEditStrategy(
            QSqlTableModel.EditStrategy.OnManualSubmit)
        
        headers = [
            'ID', 'User ID', 'Account Name', 'Balance'
        ]
        for col, text in enumerate(headers):
            self.model.setHeaderData(col, Qt.Horizontal, text)
        
        self.model.select()
        
        # 3. Create the view and set its model.
        
        self.view = QTableView()        
        self.view.setModel(self.model)
        layout.addWidget(self.view)
        
        self.label = QLabel()
        layout.addWidget(self.label)
        
        self.view.selectionModel().currentChanged.connect(
            self.save_changes)
    
    # 4. Save the changes to the database
    #    when the current cell changes.
    
    @Slot(QModelIndex, QModelIndex)
    def save_changes(self, current, previous):
        
        if not previous.isValid():
            return
        
        if self.model.isDirty():
            if self.model.submitAll():
                self.label.setStyleSheet('color: green')
                self.label.setText('Changes saved')
                self.view.setCurrentIndex(current)
            else:
                error_text = self.model.lastError().text()
                self.label.setStyleSheet('color: red')
                self.label.setText(error_text)
                self.model.revertAll()
        else:
            self.label.clear()


if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    main_window = Window()
    main_window.show()
    sys.exit(app.exec())
