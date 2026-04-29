import sys
from PySide6.QtCore import QItemSelection, Slot
from PySide6.QtWidgets import (QApplication, QWidget,
    QTableView, QVBoxLayout, QFormLayout, QGroupBox,
    QLabel, QAbstractItemView)
from csvmodel import CsvModel


class Window(QWidget):

    def __init__(self):

        super().__init__()

        layout = QVBoxLayout()
        self.setLayout(layout)
        
        # 1. Create the model and the view.

        self.model = CsvModel()
        self.view = QTableView()
        self.view.setModel(self.model)
        self.view.setSelectionBehavior(
            QAbstractItemView.SelectionBehavior.SelectRows)
        self.view.setSelectionMode(
            QAbstractItemView.SelectionMode.SingleSelection)
        self.view.resizeColumnsToContents()
        layout.addWidget(self.view)

        # 2. Create the detail panel.

        group = QGroupBox('Selected Indicator')
        form = QFormLayout()
        group.setLayout(form)

        self.name_label = QLabel('-')
        self.value_label = QLabel('-')
        self.aggregate_label = QLabel('-')

        form.addRow('Indicator:', self.name_label)
        form.addRow('Value (%):', self.value_label)
        form.addRow('Aggregate:', self.aggregate_label)
        layout.addWidget(group)

        # 3. Connect the selection model selectionChange
        #    to the slot.

        self.view.selectionModel().selectionChanged.connect(
            self.on_selection_changed)
    
    @Slot(QItemSelection, QItemSelection)
    def on_selection_changed(self, selected, deselected):

        indexes = selected.indexes()

        if not indexes:
            self.name_label.setText('-')
            self.value_label.setText('-')
            self.aggregate_label.setText('-')
            return

        row = indexes[0].row()

        self.name_label.setText(
            str(self.model.index(row, 0).data()))
        self.value_label.setText(
            str(self.model.index(row, 1).data()))

        aggregate = self.model.index(row, 2).data()
        self.aggregate_label.setText('Yes' if aggregate == 1 else 'No')


if __name__ == '__main__':

    app = QApplication(sys.argv)
    main_window = Window()
    main_window.show()
    sys.exit(app.exec())
