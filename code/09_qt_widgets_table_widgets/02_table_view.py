# QTableView implements a table view
# that displays items from a model.

import sys
from PySide6.QtCore import Slot, Qt
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtWidgets import (QApplication, QWidget,
    QVBoxLayout, QTableView, QLabel)


class Window(QWidget):
    
    def __init__(self, parent=None):

        super().__init__(parent)
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        self.header = ['Indicator', 'Value (%)', 
            'Aggregate', 'Include in report']
        self.data = [
            ['GDP', 3, True, True],
            ['CPI', 6, True, True],
            ['Jobs', 5, True, True],
            ['Confidence', 75, True, True],
            ['Industry', 92, True, True],
            ['Retail', 4, True, True],
        ]
        
        # 1. Create the view
        
        self.table_view = QTableView()
        self.table_view.setSizeAdjustPolicy(
            QTableView.SizeAdjustPolicy.AdjustToContents)
        
        rows = len(self.data)
        columns = len(self.data[0])
        
        # 2. Create the model.

        self.model = QStandardItemModel(rows, columns)
        self.model.setHorizontalHeaderLabels(self.header)

        for row in range(rows):
            for col in range(columns):
                item = QStandardItem()
                if col == 0:
                    item.setFlags(Qt.ItemFlag.NoItemFlags)
                data = self.data[row][col]
                item.setData(data, Qt.ItemDataRole.DisplayRole)
                self.model.setItem(row, col, item)
                
        # 3. Connect the model with the view.

        self.table_view.setModel(self.model)

        self.notify_label = QLabel()
        self.notify_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.model.itemChanged.connect(self.notify_users)
        
        layout.addWidget(self.table_view)
        layout.addWidget(self.notify_label)
    
    @Slot(QStandardItem)
    def notify_users(self, item):
        row = item.row()
        col = item.column()
        text = item.text()
        self.notify_label.setText(
            f'Cell[{row}, {col}]: new value is {text}')


if __name__ == '__main__':

    app = QApplication(sys.argv)
    main_window = Window()
    main_window.show()
    sys.exit(app.exec())
