import sys
from PySide6.QtWidgets import QApplication, QTableView, QWidget, QVBoxLayout
from PySide6.QtTest import QAbstractItemModelTester
from models import CsvModel
from delegates import LedDelegate


class Window(QWidget):
    
    def __init__(self):

        super().__init__()

        layout = QVBoxLayout()
        self.setLayout(layout)

        model = CsvModel()
        QAbstractItemModelTester(model,
            QAbstractItemModelTester.FailureReportingMode.Warning)

        delegate = LedDelegate()
        
        view = QTableView()
        view.setModel(model)
        
        view.setItemDelegateForColumn(2, delegate)
        view.setItemDelegateForColumn(3, delegate)
        
        view.resizeColumnsToContents()
        view.setCurrentIndex(model.index(0, 2))
        view.setEditTriggers(
            QTableView.EditTrigger.EditKeyPressed |
            QTableView.EditTrigger.DoubleClicked)
        
        view.setFocus()
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
