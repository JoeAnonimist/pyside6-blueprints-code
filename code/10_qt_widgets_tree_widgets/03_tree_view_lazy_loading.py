import sys
from pathlib import Path
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtWidgets import (QApplication,
    QWidget, QVBoxLayout, QTreeView)


class Window(QWidget):
    
    def __init__(self):

        super().__init__()
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        # 1. Create a QTreeView and a QStandardItemModel.
        
        tree = QTreeView()
        
        home = Path.home()
        home_item = QStandardItem('home')
        home_item.setData(home)
        placeholder = QStandardItem()
        placeholder.setData('placeholder')
        home_item.appendRow(placeholder)
        
        self.model = QStandardItemModel()
        self.model.invisibleRootItem().appendRow(home_item)
        
        tree.setModel(self.model)
        
        # 2. Connect the expanded() signal to a slot.
        
        tree.expanded.connect(self.get_subdirectories)
        
        layout.addWidget(tree)
    
    # 3. Load subdirectories on demand.
        
    def get_subdirectories(self, index):
        parent = self.model.itemFromIndex(index)
        if parent.rowCount() == 1:
            if parent.child(0).data() == 'placeholder':
                parent.removeRow(0)
                print(parent.text())
                children = [d for d in parent.data().iterdir() if d.is_dir()]
                for child in children:
                    item = QStandardItem(child.name)
                    item.setData(child)
                    placeholder_item = QStandardItem()
                    placeholder_item.setData('placeholder')
                    item.appendRow(placeholder_item)
                    parent.appendRow(item)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    main_window = Window()
    main_window.show()
    sys.exit(app.exec())
