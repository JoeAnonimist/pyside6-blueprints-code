# The QListWidget class provides
# an item-based list widget

import sys
from PySide6.QtCore import Slot, Qt
from PySide6.QtWidgets import (QApplication,
    QWidget, QVBoxLayout, QListWidget, QLabel,
    QListWidgetItem)


class Window(QWidget):
    
    def __init__(self):

        super().__init__()
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        transactions = [
            ('🛒 Groceries', 'Whole Foods, Jul 21, -$84.32'),
            ('⚡ Electric Bill', 'City Power, Jul 18, -$112.50'),
            ('💰 Salary Deposit', 'Acme Payroll, Jul 15, +$3,200.00'),
            ('🍽️ Dining Out', 'The Copper Pot, Jul 20, -$46.75'),
            ('🚗 Auto Insurance', 'Safe Insurance, Jul 12, -$98.00'),
            ('🏠 Rent Payment', 'Acme Properties, Jul 1, -$1,450.00'),
        ]
        
        # 1. Create a list widget and add items to it.
        
        self.transaction_list = QListWidget()
        
        for description, details in transactions:
            item = QListWidgetItem(description)
            item.setData(Qt.ItemDataRole.UserRole, details)
            self.transaction_list.addItem(item)

        self.selected_label = QLabel()
        self.details_label = QLabel()
        self.selected_label.setStyleSheet("font-size: 24px;")
        
        layout.addWidget(self.transaction_list)
        layout.addWidget(self.selected_label)
        layout.addWidget(self.details_label)
        
        # 3. Connect the signal to the slot.

        self.transaction_list.currentItemChanged.connect(
            self.select_transaction)
        self.transaction_list.setCurrentRow(0)
    
    # 3. Create the slot.
    
    @Slot(QListWidgetItem, QListWidgetItem)
    def select_transaction(self, current, previous):

        transaction = current.data(Qt.ItemDataRole.DisplayRole)
        details = current.data(Qt.ItemDataRole.UserRole)
        self.selected_label.setText(transaction)
        self.details_label.setText(details)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    main_window = Window()
    main_window.show()
    sys.exit(app.exec())
