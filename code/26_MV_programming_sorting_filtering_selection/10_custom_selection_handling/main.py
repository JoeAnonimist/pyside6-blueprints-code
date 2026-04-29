import sys
from PySide6.QtWidgets import (QApplication, QWidget,
    QTableView, QVBoxLayout, QPushButton, QAbstractItemView)
from csvmodel import CsvModel
from selectionmodels import AggregateSelectionModel


class Window(QWidget):

    def __init__(self):

        super().__init__()

        layout = QVBoxLayout()
        self.setLayout(layout)

        model = CsvModel()

        self.view = QTableView()
        self.view.setModel(model)
        self.view.setSelectionBehavior(
            QAbstractItemView.SelectionBehavior.SelectRows)
        self.view.setSelectionMode(
            QAbstractItemView.SelectionMode.ExtendedSelection)

        # 2. Replace the view's default selection model.

        self.view.setSelectionModel(
            AggregateSelectionModel(model, self))

        self.view.resizeColumnsToContents()
        layout.addWidget(self.view)
        
        # 3. Let the user select all aggregate rows.
        
        self.select_button = QPushButton('Select all aggregate rows.')
        self.select_button.clicked.connect(self.view.selectAll)
        layout.addWidget(self.select_button)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    main_window = Window()
    main_window.show()
    sys.exit(app.exec())
