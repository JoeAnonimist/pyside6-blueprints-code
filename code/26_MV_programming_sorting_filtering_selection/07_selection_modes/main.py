import sys
from PySide6.QtWidgets import (QApplication, QWidget,
    QTableView, QVBoxLayout, QComboBox, QLabel)
from csvmodel import CsvModel


class Window(QWidget):

    def __init__(self):

        super().__init__()

        layout = QVBoxLayout()
        self.setLayout(layout)

        model = CsvModel()

        # 1. Create the view and set the initial
        #    selection behavior and mode.

        self.view = QTableView()
        self.view.setModel(model)
        self.view.setSelectionBehavior(
            QTableView.SelectionBehavior.SelectItems)
        self.view.setSelectionMode(
            QTableView.SelectionMode.SingleSelection)
        self.view.resizeColumnsToContents()
        layout.addWidget(self.view)

        # 2. Add a combobox to switch between selection modes.

        self.mode_combo = QComboBox()
        self.mode_combo.addItem('Single',
            QTableView.SelectionMode.SingleSelection)
        self.mode_combo.addItem('Contiguous',
            QTableView.SelectionMode.ContiguousSelection)
        self.mode_combo.addItem('Extended',
            QTableView.SelectionMode.ExtendedSelection)
        self.mode_combo.addItem('Multi',
            QTableView.SelectionMode.MultiSelection)
        self.mode_combo.addItem('No Selection',
            QTableView.SelectionMode.NoSelection)
        
        self.mode_combo.setCurrentIndex(0)
        self.mode_combo.currentIndexChanged.connect(self.on_mode_changed)
        layout.addWidget(QLabel('Choose Selection Mode'))
        layout.addWidget(self.mode_combo)
        
        # 3. Add the combobox to change selection behavior.
        
        self.behavior_combo = QComboBox()
        self.behavior_combo.addItem('Select Items',
            QTableView.SelectionBehavior.SelectItems)
        self.behavior_combo.addItem('Select Rows',
            QTableView.SelectionBehavior.SelectRows)
        self.behavior_combo.addItem('Select Columns',
            QTableView.SelectionBehavior.SelectColumns)
        
        self.behavior_combo.setCurrentIndex(0)
        self.behavior_combo.currentIndexChanged.connect(
            self.on_behavior_changed)        
        layout.addWidget(QLabel('Choose Selection Behavior'))
        layout.addWidget(self.behavior_combo)

    def on_mode_changed(self, index):
        mode = self.mode_combo.itemData(index)
        self.view.setSelectionMode(mode)
        
    def on_behavior_changed(self, index):
        behavior = self.behavior_combo.itemData(index)
        self.view.setSelectionBehavior(behavior)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    main_window = Window()
    main_window.show()
    sys.exit(app.exec())
