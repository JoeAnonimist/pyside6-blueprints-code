import sys
from random import randint
from PySide6.QtWidgets import (QApplication, 
    QWidget, QLCDNumber, QVBoxLayout)


class Window(QWidget):

    def __init__(self):

        super().__init__()
        self.setWindowTitle('Transaction counter panel')
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        transaction_count = randint(0, 99)
        
        # 1. Create a QLCdNumber.
        
        self.lcd_number = QLCDNumber()
        self.lcd_number.setFixedSize(250, 100)
        
        # 2. Set the number of digits.
        
        self.lcd_number.setDigitCount(2)
        
        # 3. Pass the number to display().
        
        self.lcd_number.display(transaction_count)
        layout.addWidget(self.lcd_number)
        

if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
