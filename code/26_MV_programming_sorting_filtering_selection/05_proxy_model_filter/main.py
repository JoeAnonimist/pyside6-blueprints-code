import sys

from PySide6.QtCore import Qt, QSortFilterProxyModel
from PySide6.QtWidgets import (QApplication, QWidget,
    QLineEdit, QTableView, QVBoxLayout)
from PySide6.QtTest import QAbstractItemModelTester
from csvmodel import CsvModel


class Window(QWidget):
    
    def __init__(self):

        super().__init__()

        layout = QVBoxLayout()
        self.setLayout(layout)

        model = CsvModel()
        QAbstractItemModelTester(model,
            QAbstractItemModelTester.FailureReportingMode.Warning)
        
        # 1. Create the proxy model and set its source.
        
        self.proxy_model = QSortFilterProxyModel()
        self.proxy_model.setSourceModel(model)
        
        # 2. Set the proxy model options.
        
        self.proxy_model.setFilterKeyColumn(1)
        self.proxy_model.setFilterCaseSensitivity(
            Qt.CaseSensitivity.CaseInsensitive)
        
        # 3. Create the view and assign the proxy model to it.
        
        view = QTableView()
        view.setModel(self.proxy_model)
        view.resizeColumnsToContents()
        layout.addWidget(view)
        
        # 4. Filter the model based on the text the user enters.
        
        filter_edit = QLineEdit()
        filter_edit.textChanged.connect(self.on_text_changed)
        layout.addWidget(filter_edit)
        
    def on_text_changed(self, text):
        self.proxy_model.setFilterRegularExpression(text)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    main_window = Window()
    main_window.show()
    sys.exit(app.exec())
