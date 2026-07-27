import sys
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtWidgets import (QApplication,
    QWidget, QVBoxLayout, QTreeView)

tree_data = [
    ('Housing', '', [
        ('Rent / Mortgage', '1800', 'Checking'),
        ('Utilities', '220', 'Checking'),
        ('Home Insurance', '95', 'Checking'),
        ('Maintenance', '150', 'Savings'),
    ]),
    ('Transportation', '', [
        ('Car Payment', '410', 'Checking'),
        ('Fuel', '160', 'Checking'),
        ('Auto Insurance', '120', 'Checking'),
        ('Public Transit', '75', 'Checking'),
    ]),
    ('Food & Dining', '', [
        ('Groceries', '500', 'Checking'),
        ('Restaurants', '250', 'Credit Card'),
        ('Coffee Shops', '60', 'Credit Card'),
    ])]


class Window(QWidget):

    def __init__(self, parent=None):

        super().__init__(parent)

        layout = QVBoxLayout(self)

        # 1. Create and populate the model.

        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(
            ['Category', 'Monthly Budget ($)', 'Paid From'])

        root = self.model.invisibleRootItem()

        for category_name, _, subcategories in tree_data:

            category_row = [
                QStandardItem(category_name),
                QStandardItem(''),
                QStandardItem('')
                ]

            root.appendRow(category_row)
            category_item = category_row[0]

            for subcat_name, budget, account in subcategories:
                category_item.appendRow([
                    QStandardItem(subcat_name),
                    QStandardItem(budget),
                    QStandardItem(account),
                ])

        # 2. Create the view.

        tree_view = QTreeView()

        # 3. Set the model as the view's model

        tree_view.setModel(self.model)
        tree_view.expandAll()
        tree_view.resizeColumnToContents(0)

        layout.addWidget(tree_view)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    main_window = Window()
    main_window.show()
    sys.exit(app.exec())
