# A splitter lets the user control the size of 
# child widgets by dragging the boundary between them. 

import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QApplication, QWidget, QHBoxLayout,
    QVBoxLayout, QSplitter, QGroupBox, QRadioButton, QListWidget,
    QTableWidget, QTableWidgetItem, QTextEdit)


class Window(QWidget):
    
    def __init__(self):

        super().__init__()
        self.resize(700, 300)
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        self.horizontal_radio = QRadioButton('Horizontal')
        self.horizontal_radio.setChecked(True)
        self.vertical_radio = QRadioButton('Vertical')
        self.horizontal_radio.toggled.connect(self.on_toggled)
        self.vertical_radio.toggled.connect(self.on_toggled)
        
        orientation_layout = QHBoxLayout()
        orientation_layout.addWidget(self.horizontal_radio)
        orientation_layout.addWidget(self.vertical_radio)
        layout.addLayout(orientation_layout)

        # 1. Create the splitter object.
        
        self.splitter = QSplitter()
        
        # 2. Create the child widgets.
        
        accounts_groupbox = QGroupBox('Accounts List')
        accounts_groupbox.setLayout(QVBoxLayout())
        
        self.accounts_list = QListWidget()
        self.accounts_list.addItems([
            'Checking', 'Savings', 'Credit Card'])
        accounts_groupbox.layout().addWidget(self.accounts_list)
        
        transactions_groupbox = QGroupBox('Transactions')
        transactions_groupbox.setLayout(QVBoxLayout())
        self.transactions_table = QTableWidget(3, 3)
        self.transactions_table.setHorizontalHeaderLabels(["Date", "Description", "Amount"])
        data = [
            ('July 27', 'UA', '-$1,189.50'),
            ('July 25', 'Salary Deposit', '+$3,250.00'),
            ('July 24', 'Whole Foods', '-$142.65')]
       
        for row, (date, desc, amount) in enumerate(data):
            self.transactions_table.setItem(row, 0, QTableWidgetItem(date))
            self.transactions_table.setItem(row, 1, QTableWidgetItem(desc))
            self.transactions_table.setItem(row, 2, QTableWidgetItem(amount))

        transactions_groupbox.layout().addWidget(self.transactions_table)

        details_groupbox = QGroupBox('Details')
        details_groupbox.setLayout(QVBoxLayout())
        self.details_text = QTextEdit()
        self.details_text.setReadOnly(True)
        self.details_text.setPlainText(
            'Account: Checking\n\n'
            'Current Balance: $8,742.35\n'
            'Available Balance: $8,742.35\n\n'
            'Last updated: July 28, 2026')
        details_groupbox.layout().addWidget(self.details_text)
        
        # 3. Add the widgets to the splitter.
        
        self.splitter.addWidget(accounts_groupbox)
        self.splitter.addWidget(transactions_groupbox)
        self.splitter.addWidget(details_groupbox)
        self.splitter.setSizes([120, 360, 200]) 

        layout.addWidget(self.splitter)
        
    def on_toggled(self):
        if self.horizontal_radio.isChecked():
            self.splitter.setOrientation(Qt.Orientation.Horizontal)
        else:
            self.splitter.setOrientation(Qt.Orientation.Vertical)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    main_window = Window()
    main_window.show()
    sys.exit(app.exec())
