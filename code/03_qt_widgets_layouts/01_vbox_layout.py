# Demonstrate how to stack widgets vertically
# using QVBoxLayout.

import sys
from PySide6.QtCore import Slot
from PySide6.QtWidgets import (QApplication,
    QWidget, QPushButton, QLabel, QVBoxLayout)


class Window(QWidget):

    def __init__(self):

        super().__init__()

        # 1. Create the layout object
        #    and set it as the window layout.

        layout = QVBoxLayout()
        self.setLayout(layout)

        # 2. Create widgets.

        checking_button = QPushButton('Checking Account')
        savings_button = QPushButton('Savings Account')
        credit_card_button = QPushButton('Credit Card Account')

        # 3. Add the widgets to the layout.

        layout.addWidget(checking_button)
        layout.addWidget(savings_button)
        layout.addWidget(credit_card_button)
        
        layout.addStretch()
        
        self.details_label = QLabel()
        layout.addWidget(self.details_label)
        
        checking_button.clicked.connect(self.show_checking)
        savings_button.clicked.connect(self.show_savings)
        credit_card_button.clicked.connect(self.show_credit_card)
        
    @Slot()
    def show_checking(self):
        self.details_label.setText('Everyday spending')
        
    @Slot()
    def show_savings(self):
        self.details_label.setText('Emergency fund')
        
    @Slot()
    def show_credit_card(self):
        self.details_label.setText('Monthly expenses')


if __name__ == '__main__':

    app = QApplication(sys.argv)
    main_window = Window()
    main_window.show()
    sys.exit(app.exec())
