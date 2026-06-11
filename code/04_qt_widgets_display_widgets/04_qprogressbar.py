import sys
from random import randint
from PySide6.QtWidgets import (QApplication, QWidget,
    QProgressBar, QLabel, QVBoxLayout)


class Window(QWidget):
    
    def __init__(self):

        super().__init__()
        
        self.setWindowTitle('Budget Utilization')
        self.resize(300, 120)
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        operating_expenses = randint(0, 10000)
        
        # 1. Create a progress bar.
        
        operating_expenses_bar = QProgressBar()
        
        # 2. Set the value range.
        
        operating_expenses_bar.setRange(0, 10000)
        
        # 3. Set the current value.
        
        operating_expenses_bar.setValue(operating_expenses)
        operating_expenses_bar.setToolTip(
            'Operating Expenses - monthly limit $10,000 '
            f'- Currently ${operating_expenses:,.2f}')
        
        capital_expenditure_bar = QProgressBar()
        capital_expenditure_bar.setRange(0, 0)
        capital_expenditure_bar.setToolTip(
            'Capital Expenditure - syncing transactions...')
        
        layout.addWidget(QLabel('Operating Expenses'))
        layout.addWidget(operating_expenses_bar)
        layout.addWidget(QLabel('Capital Expenditure'))
        layout.addWidget(capital_expenditure_bar)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
