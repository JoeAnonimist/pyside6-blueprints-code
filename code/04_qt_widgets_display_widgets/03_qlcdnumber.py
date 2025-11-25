import sys
from PySide6.QtWidgets import (QApplication, 
    QWidget, QLCDNumber, QVBoxLayout)

class Window(QWidget):
    
    # Displays an LCD-like number
    
    def __init__(self):

        super().__init__()
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        self.lcd_number = QLCDNumber()
        self.lcd_number.setFixedSize(250, 100)
        self.lcd_number.setDigitCount(4)
        self.lcd_number.display(1337)
        layout.addWidget(self.lcd_number)
        

if __name__ == '__main__':

    app = QApplication(sys.argv)
    main_window = Window()
    main_window.show()
    sys.exit(app.exec())
