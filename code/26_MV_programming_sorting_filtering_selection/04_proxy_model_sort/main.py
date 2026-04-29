import sys
from PySide6.QtCore import QSortFilterProxyModel
from PySide6.QtWidgets import (QApplication, QWidget,
    QTableView, QVBoxLayout, QLabel)
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
        
        view = QTableView()
        view.setModel(model)
        
        # 1. Create the proxy model and set its source model.
        
        proxy_model = QSortFilterProxyModel(self)
        proxy_model.setSourceModel(model)
        
        # 2. Create the view and assign the proxy model to it.
        
        proxy_view = QTableView()
        proxy_view.setModel(proxy_model)
        
        # 3. Enable sorting in the view.
        
        proxy_view.setSortingEnabled(True)
        
        proxy_view.resizeColumnsToContents()
        layout.addWidget(QLabel('Source Model View'))
        layout.addWidget(view)
        layout.addWidget(QLabel('Proxy Model View'))
        layout.addWidget(proxy_view)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    main_window = Window()
    main_window.show()
    sys.exit(app.exec())
