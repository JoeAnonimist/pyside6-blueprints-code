import sys
from PySide6.QtWidgets import (QApplication, QWidget,
    QTableView, QVBoxLayout)
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
        
        view.setSortingEnabled(True)
        
        view.resizeColumnsToContents()
        layout.addWidget(view)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    main_window = Window()
    main_window.show()
    sys.exit(app.exec())

