# QListView presents items stored in a model.
# ie. it uses the QT model/view architecture
# Models contain data and views display it
# so one model can be used with multiple views.

import sys
from pathlib import Path
from PySide6.QtCore import Qt
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtWidgets import (QApplication, QWidget,
    QVBoxLayout, QListView, QAbstractItemView, QStyle)


class Window(QWidget):
    
    def __init__(self, parent=None):

        super().__init__(parent)
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        # 1. Create the view
        
        self.list_view = QListView()
        self.list_view.setEditTriggers(
            QAbstractItemView.EditTrigger.NoEditTriggers)
        
        # 2. Create the model and populate it with data
        
        self.model = QStandardItemModel()
        
        home = Path.home()
        fs_entries = home.iterdir()

        for entry in fs_entries:
            item = QStandardItem(entry.name)
            icon = self.get_icon(entry)
            item.setIcon(icon)
            tooltip = self.get_tooltip_data(entry)
            item.setData(tooltip, Qt.ItemDataRole.ToolTipRole)
            self.model.appendRow(item)
        
        # 3. Set the view's model
        
        self.list_view.setModel(self.model)
        
        layout.addWidget(self.list_view)
        
    def get_icon(self, path):
        if path.is_dir():
            return self.style().standardIcon(
                QStyle.StandardPixmap.SP_DirIcon)
        else:
            return self.style().standardIcon(
                QStyle.StandardPixmap.SP_FileIcon)
            
    def get_tooltip_data(self, path):
        if path.is_dir():
            return 'Directory'
        elif path.is_file():
            size = round(path.stat().st_size / 1024, 2)
            return f'File: {size} KB'
        else:
            return 'File System Entry'


if __name__ == '__main__':

    app = QApplication(sys.argv)
    main_window = Window()
    main_window.show()
    sys.exit(app.exec())
