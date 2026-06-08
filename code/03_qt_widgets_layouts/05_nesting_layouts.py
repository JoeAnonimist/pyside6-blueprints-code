import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QApplication, QWidget,
    QPushButton, QLabel, QVBoxLayout, QHBoxLayout)


ACCOUNTS = [
    ("Checking Account", 1240.00),
    ("Savings Account", 8500.00),
    ("Credit Card", 340.00)
]


class Window(QWidget):

    def __init__(self):

        super().__init__()
        self.setFixedSize(240, 180)
        
        # 1. Create the parent layout.

        layout = QVBoxLayout()
        self.setLayout(layout)
        
        for name, balance in ACCOUNTS:
            
            # 2. Create child layouts.
            
            row_layout = QHBoxLayout()

            account_button = QPushButton(name)
            account_button.setMinimumWidth(120)
            account_button.clicked.connect(
                lambda checked, name=name, balance=balance:
                    self.show_account_details(name, balance))

            balance_label = QLabel(f'${balance:.2f}')
            balance_label.setAlignment(Qt.AlignmentFlag.AlignRight)
            balance_label.setMinimumWidth(80)

            row_layout.addWidget(account_button)
            row_layout.addStretch()
            row_layout.addWidget(balance_label)
            
            # 3. Add child layouts to the parent layout.
            
            layout.addLayout(row_layout)
        
        layout.addStretch()
        
        self.details_label = QLabel()
        self.details_label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        layout.addWidget(self.details_label)
        
    def show_account_details(self, name, balance):
        self.details_label.setText(
            f'Selected: {name}  ${balance:.2f}')


if __name__ == '__main__':

    app = QApplication(sys.argv)
    main_window = Window()
    main_window.show()
    sys.exit(app.exec())
