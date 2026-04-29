import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QApplication, QWidget,
    QTableView, QVBoxLayout)
from PySide6.QtTest import QAbstractItemModelTester
from csvmodel import CsvModel


class Window(QWidget):
    
    def __init__(self):

        super().__init__()

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.model = CsvModel()
        QAbstractItemModelTester(self.model,
            QAbstractItemModelTester.FailureReportingMode.Warning)
        
        # 3. Perform the initial sort.
        
        self.model.sort(0, Qt.SortOrder.AscendingOrder)
        
        self.view = QTableView()
        self.view.setModel(self.model)

        self.view.resizeColumnsToContents()
        layout.addWidget(self.view)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    main_window = Window()
    main_window.show()
    sys.exit(app.exec())
