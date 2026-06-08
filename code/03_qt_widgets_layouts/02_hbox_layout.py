# QHBoxLayout is the horizontal box layout.

import sys
from PySide6.QtCore import Slot
from PySide6.QtWidgets import (QApplication, 
    QWidget, QPushButton, QLabel, QHBoxLayout)


class Window(QWidget):
    
    def __init__(self):

        super().__init__()
        
        # 1. Create the layout 
        #    and set it as the window layout
        
        layout = QHBoxLayout()
        self.setLayout(layout)
        
        # 2. Create the widgets

        button = QPushButton('Savings account')
        self.label = QLabel('')
        self.label.setMinimumWidth(100)

        # 3 - Add widgets to the layout
        
        layout.addWidget(button)
        layout.addStretch()
        layout.addWidget(self.label)

        button.clicked.connect(self.show_account_details)
        
    @Slot()
    def show_account_details(self):
        self.label.setText('Emergency Fund')


if __name__ == '__main__':

    app = QApplication(sys.argv)
    main_window = Window()
    main_window.show()
    sys.exit(app.exec())
