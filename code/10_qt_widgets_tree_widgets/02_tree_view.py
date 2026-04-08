import sys
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtWidgets import (QApplication,
    QWidget, QVBoxLayout, QTreeView)

tree_data = [
    ('Europe', '', [
        ('Germany', '83', 'Berlin'),
        ('France', '67', 'Paris'),
        ('Spain', '47', 'Madrid'),
        ('Italy', '59', 'Rome'),
    ]),
    ('Asia', '', [
        ('China', '1400', 'Beijing'),
        ('India', '1380', 'New Delhi'),
        ('Japan', '125', 'Tokyo'),
        ('South Korea', '51', 'Seoul'),
    ]),
    ('North America', '', [
        ('United States', '331', 'Washington, D.C.'),
        ('Canada', '38', 'Ottawa'),
        ('Mexico', '126', 'Mexico City'),
    ]),
]


class Window(QWidget):
    
    def __init__(self, parent=None):
        
        super().__init__(parent)

        layout = QVBoxLayout(self)
        
        # 1. Create and populate the model.

        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(
            ['Name', 'Population (M)', 'Capital'])

        root = self.model.invisibleRootItem()

        for continent_name, _, countries in tree_data:
            
            continent_row = [
                QStandardItem(continent_name),
                QStandardItem(''),
                QStandardItem('')
                ]
            
            root.appendRow(continent_row)
            continent_item = continent_row[0]

            for country_name, population, capital in countries:
                continent_item.appendRow([
                    QStandardItem(country_name),
                    QStandardItem(population),
                    QStandardItem(capital),
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
