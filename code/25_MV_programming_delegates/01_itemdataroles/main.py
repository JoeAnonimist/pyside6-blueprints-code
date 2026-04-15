import sys
from PySide6.QtWidgets import (QApplication,
    QWidget, QTableView, QVBoxLayout)
from PySide6.QtTest import QAbstractItemModelTester
from models import CsvModel


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
        view.resizeColumnsToContents()
        layout.addWidget(view)
        
        model.dataChanged.connect(self.on_data_changed)
        
    def on_data_changed(self, topLeft, bottomRight, roles):
        for row in topLeft.model().csv_data:
            print(row)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    main_window = Window()
    main_window.show()
    sys.exit(app.exec())
