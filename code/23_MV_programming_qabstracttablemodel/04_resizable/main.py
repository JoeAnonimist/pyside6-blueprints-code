import sys
from PySide6.QtCore import Qt
from PySide6.QtTest import QAbstractItemModelTester
from PySide6.QtWidgets import (QApplication, QWidget,
    QTableView, QVBoxLayout, QPushButton)
from csvmodel import CsvModel


class Window(QWidget):
    
    def __init__(self):

        super().__init__()

        layout = QVBoxLayout()
        self.setLayout(layout)
        
        # 2. Create the model and view objects.

        self.model = CsvModel('data.csv')
        QAbstractItemModelTester(self.model,
            QAbstractItemModelTester.FailureReportingMode.Warning)
        self.view = QTableView()
        self.view.setModel(self.model)
        self.model.rowsInserted.connect(self.on_rows_inserted)
        self.view.resizeColumnsToContents()
        
        # 3. Add the Insert, Append and Remove buttons.

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
        
        self.model.dataChanged.connect(self.on_data_changed)
        
    def on_insert(self):
        row = self.view.currentIndex().row()
        self.model.insertRows(row, 1)
        
    def on_append(self):
        row = self.model.rowCount()
        self.model.insertRows(row, 1)
        index = self.model.index(row, 0)
        self.view.scrollTo(index)
    
    def on_remove(self):
        row = self.view.currentIndex().row()
        self.model.removeRows(row, 1)
        
    def on_rows_inserted(self, parent, first, last):
        index = self.model.index(first, 0)
        if index.isValid():
            self.view.setCurrentIndex(index)
        
    def on_data_changed(self, topLeft, bottomRight, roles):
        print(f'Model changed, r: {topLeft.row()}, c: {topLeft.column()}')
        data = topLeft.model().data(topLeft, Qt.ItemDataRole.DisplayRole)
        print(f'Data: {data}')
           

if __name__ == '__main__':

    app = QApplication(sys.argv)
    main_window = Window()
    main_window.show()
    sys.exit(app.exec())
