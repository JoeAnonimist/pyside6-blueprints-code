import sys
from PySide6.QtCore import QSortFilterProxyModel
from PySide6.QtWidgets import (QApplication, QWidget,
    QTableView, QVBoxLayout)
from PySide6.QtTest import QAbstractItemModelTester
from models import CsvModel
from proxymodels import OutlierProxyModel



class Window(QWidget):
    
    def __init__(self):

        super().__init__()

        layout = QVBoxLayout()
        self.setLayout(layout)

        model = CsvModel()
        QAbstractItemModelTester(model,
            QAbstractItemModelTester.FailureReportingMode.Warning)
        
        # 3. Create an OutlierProxyModel and assign it to the view.
        
        self.proxy_model = OutlierProxyModel(1.0, 50.0, self)
        self.proxy_model.setSourceModel(model)
        
        view = QTableView()
        view.setModel(self.proxy_model)
        view.resizeColumnsToContents()
        layout.addWidget(view)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    main_window = Window()
    main_window.show()
    sys.exit(app.exec())
