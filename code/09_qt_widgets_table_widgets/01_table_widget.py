# The QTableWidget class provides an
# item-based table view with a default model.

import sys
from PySide6.QtCore import Slot, Qt
from PySide6.QtWidgets import (QApplication, QWidget, QVBoxLayout,
    QTableWidget, QTableWidgetItem, QLabel, QPushButton)


class Window(QWidget):

    def __init__(self, parent=None):

        super().__init__(parent)

        layout = QVBoxLayout()
        self.setLayout(layout)
        
        self.headers = ["Feature", "Free", "Pro", "Enterprise"]
        
        self.data = [
            ["Price", "$0/mo", "$29/mo", "Custom"],
            ["Storage", "2 GB", "100 GB", "Unlimited"],
            ["Users", "1", "Unlimited", "Unlimited"],
            ["Custom Domain", False, True, True],
            ["API Access", False, True, True]
        ]
        
        rows = len(self.data)
        columns = len(self.data[0])
        
        # 1. Create a table widget.

        self.table_widget = QTableWidget(rows, columns)
        self.table_widget.setHorizontalHeaderLabels(self.headers)
        self.table_widget.setAlternatingRowColors(True)
        self.table_widget.setSizeAdjustPolicy(
            QTableWidget.SizeAdjustPolicy.AdjustToContents)
        
        # 2. Populate the widget.

        for row in range(rows):
            for col in range(columns):
                item = QTableWidgetItem()
                item.setData(
                    Qt.ItemDataRole.DisplayRole,
                    str(self.data[row][col]))
                self.table_widget.setItem(row, col, item)

        self.table_widget.itemChanged.connect(self.on_item_changed)

        self.label = QLabel()
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.export_button = QPushButton('Export table')
        self.export_button.clicked.connect(self.export_data)

        layout.addWidget(self.table_widget)
        layout.addWidget(self.label)
        layout.addWidget(self.export_button)
        
    # 3. Create the required slots.

    @Slot(QTableWidgetItem)
    def on_item_changed(self, item):
        row = item.row()
        col = item.column()
        text = item.text()
        self.label.setText(
            f'Cell[{row}, {col}]: new value is {text}')
        
    @Slot()
    def export_data(self):
        print(', '.join(self.headers))
        for r in range(self.table_widget.rowCount()):
            row_data = []
            for c in range(self.table_widget.columnCount()):
                row_data.append(self.table_widget.item(r, c).text())
            print(', '.join(row_data))


if __name__ == '__main__':

    app = QApplication(sys.argv)
    main_window = Window()
    main_window.show()
    sys.exit(app.exec())
