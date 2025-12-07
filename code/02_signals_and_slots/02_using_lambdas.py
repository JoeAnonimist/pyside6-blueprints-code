# Demonstrate using a Python lambda function
# as a slot. Lambdas are anonymous functions,
# ie. they have no name.

import sys
from PySide6.QtWidgets import (QApplication, 
    QWidget, QPushButton, QVBoxLayout)


class Window(QWidget):
    
    def __init__(self):

        super().__init__()
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        # 1 - Create the widget
        
        button = QPushButton('Click me!')

        # 2 - In this case the slot is a Python lambda

        button.clicked.connect(
            lambda : self.log('My log message'))

        layout.addWidget(button)
    
    def log(self, message):
        print('Button clicked')
        print(message)
        

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    main_window = Window()
    main_window.show()
    sys.exit(app.exec())
