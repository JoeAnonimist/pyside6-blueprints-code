import sys
from PySide6.QtTest import QAbstractItemModelTester
from PySide6.QtWidgets import (QApplication, QWidget,
    QPushButton, QTreeView, QVBoxLayout)
from jsonmodel import JsonModel


class Window(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.model = JsonModel('data.json')
        QAbstractItemModelTester(self.model,
            QAbstractItemModelTester.FailureReportingMode.Warning)
        
        self.view = QTreeView()
        self.view.setModel(self.model)

        self.insert_sibling_button = QPushButton('Insert sibling node')
        self.insert_sibling_button.clicked.connect(self.on_insert_sibling)
        
        self.insert_child_button = QPushButton('Insert child node')
        self.insert_child_button.clicked.connect(self.on_insert_child)
        
        self.remove_button = QPushButton('Remove current node')
        self.remove_button.clicked.connect(self.on_remove)

        layout.addWidget(self.view)
        layout.addWidget(self.insert_sibling_button)
        layout.addWidget(self.insert_child_button)
        layout.addWidget(self.remove_button)
        
    def on_insert_sibling(self):
        row = self.view.selectionModel().currentIndex().row()
        parent = self.view.selectionModel().currentIndex().parent()
        self.model.insertRow(row + 1, parent)
    
    def on_insert_child(self):
        parent = self.view.selectionModel().currentIndex()
        self.model.insertRow(self.model.rowCount(parent), parent)
    
    def on_remove(self):
        row = self.view.selectionModel().currentIndex().row()
        parent = self.view.selectionModel().currentIndex().parent()
        self.model.removeRow(row, parent)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    main_window = Window()
    main_window.show()
    sys.exit(app.exec())
