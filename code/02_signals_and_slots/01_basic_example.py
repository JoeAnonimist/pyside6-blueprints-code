# Signals are event notifications emitted by widgets.
# Slots are Python methods/functions that respond to them.
# connect() establishes the relationship between the two.

import sys
from PySide6.QtCore import Slot
from PySide6.QtWidgets import (QApplication, 
    QWidget, QLabel, QPushButton, QVBoxLayout)


class Window(QWidget):
    
    def __init__(self):

        super().__init__()
        
        self.setWindowTitle('Refresh Balance')
        self.setMinimumWidth(150)
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        # 1. Create the label.
        #    We keep a reference so the slot can update it.
        
        self.balance_label = QLabel('Balance: -')
        layout.addWidget(self.balance_label)
        
        # 2. Create the button.
        #    Clicking it emits the clicked() signal.
        
        self.button = QPushButton('Click me!')
        layout.addWidget(self.button)
        
        # 3. Connect the signal to the slot.
        #    Note there are no parentheses after on_refresh_clicked:
        #    connect() expects a function object, not a function call.
        
        self.button.clicked.connect(self.refresh_balance)
    
    @Slot()
    def refresh_balance(self):
        self.balance_label.setText('Balance: $4,250,00')
        

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    main_window = Window()
    main_window.show()
    sys.exit(app.exec())
