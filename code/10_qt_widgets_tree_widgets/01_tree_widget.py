import sys
from PySide6.QtCore import Slot, Qt
from PySide6.QtWidgets import (QApplication, QWidget,
    QVBoxLayout, QTreeWidget, QTreeWidgetItem, QLabel)


tree_data = (
    'Application Settings', '', [
        ('General', '', [
            ('Application Name', 'Personal Finance Manager', []),
            ('Version', '3.2.0', []),
            ('Base Currency', 'USD', []),
            ('Fiscal Year Start', 'January', []),
            ('Round Transactions to Cents', True, []),
            ('Default Account', 'Checking', []),
        ]),
        ('Notifications', '', [
            ('Low Balance Alerts', True, []),
            ('Low Balance Threshold', '$100.00', []),
            ('Large Transaction Alerts', True, []),
            ('Large Transaction Threshold', '$500.00', []),
            ('Weekly Summary Email', False, []),
            ('Recipient', 'john.doe@example.com', []),
        ])])



class Window(QWidget):
    
    def __init__(self):

        super().__init__()
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        # 1. Create a QTreeWidget object
        #    and set its column count.
        
        self.tree = QTreeWidget()
        self.tree.setColumnCount(2)
        self.tree.setHeaderLabels(['Name', 'Value'])
        self.tree.itemChanged.connect(self.save_settings)
        
        # 2. Use the data store to add
        #    the items to the tree widget.
        
        self.tree.blockSignals(True)
        self.build_tree(self.tree, tree_data)
        self.tree.expandAll()
        self.tree.blockSignals(False)
        
        self.label = QLabel()

        layout.addWidget(self.tree)
        layout.addWidget(self.label)   

    def build_tree(self, parent, data):
        name, value, children = data
        item = QTreeWidgetItem(parent, [name, str(value)])
        if len(children) == 0:
            item.setFlags(item.flags() | Qt.ItemFlag.ItemIsEditable)
        for child in children:
            self.build_tree(item, child)
        return item
    
    # 3. Save the changes to the configuration.
    
    @Slot(QTreeWidgetItem, int)
    def save_settings(self, item, column):
        name = item.data(0, Qt.ItemDataRole.DisplayRole)
        value = item.data(1, Qt.ItemDataRole.DisplayRole)
        print(f'{name} changed to : {value}. Saving...')


if __name__ == '__main__':

    app = QApplication(sys.argv)
    main_window = Window()
    main_window.show()
    sys.exit(app.exec())
