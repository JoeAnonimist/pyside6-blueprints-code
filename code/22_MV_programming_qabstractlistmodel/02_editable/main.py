import sys
from PySide6.QtWidgets import (QApplication,
    QWidget, QListView, QVBoxLayout)
from PySide6.QtTest import QAbstractItemModelTester
from txtfilemodel import TxtFileModel


class Window(QWidget):
    
    def __init__(self, parent=None):

        super().__init__(parent)
        layout = QVBoxLayout()
        self.setLayout(layout)

        model = TxtFileModel('data.txt')
        QAbstractItemModelTester(model)
        view = QListView()
        view.setModel(model)
        layout.addWidget(view)
        
        model.dataChanged.connect(self.on_data_changed)
    
    # Handle the dataChanged signals
    
    def on_data_changed(self, topLeft, bottomRight, roles):
        print('Model changed, row:', topLeft.row())


if __name__ == '__main__':

    app = QApplication(sys.argv)
    main_window = Window()
    main_window.show()
    sys.exit(app.exec())
