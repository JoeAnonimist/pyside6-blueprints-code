# The QToolBox class provides a column of tabbed widget items.

import sys
from PySide6.QtCore import Slot
from PySide6.QtWidgets import (QApplication, QWidget,
    QHBoxLayout, QVBoxLayout, QToolBox, QPushButton, QLabel)


class Window(QWidget):
    
    def __init__(self):

        super().__init__()
        self.resize(440, 200)
        layout = QHBoxLayout()
        layout.setSpacing(20)
        self.setLayout(layout)
        
        # 1. Create the toolbox
        
        toolbox = QToolBox()
        
        # 2. Create the widgets.
        
        checking_widget = QWidget()
        checking_widget.setLayout(QVBoxLayout())
        recent_transactions_btn = QPushButton('Recent Transactions')
        recent_transactions_btn.clicked.connect(
            self.show_recent_transactions)
        checking_widget.layout().addWidget(recent_transactions_btn)
        checking_widget.layout().addStretch()
        
        savings_widget = QWidget()
        savings_widget.setLayout(QVBoxLayout())

        deposit_money_btn = QPushButton('Deposit Money')
        deposit_money_btn.clicked.connect(self.deposit_money)
        savings_widget.layout().addWidget(deposit_money_btn)
        
        view_rate_btn = QPushButton('View Interest Rate')
        view_rate_btn.clicked.connect(self.view_rate)
        savings_widget.layout().addWidget(view_rate_btn)
        savings_widget.layout().addStretch()
        
        credit_card_widget = QWidget()
        credit_card_widget.setLayout(QVBoxLayout())
        make_payment_btn = QPushButton('Make Payment')
        make_payment_btn.clicked.connect(self.make_payment)
        credit_card_widget.layout().addWidget(make_payment_btn)
        credit_card_widget.layout().addStretch()
        
        
        # 3. Add widgets to the toolbox.
        
        toolbox.addItem(checking_widget, 'Checking Accounts')
        toolbox.addItem(savings_widget, 'Savings Accounts')
        toolbox.addItem(credit_card_widget, 'Credit Cards Accounts')
        

        self.label = QLabel()
        self.label.setMinimumWidth(250)

        layout.addWidget(toolbox)
        layout.addWidget(self.label)
    
    @Slot()
    def show_recent_transactions(self):
        self.label.setText(
            'UA - Business Class - $1,189.50 - Jul 27, 2026\n'
            'Salary Deposit - $3,250.00 - Jul 25, 2026\n'
            'Consulting Invoice - $2,450.00 - Jul 24, 2026'
    )
        
    @Slot()
    def deposit_money(self):
        self.label.setText(
            'Successfully deposited $15,000.00 into Savings')
        
    @Slot()
    def view_rate(self):
        self.label.setText(
            'Current Interest Rate: 4.50% APY\n'
            'Interest earned this month: $87.65')
        
    @Slot()
    def make_payment(self):
        self.label.setText('$10,000.00 paid')


if __name__ == '__main__':

    app = QApplication(sys.argv)
    main_window = Window()
    main_window.show()
    sys.exit(app.exec())
