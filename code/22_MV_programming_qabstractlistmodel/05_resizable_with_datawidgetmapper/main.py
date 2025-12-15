import sys
from PySide6.QtWidgets import (QApplication,
    QWidget, QListView, QLineEdit, QPushButton,
    QHBoxLayout, QVBoxLayout, QDataWidgetMapper)
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
        self.view.selectionModel().currentChanged.connect(
            self.on_current_changed)
        
        self.lineedit = QLineEdit()
        self.lineedit.returnPressed.connect(self.submit_new_value)
        self.view.activated.connect(self.lineedit.setFocus)

        self.mapper = QDataWidgetMapper()
        self.mapper.setModel(self.model)
        self.mapper.setSubmitPolicy(
            QDataWidgetMapper.SubmitPolicy.ManualSubmit)
        self.mapper.addMapping(self.lineedit, 0)
        self.mapper.toFirst()
        
        self.submit_button = QPushButton('Submit')
        self.submit_button.clicked.connect(self.submit_new_value)
        
        self.insert_button = QPushButton('Insert new')
        self.insert_button.clicked.connect(self.on_insert)
        
        self.append_button = QPushButton('Append new')
        self.append_button.clicked.connect(self.on_append)
        
        self.remove_button = QPushButton('Remove current')
        self.remove_button.clicked.connect(self.on_remove)

        input_layout = QVBoxLayout()
        input_layout.addWidget(self.lineedit)
        input_layout.addWidget(self.submit_button)

        buttons_layout = QVBoxLayout()
        buttons_layout.addWidget(self.insert_button)
        buttons_layout.addWidget(self.append_button)
        buttons_layout.addWidget(self.remove_button)

        controls_layout = QHBoxLayout()
        controls_layout.addLayout(input_layout)
        controls_layout.addLayout(buttons_layout)

        layout.addWidget(self.view)
        layout.addLayout(controls_layout)
        
    def on_current_changed(self, current, previous):
        self.mapper.setCurrentIndex(current.row())
        
    def submit_new_value(self):
        self.mapper.submit()
        self.view.setFocus()
        
    def on_insert(self):
        row = self.view.selectionModel().currentIndex().row()
        if self.model.insertRows(row, 1):
            self.mapper.setCurrentIndex(row)
            self.lineedit.setFocus()
        
    def on_append(self):
        row = self.model.rowCount()
        self.model.insertRows(row, 1)
        index = self.model.index(row, 0)
        self.view.scrollTo(index)
        self.lineedit.setFocus()
    
    def on_remove(self):
        index = self.view.currentIndex()
        self.model.removeRows(index.row(), 1)
    
    def on_rows_inserted(self, parent, first, last):
        index = self.model.index(first, 0)
        if index.isValid():
            self.view.setCurrentIndex(index)
            self.lineedit.setFocus()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    main_window = Window()
    main_window.show()
    sys.exit(app.exec())
