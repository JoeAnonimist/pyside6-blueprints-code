import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QApplication,
    QWidget, QTableView, QVBoxLayout)
from PySide6.QtTest import QAbstractItemModelTester
from csvmodel import CsvModel


class Window(QWidget):
    
    def __init__(self):

        super().__init__()

        layout = QVBoxLayout()
        self.setLayout(layout)
        
        # 5. Use the model
        #    Create the model, create the view
        #    and assign the model to the view.

        model = CsvModel('data.csv')
        QAbstractItemModelTester(model,
            QAbstractItemModelTester.FailureReportingMode.Warning)
        view = QTableView()
        view.setModel(model)
        view.resizeColumnsToContents()
        layout.addWidget(view)
        
        model.dataChanged.connect(self.on_data_changed)
        
    def on_data_changed(self, topLeft, bottomRight, roles):
        print(f'Model changed, r: {topLeft.row()}, c: {topLeft.column()}')
        data = topLeft.model().data(topLeft, Qt.ItemDataRole.DisplayRole)
        print(f'Data: {data}')


if __name__ == '__main__':

    app = QApplication(sys.argv)
    main_window = Window()
    main_window.show()
    sys.exit(app.exec())

