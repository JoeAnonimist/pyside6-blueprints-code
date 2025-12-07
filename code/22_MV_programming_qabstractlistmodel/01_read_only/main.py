import sys
from PySide6.QtWidgets import (QApplication,
    QWidget, QListView, QVBoxLayout)
from PySide6.QtTest import QAbstractItemModelTester
from txtfilemodel import TxtFileModel


class Window(QWidget):
    
    def __init__(self):

        super().__init__()
        layout = QVBoxLayout()
        self.setLayout(layout)

        model = TxtFileModel('data.txt')
        QAbstractItemModelTester(model)
        view = QListView()
        view.setModel(model)
        layout.addWidget(view)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    main_window = Window()
    main_window.show()
    sys.exit(app.exec())

