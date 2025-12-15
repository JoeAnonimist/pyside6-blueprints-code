import sys
from PySide6.QtWidgets import (QApplication,
    QWidget, QListView, QPushButton, QVBoxLayout)
from PySide6.QtTest import QAbstractItemModelTester
from txtfilemodel import TxtFileModel


class Window(QWidget):
    
    def __init__(self):

        super().__init__()

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.model = TxtFileModel('data.txt')
        QAbstractItemModelTester(self.model)
        self.model.rowsInserted.connect(self.on_rows_inserted)
        
        self.view = QListView()
        self.view.setModel(self.model)
     
        self.insert_button = QPushButton('Insert new')
        self.insert_button.clicked.connect(self.on_insert)
        
        self.append_button = QPushButton('Append new')
        self.append_button.clicked.connect(self.on_append)
        
        self.remove_button = QPushButton('Remove current')
        self.remove_button.clicked.connect(self.on_remove)

        layout.addWidget(self.view)
        layout.addWidget(self.insert_button)
        layout.addWidget(self.append_button)
        layout.addWidget(self.remove_button)
    
    # 4. Use insertRows() and removeRows()
    
    def on_insert(self):
        row = self.view.selectionModel().currentIndex().row()
        self.model.insertRow(row)
        
    def on_append(self):
        row = self.model.rowCount()
        self.model.insertRow(row)
        index = self.model.index(row, 0)
        self.view.scrollTo(index)
    
    def on_remove(self):
        index = self.view.currentIndex()
        self.model.removeRow(index.row())
    
    def on_rows_inserted(self, parent, first, last):
        index = self.model.index(first, 0)
        if index.isValid():
            self.view.setCurrentIndex(index)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    main_window = Window()
    main_window.show()
    sys.exit(app.exec())
